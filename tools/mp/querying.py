from __future__ import annotations

import glob
import os

import numpy as np
import pandas as pd
import yaml
from ase import Atoms
from ase.io import read
from pandas import DataFrame
from pymatgen.core import Structure
from pymatgen.ext.matproj import MPRester
from pymatgen.io.ase import AseAtomsAdaptor

with open(os.path.join(os.path.dirname(__file__), "mpint_config.yaml")) as f:
    temp = yaml.safe_load(f)

matprj = MPRester(temp["mp_api"])
matget2ase = AseAtomsAdaptor()


def get_crystals(chemical_formula: str, verbose: bool = True) -> tuple[DataFrame, Structure, Atoms]:
    mat = matprj.get_materials_ids(chemical_formula)
    # Get Energy and formation Energy per atoms
    Energy = []
    Ef = []
    for id_ in mat:
        Energy.append(matprj.query(criteria={"task_id": id_}, properties=["energy_per_atom"])[0]["energy_per_atom"])
        Ef.append(
            matprj.query(criteria={"task_id": id_}, properties=["formation_energy_per_atom"])[0][
                "formation_energy_per_atom"
            ]
        )
    # Get unit cell
    systems = []
    systems_ase = []
    for id_ in mat:
        systems.append(matprj.get_structure_by_material_id(id_))
        systems_ase.append(matget2ase.get_atoms(systems[-1]))
    # store info
    properties_df = pd.DataFrame(index=mat)
    properties_df["energy_per_atom"] = Energy
    properties_df["formation_energy_per_atom"] = Ef
    if verbose:
        print(f"N={len(mat)} crsital units found for the chemical formula `{chemical_formula}`")

    return properties_df, systems, systems_ase


def load_cifs(dir: str) -> list[tuple[str, Structure, Atoms]]:
    systems = []

    for path in np.sort(glob.glob(os.path.join(dir, "*.cif"))):
        system_name = path.split(os.sep)[-1].split(".cif")[0].split("-")[1:]
        system_name = "-".join(system_name)
        systems.append((system_name, Structure.from_file(path), read(path)))
    return systems
