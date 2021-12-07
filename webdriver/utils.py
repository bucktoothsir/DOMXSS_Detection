import os
from contextlib import contextmanager
from sys import platform
from enum import Enum, auto


class OS(Enum):
    WINDOWS = auto()
    LINUX = auto()
    MACOS = auto()


def get_os():
    if platform == "linux" or platform == "linux2":
        return OS.LINUX
    elif platform == "darwin":
        return OS.MACOS
    elif platform == "win32":
        return OS.WINDOWS


def get_path_delimiter():
    operating_system = get_os()
    if operating_system == OS.WINDOWS:
        return ';'
    else:
        return ':'


@contextmanager
def add_drivers_to_path(proj_dir):
    path_delimiter = get_path_delimiter()
    current_path = os.environ['PATH']
    current_path_list = current_path.split(path_delimiter)
    driver_path = os.path.join(proj_dir, 'drivers')
    driver_path = os.path.abspath(driver_path)
    new_path = [driver_path] + current_path_list
    new_path = path_delimiter.join(new_path)
    os.environ['PATH'] = new_path
    try:
        yield
    finally:
        os.environ['PATH'] = current_path
