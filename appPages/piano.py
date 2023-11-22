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

from nicegui import ui, app
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

from appPages import piano
from appPages import fitness

def create() -> None:
    @ui.page("/piano") 
    def piano() -> None:
        with theme.frame("- PIANO -"):
            u_today_date                = ui.date().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_frontlineRaiseSets        = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_frontlineRaiseReps        = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_frontlineRaiseWeight      = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_shoulderPressReps         = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_shoulderPressSets         = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_shoulderPressWeight       = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_elbowOutRowReps           = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_elbowOutRowSets           = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_elbowOutRowWeight         = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_bicepCurlReps             = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_bicepCurlSets             = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_bicepCurlWeight           = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_closeGripPushupReps       = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_closeGripPushupSets       = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_closeGripPushupWeight     = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_rearDeltFlyReps           = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_rearDeltFlySets           = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_rearDeltFlyWeight         = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_sideBendReps              = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_sideBendSets              = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_sideBendWeight            = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_lateralRaiseReps          = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_lateralRaiseSets          = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_lateralRaiseWeight        = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_stiffLegRDLReps           = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_stiffLegRDLSets           = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_stiffLegRDLWeight         = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_hamstringCurlReps         = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_hamstringCurlSets         = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_hipThrusterReps           = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_hipThrusterSets           = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_hipThrusterWeight         = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_frontSquatReps            = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_frontSquatSets            = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_frontSquatWeight          = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_sumoSquatReps             = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_sumoSquatSets             = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_sumoSquatWeight           = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_cyclistSquatReps          = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_cyclistSquatSets          = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_calfRaiseReps             = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_calfRaiseSets             = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_calfRaiseWeight           = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_longLeverCrunchesReps     = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_longLeverCrunchesSets     = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_sidelineSculpt            = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_abdominals                = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_walk                      = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            u_walkDistance              = ui.number().classes('hidden').style('font-style: normal, font-family : "Atkinson Hyperlegible"')

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
                u_abdominals,
                u_walk,
                u_walkDistance
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
                    if not isinstance(exercise.value, int):
                        exercise.value = int(math.ciel(num))
                    else:
                        continue
                today_date              = (u_today_date.value)
                frontlineRaiseReps      = int(u_frontlineRaiseReps.value)
                frontlineRaiseSets      = int(u_frontlineRaiseReps.value)
                frontlineRaiseWeight    = int(u_frontlineRaiseReps.value)
                shoulderPressReps       = int(u_shoulderPressReps.value)
                shoulderPressSets       = int(u_shoulderPressSets.value)
                shoulderPressWeight     = int(u_shoulderPressWeight.value)
                elbowOutRowReps         = int(u_elbowOutRowReps.value)
                elbowOutRowSets         = int(u_elbowOutRowSets.value)
                elbowOutRowWeight       = int(u_elbowOutRowWeight.value)
                bicepCurlReps           = int(u_bicepCurlReps.value)
                bicepCurlSets           = int(u_bicepCurlSets.value)
                bicepCurlWeight         = int(u_bicepCurlWeight.value)
                closeGripPushupReps     = int(u_closeGripPushupReps.value)
                closeGripPushupSets     = int(u_frontlineRaiseReps.value)
                closeGripPushupWeight   = int(u_closeGripPushupWeight.value)
                rearDeltFlyReps         = int(u_rearDeltFlyReps.value)
                rearDeltFlySets         = int(u_rearDeltFlySets.value)
                rearDeltFlyWeight       = int(u_rearDeltFlyWeight.value)
                sideBendReps            = int(u_sideBendReps.value)
                sideBendSets            = int(u_sideBendSets.value)
                sideBendWeight          = int(u_sideBendWeight.value)
                lateralRaiseReps        = int(u_lateralRaiseReps.value)
                lateralRaiseSets        = int(u_lateralRaiseSets.value)
                lateralRaiseWeight      = int(u_lateralRaiseWeight.value)
                stiffLegRDLReps         = int(u_stiffLegRDLReps.value)
                stiffLegRDLSets         = int(u_stiffLegRDLSets.value)
                stiffLegRDLWeight       = int(u_stiffLegRDLWeight.value)
                hamstringCurlReps       = int(u_hamstringCurlReps.value)
                hamstringCurlSets       = int(u_hamstringCurlSets.value)
                hipThrusterReps         = int(u_hipThrusterReps.value)
                hipThrusterSets         = int(u_hipThrusterSets.value)
                hipThrusterWeight       = int(u_hipThrusterWeight.value)
                frontSquatReps          = int(u_frontSquatReps.value)
                frontSquatSets          = int(u_frontSquatSets.value)
                frontSquatWeight        = int(u_frontSquatWeight.value)
                sumoSquatReps           = int(u_sumoSquatReps.value)
                sumoSquatSets           = int(u_sumoSquatSets.value)
                sumoSquatWeight         = int(u_sumoSquatWeight.value)
                cyclistSquatReps        = int(u_cyclistSquatReps.value)
                cyclistSquatSets        = int(u_cyclistSquatSets.value)
                calfRaiseReps           = int(u_calfRaiseReps.value)
                calfRaiseSets           = int(u_calfRaiseSets.value)
                calfRaiseWeight         = int(u_calfRaiseWeight.value)
                longLeverCrunchesReps   = int(u_longLeverCrunchesReps.value)
                longLeverCrunchesSets   = int(u_longLeverCrunchesSets.value)
                sidelineSculpt          = int(u_sidelineSculpt.value)
                abdominals              = int(u_abdominals.value)
                walk                    = int(u_walk.value)
                walkDistance            = int(u_walkDistance.value)

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
                            ABDOMINALS,
                            WALK,
                            WALK_DISTANCE
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
                                abdominals,
                                walk,
                                walkDistance
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
                ui.label('UPPER BODY').classes('text-2xl').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Frontline Raise').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_frontlineRaiseReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Frontline Raise Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_frontlineRaiseSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Frontline Raise Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_frontlineRaiseWeight.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Frontline Raise Weight"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Arnold Presses').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_shoulderPressReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Shoulder Press Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_shoulderPressSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Shoulder Press Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_shoulderPressWeight.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Shoulder Press Weight"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Elbow Out Row').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_elbowOutRowReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Elbow Out Row Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_elbowOutRowSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Elbow Out Row Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_elbowOutRowWeight.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Elbow Out Row Weight"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Supinating Bicep Curl').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_bicepCurlReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Bicep Curls Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_bicepCurlSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Bicep Curls Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_bicepCurlWeight.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Bicep Curls Weight"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Close Grip Pushup').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_closeGripPushupReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Close Grip Pushup Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_closeGripPushupSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Close Grip Pushup Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'STAIR', value ="", on_change = lambda e: u_closeGripPushupWeight.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Close Grip Pushup Stair"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Seated Rear Delt Fly').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_rearDeltFlyReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Rear Delt Fly Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_rearDeltFlySets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Rear Delt Fly Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_rearDeltFlyWeight.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Rear Delt Fly Weight"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Standing Side Bend').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_sideBendReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Side Bend Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_sideBendSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Side Bend Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_sideBendWeight.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Side Bend Weight"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Lateral Raise').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_lateralRaiseReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Lateral Raise Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_lateralRaiseSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Lateral Raise Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_lateralRaiseWeight.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Lateral Raise Weight"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap py-4'):
                ui.label('LOWER BODY WORK').classes('text-2xl').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Stiff Leg RDL').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_stiffLegRDLReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Stiff Leg RDL Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_stiffLegRDLSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Stiff Leg RDL Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_stiffLegRDLWeight.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Stiff Leg RDL Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Hamstring Curl').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_hamstringCurlReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Hamstring Curl Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_hamstringCurlSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Hamstring Curl Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.label(" ").classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Hip Thruster').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_hipThrusterReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Hip Thruster Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_hipThrusterSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Hip Thruster Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_hipThrusterWeight.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Hip Thruster Weight"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Front Squat').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_frontSquatReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Front Squat Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_frontSquatSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Front Squat Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_frontSquatWeight.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Front Squat Weight"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Sumo Squat').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_sumoSquatReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Forward Lunge Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_sumoSquatSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Forward Lunge Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_sumoSquatWeight.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Forward Lunge Weight"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Cyclist Squat').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_cyclistSquatReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Cyclist Squat Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_cyclistSquatSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Cyclist Squat Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.label(" ").classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Calf Raise').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_calfRaiseReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Calf Raise Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_calfRaiseSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Calf Raise Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'WEIGHT', value ="", on_change = lambda e: u_calfRaiseWeight.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Cald Raise Weight"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Long Lever Crunches').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'REPS', value ="", on_change = lambda e: u_longLeverCrunchesReps.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Calf Raise Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'SETS', value ="", on_change = lambda e: u_longLeverCrunchesSets.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Calf Raise Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.label("").classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap py-4'):
                ui.label('CORE WORK').classes('text-2xl').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Sideline Sculpt').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'DONE', value ="", on_change = lambda e: u_sidelineSculpt.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Long Lever Crunch Reps"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.label(" ").classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.label(" ").classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Abdominals').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = 'DONE', value ="", on_change = lambda e: u_abdominals.set_value(e.value)).classes('w-1/4 text-base').props('aria-label="Long Lever Crunch Sets"').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.label(" ").classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.label(" ").classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap py-4'):
                ui.label('WALKING').classes('text-2xl').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label('Walking').classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = "Did I Walk", value = "", on_change = lambda e: u_walk.set_value(e.value)).classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.label(" ").classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.label(" ").classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.label("Distance Walked").classes("w-1/4").style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.number(label = "Distance", value = "", on_change = lambda e: u_walkDistance.set_value(math.ceil(e.value))).classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.label(" ").classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
                ui.label(" ").classes('w-1/4 text-base').style('font-style: normal, font-family : "Atkinson Hyperlegible"')
            with ui.row().classes('w-full no-wrap'):
                ui.button('SAVE', on_click = save)
                ui.button('EXIT', on_click = app.shutdown)

