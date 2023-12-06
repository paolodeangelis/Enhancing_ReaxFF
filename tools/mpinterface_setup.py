#!/usr/bin/env python3
"""Script to set `Material Project` API Key."""

import argparse
import os
import sys

sys.path.insert(0, os.path.abspath("."))
MPINT_CONFIG_YAML = None


def get_package_path():  # noqa: D103
    try:
        import tools

        PACKAGE_PATH = os.path.dirname(tools.__file__)
    except ImportError:
        import mp  # noqa: F401

        PACKAGE_PATH = os.getcwd()
    global MPINT_CONFIG_YAML
    MPINT_CONFIG_YAML = os.path.join(PACKAGE_PATH, "mp", "mpint_config.yaml")


def check_and_remove(mpi_config_yaml):  # noqa: D103
    if os.path.exists(mpi_config_yaml):
        os.remove(mpi_config_yaml)
        print("\033[33m[W]: the configuration file already exist, it will be overwrite\033[0m")


def write_yaml(mpi_config_yaml, api_key=None):  # noqa: D103
    if api_key is None:
        api_key = "null"
    with open(mpi_config_yaml, "w") as file_:
        file_.write(
            f"""username: {os.getlogin( )}  # your UF HPC username
mp_api: {api_key}  # your Materials Project API key
                """
        )


def main(api_key=None):  # noqa: D103
    get_package_path()
    check_and_remove(MPINT_CONFIG_YAML)
    write_yaml(MPINT_CONFIG_YAML, api_key=api_key)


if __name__ == "__main__":
    # Construct the argument parser
    ap = argparse.ArgumentParser()
    # Add the arguments to the parser
    ap.add_argument("-k", "--apikey", required=True, help="Material Project API key")
    args = vars(ap.parse_args())
    main(api_key=args["apikey"])
    print(f"[I]: mpinterface configuration file saved in: \n\t{MPINT_CONFIG_YAML}")
