import os
from ctypes import c_char_p
from multiprocessing import Manager, Pool
from multiprocessing.managers import ListProxy, ValueProxy

import numpy as np
import pandas as pd


def progressbar(percentage: float, info: str = "", screen: int = 100, status: str = "info"):
    if percentage is None:
        percentage = 0.0
    if info != "":
        info = info.strip() + " "
    bar_length = screen - len(info) - 2 - 6
    status_chars = [
        " ",
        "\u258f",
        "\u258e",
        "\u258d",
        "\u258c",
        "\u258b",
        "\u258a",
        "\u2589",
        "\u2588",
    ]
    # if percentage <= 1.:
    #     percentage *= 100
    length = percentage * bar_length / 100
    units = int(length // 1)  # floor of the percentage
    decimal = length % 1  # mantissa of the percentage
    empty = bar_length - units
    full = 1 - int(percentage / 100)
    if status == "success":
        color = "\x1b[32m"
    elif status == "warning":
        color = "\x1b[33m"
    elif status == "danger":
        color = "\x1b[31m"
    else:
        color = "\x1b[0m"
    # Print bar
    text = "{:s}{:s}{:s}\x1b[0m {:4.1f}%".format(
        info,
        color,
        "\u2588" * units + status_chars[int(decimal * 8)] * full + " " * empty,
        percentage,
    )
    return text


def chunkify(file_path, nlines=1024):
    fileEnd = os.path.getsize(file_path)
    with open(file_path) as file_obj:
        chunkEnd = file_obj.tell()
        while True:
            chunkStart = chunkEnd
            n = 0
            while True:
                line = file_obj.readline()  # noqa
                chunkEnd = file_obj.tell()
                n += 1
                if n >= nlines:
                    break
            yield chunkEnd / fileEnd, chunkStart, chunkEnd - chunkStart
            if chunkEnd >= fileEnd:
                break


def storing_in_dataframe(file_path, interface_names, interface_x, interface_isactive, chunkStart, chunkSize, nlines):
    if isinstance(nlines, ValueProxy):
        nlines = nlines.get()
    if isinstance(file_path, ValueProxy):
        file_path = file_path.get()
    if isinstance(interface_names, ListProxy):
        interface_names = list(interface_names)
    if isinstance(interface_x, ListProxy):
        interface_x = list(interface_x)
    if isinstance(interface_isactive, ListProxy):
        interface_isactive = list(interface_isactive)
    dataset_df = pd.DataFrame(index=np.arange(nlines), columns=["index", "fx", "time"] + interface_names)
    active_index = np.where(interface_isactive)[0]
    n = 0
    with open(file_path) as file_obj:
        file_obj.seek(chunkStart)
        lines = file_obj.read(chunkSize).splitlines()
        for line in lines:
            if line[0] == "#":
                continue
            data = line.split()
            dataset_df.loc[n, "index"] = int(data[0])
            dataset_df.loc[n, "fx"] = float(data[1])
            dataset_df.loc[n, "time"] = float(data[2])
            dataset_df.iloc[n, 3:] = interface_x
            dataset_df.iloc[n, active_index + 3] = [float(d) for d in data[3:]]
            n += 1
    dataset_df = dataset_df.dropna(axis=0, how="all")
    return dataset_df


def get_run_history(file_path, interface, workers=4, nlines=1024):
    dataframes = []  # noqa
    pool = Pool(processes=workers)
    jobs = []
    # shared memory ojects
    manager = Manager()
    s_nlines = manager.Value("i", nlines)
    s_file_path = manager.Value(c_char_p, file_path)
    s_interface_names = manager.list(interface.names)
    s_interface_x = manager.list(interface.x)
    s_interface_isactive = manager.list(interface.is_active)
    for i, (perc_, chunkStart_, chunkSize_) in enumerate(chunkify(file_path, nlines=nlines)):
        jobs.append(
            pool.apply_async(
                storing_in_dataframe,
                args=(
                    s_file_path,
                    s_interface_names,
                    s_interface_x,
                    s_interface_isactive,
                    chunkStart_,
                    chunkSize_,
                    s_nlines,
                ),
            )
        )  # file_path, interface_names, interface_x, interface_isactive, chunkStart, chunkSize, nlines
        print(
            f"Warmup (jobs: {i+1}, cores used {workers})".ljust(35) + progressbar(0.0, status="info", screen=65),
            end="\r",
            flush=True,
        )
    N_jobs_rest = N_jobs = len(jobs)
    results = []
    n = 0
    print(
        f"Reading (Jobs remaining: {N_jobs_rest})".ljust(35)
        + progressbar(n / N_jobs * 100.0, status="info", screen=65),
        end="\r",
        flush=True,
    )
    while N_jobs_rest > 0:
        job = jobs.pop(0)
        results.append(job.get())
        n += 1
        N_jobs_rest = len(jobs)
        print(
            f"Reading (Jobs remaining: {N_jobs_rest})".ljust(35)
            + progressbar(n / N_jobs * 100.0, status="info", screen=65),
            end="\r",
            flush=True,
        )
    print("DONE".ljust(35) + progressbar(n / N_jobs * 100.0, status="info", screen=65), end="\n", flush=True)
    pool.close()
    pool.join()
    return results
