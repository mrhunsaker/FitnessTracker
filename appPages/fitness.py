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

import math
import os
import sqlite3
import sys
from datetime import datetime

import pandas as pd
from nicegui import ui, app

module_path = os.path.abspath(os.getcwd())
if module_path not in sys.path:
    sys.path.append(module_path)
from appTheming import theme
from appHelpers.helpers import (
    dataBasePath,
)


def create() -> None:
    @ui.page("/fitness")
    def fitness() -> None:
        with theme.frame("- FITNESS -"):
            with ui.tabs() as tabs:
                ui.tab("WORKOUT INPUT")
                ui.tab("WORKOUT DATA")
            with ui.tab_panels(tabs, value="WORKOUT INPUT"):
                with ui.tab_panel("WORKOUT INPUT"):
                    u_today_date = (
                        ui.date()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_frontlineRaiseSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_frontlineRaiseReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_frontlineRaiseWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_shoulderPressReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_shoulderPressSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_shoulderPressWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_elbowOutRowReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_elbowOutRowSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_elbowOutRowWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_bicepCurlReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_bicepCurlSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_bicepCurlWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_closeGripPushupReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_closeGripPushupSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_closeGripPushupWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_rearDeltFlyReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_rearDeltFlySets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_rearDeltFlyWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_sideBendReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_sideBendSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_sideBendWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_lateralRaiseReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_lateralRaiseSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_lateralRaiseWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_stiffLegRDLReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_stiffLegRDLSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_stiffLegRDLWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_hamstringCurlReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_hamstringCurlSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_hamstringCurlWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_hipThrusterReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_hipThrusterSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_hipThrusterWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_frontSquatReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_frontSquatSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_frontSquatWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_sumoSquatReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_sumoSquatSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_sumoSquatWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_cyclistSquatReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_cyclistSquatSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_cyclistSquatWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_calfRaiseReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_calfRaiseSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_calfRaiseWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_longLeverCrunchesReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_longLeverCrunchesSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_longLeverCrunchesWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_sidelineSculptWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_abdominalsWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_sidelineSculpt = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_abdominals = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_walk = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_walkDistance = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoStepupReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoStepupSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoStepupWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoLateralStepupReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoLateralStepupSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoLateralStepupWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoPistolSquatReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoPistolSquatSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoPistolSquatWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoSplitSquatReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoSplitSquatSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoSplitSquatWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoSidePlankReps = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoSidePlankSets = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )
                    u_plyoSidePlankWeight = (
                        ui.number()
                        .classes("hidden")
                        .style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    )                                                                                                                        
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
                            u_longLeverCrunchesWeight,
                            u_sidelineSculpt,
                            u_sidelineSculptWeight,
                            u_abdominals,
                            u_abdominalsWeight,
                            u_walk,
                            u_walkDistance,
                            u_plyoStepupReps,
                            u_plyoStepupSets,
                            u_plyoStepupWeight,
                            u_plyoLateralStepupReps,
                            u_plyoLateralStepupSets,
                            u_plyoLateralStepupWeight,
                            u_plyoPistolSquatReps,
                            u_plyoPistolSquatSets,
                            u_plyoPistolSquatWeight,
                            u_plyoSplitSquatReps,
                            u_plyoSplitSquatSets,
                            u_plyoSplitSquatWeight,
                            u_plyoSidePlankReps,
                            u_plyoSidePlankSets,
                            u_plyoSidePlankWeight,
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
                            
                        today_date_str = str(u_today_date.value)
                        try:
                            today_date = datetime.strptime(today_date_str, "%Y-%m-%d")
                        except ValueError as e:
                            ui.notify(
                                str(e),  # Converting exception object to string for the error message
                                position="center",
                                type="warning",
                                close_button="OK",
                            )
                            
                        today_date = today_date.strftime("%Y-%m-%d %H:%M:%S")
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
                        longLeverCrunchesWeight = int(u_longLeverCrunchesWeight.value)
                        sidelineSculpt = int(u_sidelineSculpt.value)
                        sidelineSculptWeight = int(u_sidelineSculptWeight.value)
                        abdominals = int(u_abdominals.value)
                        abdominalsWeight = int(u_abdominalsWeight.value)
                        walk = int(u_walk.value)
                        walkDistance = int(u_walkDistance.value)
                        plyoStepupReps =int(u_plyoStepupReps.value)
                        plyoStepupSets = int(u_plyoStepupSets.value)
                        plyoStepupWeight = int(u_plyoStepupWeight.value)
                        plyoLateralStepupReps = int(u_plyoLateralStepupReps.value)
                        plyoLateralStepupSets = int(u_plyoLateralStepupSets.value)
                        plyoLateralStepupWeight = int(u_plyoLateralStepupWeight.value)
                        plyoPistolSquatReps = int(u_plyoPistolSquatReps.value)
                        plyoPistolSquatSets = int(u_plyoPistolSquatSets.value)
                        plyoPistolSquatWeight = int(u_plyoPistolSquatWeight.value)
                        plyoSplitSquatReps = int(u_plyoSplitSquatReps.value)
                        plyoSplitSquatSets = int(u_plyoSplitSquatSets.value)
                        plyoSplitSquatWeight = int(u_plyoSplitSquatWeight.value)
                        plyoSidePlankReps = int(u_plyoSidePlankReps.value)
                        plyoSidePlankSets = int(u_plyoSidePlankSets.value)
                        plyoSidePlankWeight = int(u_plyoSidePlankWeight.value)
                        
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
                            try:
                                conn = sqlite3.connect(dataBasePath)
                                if conn is not None:
                                    c = conn.cursor()
                                    try:
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
                                            SINGLELEGCALFRAISE_WEIGHT,
                                            LONGLEVERCRUNCHES_REPS,
                                            LONGLEVERCRUNCHES_SETS,
                                            LONGLEVERCRUNCHES_WEIGHT,
                                            SIDELINESCULPT,
                                            SIDELINESCULPT_WEIGHT,
                                            ABDOMINALS,
                                            ABDOMINALS_WEIGHT,
                                            WALK,
                                            WALK_DISTANCE,
                                            PLYOSTEPUP_REPS,
                                            PLUOSTEUPUP_SETS,
                                            PLYOSTEPUP_WEIGHT,
                                            PLYOLATERALSTEPUP_REPS,
                                            PLYOLATERALSTEPUP_SETS,
                                            PLYOLATERALSTEPUP_WEIGHT,
                                            PLYOPISTOLSQUAT_REPS,
                                            PLYOPISTOLSQUAT_SETS,
                                            PLYOPISTOLSQUAT_WEIGHT
                                            PLYOSIDEPLANK_REPS,
                                            PLYOSIDEPLANK_SETS,
                                            PLYOSIDEPLANK_WEIGHT,
                                            PLYOSPLITSQUAT_REPS,
                                            PLYOSPLITSQUAT_SETS,
                                            PLYOSPLITSQUAT_WEIGHT
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
                                                calfRaiseWeight,
                                                longLeverCrunchesReps,
                                                longLeverCrunchesSets,
                                                longLeverCrunchesWeight,
                                                sidelineSculpt,
                                                sidelineSculptWeight,
                                                abdominals,
                                                abdominalsWeight,
                                                walk,
                                                walkDistance,
                                                plyoStepupReps,
                                                plyoStepupSets,
                                                plyoStepupWeight,
                                                plyoLateralStepupReps,
                                                plyoLateralStepupSets,
                                                plyoLateralStepupWeight,
                                                plyoPistolSquatReps,
                                                plyoPistolSquatSets,
                                                plyoPistolSquatWeight,
                                                plyoSidePlankReps,
                                                plyoSidePlankSets,
                                                plyoSidePlankWeight,
                                                plyoSplitSquatReps,
                                                plyoSplitSquatSets,
                                                plyoSplitSquatWeight
                                            ),
                                        )
                                        conn.commit()
                                    except ValueError as e:
                                        ui.notify(
                                            str(e),  # Converting exception object to string for the error message
                                            position="center",
                                            type="negative",
                                            close_button="OK",
                                        )
                            except sqlite3.Error as e:
                                ui.notify(
                                    f"SQLite error: {e}",
                                    position="center",
                                    type="negative",
                                    close_button="OK",
                                )
                            conn.close()
                            ui.notify(
                                "Saved successfully!",
                                position="center",
                                type="positive",
                                close_button="OK",
                            )
                        data_entry()
                    with ui.row().classes("w-full no-wrap"):
                        ui.date(
                            value="f{datenow}",
                            on_change=lambda e: u_today_date.set_value(e.value),
                        ).classes("w-1/2")
                    with ui.row().classes("w-full no-wrap py-4"):
                        ui.label("UPPER BODY").classes("text-2xl").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Frontline Raise").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_frontlineRaiseReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Frontline Raise Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_frontlineRaiseSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Frontline Raise Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_frontlineRaiseWeight.set_value(
                                e.value
                            ),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Frontline Raise Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Arnold Presses").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_shoulderPressReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Shoulder Press Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_shoulderPressSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Shoulder Press Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_shoulderPressWeight.set_value(
                                e.value
                            ),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Shoulder Press Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Elbow Out Row").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_elbowOutRowReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Elbow Out Row Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_elbowOutRowSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Elbow Out Row Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_elbowOutRowWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Elbow Out Row Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Supinating Bicep Curl").classes(
                            "w-1/4 text-base"
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_bicepCurlReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Bicep Curls Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_bicepCurlSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Bicep Curls Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_bicepCurlWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Bicep Curls Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Close Grip Pushup").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_closeGripPushupReps.set_value(
                                e.value
                            ),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Close Grip Pushup Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_closeGripPushupSets.set_value(
                                e.value
                            ),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Close Grip Pushup Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="STAIR",
                            value=0,
                            on_change=lambda e: u_closeGripPushupWeight.set_value(
                                e.value
                            ),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Close Grip Pushup Stair"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Seated Rear Delt Fly").classes(
                            "w-1/4 text-base"
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_rearDeltFlyReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Rear Delt Fly Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_rearDeltFlySets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Rear Delt Fly Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_rearDeltFlyWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Rear Delt Fly Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Standing Side Bend").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_sideBendReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Side Bend Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_sideBendSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Side Bend Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_sideBendWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Side Bend Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Lateral Raise").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_lateralRaiseReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Lateral Raise Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_lateralRaiseSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Lateral Raise Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_lateralRaiseWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Lateral Raise Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap py-4"):
                        ui.label("LOWER BODY WORK").classes("text-2xl").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Stiff Leg RDL").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_stiffLegRDLReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Stiff Leg RDL Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_stiffLegRDLSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Stiff Leg RDL Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_stiffLegRDLWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Stiff Leg RDL Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Hamstring Curl").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_hamstringCurlReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Hamstring Curl Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_hamstringCurlSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Hamstring Curl Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_hamstringCurlWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Hamstring Curl Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Hip Thruster").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_hipThrusterReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Hip Thruster Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_hipThrusterSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Hip Thruster Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_hipThrusterWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Hip Thruster Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Front Squat").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_frontSquatReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Front Squat Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_frontSquatSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Front Squat Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_frontSquatWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Front Squat Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Sumo Squat").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_sumoSquatReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Forward Lunge Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_sumoSquatSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Forward Lunge Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_sumoSquatWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Forward Lunge Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Cyclist Squat").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_cyclistSquatReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Cyclist Squat Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_cyclistSquatSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Cyclist Squat Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_cyclistSquatWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Cyclist Squat Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Calf Raise").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_calfRaiseReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Calf Raise Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_calfRaiseSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Calf Raise Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_calfRaiseWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Cald Raise Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Long Lever Crunches").classes(
                            "w-1/4 text-base"
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_longLeverCrunchesReps.set_value(
                                e.value
                            ),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Long Lever Crunches Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_longLeverCrunchesSets.set_value(
                                e.value
                            ),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Long Lever Crunches Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_longLeverCrunchesWeight.set_value(
                                e.value
                            ),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Long Lever Crunches Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap py-4"):
                        ui.label("PLYO BOX EXERCISES").classes("text-2xl").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Plyo Box Step-Up").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_plyoStepupReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box Step-Up Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_plyoStepupSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box Step-Up Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_plyoStepupWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box Step-Up Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Plyo Box Lateral Step-Up").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_plyoLateralStepupReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box Lateral Step-Up Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_plyoLateralStepupSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box Lateral Step-Up Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_plyoLateralStepupWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box Lateral Step-Up Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Plyo Box Pistol Squat").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_plyoPistolSquatReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box Pistol Squat Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_plyoPistolSquatSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box Pistol Squat Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_plyoPistolSquatWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box Pistol Squat Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Plyo Box Pistol Squat").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_plyoSplitSquatReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box  Bulgarian Split Squat Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_plyoSplitSquatSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box  Bulgarian Split Squat Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_plyoSplitSquatWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box Bulgarian Split Squat Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Plyo Box Side Plank").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="REPS",
                            value=0,
                            on_change=lambda e: u_plyoSidePlankReps.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box Side Plank Reps"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="SETS",
                            value=0,
                            on_change=lambda e: u_plyoSidePlankSets.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box  Side Plank Sets"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="WEIGHT",
                            value=0,
                            on_change=lambda e: u_plyoSidePlankWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Plyo Box Side Plank Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )

                    with ui.row().classes("w-full no-wrap py-4"):
                        ui.label("CORE WORK").classes("text-2xl").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Sideline Sculpt").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="DONE",
                            value=0,
                            on_change=lambda e: u_sidelineSculpt.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Sideline Sculpt"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="Weight",
                            value=0,
                            on_change=lambda e: u_sidelineSculptWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Sideline Sculpt Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Abdominals").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="DONE",
                            value=0,
                            on_change=lambda e: u_abdominals.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Abdominals"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="Weight",
                            value=0,
                            on_change=lambda e: u_abdominalsWeight.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                            'aria-label="Abdominals Weight"'
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap py-4"):
                        ui.label("WALKING").classes("text-2xl").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Walking").classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="Did I Walk",
                            value=0,
                            on_change=lambda e: u_walk.set_value(e.value),
                        ).classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                            label="Distance Walked",
                            value=0,
                            on_change=lambda e: u_walkDistance.set_value(
                                math.ceil(e.value)
                            ),
                        ).classes("w-1/4 text-base").style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.button("SAVE", on_click=save).props('color=secondary')
                        ui.button("EXIT", on_click=app.shutdown).props('color=secondary')
                        ui.button("HOME", on_click=lambda: ui.open("/")).props('color=secondary')
            with ui.tab_panels(tabs, value="WORKOUT DATA"):
                with ui.tab_panel("WORKOUT DATA"):
                    conn = sqlite3.connect(dataBasePath)
                    dfSQL = pd.read_sql_query("SELECT * FROM WORKOUTS", conn)
                    conn.close()
                    df = dfSQL.drop(columns=["ID"])
                    df = df.sort_values(by=["DATE"], ascending=False)
                    df_last8 = df.drop(
                        columns=[
                            "FRONTLINE_SETS",
                            "SHOULDERZPRESS_SETS",
                            "ELBOWOUTROW_SETS",
                            "SUPINEBICEPCURL_SETS",
                            "CLOSEGRIPPUSHUP_SETS",
                            "REARDELTFLY_SETS",
                            "SIDEBEND_SETS",
                            "LATERALRAISE_SETS",
                            "STIFFLEGRDL_SETS",
                            "SLIDERHAMSTRINGCURL_SETS",
                            "HIPTHRUSTER_SETS",
                            "FORWARDSQUAT_SETS",
                            "SUMOSQUAT_SETS",
                            "CYCLISTSQUAT_SETS",
                            "SINGLELEGCALFRAISE_SETS",
                            "LONGLEVERCRUNCHES_SETS",
                            "FRONTLINE_WEIGHT",
                            "SHOULDERZPRESS_WEIGHT",
                            "ELBOWOUTROW_WEIGHT",
                            "SUPINEBICEPCURL_WEIGHT",
                            "CLOSEGRIPPUSHUP_STAIR",
                            "REARDELTFLY_WEIGHT",
                            "SIDEBEND_WEIGHT",
                            "LATERALRAISE_WEIGHT",
                            "STIFFLEGRDL_WEIGHT",
                            "SLIDERHAMSTRINGCURL_WEIGHT",
                            "HIPTHRUSTER_WEIGHT",
                            "FORWARDSQUAT_WEIGHT",
                            "SUMOSQUAT_WEIGHT",
                            "CYCLISTSQUAT_WEIGHT",
                            "SINGLELEGCALFRAISE_WEIGHT",
                            "LONGLEVERCRUNCHES_WEIGHT",
                            "SIDELINESCULPT_WEIGHT",
                            "ABDOMINALS_WEIGHT",
                            "PLYOSTEPUP_SETS",
                            "PLYOSTEPUP_WEIGHT",
                            "PLYOLATERALSTEPUP_SETS",
                            "PLYOLATERALSTEPUP_WEIGHT",
                            "PLYOPISTOLSQUAT_SETS",
                            "PLYOPISTOLSQUAT_WEIGHT",
                            "PLYOSPLITSQUAT_SETS",
                            "PLYOSPLITSQUAT_WEIGHT",
                            "PLYOSIDEPLANK_SETS",
                            "PLYOSIDEPLANK_WEIGHT"
                        ]
                    )
                    df_last8 = df_last8.rename(
                        columns={
                            "DATE": "Date",
                            "FRONTLINE_REPS": "Frontline POW Raise",
                            "SHOULDERZPRESS_REPS": "Arnold Press",
                            "ELBOWOUTROW_REPS": "Elbow Out Row",
                            "SUPINEBICEPCURL_REPS": "Supinating Bicep Curl",
                            "CLOSEGRIPPUSHUP_REPS": "Close Grip Pushup",
                            "REARDELTFLY_REPS": "Rear Delt Fly",
                            "SIDEBEND_REPS": "Side Bend",
                            "LATERALRAISE_REPS": "Lateral Raise",
                            "STIFFLEGRDL_REPS": "Stiff Legged RDL",
                            "SLIDERHAMSTRINGCURL_REPS": "Hamstring Curls",
                            "HIPTHRUSTER_REPS": "Hip Thrusters",
                            "FORWARDSQUAT_REPS": "Forward Squat",
                            "SUMOSQUAT_REPS": "Sumo Squat",
                            "CYCLISTSQUAT_REPS": "Cyclist Squat",
                            "SINGLELEGCALFRAISE_REPS": "Single Leg Calf Raise",
                            "LONGLEVERCRUNCHES_REPS": "Long Lever Crunches",
                            "SIDELINESCULPT": "Sideline Sculpt",
                            "ABDOMINALS": "Abdominals",
                            "WALK": "Walk",
                            "WALK_DISTANCE": "Distance Walked",
                            "PLYOSTEPUP_REPS": "Plyo Step-Up",
                            "PLYOLATERALSTEPUP_REPS": "Plyo Lateral Step-Up",
                            "PLYOPISTOLSQUAT_REPS":  "Plyo Pistol Squat",
                            "PLYOSPLITSQUAT_REPS": "Plyo Bulgarian Split Squat",
                            "PLYOSIDEPLANK_REPS": "Plyo Side Plank",
                        }
                    )
                    df = df.rename(
                        columns={
                            "DATE": "Date",
                            "FRONTLINE_REPS": "Frontline POW Raise reps",
                            "FRONTLINE_SETS": "Frontline POW Raise sets",
                            "FRONTLINE_WEIGHT": "Frontline POW Raise Weight",
                            "DOWNDOGPUSHUP_REPS": "Downdog reps",
                            "DOWNDOGPUSHUP_SETS": "Downdog sets",
                            "SHOULDERZPRESS_REPS": "Arnold press reps",
                            "SHOULDERZPRESS_SETS": "Arnold press sets",
                            "SHOULDERZPRESS_WEIGHT": "Arnold press Weight",
                            "ELBOWOUTROW_REPS": "Elbow Out Row reps",
                            "ELBOWOUTROW_SETS": "Elbow Out Row sets",
                            "ELBOWOUTROW_WEIGHT": "Elbow Out Row Weight",
                            "SUPINEBICEPCURL_REPS": "Supinating Bicep Curl reps",
                            "SUPINEBICEPCURL_SETS": "Supinating Bicep Curl sets",
                            "SUPINEBICEPCURL_WEIGHT": "Supinating Bicep Curl Weight",
                            "CLOSEGRIPPUSHUP_REPS": "Close Grip Pushup reps",
                            "CLOSEGRIPPUSHUP_SETS": "Close Grip Pshup sets",
                            "CLOSEGRIPPUSHUP_STAIR": "Close Grip Pushup Stair",
                            "REARDELTFLY_REPS": "Rear Delt Fly reps",
                            "REARDELTFLY_SETS": "Rear Delt Fly sets",
                            "REARDELTFLY_WEIGHT": "Rear Delt Fly Weight",
                            "SIDEBEND_REPS": "Side Bend reps",
                            "SIDEBEND_SETS": "Side Bend sets",
                            "SIDEBEND_WEIGHT": "Side Bend Weight",
                            "LATERALRAISE_REPS": "Lateral Raise reps",
                            "LATERALRAISE_SETS": "Lateral Raise sets",
                            "LATERALRAISE_WEIGHT": "Lateral Raise Weight",
                            "STIFFLEGRDL_REPS": "Stiff Legged RDL reps",
                            "STIFFLEGRDL_SETS": "Stiff Legged RDL sets",
                            "STIFFLEGRDL_WEIGHT": "Stiff Legged RDL Weight",
                            "SLIDERHAMSTRINGCURL_REPS": "Hamstring Curls reps",
                            "SLIDERHAMSTRINGCURL_SETS": "Hamstring Curls sets",
                            "SLIDERHAMSTRINGCURL_WEIGHT": "Hamstring Curls Weight",
                            "HIPTHRUSTER_REPS": "Hip Thrusters reps",
                            "HIPTHRUSTER_SETS": "Hip Thrusters sets",
                            "HIPTHRUSTER_WEIGHT": "Hip Thrusters Weight",
                            "FORWARDSQUAT_REPS": "Forward Squat reps",
                            "FORWARDSQUAT_SETS": "Forward Squat sets",
                            "FORWARDSQUAT_WEIGHT": "Forward Squat Weight",
                            "SUMOSQUAT_REPS": "Sumo Squat reps",
                            "SUMOSQUAT_SETS": "Sumo Squat sets",
                            "SUMOSQUAT_WEIGHT": "Sumo Squat Weight",
                            "CYCLISTSQUAT_REPS": "Cyclist Squat reps",
                            "CYCLISTSQUAT_SETS": "Cyclist Squat sets",
                            "CYCLISTSQUAT_WEIGHT": "Cyclist Squat Weight",
                            "SINGLELEGCALFRAISE_REPS": "Single Leg Calf Raise reps",
                            "SINGLELEGCALFRAISE_SETS": "Single Leg Calf Raise sets",
                            "SINGLELEGCALFRAISE_WEIGHT": "Single Leg Calf Raise Weight",
                            "LONGLEVERCRUNCHES_REPS": "Long Lever Crunches reps",
                            "LONGLEVERCRUNCHES_SETS": "Long Lever Crunches sets",
                            "LONGLEVERCRUNCHES_WEIGHT": "Long Lever Crunches Weight",
                            "SIDELINESCULPT": "Sideline Scupt",
                            "ABDOMINALS": "Abdominals",
                            "SIDELINESCULPT_WEIGHT": "Sideline Scupt Weight",
                            "ABDOMINALS_WEIGHT": "Abdominals Weight",
                            "WALK": "Walk",
                            "WALK_DISTANCE": "Walk Distance",
                            "PLYOSTEPUP_REPS": "Plyo Step-Up reps",
                            "PLYOLATERALSTEPUP_REPS": "Plyo Lateral Step-Up reps",
                            "PLYOPISTOLSQUAT_REPS":  "Plyo Pistol Squat reps",
                            "PLYOSPLITSQUAT_REPS": "Plyo Bulgarian Split Squat reps",
                            "PLYOSIDEPLANK_REPS": "Plyo Side Plank reps",
                            "PLYOSTEPUP_SETS": "Plyo Step-Up sets",
                            "PLYOLATERALSTEPUP_SETS": "Plyo Lateral Step-Up sets",
                            "PLYOPISTOLSQUAT_SETS":  "Plyo Pistol Squat sets",
                            "PLYOSPLITSQUAT_SETS": "Plyo Bulgarian Split Squat sets",
                            "PLYOSIDEPLANK_SETS": "Plyo Side Plank sets",
                            "PLYOSTEPUP_WEIGHT": "Plyo Step-Up Weight",
                            "PLYOLATERALSTEPUP_WEIGHT": "Plyo Lateral Step-Up Weight",
                            "PLYOPISTOLSQUAT_WEIGHT":  "Plyo Pistol Squat Weight",
                            "PLYOSPLITSQUAT_WEIGHT": "Plyo Bulgarian Split Squat Weight",
                            "PLYOSIDEPLANK_WEIGHT": "Plyo Side Plank Weight",
                        }
                    )
                    lower_df = df_last8.drop(
                        columns=[
                            "Frontline POW Raise",
                            "Arnold Press",
                            "Elbow Out Row",
                            "Supinating Bicep Curl",
                            "Close Grip Pushup",
                            "Rear Delt Fly",
                            "Side Bend",
                            "Lateral Raise",
                            "Abdominals",
                            "Sideline Sculpt",
                            "Walk",
                            "Distance Walked",
                            "Plyo Step-Up",
                            "Plyo Lateral Step-Up",
                            "Plyo Pistol Squat",
                            "Plyo Bulgarian Split Squat",
                            "Plyo Side Plank",
                        ]
                    )
                    upper_df = df_last8.drop(
                        columns=[
                            "Stiff Legged RDL",
                            "Hamstring Curls",
                            "Hip Thrusters",
                            "Forward Squat",
                            "Sumo Squat",
                            "Cyclist Squat",
                            "Single Leg Calf Raise",
                            "Long Lever Crunches",
                            "Abdominals",
                            "Sideline Sculpt",
                            "Walk",
                            "Distance Walked",
                            "Plyo Step-Up",
                            "Plyo Lateral Step-Up",
                            "Plyo Pistol Squat",
                            "Plyo Bulgarian Split Squat",
                            "Plyo Side Plank",
                        ]
                    )
                    abs_df = df_last8.drop(
                        columns=[
                            "Stiff Legged RDL",
                            "Hamstring Curls",
                            "Hip Thrusters",
                            "Forward Squat",
                            "Sumo Squat",
                            "Cyclist Squat",
                            "Single Leg Calf Raise",
                            "Long Lever Crunches",
                            "Frontline POW Raise",
                            "Arnold Press",
                            "Elbow Out Row",
                            "Supinating Bicep Curl",
                            "Close Grip Pushup",
                            "Rear Delt Fly",
                            "Side Bend",
                            "Lateral Raise",
                            "Walk",
                            "Distance Walked",
                            "Plyo Step-Up",
                            "Plyo Lateral Step-Up",
                            "Plyo Pistol Squat",
                            "Plyo Bulgarian Split Squat",
                            "Plyo Side Plank",
                        ]
                    )
                    walk_df = df_last8.drop(
                        columns=[
                            "Stiff Legged RDL",
                            "Hamstring Curls",
                            "Hip Thrusters",
                            "Forward Squat",
                            "Sumo Squat",
                            "Cyclist Squat",
                            "Single Leg Calf Raise",
                            "Long Lever Crunches",
                            "Frontline POW Raise",
                            "Arnold Press",
                            "Elbow Out Row",
                            "Supinating Bicep Curl",
                            "Close Grip Pushup",
                            "Rear Delt Fly",
                            "Side Bend",
                            "Lateral Raise",
                            "Abdominals",
                            "Sideline Sculpt",
                            "Distance Walked",
                            "Plyo Step-Up",
                            "Plyo Lateral Step-Up",
                            "Plyo Pistol Squat",
                            "Plyo Bulgarian Split Squat",
                            "Plyo Side Plank",
                        ]
                    )
                    plyo_df = df_last8.drop(
                        columns=[
                            "Stiff Legged RDL",
                            "Hamstring Curls",
                            "Hip Thrusters",
                            "Forward Squat",
                            "Sumo Squat",
                            "Cyclist Squat",
                            "Single Leg Calf Raise",
                            "Long Lever Crunches",
                            "Frontline POW Raise",
                            "Arnold Press",
                            "Elbow Out Row",
                            "Supinating Bicep Curl",
                            "Close Grip Pushup",
                            "Rear Delt Fly",
                            "Side Bend",
                            "Lateral Raise",
                            "Abdominals",
                            "Sideline Sculpt",
                            "Distance Walked",
                            "Walk",
                            "Abdominals"
                        ]
                    )
                    
                    def reshape_and_rename(input_df):
                        """
                        Reshape and rename a DataFrame containing exercise data.
                        
                        Parameters
                        ----------
                        input_df : pandas.DataFrame
                            Input DataFrame containing exercise data with columns 'Date', exercise names as columns,
                            and corresponding values representing exercise metrics.
                            
                        Returns
                        -------
                        pandas.DataFrame
                            Reshaped and renamed DataFrame with the following columns:
                            - 'Exercises': Exercise names.
                            - 'Most Recent': The most recent date for each exercise.
                            - 'Days Since Last': Number of days since the last exercise recorded.
                            
                        Notes
                        -----
                        This function performs the following steps:
                        1. Melt the input DataFrame to transform it into a long format.
                        2. Remove rows with 'value' equal to 0.
                        3. Group by 'Exercises' and find the most recent date for each exercise.
                        4. Merge the melted DataFrame with the most recent dates.
                        5. Drop unnecessary columns ('Date', 'value') and sort by the most recent date.
                        6. Keep only the first occurrence of each exercise, removing duplicates.
                        7. Calculate the 'Days Since Last' based on the time elapsed since the previous record.
                        
                        Examples
                        --------
                        >>> import pandas as pd
                        >>> from datetime import datetime, timedelta
                        >>> # Creating a sample DataFrame
                        >>> data = {'Date': ['2023-01-01', '2023-01-02', '2023-01-03'],
                        ...         'Exercise_A': [10, 15, 0],
                        ...         'Exercise_B': [5, 0, 20]}
                        >>> df = pd.DataFrame(data)
                        >>> df['Date'] = pd.to_datetime(df['Date'])
                        >>> # Applying reshape_and_rename function
                        >>> result_df = reshape_and_rename(df)
                        >>> print(result_df)
                        """
                        melted_df = pd.melt(
                            input_df,
                            id_vars=["Date"],
                            var_name="Exercises",
                            value_name="value",
                        )
                        # Filter out rows with zero values and NaN values
                        melted_df = melted_df[(melted_df["value"] != 0) & melted_df["value"].notna()]
                        # Group by "Exercises" and find the most recent date for each
                        recent_df = (
                            melted_df.groupby(["Exercises"])
                            .agg({"Date": "max"})
                            .reset_index()
                        )
                        recent_df.columns = ["Exercises", "Most_Recent"]
                        # Merge melted_df with recent_df based on "Exercises" and "Weight"
                        reformed_df = pd.merge(melted_df, recent_df, on=["Exercises"])
                        # Drop unnecessary columns
                        reformed_df = reformed_df.drop(["Date", "value"], axis=1)
                        # Sort by "Most_Recent" column
                        reformed_df = reformed_df.sort_values(by=["Most_Recent"])
                        # Drop duplicate rows, keeping only the first occurrence of each exercise
                        reformed_df = reformed_df.drop_duplicates(subset=["Exercises"], keep="first")
                        # Calculate "Days Since" based on the most recent date
                        reformed_df["Days_Ago"] = (
                            datetime.now() - pd.to_datetime(reformed_df["Most_Recent"])
                        ).dt.days
                        # Drop the "Most_Recent" column
                        reformed_df = reformed_df.drop("Most_Recent", axis=1)
                        return reformed_df
                    def process_exercise_data(df):
                        """
                        Filter and process exercise data DataFrame.

                        Parameters
                        ----------
                        df : pandas.DataFrame
                            Input DataFrame containing exercise data.

                        Returns
                        -------
                        pandas.DataFrame
                            Processed DataFrame with exercise data.

                        Notes
                        -----
                        This function filters columns ending with 'weight' or 'stair', melts the DataFrame, 
                        drops NaN values, removes rows with zero level, sorts values, extracts the last 
                        level for each exercise, identifies exercises with zero level, sets their level 
                        as 'None', and concatenates the previous levels with zero level exercises. 
                        Finally, sorts the resulting DataFrame by exercise names.
                        """
                        # Filter columns ending with 'weight' or 'stair'
                        df_filtered = df[[col for col in df.columns if col.lower().endswith(('weight', 'stair'))]]
                        
                        # Melt the DataFrame
                        melted_df = df_filtered.melt(var_name='Exercises', value_name='Level')
                        
                        # Drop NaN values
                        melted_df = melted_df.dropna()
                        
                        # Create a copy of the melted DataFrame
                        melted_df_copy = melted_df.copy()
                        
                        # Remove rows with zero level
                        melted_df = melted_df[melted_df['Level'] != 0]
                        
                        # Sort values by exercise names
                        melted_df = melted_df.sort_values('Exercises', ascending=True)
                        
                        # Extract the last level for each exercise
                        previous_weight = melted_df.groupby('Exercises')[['Level']].last().reset_index()
                        
                        # Identify exercises with zero level
                        zero_level_df = melted_df_copy[melted_df_copy.groupby('Exercises')['Level'].transform('max') == 0]
                        
                        # Sort zero level exercises and drop duplicates, set level as 'None'
                        zero_level_df = zero_level_df.sort_values('Level').drop_duplicates('Exercises', keep='last')
                        zero_level_df['Level'] = 'None'
                        
                        # Concatenate previous levels with zero level exercises
                        previous_weight = pd.concat([previous_weight, zero_level_df], ignore_index=True)
                        
                        # Sort resulting DataFrame by exercise names
                        previous_weight = previous_weight.sort_values(by=['Exercises'])
                        
                        return previous_weight
                    previous_weight = process_exercise_data(df)

                    """Drop Rows for Easier Data Presentation"""
                    upper_df = reshape_and_rename(upper_df)
                    lower_df = reshape_and_rename(lower_df)
                    abs_df = reshape_and_rename(abs_df)
                    walk_df = reshape_and_rename(walk_df)
                    plyo_df = reshape_and_rename(plyo_df)
                    with ui.row().classes("w-full no-wrap"):
                        ui.button("HOME", on_click=lambda: ui.open("/")).props('color=secondary')
                        ui.button("EXIT", on_click=app.shutdown).props('color=secondary')
                    with ui.row():
                        ui.label("Most Recent Exercises").classes(
                            "text-3xl text-bold"
                        ).style('font-family : "JetBrainsMono"')
                    with ui.row():
                        with ui.column():
                            with ui.card():
                                ui.label("Upper Body Exercises").classes(
                                    "text-xl text-bold"
                                ).style(
                                    'font-family : "Atkinson Hyperlegible"'
                                )
                                ui.separator().classes("w-full h-1").props("color=positive")
                                table_c = ui.table(
                                    columns=[
                                        {"name": col, "label": col, "field": col,
                                        "headerClasses": "border-b border-secondary",
                                        "align": 'left'}
                                        for col in upper_df.columns
                                    ],
                                    rows=upper_df.to_dict("records"),
                                ).style(
                                    "font-family: JetBrainsMono; background-color: #f5f5f5"
                                ).classes("text-lg font-normal my-table")
                                table_c.add_slot('body-cell-Days_Ago', '''
                                    <q-td key="Days_Ago" :props="props">
                                    <q-badge :color="props.value  <= 8 ? 'blue' : props.value <= 14 ? 'green' : props.value <= 21 ? 'orange' :  'red'" text-color="black" outline>
                                        {{ props.value }}
                                    </q-badge>
                                    </q-td>
                                    ''')
                            with ui.card():
                                ui.label("Abdominal Exercises").classes(
                                    "text-xl text-bold"
                                ).style(
                                    'font-family : "Atkinson Hyperlegible"'
                                )
                                ui.separator().classes("w-full h-1").props("color=positive")
                                table_a = ui.table(
                                    columns=[
                                        {"name": col, "label": col, "field": col,
                                        "headerClasses": "border-b border-secondary",
                                        "align": 'left'}
                                        for col in abs_df.columns
                                    ],
                                    rows=abs_df.to_dict("records"),
                                ).style(
                                    "font-family: JetBrainsMono; background-color: #f5f5f5"
                                ).classes("text-lg font-normal my-table")
                                table_a.add_slot('body-cell-Days_Ago', '''
                                    <q-td key="Days_Ago" :props="props">
                                    <q-badge :color="props.value  <= 8 ? 'blue' : props.value <= 14 ? 'green' : props.value <= 21 ? 'orange' :  'red'" text-color="black" outline>
                                        {{ props.value }}
                                    </q-badge>
                                    </q-td>
                                    ''')
                            with ui.card():
                                        ui.label("Plyo Exercises").classes("text-xl text-bold").style(
                                            'font-family : "Atkinson Hyperlegible"'
                                        )
                                        ui.separator().classes("w-full h-1").props("color=positive")
                                        table_w = ui.table(
                                            columns=[
                                                {"name": col, "label": col, "field": col,
                                                "headerClasses": "border-b border-secondary",
                                                "align": 'left'}
                                                for col in plyo_df.columns
                                            ],
                                            rows=plyo_df.to_dict("records"),
                                        ).style(
                                            "font-family: JetBrainsMono; background-color: #f5f5f5"
                                        ).classes("text-lg font-normal my-table")
                                        table_w.add_slot('body-cell-Days_Ago', '''
                                            <q-td key="Days_Ago" :props="props">
                                            <q-badge :color="props.value  <= 8 ? 'blue' : props.value <= 14 ? 'green' : props.value <= 21 ? 'orange' :  'red'" text-color="black" outline>
                                                {{ props.value }}
                                            </q-badge>
                                            </q-td>
                                            ''')
                        with ui.column():
                            with ui.card():
                                    ui.label("Lower Body Exercises").classes(
                                        "text-xl text-bold"
                                    ).style(
                                        'font-family : "Atkinson Hyperlegible"'
                                    )
                                    ui.separator().classes("w-full h-1").props("color=positive")
                                    table_b = ui.table(
                                        columns=[
                                            {"name": col, "label": col, "field": col,
                                            "headerClasses": "border-b border-secondary",
                                            "align": 'left'}
                                            for col in lower_df.columns
                                        ],
                                        rows=lower_df.to_dict("records"),
                                    ).style(
                                        "font-family: JetBrainsMono; background-color: #f5f5f5"
                                    ).classes("text-lg font-normal my-table")
                                    table_b.add_slot('body-cell-Days_Ago', '''
                                        <q-td key="Days_Ago" :props="props">
                                        <q-badge :color="props.value  <= 8 ? 'blue' : props.value <= 14 ? 'green' : props.value <= 21 ? 'orange' :  'red'" text-color="black" outline>
                                        {{ props.value }}
                                        </q-badge>
                                        </q-td>
                                        ''')
                            with ui.row():
                                with ui.card():
                                    ui.label("Walking").classes("text-xl text-bold").style(
                                        'font-family : "Atkinson Hyperlegible"'
                                    )
                                    ui.separator().classes("w-full h-1").props("color=positive")
                                    table_w = ui.table(
                                        columns=[
                                            {"name": col, "label": col, "field": col,
                                            "headerClasses": "border-b border-secondary",
                                            "align": 'left'}
                                            for col in walk_df.columns
                                        ],
                                        rows=walk_df.to_dict("records"),
                                    ).style(
                                        "font-family: JetBrainsMono; background-color: #f5f5f5"
                                    ).classes("text-lg font-normal my-table")
                                    table_w.add_slot('body-cell-Days_Ago', '''
                                        <q-td key="Days_Ago" :props="props">
                                        <q-badge :color="props.value  <= 8 ? 'blue' : props.value <= 14 ? 'green' : props.value <= 21 ? 'orange' :  'red'" text-color="black" outline>
                                            {{ props.value }}
                                        </q-badge>
                                        </q-td>
                                        ''')
                                
                        with ui.card():
                            ui.label("Previous Weight").classes(
                                "text-xl text-bold"
                            ).style(
                                'font-family : "Atkinson Hyperlegible"'
                            )
                            ui.separator().classes("w-full h-1").props("color=positive")
                            table_b = ui.table(
                                columns=[
                                    {"name": col, "label": col, "field": col,
                                    "headerClasses": "border-b border-secondary",
                                    "align": 'left'}
                                    for col in previous_weight.columns
                                ],
                                rows=previous_weight.to_dict("records"),
                            ).style(
                                "font-family: JetBrainsMono; background-color: #f5f5f5"
                            ).classes("text-lg font-normal my-table") 
                            
                    with ui.row():
                        ui.label("Cumulative Exercise Log").classes(
                            "text-3xl text-bold"
                        ).style(
                            'font-family : "Atkinson Hyperlegible"'
                        )
                    table = (
                        ui.table(
                            columns=[
                                {"name": col,
                                "label": col,
                                "field": col,
                                "headerClasses": "border-b border-secondary",
                                "align": 'left'}  
                                for col in df.columns
                            ],
                            rows=df.to_dict("records"), pagination={'rowsPerPage': 10}
                        ).style("font-family: JetBrainsMono; background-color: #f5f5f5").classes('my-table')
                    )




