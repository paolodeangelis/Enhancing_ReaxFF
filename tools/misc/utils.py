import os

import numpy as np


def make_dir(dirpath: str) -> None:
    """Make a new folder if it does not exist

    Args:
        dirpath (str): path of the new folder
    """
    dirs = dirpath.split(os.sep)
    for i in range(len(dirs)):
        dirpath_ = os.path.join(*dirs[: i + 1])
        if not os.path.isdir(dirpath_):
            os.mkdir(dirpath_)


def mtx2str(strain_mtx):
    sigma_str = ["1", "2", "3"]
    strain_idx_0, strain_idx_1 = np.where(strain_mtx)
    simple_str = []
    latex_str = []
    for i0, i1 in zip(strain_idx_0, strain_idx_1):
        simple_str.append(f"e_{sigma_str[i0]}{sigma_str[i1]}")
        latex_str.append(f"\\varepsilon_{{ {sigma_str[i0]} {sigma_str[i1]} }}")
    simple_str = " ".join(simple_str)
    latex_str = "$" + " ".join(latex_str) + "$"
    return simple_str, latex_str
