# Enhancing the ReaxFF

[![Data FAIR](https://custom-icon-badges.demolab.com/badge/data-FAIR-blue?logo=database\&logoColor=white)](https://www.nature.com/articles/sdata201618)
[![Made with Python](https://custom-icon-badges.demolab.com/badge/Python-3.9+-blue?logo=python\&logoColor=white)](https://python.org)
[![OS - Linux](https://custom-icon-badges.demolab.com/badge/OS-Linux-orange?logo=linux\&logoColor=white)](https://www.linux.org/)
[![Contributions - close](https://custom-icon-badges.demolab.com/badge/contributions-open-red?logo=code-of-conduct\&logoColor=white)](CONTRIBUTING.md)
[![Code style - black](https://custom-icon-badges.demolab.com/badge/code%20style-black-000000?logo=code\&logoColor=white)](https://github.com/psf/black)

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/paolodeangelis/Enhancing_ReaxFF_DFT_database/main.svg)](https://results.pre-commit.ci/badge/github/paolodeangelis/Enhancing_ReaxFF_DFT_database/main.svg)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ba532ddf0c974cccab358938902104d9)](TODO)
[![License - CC BY 4.0](https://custom-icon-badges.demolab.com/badge/license-CC--BY%204.0-lightgray?logo=law\&logoColor=white)](LICENSE)
[![DOI](https://sandbox.zenodo.org/badge/DOI/10.5281/zenodo.7959121.svg)](TODO)


This repository contains the jupyter notebooks used to re-parametrize the ReaxFF force field for LiF, an inorganic compound.
The purpose of the set of notebooks is to facilitate the reparameterization ReaxFF force field for LiF. The results and method used were published in the article [Enhancing ReaxFF for Molecular Dynamics Simulations of Lithium-Ion Batteries: An interactive reparameterization protocol][article-doi].

The database containing the simulation data from *ab initio* simulations obtained from this protocol is published in [Enhancing ReaxFF repository DFT Database][enhancing-reaxFF-database-repository].

## Table of Contents

* [Installation](#installation)
* [Folder Structure](#folder-structure)
* [Interacting with the Database](#interacting-with-the-database)
  * [ASE db Command-line](#ase-db-command-line)
  * [Web Interface](#web-interface)
  * [ASE Python Interface](#ase-python-interface)
* [Contributing](#contributing)
* [How to Cite](#how-to-cite)
* [License](#license)
* [Acknowledgments](#acknowledgments)

## Installation

To use the database and interact with it, ensure that you have the following Python requirements installed:

**Minimum Requirements:**

* Python 3.9 or above
* Atomic Simulation Environment (ASE) library
* Jupyter Lab

**Requirements for Re-running or Performing New Simulations:**

* SCM (Software for Chemistry & Materials) Amsterdam Modeling Suite
* PLAMS (Python Library for Automating Molecular Simulation) library

**Requirements for Re-running ReaxFF optimization:**

* AMS (Amsterdam Modeling Suite) Python Stack ([more info here](https://www.scm.com/doc/Scripting/Python_Stack/Python_Stack.html))

You can install the required Python packages using pip:

```shell
pip install -r requirements.txt
```

> **Warning**
>
> This do not include the ParAMS packages since is available only in AMS Python Stack.
>
> See instruction below.

```shell
export SCM_PYTHONDIR=$(pwd)/venv
$AMSBIN/amspython --install_venv
source venv/AMSYYYY.X.venv/bin/activate # Replace YYYY.X with the correct AMS version
```

> **Warning**
>
> Make sure to have the appropriate licenses and installations of SCM Amsterdam Modeling Suite and any other necessary software for running simulations.

### Configure `Material Project API`

**Get *Material Project* API key**

Access to [Material Project](https://materialsproject.org/) and follow the istruction on the [documentation](https://materialsproject.org/api)

#### Make the configuration file

1.  Run the script replacing `<MATERIAL_PROJECT_KEY>` with the Material Project API key.

```shell
python tools/mpinterface_setup.py -k <MATERIAL_PROJECT_KEY>
```

## Folder Structure

The repository has the following folder structure:

```bash
.
├── CONTRIBUTING.md
├── CREDITS.md
├── LICENSE
├── README.md
├── requirements.txt
├── assets
├── data
│   ├── LiF.db
│   ├── LiF.json
│   └── LiF.yaml
├── notebooks
│   ├── browsing_db.ipynb
│   └── running_simulation.ipynb
└── tools
    ├── db
    ├── plams_experimental
    └── scripts
```

* `CONTRIBUTING.md`: This file provides guidelines and instructions for contributing to the repository. It outlines the contribution process, coding conventions, and other relevant information for potential contributors.
* `CREDITS.md`: This file acknowledges and credits the individuals or organizations that have contributed to the repository.
* `LICENSE`: This file contains the license information for the repository (CC BY 4.0). It specifies the terms and conditions under which the repository's contents are distributed and used.
* `README.md`: This file.
* `requirements.txt`: This file lists the required Python packages and their versions. (see [installation section](#installation))
* `assets`: This folder contains any additional assets, such as images or documentation, related to the repository.
* `data`: This folder contains the data files used in the repository.
  * `LiF.db`: This file is the SQLite database file that includes the DFT data used for the ReaxFF force field. Specifically, it contains data related to the inorganic compound LiF.
  * `LiF.json`: This file provides the database metadata in a human-readable format using JSON.
  * `LiF.yaml`: This file also contains the database metadata in a more human-readable format, still using YAML.
* `notebooks`: This folder contains Jupyter notebooks that provide demonstrations and examples of how to use and analyze the database.
  * `browsing_db.ipynb`: This notebook demonstrates how to handle, select, read, and understand the data points in the `LiF.db` database using the ASE database Python interface. It serves as a guide for exploring and navigating the database effectively.
  * `running_simulation.ipynb`: In this notebook, you will find an example of how to get a data point from the `LiF.db` database and use it to perform a new simulation. The notebook showcases how to utilize either the [PLAMS](https://www.scm.com/doc/plams/index.html) library or the [AMSCalculator](https://www.scm.com/doc/plams/interfaces/amscalculator.html) and ASE Python library to conduct simulations based on the retrieved data and then store it as a new data point in the `LiF.db` database. It provides step-by-step instructions and code snippets for a seamless simulation workflow.
* `tools`: This directory contains a collection of Python modules and scripts that are useful for reading, analyzing, and re-running simulations stored in the database. These tools are indispensable for ensuring that this repository adheres to the principles of **I**nteroperability and **R**eusability, as outlined by the [FAIR principles](https://www.go-fair.org/fair-principles/).
  * `db`: This Python module provides functionalities for handling, reading, and storing data into the database.
  * `plasm_experimental`: This Python module includes the necessary components for using the `AMSCalculator` with PLASM and the SCM software package, utilizing the ASE API. It facilitates running simulations, performing calculations.
  * `scripts`: This directory contains additional scripts for dvanced usage scenarios of this repository.

## Interacting with the Database

There are three ways to interact with the database: using the ASE db command line, the web interface, and the ASE Python interface.

### ASE db Command-line

To interact with the database using the ASE db terminal command, follow these steps:

1. Open a terminal and navigate to the directory containing the `LiF.db` file.

2. Run the following command to start the ASE db terminal:

   ```shell
   ase db LiF.db
   ```

3. You can now use the available commands in the terminal to query and manipulate the database. More information can be found in the [ASE database documentation](https://wiki.fysik.dtu.dk/ase/ase/db/db.html).

### Web Interface

To interact with the database using the web interface, follow these steps:

1. Open a terminal and navigate to the directory containing the `LiF.db` file.

2. Run the following command to start the ASE db terminal:

   ```shell
   ase db -w LiF.db
   ```

3. Open your web browser and connect to the local server at <http://127.0.0.1:5000>.

![Example of Web Interface](assets/img/ase_db_web.gif)

> **Warning**
>
> To visualize the 3D structure of the system, you need to install the [JMOL extension](https://jmol.sourceforge.net/). You can use the script `tools/scripts/install_jmol.py` to automatically download and install it:
>
> ```shell
> cd tools/scripts/
> python install_jmol.py
> ```

### ASE Python Interface

To interact with the database using the ASE Python interface, you can use the following example code:

```python
from ase.db import connect

# Connect to the database
db = connect("database.db")

# Query the database
results = db.select('formula = "LiF"')

# Iterate over the results
for row in results:
    print(f"ID: {row.id}, Energy: {row.energy}")
```

For a more detailed example, refer to the notebook `notebooks/browsing_db.ipynb`. To learn how to perform a simulation, check the notebook `notebooks/running_simulation.ipynb`.

## Contributing

If you would like to contribute to the Enhancing ReaxFF DFT Database by performing new simulations and expanding the database, please follow the guidelines outlined in the [Contribution Guidelines](CONTRIBUTING.md). You are welcome to submit pull requests or open issues in the repository. Your contributions are greatly appreciated!

## How to Cite

If you use the database or the tools provided in this repository for your work, please cite it using the following BibTeX entry:

```bibtex
@dataset{EnhReaxFFdatabase,
  author       = {De Angelis, Paolo and
                  Cappabianca, Roberta and
                  Fasano, Matteo and
                  Asianri, Pietro and
                  Chiavazzo, Chiavazzo},
  title        = {{Enhancing the ReaxFF DFT database}},
  month        = may,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {1.0.0-beta},
  doi          = {10.5072/zenodo.1204707},
  url          = {https://doi.org/10.5281/zenodo.7959121}
}
```

## License

The contents of this repository are licensed under the [Creative Commons Attribution 4.0 International License][cc-by].

## Acknowledgments

This project has received funding from the European Union’s [Horizon 2020 research and innovation programme](https://ec.europa.eu/programmes/horizon2020/en) under grant agreement [No 957189](https://cordis.europa.eu/project/id/957189).
The project is part of [BATTERY 2030+](https://battery2030.eu/), the large-scale European research initiative for inventing the sustainable batteries of the future.

The authors also acknowledge that the simulation results of this database have been achieved using the [DECI](https://prace-ri.eu/hpc-access/deci-access/) resource [ARCHER2](https://www.archer2.ac.uk/) based in UK at [EPCC](https://www.epcc.ed.ac.uk/) with support from the [PRACE](https://prace-ri.eu/) aisbl.

<hr width="100%">
<div style="display: flex; justify-content: space-between; align-items: center;">
    <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Licence" style="border-width:0; height:35px" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>
   <span style="float:right;">
    &nbsp;
    <a rel="big-map" href="https://www.big-map.eu/">
        <img style="border-width:0; height:35px" src="assets/img//logo-bigmap.png" alt="BIG MAP site" >
    </a>
    &nbsp;
    <a rel="small" href="https://areeweb.polito.it/ricerca/small/">
        <img style="border-width:0; height:35px" src="assets/img//logo-small.png" alt="SMALL site" >
    </a>
    &nbsp;
    <a rel="polito"href="https://www.polito.it/">
        <img style="border-width:0; height:35px" src="assets/img//logo-polito.png" alt="POLITO site" >
    </a>
</span>
</div>

<!-- [![CC BY 4.0][cc-by-image]][cc-by] -->

[cc-by]: http://creativecommons.org/licenses/by/4.0/

[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png

[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

[article-doi]: https://doi.org/TBD

[enhancing-reaxFF-repository]: https://github.com/paolodeangelis/Enhancing_ReaxFF_DFT_database
