PARAM_SCRIP_TEMPLATE = f"""# PARAM Script
print(f" START ".center(80, '='))
import os, sys, pickle
import datetime, pytz
import numpy as np
import scm.plams as scm
import scm.params as params
from scm.params.core.lossfunctions import  MAE, RMSE, SSE, SAE
sys.path.insert(1,"{ os.path.abspath('last_attempt')}")

"""

PARAM_SCRIP_TEMPLATE += """
TIMEZONE = pytz.timezone('Europe/Rome')
SEED={:d}
JOBCOLLECTION_YAML="{:s}"
DATASET_YAML="{:s}"
TRAININGSET_YAML="{:s}"
VALIDATIONSET_YAML="{:s}"
PARAMETERS_YAML="{:s}"
CALLBACKS_PICKLE="{:s}"
OPTIMIZER_PICKLE="{:s}"

np.random.seed(SEED)


def get_time():
    now = datetime.datetime.now(TIMEZONE)
    return f"[{{datetime.datetime.now(TIMEZONE).strftime('%Y-%m-%d %H:%M:%S %Z')}}]"


def load_pickle(pickle_file):
    with open(pickle_file, 'rb') as file:
        output = pickle.load(file)
    return output


totaltime = params.Timer()
print(f" LOADING ".center(80, '-'))
# Job Collection
jobcollection = params.JobCollection()
jobcollection.pickle_load(JOBCOLLECTION_YAML)
print(f"{{get_time()}} JobCollection LOADED")
# Training Set
datagset = params.DataSet(DATASET_YAML)
trainingset = params.DataSet(TRAININGSET_YAML)
validationset = params.DataSet(VALIDATIONSET_YAML)
print(f"{{get_time()}} DataSet LOADED")
bad_ids = trainingset.check_consistency(jobcollection)

if len(bad_ids) > 0:
    raise RuntimeError(f'The Dataset entries {{len(bad_ids)}} are INCONSISTENT with the JobCollection')
else:
    print("ALL GOOD")

# ReaxFF Parameters
# interface = params.ReaxParams.yaml_load(PARAMETERS_YAML)
interface = params.ReaxParams.pickle_load(PARAMETERS_YAML)
print(f"{{get_time()}} ReaxParams LOADED")
print(f"{{get_time()}} {{interface.is_active.count(True)}}/{{len(interface)}} parameters to re-train")
print(interface.get_engine().settings)

print(f" OPTIMIZATION SET-UP ".center(80, '-'))
# Call Backs
callbacks = load_pickle(CALLBACKS_PICKLE)
print(f"{{get_time()}} CallBacks LOADED")"""
# """
# # Optimizer
# optimizer_kwargs = {{
#     'sigma':    {:.3f},
#     'popsize':  {:d},
#     'seed':     SEED,
# }}
# optimizer = params.CMAOptimizer(**optimizer_kwargs)
# print(f"{{get_time()}} CMAOptimizer with " + " ".join([f"{{k}}={{v}}" for k, v in optimizer_kwargs.items() ]))
# """ +
PARAM_SCRIP_TEMPLATE += """
# Optimizer
optimizer, optimizer_info = load_pickle(OPTIMIZER_PICKLE)
print(f"{{get_time()}} {{optimizer_info['name']}} optimizer with " + " ".join([f"{{k}}={{v}}" for k, v in optimizer_info['kwargs'].items() ]))
"""
PARAM_SCRIP_TEMPLATE += """
# Parallel Strategy
parallel_kwargs = {{
    'parametervectors': {:d}, 
    'jobs':             {:d}, 
    'processes':        {:d}, 
    'threads':          {:d}
}}
parallel = params.ParallelLevels(**parallel_kwargs)
print(f"{{get_time()}} ParallelLevels with " + " ".join([f"{{k}}={{v}}" for k, v in parallel_kwargs.items() ]))
# Optimization
tmp_dir = os.path.abspath('tmp_sim')

if not os.path.isdir(tmp_dir) :
    os.mkdir(tmp_dir)

optimization_kwargs = {{
    'loss'                : SSE(),   # The loss function to be evaluated. (Sum of Squares Error) #(Mean Absolute Error) #(Root-Mean-Square Error)
    # 'validation'          : .15,     # Percentage of the training set to be used as validation, or another DataSet() instance
    'parallel'            : parallel,
    'callbacks'           : callbacks,
    'plams_workdir_path'  : tmp_dir, 
    # 'batch_size'          : 32,     # At every iteration, only compute a maximum of `batch_size` properties
    # 'use_pipe'            : True,     # Use the AMSPipe interface where possible
    # 'n_cores'             : None,     # Use N CPU cores for the execution of jobs during an optimization. Defaults to the number of physical cores
}}
# optimization  = params.Optimization(jobcollection, [trainingset, validationset], interface, optimizer, skip_x0=False, **optimization_kwargs)
optimization  = params.Optimization(jobcollection, datagset, interface, optimizer, skip_x0=False, **optimization_kwargs)
print(f"{{get_time()}} Optimization READY with: " )
optimization.summary()

# START OPTIMIZATION
print(f" START OPTIMIZATION ".center(80, '-'))
optimization.optimize()

print(f" SAVE ReaxFF ".center(80, '-'))
interface.write('ffield.reax.ff.optimized') # and write the optimized ffield to 'ffield.reax.ff.optimized'
print('')
print('='*80)
print(f'DONE after {{totaltime()}}.')
print('='*80)

"""


SLURM_SCRIP_TEMPLATE = """#!/bin/bash
#SBATCH --partition=standard
#SBATCH --qos=standard
#SBATCH --time=24:00:00
#SBATCH --account=pr1u1751
#SBATCH --job-name={0:s}
#SBATCH --error={0:s}-%j.err
#SBATCH --output={0:s}-%j.out
#SBATCH --nodes={1:d}
#SBATCH --ntasks-per-node={2:d}
#SBATCH --cpus-per-task={3:d}

# MODULEs
module use --append /work/pr1u1751/pr1u1751/shared/modules
module load ams/2021.104

export OMP_NUM_THREADS={3:d}
export PYTHONUNBUFFERED=TRUE
export SCM_PYTHONDIR=/work/pr1u1751/pr1u1751/pr1id026/venv_ams
source $SCM_PYTHONDIR/AMS2021.1.venv/bin/activate
which python

python ./{4:s}
"""