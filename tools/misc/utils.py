import os

def make_dir(dirpath: str) -> None:
    """Make a new folder if it does not exist

    Args:
        dirpath (str): path of the new folder
    """
    dirs = dirpath.split(os.sep)
    for i in range(len(dirs)):
        dirpath_ = os.path.join(*dirs[:i+1])
        if not os.path.isdir(dirpath_) :
            os.mkdir(dirpath_)
