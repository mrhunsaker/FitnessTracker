# coding=utf-8
###############################################################################
#    Copyright 2023 Michael Ryan Hunsaker, M.Ed., Ph.D.                       #
#    email: hunsakerconsulting@gmail.com                                      #
#                                                                             #
#    Licensed under the Apache License, Version 2.0 (the "License");          #
#    you may not use this file except in compliance with the License.         #
#    You may obtain a copy of the License at                                  #
#                                                                             #
#        http://www.apache.org/licenses/LICENSE-2.0                           #
#                                                                             #
#    Unless required by applicable law or agreed to in writing, software      #
#    distributed under the License is distributed on an "AS IS" BASIS,        #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #
#    See the License for the specific language governing permissions and      #
#    limitations under the License.                                           #
###############################################################################

import datetime
import os
import sqlite3
from pathlib import Path
from sqlite3 import Error

from screeninfo import get_monitors
import numpy as np
import pandas as pd
from nicegui import app, ui
from pandas.api.types import is_bool_dtype, is_numeric_dtype


os.chdir(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DIR = ""


def set_directory() -> Path:
    """
    Set the user directory based on the operating system.

    Returns:
        Path: The user directory path.

    Raises:
        OSError: If the HOME directory cannot be determined.

    Examples:
        >>> set_directory()
        PosixPath('/home/user/Documents')  # Example for a POSIX system
        >>> set_directory()
        WindowsPath('C:/Users/User/Documents')  # Example for a Windows system
    """
    if os.name == 'nt':
        tmppath = Path(os.environ['USERPROFILE']).joinpath('Documents')
        Path.mkdir(tmppath, parents=True, exist_ok=True)
        START_DIR = Path(tmppath)
        tmppath = Path(os.environ['USERPROFILE']).joinpath('Documents', 'Fitness')
        Path.mkdir(tmppath, parents=True, exist_ok=True)
    elif os.name == 'posix':
        tmppath = Path(os.environ['HOME']).joinpath('Documents')
        Path.mkdir(tmppath, parents=True, exist_ok=True)
        START_DIR = Path(tmppath)
        tmppath = Path(os.environ['USERPROFILE']).joinpath('Documents', 'Fitness')
        Path.mkdir(tmppath, parents=True, exist_ok=True)
    else:
        raise OSError("Error! Cannot find HOME directory")

    return START_DIR
USER_DIR=set_directory()
os.chdir(USER_DIR)

dataBasePath = Path(USER_DIR).joinpath('Fitness/workoutLog.db')

def create_connection(db_file):
    """
    Create a SQLite database connection.

    Parameters
    ----------
    db_file : str
        The path to the SQLite database file.

    Returns
    -------
    None

    Raises
    ------
    Error
        If an error occurs while connecting to the database.

    Examples
    --------
    >>> create_connection("example.db")
    2.6.0  # Example output for SQLite version
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return conn

create_connection(dataBasePath)

def create_table(conn, sql_create_sql_table):
    """
    Create a table in the SQLite database using the provided SQL statement.

    Parameters
    ----------
    conn : sqlite3.Connection
        The SQLite database connection.
    sql_create_sql_table : str
        The SQL statement for creating the table.

    Returns
    -------
    None

    Raises
    ------
    Error
        If an error occurs while executing the SQL statement.

    Examples
    --------
    >>> conn = sqlite3.connect("example.db")
    >>> create_table(conn, "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_sql_table)
    except Error as e:
        print(e)
    conn.close()


def implement_tables():
    """
    Create or initialize the WORKOUTS table in the SQLite database.

    This function establishes a connection to the SQLite database, creates a table
    named WORKOUTS with specified columns, and closes the connection.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Examples
    --------
    >>> implement_tables()
    """
    sql_create_workout_table = """CREATE TABLE IF NOT EXISTS WORKOUTS (
        ID                          INTEGER PRIMARY KEY AUTOINCREMENT,
        DATE                        TEXT,
        FRONTLINE_REPS              INTEGER,
        FRONTLINE_SETS              INTEGER,
        FRONTLINE_WEIGHT            INTEGER,
        SHOULDERZPRESS_REPS	        INTEGER,
        SHOULDERZPRESS_SETS	        INTEGER,
        SHOULDERZPRESS_WEIGHT	    INTEGER,
        ELBOWOUTROW_REPS	        INTEGER,
        ELBOWOUTROW_SETS	        INTEGER,
        ELBOWOUTROW_WEIGHT	        INTEGER,
        SUPINEBICEPCURL_REPS	    INTEGER,
        SUPINEBICEPCURL_SETS	    INTEGER,
        SUPINEBICEPCURL_WEIGHT	    INTEGER,
        CLOSEGRIPPUSHUP_REPS        INTEGER,
        CLOSEGRIPPUSHUP_SETS        INTEGER,
        CLOSEGRIPPUSHUP_STAIR       INTEGER,
        REARDELTFLY_REPS	        INTEGER,
        REARDELTFLY_SETS            INTEGER,
        REARDELTFLY_WEIGHT          INTEGER,
        SIDEBEND_REPS	            INTEGER,
        SIDEBEND_SETS               INTEGER,
        SIDEBEND_WEIGHT             INTEGER,
        LATERALRAISE_REPS	        INTEGER,
        LATERALRAISE_SETS	        INTEGER,
        LATERALRAISE_WEIGHT	        INTEGER,
        STIFFLEGRDL_REPS	        INTEGER,
        STIFFLEGRDL_SETS	        INTEGER,
        STIFFLEGRDL_WEIGHT          INTEGER,
        SLIDERHAMSTRINGCURL_REPS 	INTEGER,
        SLIDERHAMSTRINGCURL_SETS 	INTEGER,
        HIPTHRUSTER_REPS	        INTEGER,
        HIPTHRUSTER_SETS	        INTEGER,
        HIPTHRUSTER_WEIGHT	        INTEGER,
        FORWARDSQUAT_REPS	        INTEGER,
        FORWARDSQUAT_SETS	        INTEGER,
        FORWARDSQUAT_WEIGHT	        INTEGER,
        SUMOSQUAT_REPS	            INTEGER,
        SUMOSQUAT_SETS	            INTEGER,
        SUMOSQUAT_WEIGHT	        INTEGER,
        CYCLISTSQUAT_REPS	        INTEGER,
        CYCLISTSQUAT_SETS	        INTEGER,
        SINGLELEGCALFRAISE_REPS	    INTEGER,
        SINGLELEGCALFRAISE_SETS	    INTEGER,
        LONGLEVERCRUNCHES_REPS      INTEGER,
        LONGLEVERCRUNCHES_SETS      INTEGER,
        SIDELINESCULPT              INTEGER,
        ABDOMINALS                  INTEGER
    );"""

    conn = create_connection(dataBasePath)
    if conn is not None:
        create_table(conn, sql_create_workout_table)
    else:
        print("Error! cannot create the database connection.")
    conn.close()

implement_tables()

datenow = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")

with ui.header().classes(replace = 'row items-center') as header:
    ui.button(on_click = lambda: left_drawer.toggle()).props('flat color=white icon=menu')
with ui.tabs() as tabs:
    ui.tab('WORKOUT INPUT')
    ui.tab('WORKOUT DATA')
with ui.tab_panels(tabs, value = 'WORKOUT INPUT'):
    with ui.tab_panel('WORKOUT INPUT'):
        u_today_date = ui.date().classes('hidden')
        u_frontlineRaiseSets = ui.number().classes('hidden')
        u_frontlineRaiseReps = ui.number().classes('hidden')
        u_frontlineRaiseWeight = ui.number().classes('hidden')
        u_shoulderPressReps = ui.number().classes('hidden')
        u_shoulderPressSets = ui.number().classes('hidden')
        u_shoulderPressWeight = ui.number().classes('hidden')
        u_elbowOutRowReps = ui.number().classes('hidden')
        u_elbowOutRowSets = ui.number().classes('hidden')
        u_elbowOutRowWeight = ui.number().classes('hidden')
        u_bicepCurlReps = ui.number().classes('hidden')
        u_bicepCurlSets = ui.number().classes('hidden')
        u_bicepCurlWeight = ui.number().classes('hidden')
        u_closeGripPushupReps = ui.number().classes('hidden')
        u_closeGripPushupSets = ui.number().classes('hidden')
        u_closeGripPushupWeight = ui.number().classes('hidden')
        u_rearDeltFlyReps = ui.number().classes('hidden')
        u_rearDeltFlySets = ui.number().classes('hidden')
        u_rearDeltFlyWeight = ui.number().classes('hidden')
        u_sideBendReps = ui.number().classes('hidden')
        u_sideBendSets = ui.number().classes('hidden')
        u_sideBendWeight = ui.number().classes('hidden')
        u_lateralRaiseReps = ui.number().classes('hidden')
        u_lateralRaiseSets = ui.number().classes('hidden')
        u_lateralRaiseWeight = ui.number().classes('hidden')
        u_stiffLegRDLReps = ui.number().classes('hidden')
        u_stiffLegRDLSets = ui.number().classes('hidden')
        u_stiffLegRDLWeight = ui.number().classes('hidden')
        u_hamstringCurlReps = ui.number().classes('hidden')
        u_hamstringCurlSets = ui.number().classes('hidden')
        u_hipThrusterReps = ui.number().classes('hidden')
        u_hipThrusterSets = ui.number().classes('hidden')
        u_hipThrusterWeight = ui.number().classes('hidden')
        u_frontSquatReps = ui.number().classes('hidden')
        u_frontSquatSets = ui.number().classes('hidden')
        u_frontSquatWeight = ui.number().classes('hidden')
        u_sumoSquatReps = ui.number().classes('hidden')
        u_sumoSquatSets = ui.number().classes('hidden')
        u_sumoSquatWeight = ui.number().classes('hidden')
        u_cyclistSquatReps = ui.number().classes('hidden')
        u_cyclistSquatSets = ui.number().classes('hidden')
        u_calfRaiseReps = ui.number().classes('hidden')
        u_calfRaiseSets = ui.number().classes('hidden')
        u_calfRaiseWeight = ui.number().classes('hidden')
        u_longLeverCrunchesReps = ui.number().classes('hidden')
        u_longLeverCrunchesSets = ui.number().classes('hidden')
        u_sidelineSculpt = ui.number().classes('hidden')
        u_abdominals = ui.number().classes('hidden')


        def save(event):
            """
            Save workout data to individual exercise variables.

            This function extracts data from input fields representing different exercises,
            converts them to integers, and assigns the values to corresponding variables.
            If an exercise value is not provided, it defaults to 0. The function also
            captures the current date.

            Parameters
            ----------
            event : EventType
                The event triggering the save operation.

            Returns
            -------
            None

            Examples
            --------
            >>> save(some_event)
            """
            exercises = [
            u_frontlineRaiseSets,
            u_frontlineRaiseReps,
            u_frontlineRaiseWeight,
            u_shoulderPressReps,
            u_shoulderPressSets,
            u_shoulderPressWeight,
            u_elbowOutRowReps,
            u_elbowOutRowSets,
            u_elbowOutRowWeight,
            u_bicepCurlReps,
            u_bicepCurlSets,
            u_bicepCurlWeight,
            u_closeGripPushupReps,
            u_closeGripPushupSets,
            u_closeGripPushupWeight,
            u_rearDeltFlyReps,
            u_rearDeltFlySets,
            u_rearDeltFlyWeight,
            u_sideBendReps,
            u_sideBendSets,
            u_sideBendWeight,
            u_lateralRaiseReps,
            u_lateralRaiseSets,
            u_lateralRaiseWeight,
            u_stiffLegRDLReps,
            u_stiffLegRDLSets,
            u_stiffLegRDLWeight,
            u_hamstringCurlReps,
            u_hamstringCurlSets,
            u_hipThrusterReps,
            u_hipThrusterSets,
            u_hipThrusterWeight,
            u_frontSquatReps,
            u_frontSquatSets,
            u_frontSquatWeight,
            u_sumoSquatReps,
            u_sumoSquatSets,
            u_sumoSquatWeight,
            u_cyclistSquatReps,
            u_cyclistSquatSets,
            u_calfRaiseReps,
            u_calfRaiseSets,
            u_calfRaiseWeight,
            u_longLeverCrunchesReps,
            u_longLeverCrunchesSets,
            u_sidelineSculpt,
            u_abdominals
            ]
            for exercise in exercises:
                """
                Ensure exercise values are not None.

                This loop iterates through a list of exercise objects and checks if the
                'value' attribute of each exercise is None. If it is, the 'value' attribute
                is set to 0. If the 'value' attribute is not None, the loop continues to the
                next iteration.

                Parameters
                ----------
                exercises : list
                    A list of exercise objects with a 'value' attribute.

                Returns
                -------
                None

                Examples
                --------
                >>> exercises = [exercise1, exercise2, exercise3]
                >>> for exercise in exercises:
                ...     if exercise.value is None:
                ...         exercise.value = 0
                ...     else:
                ...         continue
                """
                if exercise.value is None:
                    exercise.value = 0
                else:
                    continue
            today_date = (u_today_date.value)
            frontlineRaiseReps = int(u_frontlineRaiseReps.value)
            frontlineRaiseSets = int(u_frontlineRaiseReps.value)
            frontlineRaiseWeight = int(u_frontlineRaiseReps.value)
            shoulderPressReps = int(u_shoulderPressReps.value)
            shoulderPressSets = int(u_shoulderPressSets.value)
            shoulderPressWeight = int(u_shoulderPressWeight.value)
            elbowOutRowReps = int(u_elbowOutRowReps.value)
            elbowOutRowSets = int(u_elbowOutRowSets.value)
            elbowOutRowWeight = int(u_elbowOutRowWeight.value)
            bicepCurlReps = int(u_bicepCurlReps.value)
            bicepCurlSets = int(u_bicepCurlSets.value)
            bicepCurlWeight = int(u_bicepCurlWeight.value)
            closeGripPushupReps = int(u_closeGripPushupReps.value)
            closeGripPushupSets = int(u_frontlineRaiseReps.value)
            closeGripPushupWeight = int(u_closeGripPushupWeight.value)
            rearDeltFlyReps = int(u_rearDeltFlyReps.value)
            rearDeltFlySets = int(u_rearDeltFlySets.value)
            rearDeltFlyWeight = int(u_rearDeltFlyWeight.value)
            sideBendReps = int(u_sideBendReps.value)
            sideBendSets = int(u_sideBendSets.value)
            sideBendWeight = int(u_sideBendWeight.value)
            lateralRaiseReps = int(u_lateralRaiseReps.value)
            lateralRaiseSets = int(u_lateralRaiseSets.value)
            lateralRaiseWeight = int(u_lateralRaiseWeight.value)
            stiffLegRDLReps = int(u_stiffLegRDLReps.value)
            stiffLegRDLSets = int(u_stiffLegRDLSets.value)
            stiffLegRDLWeight = int(u_stiffLegRDLWeight.value)
            hamstringCurlReps = int(u_hamstringCurlReps.value)
            hamstringCurlSets = int(u_hamstringCurlSets.value)
            hipThrusterReps = int(u_hipThrusterReps.value)
            hipThrusterSets = int(u_hipThrusterSets.value)
            hipThrusterWeight = int(u_hipThrusterWeight.value)
            frontSquatReps = int(u_frontSquatReps.value)
            frontSquatSets = int(u_frontSquatSets.value)
            frontSquatWeight = int(u_frontSquatWeight.value)
            sumoSquatReps = int(u_sumoSquatReps.value)
            sumoSquatSets = int(u_sumoSquatSets.value)
            sumoSquatWeight = int(u_sumoSquatWeight.value)
            cyclistSquatReps = int(u_cyclistSquatReps.value)
            cyclistSquatSets = int(u_cyclistSquatSets.value)
            calfRaiseReps = int(u_calfRaiseReps.value)
            calfRaiseSets = int(u_calfRaiseSets.value)
            calfRaiseWeight = int(u_calfRaiseWeight.value)
            longLeverCrunchesReps = int(u_longLeverCrunchesReps.value)
            longLeverCrunchesSets = int(u_longLeverCrunchesSets.value)
            sidelineSculpt = int(u_sidelineSculpt.value)
            abdominals = int(u_abdominals.value)

            def data_entry():
                """
                Insert workout data into the WORKOUTS table in the SQLite database.

                This function connects to the SQLite database, creates a cursor, and executes
                an SQL INSERT statement to add workout data to the WORKOUTS table. The data is
                provided as parameters, including the current date and various exercise details.
                After execution, the changes are committed, and the connection is closed.

                Parameters
                ----------
                None

                Returns
                -------
                None

                Examples
                --------
                >>> data_entry()
                """
                conn = sqlite3.connect(dataBasePath)
                if conn is not None:
                    c = conn.cursor()
                    c.execute(
                            """INSERT INTO WORKOUTS (
                        DATE,
                        FRONTLINE_REPS,
                        FRONTLINE_SETS,
                        FRONTLINE_WEIGHT,
                        SHOULDERZPRESS_REPS,
                        SHOULDERZPRESS_SETS,
                        SHOULDERZPRESS_WEIGHT,
                        ELBOWOUTROW_REPS,
                        ELBOWOUTROW_SETS,
                        ELBOWOUTROW_WEIGHT,
                        SUPINEBICEPCURL_REPS,
                        SUPINEBICEPCURL_SETS,
                        SUPINEBICEPCURL_WEIGHT,
                        CLOSEGRIPPUSHUP_REPS,
                        CLOSEGRIPPUSHUP_SETS,
                        CLOSEGRIPPUSHUP_STAIR,
                        REARDELTFLY_REPS,
                        REARDELTFLY_SETS,
                        REARDELTFLY_WEIGHT,
                        SIDEBEND_REPS,
                        SIDEBEND_SETS,
                        SIDEBEND_WEIGHT,
                        LATERALRAISE_REPS,
                        LATERALRAISE_SETS,
                        LATERALRAISE_WEIGHT,
                        STIFFLEGRDL_REPS,
                        STIFFLEGRDL_SETS,
                        STIFFLEGRDL_WEIGHT,
                        SLIDERHAMSTRINGCURL_REPS,
                        SLIDERHAMSTRINGCURL_SETS,
                        HIPTHRUSTER_REPS,
                        HIPTHRUSTER_SETS,
                        HIPTHRUSTER_WEIGHT,
                        FORWARDSQUAT_REPS,
                        FORWARDSQUAT_SETS,
                        FORWARDSQUAT_WEIGHT,
                        SUMOSQUAT_REPS,
                        SUMOSQUAT_SETS,
                        SUMOSQUAT_WEIGHT,
                        CYCLISTSQUAT_REPS,
                        CYCLISTSQUAT_SETS,
                        SINGLELEGCALFRAISE_REPS,
                        SINGLELEGCALFRAISE_SETS,
                        LONGLEVERCRUNCHES_REPS,
                        LONGLEVERCRUNCHES_SETS,
                        SIDELINESCULPT,
                        ABDOMINALS
                        )
                        VALUES (
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?,
                        ?
                        )
                        """,
                            (
                            today_date,
                            frontlineRaiseReps,
                            frontlineRaiseSets,
                            frontlineRaiseWeight,
                            shoulderPressReps,
                            shoulderPressSets,
                            shoulderPressWeight,
                            elbowOutRowReps,
                            elbowOutRowSets,
                            elbowOutRowWeight,
                            bicepCurlReps,
                            bicepCurlSets,
                            bicepCurlWeight,
                            closeGripPushupReps,
                            closeGripPushupSets,
                            closeGripPushupWeight,
                            rearDeltFlyReps,
                            rearDeltFlySets,
                            rearDeltFlyWeight,
                            sideBendReps,
                            sideBendSets,
                            sideBendWeight,
                            lateralRaiseReps,
                            lateralRaiseSets,
                            lateralRaiseWeight,
                            stiffLegRDLReps,
                            stiffLegRDLSets,
                            stiffLegRDLWeight,
                            hamstringCurlReps,
                            hamstringCurlSets,
                            hipThrusterReps,
                            hipThrusterSets,
                            hipThrusterWeight,
                            frontSquatReps,
                            frontSquatSets,
                            frontSquatWeight,
                            sumoSquatReps,
                            sumoSquatSets,
                            sumoSquatWeight,
                            cyclistSquatReps,
                            cyclistSquatSets,
                            calfRaiseReps,
                            calfRaiseSets,
                            longLeverCrunchesReps,
                            longLeverCrunchesSets,
                            sidelineSculpt,
                            abdominals
                            )
                        )
                    conn.commit()
                else:
                    print("Error! cannot create the database connection.")
                conn.close()
                ui.notify(
                        "Saved successfully!",
                        position="center",
                        type="positive",
                        close_button="OK",
                    )
            data_entry()

        with ui.row().classes('w-full no-wrap'):
            ui.date(value = 'f{datenow}', on_change = lambda e: u_today_date.set_value(e.value)).classes('w-1/2')
        with ui.row().classes('w-full no-wrap py-4'):
            ui.label('UPPER BODY').classes('text-lg')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Frontline Raise').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_frontlineRaiseReps.set_value(e.value)).classes('w-1/4').props('aria-label="Frontline Raise Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_frontlineRaiseSets.set_value(e.value)).classes('w-1/4').props('aria-label="Frontline Raise Sets"')
            ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_frontlineRaiseWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Frontline Raise Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Arnold Presses').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_shoulderPressReps.set_value(e.value)).classes('w-1/4').props('aria-label="Shoulder Press Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_shoulderPressSets.set_value(e.value)).classes('w-1/4').props('aria-label="Shoulder Press Sets"')
            ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_shoulderPressWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Shoulder Press Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Elbow Out Row').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_elbowOutRowReps.set_value(e.value)).classes('w-1/4').props('aria-label="Elbow Out Row Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_elbowOutRowSets.set_value(e.value)).classes('w-1/4').props('aria-label="Elbow Out Row Sets"')
            ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_elbowOutRowWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Elbow Out Row Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Supinating Bicep Curl').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_bicepCurlReps.set_value(e.value)).classes('w-1/4').props('aria-label="Bicep Curls Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_bicepCurlSets.set_value(e.value)).classes('w-1/4').props('aria-label="Bicep Curls Sets"')
            ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_bicepCurlWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Bicep Curls Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Close Grip Pushup').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_closeGripPushupReps.set_value(e.value)).classes('w-1/4').props('aria-label="Close Grip Pushup Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_closeGripPushupSets.set_value(e.value)).classes('w-1/4').props('aria-label="Close Grip Pushup Sets"')
            ui.number(label = 'STAIR', value ="", on_change = lambda e: u_closeGripPushupWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Close Grip Pushup Stair"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Seated Rear Delt Fly').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_rearDeltFlyReps.set_value(e.value)).classes('w-1/4').props('aria-label="Rear Delt Fly Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_rearDeltFlySets.set_value(e.value)).classes('w-1/4').props('aria-label="Rear Delt Fly Sets"')
            ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_rearDeltFlyWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Rear Delt Fly Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Standing Side Bend').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_sideBendReps.set_value(e.value)).classes('w-1/4').props('aria-label="Side Bend Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_sideBendSets.set_value(e.value)).classes('w-1/4').props('aria-label="Side Bend Sets"')
            ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_sideBendWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Side Bend Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Lateral Raise').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_lateralRaiseReps.set_value(e.value)).classes('w-1/4').props('aria-label="Lateral Raise Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_lateralRaiseSets.set_value(e.value)).classes('w-1/4').props('aria-label="Lateral Raise Sets"')
            ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_lateralRaiseWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Lateral Raise Weight"')
        with ui.row().classes('w-full no-wrap py-4'):
            ui.label('LOWER BODY WORK').classes('text-lg')        
        with ui.row().classes('w-full no-wrap'):
            ui.label('Stiff Leg RDL').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_stiffLegRDLReps.set_value(e.value)).classes('w-1/4').props('aria-label="Stiff Leg RDL Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_stiffLegRDLSets.set_value(e.value)).classes('w-1/4').props('aria-label="Stiff Leg RDL Sets"')
            ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_stiffLegRDLWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Stiff Leg RDL Sets"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Hamstring Curl').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_hamstringCurlReps.set_value(e.value)).classes('w-1/4').props('aria-label="Hamstring Curl Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_hamstringCurlSets.set_value(e.value)).classes('w-1/4').props('aria-label="Hamstring Curl Sets"')
            ui.label(" ").classes('w-1/4')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Hip Thruster').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_hipThrusterReps.set_value(e.value)).classes('w-1/4').props('aria-label="Hip Thruster Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_hipThrusterSets.set_value(e.value)).classes('w-1/4').props('aria-label="Hip Thruster Sets"')
            ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_hipThrusterWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Hip Thruster Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Front Squat').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_frontSquatReps.set_value(e.value)).classes('w-1/4').props('aria-label="Front Squat Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_frontSquatSets.set_value(e.value)).classes('w-1/4').props('aria-label="Front Squat Sets"')
            ui.number(label = 'STAIR', value ="", on_change = lambda e: u_frontSquatWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Front Squat Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Sumo Squat').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_sumoSquatReps.set_value(e.value)).classes('w-1/4').props('aria-label="Forward Lunge Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_sumoSquatSets.set_value(e.value)).classes('w-1/4').props('aria-label="Forward Lunge Sets"')
            ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_sumoSquatWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Forward Lunge Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Cyclist Squat').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_cyclistSquatReps.set_value(e.value)).classes('w-1/4').props('aria-label="Cyclist Squat Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_cyclistSquatSets.set_value(e.value)).classes('w-1/4').props('aria-label="Cyclist Squat Sets"')
            ui.label(" ").classes('w-1/4')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Calf Raise').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_calfRaiseReps.set_value(e.value)).classes('w-1/4').props('aria-label="Calf Raise Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_calfRaiseSets.set_value(e.value)).classes('w-1/4').props('aria-label="Calf Raise Sets"')
            ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_calfRaiseWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Cald Raise Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Long Lever Crunches').classes('w-1/4')
            ui.number(label = 'REPS', value ="", on_change = lambda e: u_longLeverCrunchesReps.set_value(e.value)).classes('w-1/4').props('aria-label="Calf Raise Reps"')
            ui.number(label = 'SETS', value ="", on_change = lambda e: u_longLeverCrunchesSets.set_value(e.value)).classes('w-1/4').props('aria-label="Calf Raise Sets"')
            ui.label("").classes('w-1/4')
        with ui.row().classes('w-full no-wrap py-4'):
            ui.label('CORE WORK').classes('text-lg')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Sideline Sculpt').classes('w-1/4')
            ui.number(label = 'DONE', value ="", on_change = lambda e: u_sidelineSculpt.set_value(e.value)).classes('w-1/4').props('aria-label="Long Lever Crunch Reps"')
            ui.label(" ").classes('w-1/4')
            ui.label(" ").classes('w-1/4')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Abdominals').classes('w-1/4')
            ui.number(label = 'DONE', value ="", on_change = lambda e: u_abdominals.set_value(e.value)).classes('w-1/4').props('aria-label="Long Lever Cruch Sets"')
            ui.label(" ").classes('w-1/4')
            ui.label(" ").classes('w-1/4')
        with ui.row().classes('w-full no-wrap'):
            ui.button('SAVE', on_click = save)
            ui.button('EXIT', on_click = app.shutdown)

with ui.tab_panels(tabs, value = 'WORKOUT DATA'):
    with ui.tab_panel('WORKOUT DATA'):
        conn = sqlite3.connect(dataBasePath)
        dfSQL = pd.read_sql_query("SELECT * FROM WORKOUTS", conn)
        conn.close()
        df = dfSQL.drop(columns = ['ID'])
        df = df.sort_values(by=['DATE'])
        df_last8=df.drop(columns = ['DATE',                 
                        'FRONTLINE_SETS',
                        'FRONTLINE_WEIGHT',
                        'SHOULDERZPRESS_SETS',
                        'SHOULDERZPRESS_WEIGHT',
                        'ELBOWOUTROW_SETS',
                        'ELBOWOUTROW_WEIGHT',
                        'SUPINEBICEPCURL_SETS',
                        'SUPINEBICEPCURL_WEIGHT',
                        'CLOSEGRIPPUSHUP_SETS',
                        'CLOSEGRIPPUSHUP_STAIR',
                        'REARDELTFLY_SETS',
                        'REARDELTFLY_WEIGHT',
                        'SIDEBEND_SETS',
                        'SIDEBEND_WEIGHT',
                        'LATERALRAISE_SETS',
                        'LATERALRAISE_WEIGHT',
                        'STIFFLEGRDL_SETS',
                        'STIFFLEGRDL_WEIGHT',
                        'SLIDERHAMSTRINGCURL_SETS',
                        'HIPTHRUSTER_SETS',
                        'HIPTHRUSTER_WEIGHT',
                        'FORWARDSQUAT_SETS',
                        'FORWARDSQUAT_WEIGHT',
                        'SUMOSQUAT_SETS',
                        'SUMOSQUAT_WEIGHT',
                        'CYCLISTSQUAT_SETS',
                        'SINGLELEGCALFRAISE_SETS',
                        'LONGLEVERCRUNCHES_SETS'
                        ]
                        )
        df_last8 = df_last8.rename(columns = {
                        'FRONTLINE_REPS': "Frontline POW Raise", 
                        'SHOULDERZPRESS_REPS': "Arnold Press", 
                        'ELBOWOUTROW_REPS': "Elbow Out Row", 
                        'SUPINEBICEPCURL_REPS': "Supinating Bicep Curl", 
                        'CLOSEGRIPPUSHUP_REPS' : "Close Grip Pushup",
                        'REARDELTFLY_REPS': "Rear Delt Fly", 
                        'SIDEBEND_REPS': "Side Bend", 
                        'LATERALRAISE_REPS': "Lateral Raise",
                        'STIFFLEGRDL_REPS': "Stiff Legged RDL", 
                        'SLIDERHAMSTRINGCURL_REPS': "Hamstring Curls",
                        'HIPTHRUSTER_REPS': "Hip Thrusters",
                        'FORWARDSQUAT_REPS': "Forward Squat",
                        'SUMOSQUAT_REPS': "Sumo Squat",
                        'CYCLISTSQUAT_REPS': "Cyclist Squat",
                        'SINGLELEGCALFRAISE_REPS': "Single Leg Calf Raise",
                        'LONGLEVERCRUNCHES_REPS' : "Long Lever Crunches",
                        'SIDELINESCULPT': "Sideline Sculpt",
                        'ABDOMINALS' : "Abdominals"
                        }
                    )
        df = df.rename(
                columns = {
                        'DATE':                     'Date',
                        'FRONTLINE_REPS':           'Frontline reps',
                        'FRONTLINE_SETS':           'Frontline sets',
                        'FRONTLINE_WEIGHT':         'Frontline weight',
                        'DOWNDOGPUSHUP_REPS':       'Downdog reps',
                        'DOWNDOGPUSHUP_SETS':       'Downdog sets',
                        'SHOULDERZPRESS_REPS':      'Shoulder press reps',
                        'SHOULDERZPRESS_SETS':      'Shoulder press sets',
                        'SHOULDERZPRESS_WEIGHT':    'Shoulder press weight',
                        'ELBOWOUTROW_REPS':         'Elbow Out Row reps',
                        'ELBOWOUTROW_SETS':         'Elbow Out Row sets',
                        'ELBOWOUTROW_WEIGHT':       'Elbow Out Row weight',
                        'SUPINEBICEPCURL_REPS':     'Bicep Curl reps',
                        'SUPINEBICEPCURL_SETS':     'Bicep Curl sets',
                        'SUPINEBICEPCURL_WEIGHT':   'Bicep Curl weight',
                        'CLOSEGRIPPUSHUP_REPS':     'Close Grip Pushup reps',
                        'CLOSEGRIPPUSHUP_SETS':     'Close Grip Pshup sets',
                        'CLOSEGRIPPUSHUP_STAIR':    'Close Grip Pushup Stair',
                        'REARDELTFLY_REPS':         'Rear Delt Fly reps',
                        'REARDELTFLY_SETS':         'Rear Delt Fly sets',
                        'REARDELTFLY_WEIGHT':       'Rear Delt Fly weight',
                        'SIDEBEND_REPS':            'Side Bend reps',
                        'SIDEBEND_SETS':            'Side Bend sets',
                        'SIDEBEND_WEIGHT':          'Side Bend weight',
                        'LATERALRAISE_REPS':        'Lateral Raise reps',
                        'LATERALRAISE_SETS':        'Lateral Raise sets',
                        'LATERALRAISE_WEIGHT':      'Lateral Raise weight',
                        'STIFFLEGRDL_REPS' :        'Stiff Leg RDL reps',
                        'STIFFLEGRDL_SETS' :        'Stiff Leg RDL sets',
                        'STIFFLEGRDL_WEIGHT' :      'Stiff Leg RDL weight',
                        'SLIDERHAMSTRINGCURL_REPS' :'Slider Hamstring Curls reps',
                        'SLIDERHAMSTRINGCURL_SETS' :'Slider Hamstring Curls sets',
                        'HIPTHRUSTER_REPS' :        'Hip Thruster reps',
                        'HIPTHRUSTER_SETS' :        'Hip thruster sets',
                        'HIPTHRUSTER_WEIGHT' :      'Hip thruster weight',
                        'FORWARDSQUAT_REPS' :       'Front Squat reps',
                        'FORWARDSQUAT_SETS' :       'Front Squat sets',
                        'FORWARDSQUAT_WEIGHT' :     'Front Squat weight',
                        'SUMOSQUAT_REPS' :          'Sumo Squat reps',
                        'SUMOSQUAT_SETS' :          'Sumo Squat sets',
                        'SUMOSQUAT_WEIGHT' :        'Sumo Squat weight',
                        'CYCLISTSQUAT_REPS' :       'Cyclist Squat reps',
                        'CYCLISTSQUAT_SETS' :       'Cyclist Squat sets',
                        'SINGLELEGCALFRAISE_REPS' : 'Single-Leg Calf Raise reps',
                        'SINGLELEGCALFRAISE_SETS' : 'Single-Leg Calf Raise sets',
                        'LONGLEVERCRUNCHES_REPS' :  'Long Lever Crunches reps',
                        'LONGLEVERCRUNCHES_SETS' :  'Long Lever Crunches sets',
                        'SIDELINESCULPT' :          'Sideline Scupt',
                        'ABDOMINALS' :              'Abdominals',
                        }
                )
        with ui.row():
            ui.label("Last 8 Exercises").classes('text-2xl text-bold')
        with ui.row():
            with ui.card():
                ui.label("Completed Exercises").classes("text-lg text-bold")
                column_names = df_last8.columns[df_last8.any()]      
                column_list = column_names.tolist()
                my_column = ui.column()
                with ui.column():
                    for item in column_list:
                        ui.label(item)

            with ui.card():
                ui.label("Exercises Not Completed").classes("text-lg text-bold")
                column_names = df_last8.columns[(df_last8 == 0).all()]      
                column_list = column_names.tolist()
                my_column = ui.column()
                with ui.column():
                    for item in column_list:
                        ui.label(item)
        with ui.row():
            ui.label('Cumulative Exercise Log').classes("text-2xl text-bold")
        ui.table(columns=[{'name' : col, 'label' : col, 'field': col} for col in df.columns],rows=df.to_dict('records'),)

with ui.footer(value=True) as footer:
    def github() -> ui.html:
        """
        Retrieve and return the GitHub icon as HTML.

        This function reads the content of the "github.svg" file located in the ROOT_DIR
        and returns it as HTML using the ui.html class.

        Returns
        -------
        ui.html
            HTML representation of the GitHub icon.

        Examples
        --------
        >>> github()
        <ui.html>...</ui.html>
        """
        return ui.html(Path(ROOT_DIR).joinpath("github.svg").read_text())
    with ui.row().classes(
            "w-screen no-wrap justify-center items-center text-l font-bold"
            ):
        ui.label(
                "Copyright © 2023 Michael Ryan Hunsaker, M.Ed., Ph.D."
                ).classes("justify-center items-center")
    with ui.row().classes(
            "w-screen no-wrap justify-center items-center text-l font-bold"
            ):
        with ui.link(target="https://github.com/mrhunsaker/FitnessTracker").classes(
                "max-[305px]:hidden"
            ).tooltip("GitHub"):
            github().classes("fill-white scale-125 m-1")

def getresolution() -> str:
    """
    Retrieve the screen resolution.

    This function iterates through all available monitors using the get_monitors
    function from the screeninfo module and returns the resolution of the last monitor
    in the format "widthxheight". If no monitors are available, an empty string is returned.

    Returns
    -------
    str
        Screen resolution in the format "widthxheight".

    Examples
    --------
    >>> getresolution()
    '1920x1080'
    """
    SCREEN = " "
    for SCREEN in get_monitors():
        SCREENRESOLUTION = "{str(SCREEN.width)}x{str(SCREEN.height)}"
    return SCREEN


MONITOR = getresolution()
print(f'SQLite Version is: {sqlite3.sqlite_version}')
print(f'SQLite DB-API Version is: {sqlite3.version}')
print(f'Monitor: \nwidth = {MONITOR.width} \nheight = {MONITOR.height}')
ui.run(
        native=True,
        reload=False,
        dark=False,
        title="Fitness Tracking",
        fullscreen=False,
        window_size=(MONITOR.width, MONITOR.height - 72),
        )
