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

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from nicegui import app, ui
from pandas.api.types import is_bool_dtype, is_numeric_dtype
from plotly.subplots import make_subplots

##############################################################################
# Define Paths
##############################################################################
os.chdir(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DIR = ""

##############################################################################
# Set User Directory based on OS
##############################################################################

if os.name == 'nt':
    tmppath = Path(os.environ['USERPROFILE']).joinpath('Documents')
    Path.mkdir(tmppath, parents = True, exist_ok = True)
    USER_DIR = Path(tmppath)
    tmppath = Path(os.environ['USERPROFILE']).joinpath('Documents', 'Fitness')
    Path.mkdir(tmppath, parents = True, exist_ok = True)
elif os.name == 'posix':
    tmppath = Path(os.environ['HOME']).joinpath('Documents')
    Path.mkdir(tmppath, parents = True, exist_ok = True)
    USER_DIR = Path(tmppath)
    tmppath = Path(os.environ['USERPROFILE']).joinpath('Documents', 'Fitness')
    Path.mkdir(tmppath, parents = True, exist_ok = True)
else:
    print("Error! Cannot find HOME directory")
# end if

os.chdir(USER_DIR)

dataBasePath = Path(USER_DIR).joinpath('Fitness/workoutLog.db')

##############################################################################
# Create SQL database with SQLite and create data tables
##############################################################################
print(f"SQLite version {sqlite3.sqlite_version}")


def create_connection(db_file):
    """

    :param db_file:
    :type db_file:
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
        # end if
    # end try


# end def create_connection

if __name__ == '__main__':
    create_connection(dataBasePath)


# end if


def create_connection(db_file):
    """

    :param db_file:
    :type db_file:
    :return:
    :rtype:
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    # end try
    return conn


# end def create_connection


def create_table(conn, sql_create_sql_table):
    """

    :param conn:
    :type conn:
    :param sql_create_sql_table:
    :type sql_create_sql_table:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_sql_table)
    except Error as e:
        print(e)
    # end try
    conn.close()


# end def create_table


def main():
    """

    """
    sql_create_upperbody_table = """CREATE TABLE IF NOT EXISTS UPPERBODY (
        ID                      INTEGER PRIMARY KEY AUTOINCREMENT,
        DATE                    TEXT NOT NULL,
        FRONTLINE_REPS          INTEGER NOT NULL,
        FRONTLINE_SETS          INTEGER NOT NULL,
        FRONTLINE_WEIGHT        INTEGER NOT NULL,
        DOWNDOGPUSHUP_REPS      INTEGER NOT NULL,
        DOWNDOGPUSHUP_SETS      INTEGER NOT NULL,
        SHOULDERZPRESS_REPS	    INTEGER NOT NULL,
        SHOULDERZPRESS_SETS	    INTEGER NOT NULL,
        SHOULDERZPRESS_WEIGHT	INTEGER NOT NULL,
        ELBOWOUTROW_REPS	    INTEGER NOT NULL,
        ELBOWOUTROW_SETS	    INTEGER NOT NULL,
        ELBOWOUTROW_WEIGHT	    INTEGER NOT NULL,
        SUPINEBICEPCURL_REPS	INTEGER NOT NULL,
        SUPINEBICEPCURL_SETS	INTEGER NOT NULL,
        SUPINEBICEPCURL_WEIGHT	INTEGER NOT NULL,
        CLOSEGRIPPUSHUP_REPS    INTEGER NOT NULL,
        CLOSEGRIPPUSHUP_SETS    INTEGER NOT NULL,
        CLOSEGRIPPUSHUP_STAIR   INTEGER NOT NULL,
        REARDELTFLY_REPS	    INTEGER NOT NULL,
        REARDELTFLY_SETS        INTEGER NOT NULL,
        REARDELTFLY_WEIGHT      INTEGER NOT NULL,
        SIDEBEND_REPS	        INTEGER NOT NULL,
        SIDEBEND_SETS           INTEGER NOT NULL,
        SIDEBEND_WEIGHT         INTEGER NOT NULL,
        LATERALRAISE_REPS	    INTEGER NOT NULL,
        LATERALRAISE_SETS	    INTEGER NOT NULL,
        LATERALRAISE_WEIGHT	    INTEGER NOT NULL
    );"""

    sql_create_lowerbody_table = """CREATE TABLE IF NOT EXISTS LOWERBODY (
        ID	                        INTEGER PRIMARY KEY AUTOINCREMENT,
        DATE	                    TEXT NOT NULL,
        ONELEGBRIDGE_REPS 	        INTEGER NOT NULL,
        ONELEGBRIDGE_SETS 	        INTEGER NOT NULL,
        WORLDSGREATEST_REPS     	INTEGER NOT NULL,
        WORLDSGREATEST_SETS 	    INTEGER NOT NULL,
        STIFFLEGRDL_REPS	        INTEGER NOT NULL,
        STIFFLEGRDL_SETS	        INTEGER NOT NULL,
        STIFFLEGRDL_WEIGHT          INTEGER NOT NULL,
        SLIDERHAMSTRINGCURL_REPS 	INTEGER NOT NULL,
        SLIDERHAMSTRINGCURL_SETS 	INTEGER NOT NULL,
        HIPTHRUSTER_REPS	        INTEGER NOT NULL,
        HIPTHRUSTER_SETS	        INTEGER NOT NULL,
        HIPTHRUSTER_WEIGHT	        INTEGER NOT NULL,
        FORWARDSQUAT_REPS	        INTEGER NOT NULL,
        FORWARDSQUAT_SETS	        INTEGER NOT NULL,
        FORWARDSQUAT_WEIGHT	        INTEGER NOT NULL,
        FORWARDLUNGE_REPS	        INTEGER NOT NULL,
        FORWARDLUNGE_SETS	        INTEGER NOT NULL,
        FORWARDLUNGE_WEIGHT	        INTEGER NOT NULL,
        CYCLISTSQUAT_REPS	        INTEGER NOT NULL,
        CYCLISTSQUAT_SETS	        INTEGER NOT NULL,
        SINGLELEGCALFRAISE_REPS	    INTEGER NOT NULL,
        SINGLELEGCALFRAISE_SETS	    INTEGER NOT NULL,
        LONGLEVERCRUNCHES_REPS	    INTEGER NOT NULL,
        LONGLEVERCRUNCHES_SETS	    INTEGER NOT NULL
    );"""

    conn = create_connection(dataBasePath)
    if conn is not None:
        create_table(conn, sql_create_upperbody_table)
    else:
        print("Error! cannot create the database connection.")
    # end if
    conn.close()
    conn = create_connection(dataBasePath)
    if conn is not None:
        create_table(conn, sql_create_lowerbody_table)
    else:
        print("Error! cannot create the database connection.")
    # end if
    conn.close()


# end def main


if __name__ == '__main__':
    main()
# end if


datenow = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")

with ui.header().classes(replace = 'row items-center') as header:
    ui.button(on_click = lambda: left_drawer.toggle()).props('flat color=white icon=menu')
with ui.tabs() as tabs:
    ui.tab('UPPER BODY INPUT')
    ui.tab('UPPER BODY DATA')
    ui.tab('LOWER BODY INPUT')
    ui.tab('LOWER BODY DATA')
    ui.tab('OVERALL GRAPHS')
with ui.tab_panels(tabs, value = 'UPPER BODY INPUT'):
    with ui.tab_panel('UPPER BODY INPUT'):
        date = ui.date().classes('hidden')
        u_frontlineRaiseSets = ui.number().classes('hidden')
        u_frontlineRaiseReps = ui.number().classes('hidden')
        u_frontlineRaiseWeight = ui.number().classes('hidden')
        u_downdogPushupReps = ui.number().classes('hidden')
        u_downdogPushupSets = ui.number().classes('hidden')
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


        def upperbodysave(event):
            """
            :param event:
            :type event:
            """
            date = datenow
            frontlineRaiseReps = int(u_frontlineRaiseReps.value)
            frontlineRaiseSets = int(u_frontlineRaiseReps.value)
            frontlineRaiseWeight = int(u_frontlineRaiseReps.value)
            downdogPushupReps = int(u_downdogPushupReps.value)
            downdogPushupSets = int(u_downdogPushupSets.value)
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

            def data_entry():
                """

                """
                conn = sqlite3.connect(dataBasePath)
                if conn is not None:
                    c = conn.cursor()
                    c.execute(
                            """INSERT INTO UPPERBODY (
                        DATE,
                        FRONTLINE_REPS,
                        FRONTLINE_SETS,
                        FRONTLINE_WEIGHT,
                        DOWNDOGPUSHUP_REPS,
                        DOWNDOGPUSHUP_SETS,
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
                        LATERALRAISE_WEIGHT
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
                        ?
                        )
                        """,
                            (
                                    date,
                                    frontlineRaiseReps,
                                    frontlineRaiseSets,
                                    frontlineRaiseWeight,
                                    downdogPushupReps,
                                    downdogPushupSets,
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
                                    lateralRaiseWeight
                                    )
                            )
                    conn.commit()
                else:
                    print("Error! cannot create the database connection.")
                # end if
                conn.close()
                ui.notify('Uploaded Successfully!', close_button = 'OK')

            data_entry()


        with ui.row().classes('w-full no-wrap'):
            ui.date(value = 'f{datenow}', on_change = lambda e: date.set_value(e.value)).classes('w-1/2')
        with ui.row().classes('w-full no-wrap py-4'):
            ui.label('EXERCISE').classes('w-1/4')
            ui.label('REPS').classes('w-1/4')
            ui.label('SETS').classes('w-1/4')
            ui.label('WEIGHT').classes('w-1/4')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Frontline Raise').classes('w-1/4')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_frontlineRaiseReps.set_value(e.value)).classes('w-1/4').props('aria-label="Frontline Raise Reps"')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_frontlineRaiseSets.set_value(e.value)).classes('w-1/4').props('aria-label="Frontline Raise Sets"')
            ui.number(label = 'WEIGHT', value = "", on_change = lambda e: u_frontlineRaiseWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Frontline Raise Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Dow Dog to Pushup').classes('w-1/4')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_downdogPushupReps.set_value(e.value)).classes('w-1/4').props('aria-label="Down Dog to Pushup Reps"')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_downdogPushupSets.set_value(e.value)).classes('w-1/4').props('aria-label="Down Dog to Pushup Sets"')
            ui.label(' ').classes('w-1/4')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Shoulder Z-Press').classes('w-1/4')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_shoulderPressReps.set_value(e.value)).classes('w-1/4').props('aria-label="Shoulder Press Reps"')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_shoulderPressSets.set_value(e.value)).classes('w-1/4').props('aria-label="Shoulder Press Sets"')
            ui.number(label = 'WEIGHT', value = "", on_change = lambda e: u_shoulderPressWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Shoulder Press Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Elbow Out Row').classes('w-1/4')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_elbowOutRowReps.set_value(e.value)).classes('w-1/4').props('aria-label="Elbow Out Row Reps"')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_elbowOutRowSets.set_value(e.value)).classes('w-1/4').props('aria-label="Elbow Out Row Sets"')
            ui.number(label = 'WEIGHT', value = "", on_change = lambda e: u_elbowOutRowWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Elbow Out Row Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Supinating Bicep Curl').classes('w-1/4')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_bicepCurlReps.set_value(e.value)).classes('w-1/4').props('aria-label="Bicep Curls Reps"')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_bicepCurlSets.set_value(e.value)).classes('w-1/4').props('aria-label="Bicep Curls Sets"')
            ui.number(label = 'WEIGHT', value = "", on_change = lambda e: u_bicepCurlWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Bicep Curls Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Close Grip Pushup').classes('w-1/4')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_closeGripPushupReps.set_value(e.value)).classes('w-1/4').props('aria-label="Close Grip Pushup Reps"')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_closeGripPushupSets.set_value(e.value)).classes('w-1/4').props('aria-label="Close Grip Pushup Sets"')
            ui.number(label = 'STAIR', value = "", on_change = lambda e: u_closeGripPushupWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Close Grip Pushup Stair"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Seated Rear Delt Fly').classes('w-1/4')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_rearDeltFlyReps.set_value(e.value)).classes('w-1/4').props('aria-label="Rear Delt Fly Reps"')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_rearDeltFlySets.set_value(e.value)).classes('w-1/4').props('aria-label="Rear Delt Fly Sets"')
            ui.number(label = 'WEIGHT', value = "", on_change = lambda e: u_rearDeltFlyWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Rear Delt Fly Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Standing Side Bend').classes('w-1/4')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_sideBendReps.set_value(e.value)).classes('w-1/4').props('aria-label="Side Bend Reps"')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_sideBendSets.set_value(e.value)).classes('w-1/4').props('aria-label="Side Bend Sets"')
            ui.number(label = 'WEIGHT', value = "", on_change = lambda e: u_sideBendWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Side Bend Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Lateral Raise').classes('w-1/4')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_lateralRaiseReps.set_value(e.value)).classes('w-1/4').props('aria-label="Lateral Raise Reps"')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_lateralRaiseSets.set_value(e.value)).classes('w-1/4').props('aria-label="Lateral Raise Sets"')
            ui.number(label = 'WEIGHT', value = "", on_change = lambda e: u_lateralRaiseWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Lateral Raise Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.button('SAVE', on_click = upperbodysave)
            ui.button('EXIT', on_click = app.shutdown)
with ui.tab_panels(tabs, value = 'LOWER BODY INPUT'):
    with ui.tab_panel('LOWER BODY INPUT'):
        date = ui.date().classes('hidden')
        u_singleLegBridgeReps = ui.number().classes('hidden')
        u_singleLegBridgeSets = ui.number().classes('hidden')
        u_worldsGreatestReps = ui.number().classes('hidden')
        u_worldsGreatestSets = ui.number().classes('hidden')
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
        u_forwardLungeReps = ui.number().classes('hidden')
        u_forwardLungeSets = ui.number().classes('hidden')
        u_forwardLungeWeight = ui.number().classes('hidden')
        u_cyclistSquatReps = ui.number().classes('hidden')
        u_cyclistSquatSets = ui.number().classes('hidden')
        u_cyclistSquatWeight = ui.number().classes('hidden')
        u_calfRaiseReps = ui.number().classes('hidden')
        u_calfRaiseSets = ui.number().classes('hidden')
        u_calfRaiseWeight = ui.number().classes('hidden')
        u_longLeverReps = ui.number().classes('hidden')
        u_longLeverSets = ui.number().classes('hidden')


        def save(event):
            """
            :param event:
            :type event:
            """
            date = datenow
            singleLegBridgeReps = int(u_singleLegBridgeReps.value)
            singleLegBridgeSets = int(u_singleLegBridgeSets.value)
            worldsGreatestReps = int(u_worldsGreatestReps.value)
            worldsGreatestSets = int(u_worldsGreatestSets.value)
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
            forwardLungeReps = int(u_forwardLungeReps.value)
            forwardLungeSets = int(u_forwardLungeSets.value)
            forwardLungeWeight = int(u_forwardLungeWeight.value)
            cyclistSquatReps = int(u_cyclistSquatReps.value)
            cyclistSquatSets = int(u_cyclistSquatSets.value)
            cyclistSquatWeight = int(u_cyclistSquatSets.value)
            calfRaiseReps = int(u_calfRaiseReps.value)
            calfRaiseSets = int(u_calfRaiseSets.value)
            calfRaiseWeight = int(u_calfRaiseWeight.value)
            longLeverReps = int(u_longLeverReps.value)
            longLeverSets = int(u_longLeverSets.value)

            def data_entry():
                """

                """
                conn = sqlite3.connect(dataBasePath)
                c = conn.cursor()
                c.execute(
                        """INSERT INTO LOWERBODY (
                    DATE,
                    ONELEGBRIDGE_REPS,
                    ONELEGBRIDGE_SETS,
                    WORLDSGREATEST_REPS,
                    WORLDSGREATEST_SETS,
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
                    FORWARDLUNGE_REPS,
                    FORWARDLUNGE_SETS,
                    FORWARDLUNGE_WEIGHT,
                    CYCLISTSQUAT_REPS,
                    CYCLISTSQUAT_SETS,
                    SINGLELEGCALFRAISE_REPS,
                    SINGLELEGCALFRAISE_SETS,
                    LONGLEVERCRUNCHES_REPS,
                    LONGLEVERCRUNCHES_SETS
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
                    ?
                    )
                    """,
                        (
                                date,
                                singleLegBridgeReps,
                                singleLegBridgeSets,
                                worldsGreatestReps,
                                worldsGreatestSets,
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
                                forwardLungeReps,
                                forwardLungeSets,
                                forwardLungeWeight,
                                cyclistSquatReps,
                                cyclistSquatSets,
                                calfRaiseReps,
                                calfRaiseSets,
                                longLeverReps,
                                longLeverSets
                                )
                        )
                conn.commit()
                ui.notify('Uploaded Successfully!', close_button = 'OK')

            data_entry()


        with ui.row().classes('w-ful no-wrap'):
            date = ui.date().classes('hidden')
            ui.date(value = 'f{datenow}', on_change = lambda e: date.set_value(e.value)).classes('w-1/2')
        with ui.row().classes('w-ful no-wrap py-4'):
            ui.label('EXERCISE').classes('w-1/4')
            ui.label('REPS').classes('w-1/4')
            ui.label('SETS').classes('w-1/4')
            ui.label('WEIGHT').classes('w-1/4')

        with ui.row().classes('w-full no-wrap'):
            ui.label('Single Leg Bridge').classes('w-1/4')
            singleLegBridgeReps = ui.number().classes('hidden')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_singleLegBridgeReps.set_value(e.value)).classes('w-1/4').props('aria-label="Single Leg Bridge Reps"')
            singleLegBridgeSets = ui.number().classes('hidden')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_singleLegBridgeSets.set_value(e.value)).classes('w-1/4').props('aria-label="Single Leg Bridge Sets"')
            ui.label(' ').classes('w-1/4')
        with ui.row().classes('w-full no-wrap'):
            ui.label("World's Greatest Stretch").classes('w-1/4')
            worldsGreatestReps = ui.number().classes('hidden')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_worldsGreatestReps.set_value(e.value)).classes('w-1/4').props('aria-label="World\'s Greatest Stretch Reps"')
            worldsGreatestSets = ui.number().classes('hidden')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_worldsGreatestSets.set_value(e.value)).classes('w-1/4').props('aria-label="World\'s Greatest Stretch Sets"')
            ui.label(' ').classes('w-1/4')

        with ui.row().classes('w-full no-wrap'):
            ui.label('Stiff Leg RDL').classes('w-1/4')
            stiffLegRDLReps = ui.number().classes('hidden')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_stiffLegRDLReps.set_value(e.value)).classes('w-1/4').props('aria-label="Stiff Leg RDL Reps"')
            stiffLegRDLSets = ui.number().classes('hidden')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_stiffLegRDLSets.set_value(e.value)).classes('w-1/4').props('aria-label="Stiff Leg RDL Sets"')
            stiffLegRDLWeight = ui.number().classes('hidden')
            ui.number(label = 'WEIGHT', value = "", on_change = lambda e: u_stiffLegRDLWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Stiff Leg RDL Sets"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Hamstring Curl').classes('w-1/4')
            hamstringCurlReps = ui.number().classes('hidden')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_hamstringCurlReps.set_value(e.value)).classes('w-1/4').props('aria-label="Hamstring Curl Reps"')
            hamstringCurlSets = ui.number().classes('hidden')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_hamstringCurlSets.set_value(e.value)).classes('w-1/4').props('aria-label="Hamstring Curl Sets"')
            ui.label(' ').classes('w-1/4')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Hip Thruster').classes('w-1/4')
            hipThrusterReps = ui.number().classes('hidden')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_hipThrusterReps.set_value(e.value)).classes('w-1/4').props('aria-label="Hip Thruster Reps"')
            hipThrusterSets = ui.number().classes('hidden')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_hipThrusterSets.set_value(e.value)).classes('w-1/4').props('aria-label="Hip Thruster Sets"')
            hipThrusterWeight = ui.number().classes('hidden')
            ui.number(label = 'WEIGHT', value = "", on_change = lambda e: u_hipThrusterWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Hip Thruster Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Front Squat').classes('w-1/4')
            frontSquatReps = ui.number().classes('hidden')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_frontSquatReps.set_value(e.value)).classes('w-1/4').props('aria-label="Front Squat Reps"')
            frontSquatSets = ui.number().classes('hidden')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_frontSquatSets.set_value(e.value)).classes('w-1/4').props('aria-label="Front Squat Sets"')
            frontSquatWeight = ui.number().classes('hidden')
            ui.number(label = 'STAIR', value = "", on_change = lambda e: u_frontSquatWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Front Squat Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Forward Lunge').classes('w-1/4')
            forwardLungeReps = ui.number().classes('hidden')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_forwardLungeReps.set_value(e.value)).classes('w-1/4').props('aria-label="Forward Lunge Reps"')
            forwardLungeSets = ui.number().classes('hidden')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_forwardLungeSets.set_value(e.value)).classes('w-1/4').props('aria-label="Forward Lunge Sets"')
            forwardLungeWeight = ui.number().classes('hidden')
            ui.number(label = 'WEIGHT', value = "", on_change = lambda e: u_forwardLungeWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Forward Lunge Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Cyclist Squat').classes('w-1/4')
            cyclistSquatReps = ui.number().classes('hidden')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_cyclistSquatReps.set_value(e.value)).classes('w-1/4').props('aria-label="Cyclist Squat Reps"')
            cyclistSquatSets = ui.number().classes('hidden')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_cyclistSquatSets.set_value(e.value)).classes('w-1/4').props('aria-label="Cyclist Squat Sets"')
            cyclistSquatWeight = ui.number().classes('hidden')
            ui.number(label = 'WEIGHT', value = "", on_change = lambda e: u_cyclistSquatWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Cyclist Squat Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Calf Raise').classes('w-1/4')
            calfRaiseReps = ui.number().classes('hidden')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_calfRaiseReps.set_value(e.value)).classes('w-1/4').props('aria-label="Calf Raise Reps"')
            calfRaiseSets = ui.number().classes('hidden')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_calfRaiseSets.set_value(e.value)).classes('w-1/4').props('aria-label="Calf Raise Sets"')
            calfRaiseWeight = ui.number().classes('hidden')
            ui.number(label = 'WEIGHT', value = "", on_change = lambda e: u_calfRaiseWeight.set_value(e.value)).classes('w-1/4').props('aria-label="Cald Raise Weight"')
        with ui.row().classes('w-full no-wrap'):
            ui.label('Long Lever Crunches').classes('w-1/4')
            longLeverReps = ui.number().classes('hidden')
            ui.number(label = 'REPS', value = "", on_change = lambda e: u_longLeverReps.set_value(e.value)).classes('w-1/4').props('aria-label="Long Lever Crunch Reps"')
            longLeverSets = ui.number().classes('hidden')
            ui.number(label = 'SETS', value = "", on_change = lambda e: u_longLeverSets.set_value(e.value)).classes('w-1/4').props('aria-label="Long Lever Cruch Sets"')
            ui.label().classes('w-1/4')
        with ui.row().classes('w-full no-wrap'):
            ui.button('SAVE', on_click = save)
            ui.button('EXIT', on_click = app.shutdown)

with ui.tab_panels(tabs, value = 'UPPER BODY DATA'):
    with ui.tab_panel('UPPER BODY DATA'):
        conn = sqlite3.connect(dataBasePath)
        dfSQL = pd.read_sql_query("SELECT * FROM UPPERBODY", conn)
        conn.close()
        df = dfSQL.drop(columns = ['ID'])
        df = df.rename(
                columns = {
                        'DATE':                   'Date',
                        'FRONTLINE_REPS':         'Frontline reps',
                        'FRONTLINE_SETS':         'Frontline sets',
                        'FRONTLINE_WEIGHT':       'Frontline weight',
                        'DOWNDOGPUSHUP_REPS':     'Downdog reps',
                        'DOWNDOGPUSHUP_SETS':     'Downdog sets',
                        'SHOULDERZPRESS_REPS':    'Shoulder press reps',
                        'SHOULDERZPRESS_SETS':    'Shoulder press sets',
                        'SHOULDERZPRESS_WEIGHT':  'Shoulder press weight',
                        'ELBOWOUTROW_REPS':       'Elbow Out Row reps',
                        'ELBOWOUTROW_SETS':       'Elbow Out Row sets',
                        'ELBOWOUTROW_WEIGHT':     'Elbow Out Row weight',
                        'SUPINEBICEPCURL_REPS':   'Bicep Curl reps',
                        'SUPINEBICEPCURL_SETS':   'Bicep Curl sets',
                        'SUPINEBICEPCURL_WEIGHT': 'Bicep Curl weight',
                        'CLOSEGRIPPUSHUP_REPS':   'Close Grip Pushup reps',
                        'CLOSEGRIPPUSHUP_SETS':   'Close Grip Pshup sets',
                        'CLOSEGRIPPUSHUP_STAIR':  'Close Grip Pushup Stair',
                        'REARDELTFLY_REPS':       'Rear Delt Fly reps',
                        'REARDELTFLY_SETS':       'Rear Delt Fly sets',
                        'REARDELTFLY_WEIGHT':     'Rear Delt Fly weight',
                        'SIDEBEND_REPS':          'Side Bend reps',
                        'SIDEBEND_SETS':          'Side Bend sets',
                        'SIDEBEND_WEIGHT':        'Side Bend weight',
                        'LATERALRAISE_REPS':      'Lateral Raise reps',
                        'LATERALRAISE_SETS':      'Lateral Raise sets',
                        'LATERALRAISE_WEIGHT':    'Lateral Raise weight'
                        }
                )


        def update(*, df: pd.DataFrame, r: int, c: int, value):
            df.iat[r, c] = value
            ui.notify(f'Set ({r}, {c}) to {value}')


        with ui.grid(rows = len(df.index) + 1).classes('grid-flow-col'):
            for c, col in enumerate(df.columns):
                ui.label(col).classes('font-bold')
                for r, row in enumerate(df.loc[:, col]):
                    if is_bool_dtype(df[col].dtype):
                        cls = ui.input
                    elif is_numeric_dtype(df[col].dtype):
                        cls = ui.input
                    else:
                        cls = ui.input
                    cls(value = row, on_change = lambda event, r = r, c = c: update(df = df, r = r, c = c, value = event.value))

with ui.tab_panels(tabs, value = 'LOWER BODY DATA'):
    with ui.tab_panel('LOWER BODY DATA'):
        conn = sqlite3.connect(dataBasePath)
        dfSQL = pd.read_sql_query("SELECT * FROM LOWERBODY", conn)
        conn.close()
        df = dfSQL.drop(columns = ['ID'])
        df = df.rename(
                columns = {
                        'DATE':                     'Date',
                        'ONELEGBRIDGE_REPS':        'One Leg Bridge reps',
                        'ONELEGBRIDGE_SETS':        'One Leg Bridge sets',
                        'WORLDSGREATEST_REPS':      'Worlds Greatest Stretch reps',
                        'WORLDSGREATEST_SETS':      'Worlds Greatest Stretch sets',
                        'STIFFLEGRDL_REPS':         'Stiff Leg RDL reps',
                        'STIFFLEGRDL_SETS':         'Stiff Leg RDL sets',
                        'STIFFLEGRDL_WEIGHT':       'Stiff Leg RDL weight',
                        'SLIDERHAMSTRINGCURL_REPS': 'Slider Hamstring Curl reps',
                        'SLIDERHAMSTRINGCURL_SETS': 'Slider Hamstring Curl sets',
                        'HIPTHRUSTER_REPS':         'Hip Thruster reps',
                        'HIPTHRUSTER_SETS':         'Hip Thruster sets',
                        'HIPTHRUSTER_WEIGHT':       'Hip Thruster weight',
                        'FORWARDSQUAT_REPS':        'Forward Squat reps',
                        'FORWARDSQUAT_SETS':        'Forward Squat sets',
                        'FORWARDSQUAT_WEIGHT':      'Forward Squat weight',
                        'FORWARDLUNGE_REPS':        'Forward Lunge reps',
                        'FORWARDLUNGE_SETS':        'Forward Lunge sets',
                        'FORWARDLUNGE_WEIGHT':      'Forward Lunge weight',
                        'CYCLISTSQUAT_REPS':        'Cyclist Squat reps',
                        'CYCLISTSQUAT_SETS':        'Cyclist Squat sets',
                        'SINGLELEGCALFRAISE_REPS':  'Calf Raise reps',
                        'SINGLELEGCALFRAISE_SETS':  'Calf Raise sets',
                        'LONGLEVERCRUNCHES_REPS':   'Long Lever Crunches reps',
                        'LONGLEVERCRUNCHES_SETS':   'Long Lever Crunches sets'
                        }
                )


        def update(*, df: pd.DataFrame, r: int, c: int, value):
            df.iat[r, c] = value
            ui.notify(f'Set ({r}, {c}) to {value}')


        with ui.grid(rows = len(df.index) + 1).classes('grid-flow-col'):
            for c, col in enumerate(df.columns):
                ui.label(col).classes('font-bold')
                for r, row in enumerate(df.loc[:, col]):
                    if is_bool_dtype(df[col].dtype):
                        cls = ui.input
                    elif is_numeric_dtype(df[col].dtype):
                        cls = ui.input
                    else:
                        cls = ui.input
                    cls(value = row, on_change = lambda event, r = r, c = c: update(df = df, r = r, c = c, value = event.value))

with ui.tab_panels(tabs, value = 'GRAPHS'):
    with ui.tab_panel('GRAPHS'):
        conn = sqlite3.connect(dataBasePath)
        dfSQLupper = pd.read_sql_query("SELECT * FROM UPPERBODY", conn)
        conn.close()
        dfSQLupper = dfSQLupper.rename(
                columns = {
                        'DATE':                   'Date',
                        'FRONTLINE_REPS':         'Frontline reps',
                        'FRONTLINE_SETS':         'Frontline sets',
                        'FRONTLINE_WEIGHT':       'Frontline weight',
                        'DOWNDOGPUSHUP_REPS':     'Downdog reps',
                        'DOWNDOGPUSHUP_SETS':     'Downdog sets',
                        'SHOULDERZPRESS_REPS':    'Shoulder press reps',
                        'SHOULDERZPRESS_SETS':    'Shoulder press sets',
                        'SHOULDERZPRESS_WEIGHT':  'Shoulder press weight',
                        'ELBOWOUTROW_REPS':       'Elbow Out Row reps',
                        'ELBOWOUTROW_SETS':       'Elbow Out Row sets',
                        'ELBOWOUTROW_WEIGHT':     'Elbow Out Row weight',
                        'SUPINEBICEPCURL_REPS':   'Bicep Curl reps',
                        'SUPINEBICEPCURL_SETS':   'Bicep Curl sets',
                        'SUPINEBICEPCURL_WEIGHT': 'Bicep Curl weight',
                        'CLOSEGRIPPUSHUP_REPS':   'Close Grip Pushup reps',
                        'CLOSEGRIPPUSHUP_SETS':   'Close Grip Pshup sets',
                        'CLOSEGRIPPUSHUP_STAIR':  'Close Grip Pushup Stair',
                        'REARDELTFLY_REPS':       'Rear Delt Fly reps',
                        'REARDELTFLY_SETS':       'Rear Delt Fly sets',
                        'REARDELTFLY_WEIGHT':     'Rear Delt Fly weight',
                        'SIDEBEND_REPS':          'Side Bend reps',
                        'SIDEBEND_SETS':          'Side Bend sets',
                        'SIDEBEND_WEIGHT':        'Side Bend weight',
                        'LATERALRAISE_REPS':      'Lateral Raise reps',
                        'LATERALRAISE_SETS':      'Lateral Raise sets',
                        'LATERALRAISE_WEIGHT':    'Lateral Raise weight'
                        }
                )
        dfSQLupper = dfSQLupper.set_index("Date")

        mu, sigma = 0, 0.25
        noise = np.random.normal(mu, sigma, [len(dfSQLupper.index), len(dfSQLupper.columns)])
        dfSQLupper = dfSQLupper + noise
        pd.options.plotting.backend = "plotly"
        figUpper = dfSQLupper.plot(
                x = dfSQLupper.index,
                y = ['Frontline weight', 'Shoulder press weight', 'Elbow Out Row weight', 'Bicep Curl weight', 'Close Grip Pushup Stair', 'Rear Delt Fly weight', 'Side Bend weight', 'Lateral Raise weight']
                )
        figUpper.update_yaxes(tickvals = [1, 2, 3, 4, 5, 8, 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55])
        figUpper.update_layout(width = 1000, height = 500)
        # figUpper.show()

        conn = sqlite3.connect(dataBasePath)
        dfSQLlower = pd.read_sql_query("SELECT * FROM LOWERBODY", conn)
        conn.close()
        dfSQLlower = dfSQLlower.rename(
                columns = {
                        'DATE':                     'Date',
                        'ONELEGBRIDGE_REPS':        'One Leg Bridge reps',
                        'ONELEGBRIDGE_SETS':        'One Leg Bridge sets',
                        'WORLDSGREATEST_REPS':      'Worlds Greatest Stretch reps',
                        'WORLDSGREATEST_SETS':      'Worlds Greatest Stretch sets',
                        'STIFFLEGRDL_REPS':         'Stiff Leg RDL reps',
                        'STIFFLEGRDL_SETS':         'Stiff Leg RDL sets',
                        'STIFFLEGRDL_WEIGHT':       'Stiff Leg RDL weight',
                        'SLIDERHAMSTRINGCURL_REPS': 'Slider Hamstring Curl reps',
                        'SLIDERHAMSTRINGCURL_SETS': 'Slider Hamstring Curl sets',
                        'HIPTHRUSTER_REPS':         'Hip Thruster reps',
                        'HIPTHRUSTER_SETS':         'Hip Thruster sets',
                        'HIPTHRUSTER_WEIGHT':       'Hip Thruster weight',
                        'FORWARDSQUAT_REPS':        'Forward Squat reps',
                        'FORWARDSQUAT_SETS':        'Forward Squat sets',
                        'FORWARDSQUAT_WEIGHT':      'Forward Squat weight',
                        'FORWARDLUNGE_REPS':        'Forward Lunge reps',
                        'FORWARDLUNGE_SETS':        'Forward Lunge sets',
                        'FORWARDLUNGE_WEIGHT':      'Forward Lunge weight',
                        'CYCLISTSQUAT_REPS':        'Cyclist Squat reps',
                        'CYCLISTSQUAT_SETS':        'Cyclist Squat sets',
                        'SINGLELEGCALFRAISE_REPS':  'Calf Raise reps',
                        'SINGLELEGCALFRAISE_SETS':  'Calf Raise sets',
                        'LONGLEVERCRUNCHES_REPS':   'Long Lever Crunches reps',
                        'LONGLEVERCRUNCHES_SETS':   'Long Lever Crunches sets'
                        }
                )
        dfSQLlower = dfSQLlower.set_index("Date")

        #
        mu, sigma = 0, 0.25
        noise = np.random.normal(mu, sigma, [len(dfSQLlower.index), len(dfSQLlower.columns)])
        dfSQLlower = dfSQLlower + noise
        pd.options.plotting.backend = "plotly"
        figLower = dfSQLlower.plot(x = dfSQLlower.index, y = ['Stiff Leg RDL weight', 'Hip Thruster weight', 'Forward Squat weight', 'Forward Lunge weight'])
        figLower.update_yaxes(tickvals = [1, 2, 3, 4, 5, 8, 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55])
        figLower.update_layout(width = 1000, height = 500)
        # figLower.show()

        figTogether = make_subplots(rows = 2, cols = 1, subplot_titles = ("Upper Body", "Lower Body"), vertical_spacing = 0.1)
        figTogether.add_trace(
                go.Scatter(
                        x = dfSQLupper.index,
                        y = dfSQLupper['Frontline weight'],
                        name = 'Frontline PPOW Raise',
                        legendgroup = 'Upper Body',
                        legendgrouptitle_text = "Upper Body Weights",
                        mode = "lines+markers+text"
                        ),
                row = 1,
                col = 1
                )
        figTogether.add_trace(
                go.Scatter(
                        x = dfSQLupper.index,
                        y = dfSQLupper['Shoulder press weight'],
                        name = 'Shoulder Press',
                        legendgroup = 'Upper Body',
                        legendgrouptitle_text = "Upper Body Weights",
                        mode = "lines+markers+text"
                        ),
                row = 1,
                col = 1
                )
        figTogether.add_trace(
                go.Scatter(
                        x = dfSQLupper.index,
                        y = dfSQLupper['Elbow Out Row weight'],
                        name = 'Elbow Out Row',
                        legendgroup = 'Upper Body',
                        legendgrouptitle_text = "Upper Body Weights",
                        mode = "lines+markers+text"
                        ),
                row = 1,
                col = 1
                )
        figTogether.add_trace(
                go.Scatter(x = dfSQLupper.index, y = dfSQLupper['Bicep Curl weight'], name = 'Bicep Curl', legendgroup = 'Upper Body', legendgrouptitle_text = "Upper Body Weights", mode = "lines+markers+text"),
                row = 1,
                col = 1
                )
        figTogether.add_trace(
                go.Scatter(
                        x = dfSQLupper.index,
                        y = dfSQLupper['Close Grip Pushup Stair'],
                        name = 'Close Grip Push Up',
                        legendgroup = 'Upper Body',
                        legendgrouptitle_text = "Upper Body Weights",
                        mode = "lines+markers+text"
                        ),
                row = 1,
                col = 1
                )
        figTogether.add_trace(
                go.Scatter(
                        x = dfSQLupper.index,
                        y = dfSQLupper['Rear Delt Fly weight'],
                        name = 'Rear Delt Fly',
                        legendgroup = 'Upper Body',
                        legendgrouptitle_text = "Upper Body Weights",
                        mode = "lines+markers+text"
                        ),
                row = 1,
                col = 1
                )
        figTogether.add_trace(go.Scatter(x = dfSQLupper.index, y = dfSQLupper['Side Bend weight'], name = 'Side Bend', legendgroup = 'Upper Body', mode = "lines+markers+text"), row = 1, col = 1)
        figTogether.add_trace(
                go.Scatter(
                        x = dfSQLupper.index,
                        y = dfSQLupper['Lateral Raise weight'],
                        name = 'Lateral Raise',
                        legendgroup = 'Upper Body',
                        legendgrouptitle_text = "Upper Body Weights",
                        mode = "lines+markers+text"
                        ),
                row = 1,
                col = 1
                )
        figTogether.add_trace(
                go.Scatter(
                        x = dfSQLlower.index,
                        y = dfSQLlower['Stiff Leg RDL weight'],
                        name = 'Stiff Leg RDL',
                        legendgroup = 'Lower Body',
                        legendgrouptitle_text = "Lower Body Weights",
                        mode = "lines+markers+text"
                        ),
                row = 2,
                col = 1
                )
        figTogether.add_trace(
                go.Scatter(x = dfSQLlower.index, y = dfSQLlower['Hip Thruster weight'], name = 'Hip Thruster', legendgroup = 'Lower Body', legendgrouptitle_text = "Lower Body Weights", mode = "lines+markers+text"),
                row = 2,
                col = 1
                )
        figTogether.add_trace(
                go.Scatter(
                        x = dfSQLlower.index,
                        y = dfSQLlower['Forward Squat weight'],
                        name = 'Forward Squat',
                        legendgroup = 'Lower Body',
                        legendgrouptitle_text = "Lower Body Weights",
                        mode = "lines+markers+text"
                        ),
                row = 2,
                col = 1
                )
        figTogether.add_trace(
                go.Scatter(
                        x = dfSQLlower.index,
                        y = dfSQLlower['Forward Lunge weight'],
                        name = 'Forward Lunge',
                        legendgroup = 'Lower Body',
                        legendgrouptitle_text = "Lower Body Weights",
                        mode = "lines+markers+text"
                        ),
                row = 2,
                col = 1
                )
        figTogether.update_yaxes(tickvals = [1, 2, 3, 4, 5, 8, 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55], range = [-0.5, 30], fixedrange = True, row = 1, col = 1)
        figTogether.update_yaxes(tickvals = [1, 2, 3, 4, 5, 8, 10, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55], range = [-0.5, 60], fixedrange = True, row = 2, col = 1)
        figTogether.update_layout(legend_tracegroupgap = 280, width = 1000, height = 1000)
        ui.plotly(figTogether).classes('w-full h-full')

with ui.footer(value = False) as footer:
    ui.label('Footer')

with ui.left_drawer().classes('bg-blue-100') as left_drawer:
    ui.label('Side menu')

with ui.page_sticky(position = 'bottom-right', x_offset = 20, y_offset = 20):
    ui.button(on_click = footer.toggle).props('fab icon=contact_support')

ui.run(reload = False)
