#!/usr/bin/env python3

"""
 Copyright 2023  Michael Ryan Hunsaker, M.Ed., Ph.D.

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

# coding=utf-8
"""
Program designed to be a data collection and instructional tool for
teachers of students with Visual Impairments
"""


import os
import sqlite3
import sys
import traceback
from pathlib import Path

from nicegui import ui
from screeninfo import get_monitors

module_path = os.path.abspath(os.getcwd())
if module_path not in sys.path:
    sys.path.append(module_path)
from appTheming import theme
from appHelpers.helpers import (
    dataBasePath,
    set_start_dir,
    USER_DIR,
    datenow,
)
from appHelpers.workingdirectory import create_user_dir
from appHelpers.sqlgenerate import create_connection, implement_tables, create_table

set_start_dir()
create_connection(dataBasePath)
implement_tables()

from appPages import piano
from appPages import fitness
from appPages import homepage


def warningmessage(exception_type, exception_value, exception_traceback) -> None:
    """
    Log an error message and display a warning notification.

    Parameters
    ----------
    exception_type : type
        The type of the exception.
    exception_value : Exception
        The value of the exception.
    exception_traceback : traceback.TracebackType
        The traceback object containing information about the exception.

    Returns
    -------
    None

    Examples
    --------
    >>> try:
    ...     # Code that may raise an exception
    ...     result = 1 / 0
    ... except Exception as e:
    ...     warningmessage(type(e), e, traceback.extract_tb(e.__traceback__))
    """
    i = ""
    message = "Please make sure all fields are selected / filled out properly\n\n"
    tb = traceback.format_exception(
        exception_type, exception_value, exception_traceback
    )
    log_path = Path(USER_DIR).joinpath(
        "errorLogs", f"logfile_{datenow}.log"
    )
    Path.touch(log_path)
    for i in tb:
        message += i
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write(f"{datenow}\n{i}" + "\n")
        errortype = str(exception_type)
    ui.notify(f"{message}\n{errortype}", type="warning", close_button="OK")


@ui.page("/")
def index_page() -> None:
    """
    Opens the homepage for the app.

    This function initializes the homepage of the app by creating various elements
    such as contact logs, abacus, session notes, observations, braille, braille note,
    CVI (Cortical Visual Impairment), iOS, screen reader, instructional materials,
    digital literacy, and keyboarding.

    Returns
    -------
    None

    Examples
    --------
    >>> index_page()
    """
    with theme.frame("QUICK VIEW"):
        homepage.content()


fitness.create()
piano.create()

MONITOR = ""


def getresolution() -> str:
    """
    Retrieve the screen resolution of the primary monitor.

    This function iterates through the available monitors using the `get_monitors` function
    from the `screeninfo` module and returns the resolution of the primary monitor in the
    format "width x height".

    Returns
    -------
    str
        A string representing the screen resolution in the format "width x height".

    Examples
    --------
    >>> getresolution()
    '1920x1080'
    """

    for SCREEN in get_monitors():
        SCREENRESOLUTION = "{str(SCREEN.width)}x{str(SCREEN.height)}"
    return SCREEN


MONITOR = getresolution()
print(f"Monitor: \nwidth = {MONITOR.width} \nheight = {MONITOR.height}")

ui.run(
    native=False,
    reload=False,
    dark=False,
    title="Habit and Fitness Tracker",
    fullscreen=False,
    # window_size=(MONITOR.width, MONITOR.height - 72) # only relevant if native=True
)
