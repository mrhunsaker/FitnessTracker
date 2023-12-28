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

import datetime
import sqlite3

import pandas as pd
from nicegui import ui

from appHelpers.helpers import dataBasePath
from appPages import fitness
from appTheming import theme


def piano() -> None:
    conn = sqlite3.connect(dataBasePath)
    dfSQL = pd.read_sql_query("SELECT * FROM PIANO", conn)
    conn.close()
    df = dfSQL.drop(columns=["ID"])
    df = df.sort_values(by=["DATE"])
    df_last8 = df.drop(
        columns=[
            "LESSON",
            "RECITAL"
        ]
    )
    df_last8 = df_last8.rename(
        columns={
            "DATE": "Date",
            "PIANO": "Practiced"
        }
    )
    df = df.rename(
        columns={
            "DATE": "Date",
            "PIANO": "Practiced",
            "LESSON": "Lesson",
            "RECITAL": "Recital"
        }
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
        melted_df = melted_df[melted_df["value"] != 0]
        melted_df = melted_df[melted_df["value"].notna()]
        recent_df = (
            melted_df.groupby("Exercises")
            .agg({"Date": "max"})
            .reset_index()
        )
        recent_df.columns = ["Exercises", "Most_Recent"]
        reformed_df = pd.merge(melted_df, recent_df, on="Exercises")
        reformed_df = reformed_df.drop("Date", axis=1)
        reformed_df = reformed_df.drop("value", axis=1)
        reformed_df = reformed_df.sort_values(by=["Most_Recent"])
        reformed_df = reformed_df.drop_duplicates(
            subset=["Exercises"], keep="first"
        )
        reformed_df["Days_Since_Last"] = (
                datetime.datetime.now()
                - pd.to_datetime(reformed_df["Most_Recent"])
        ).dt.days
        return reformed_df

    """Drop Rows for Easier Data Presentation"""
    piano_df = reshape_and_rename(df_last8)

    with ui.row():
        ui.label("Piano Practice").classes(
            "text-3xl text-bold"
        ).style('font-family : "JetBrainsMono"')
    with ui.row():
        with ui.card():
            ui.label("Time Since Last Practice").classes(
                "text-xl text-bold"
            ).style(
                'font-family : "Atkinson Hyperlegible"'
            )
            ui.separator().classes("w-full h-1").props("color=positive")
            table_p = ui.table(
                columns=[
                    {"name": col, "label": col, "field": col, "headerClasses": "border-b border-secondary",
                     "align": 'left'}
                    for col in piano_df.columns
                ],
                rows=piano_df.to_dict("records"),
            ).style(
                "font-family: JetBrainsMono"
            ).classes("text-lg font-normal")
            table_p.add_slot('body-cell-Days_Since_Last', '''
                <q-td key="Days_Since_Last" :props="props">
                <q-badge :color="props.value  <= 2 ? 'blue' : props.value <= 3? 'green' : props.value <= 4? 'orange' :  'red'" text-color="black" outline>
                    {{ props.value }}
                </q-badge>
                </q-td>
                ''')


def fitness() -> None:
    conn = sqlite3.connect(dataBasePath)
    dfSQL = pd.read_sql_query("SELECT * FROM WORKOUTS", conn)
    conn.close()
    df = dfSQL.drop(columns=["ID"])
    df = df.sort_values(by=["DATE"])
    df_last8 = df.drop(
        columns=[
            "FRONTLINE_SETS",
            "FRONTLINE_WEIGHT",
            "SHOULDERZPRESS_SETS",
            "SHOULDERZPRESS_WEIGHT",
            "ELBOWOUTROW_SETS",
            "ELBOWOUTROW_WEIGHT",
            "SUPINEBICEPCURL_SETS",
            "SUPINEBICEPCURL_WEIGHT",
            "CLOSEGRIPPUSHUP_SETS",
            "CLOSEGRIPPUSHUP_STAIR",
            "REARDELTFLY_SETS",
            "REARDELTFLY_WEIGHT",
            "SIDEBEND_SETS",
            "SIDEBEND_WEIGHT",
            "LATERALRAISE_SETS",
            "LATERALRAISE_WEIGHT",
            "STIFFLEGRDL_SETS",
            "STIFFLEGRDL_WEIGHT",
            "SLIDERHAMSTRINGCURL_SETS",
            "HIPTHRUSTER_SETS",
            "HIPTHRUSTER_WEIGHT",
            "FORWARDSQUAT_SETS",
            "FORWARDSQUAT_WEIGHT",
            "SUMOSQUAT_SETS",
            "SUMOSQUAT_WEIGHT",
            "CYCLISTSQUAT_SETS",
            "SINGLELEGCALFRAISE_SETS",
            "LONGLEVERCRUNCHES_SETS",
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
        }
    )
    df = df.rename(
        columns={
            "DATE": "Date",
            "FRONTLINE_REPS": "Frontline reps",
            "FRONTLINE_SETS": "Frontline sets",
            "FRONTLINE_WEIGHT": "Frontline weight",
            "DOWNDOGPUSHUP_REPS": "Downdog reps",
            "DOWNDOGPUSHUP_SETS": "Downdog sets",
            "SHOULDERZPRESS_REPS": "Shoulder press reps",
            "SHOULDERZPRESS_SETS": "Shoulder press sets",
            "SHOULDERZPRESS_WEIGHT": "Shoulder press weight",
            "ELBOWOUTROW_REPS": "Elbow Out Row reps",
            "ELBOWOUTROW_SETS": "Elbow Out Row sets",
            "ELBOWOUTROW_WEIGHT": "Elbow Out Row weight",
            "SUPINEBICEPCURL_REPS": "Bicep Curl reps",
            "SUPINEBICEPCURL_SETS": "Bicep Curl sets",
            "SUPINEBICEPCURL_WEIGHT": "Bicep Curl weight",
            "CLOSEGRIPPUSHUP_REPS": "Close Grip Pushup reps",
            "CLOSEGRIPPUSHUP_SETS": "Close Grip Pshup sets",
            "CLOSEGRIPPUSHUP_STAIR": "Close Grip Pushup Stair",
            "REARDELTFLY_REPS": "Rear Delt Fly reps",
            "REARDELTFLY_SETS": "Rear Delt Fly sets",
            "REARDELTFLY_WEIGHT": "Rear Delt Fly weight",
            "SIDEBEND_REPS": "Side Bend reps",
            "SIDEBEND_SETS": "Side Bend sets",
            "SIDEBEND_WEIGHT": "Side Bend weight",
            "LATERALRAISE_REPS": "Lateral Raise reps",
            "LATERALRAISE_SETS": "Lateral Raise sets",
            "LATERALRAISE_WEIGHT": "Lateral Raise weight",
            "STIFFLEGRDL_REPS": "Stiff Leg RDL reps",
            "STIFFLEGRDL_SETS": "Stiff Leg RDL sets",
            "STIFFLEGRDL_WEIGHT": "Stiff Leg RDL weight",
            "SLIDERHAMSTRINGCURL_REPS": "Slider Hamstring Curls reps",
            "SLIDERHAMSTRINGCURL_SETS": "Slider Hamstring Curls sets",
            "HIPTHRUSTER_REPS": "Hip Thruster reps",
            "HIPTHRUSTER_SETS": "Hip thruster sets",
            "HIPTHRUSTER_WEIGHT": "Hip thruster weight",
            "FORWARDSQUAT_REPS": "Front Squat reps",
            "FORWARDSQUAT_SETS": "Front Squat sets",
            "FORWARDSQUAT_WEIGHT": "Front Squat weight",
            "SUMOSQUAT_REPS": "Sumo Squat reps",
            "SUMOSQUAT_SETS": "Sumo Squat sets",
            "SUMOSQUAT_WEIGHT": "Sumo Squat weight",
            "CYCLISTSQUAT_REPS": "Cyclist Squat reps",
            "CYCLISTSQUAT_SETS": "Cyclist Squat sets",
            "SINGLELEGCALFRAISE_REPS": "Single-Leg Calf Raise reps",
            "SINGLELEGCALFRAISE_SETS": "Single-Leg Calf Raise sets",
            "LONGLEVERCRUNCHES_REPS": "Long Lever Crunches reps",
            "LONGLEVERCRUNCHES_SETS": "Long Lever Crunches sets",
            "SIDELINESCULPT": "Sideline Scupt",
            "ABDOMINALS": "Abdominals",
            "WALK": "Walk",
            "WALK_DISTANCE": "Distance Walked",
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
        melted_df = melted_df[melted_df["value"] != 0]
        melted_df = melted_df[melted_df["value"].notna()]
        recent_df = (
            melted_df.groupby("Exercises")
            .agg({"Date": "max"})
            .reset_index()
        )
        recent_df.columns = ["Exercises", "Most_Recent"]
        reformed_df = pd.merge(melted_df, recent_df, on="Exercises")
        reformed_df = reformed_df.drop("Date", axis=1)
        reformed_df = reformed_df.drop("value", axis=1)
        reformed_df = reformed_df.sort_values(by=["Most_Recent"])
        reformed_df = reformed_df.drop_duplicates(
            subset=["Exercises"], keep="first"
        )
        reformed_df["Days_Since_Last"] = (
                datetime.datetime.now()
                - pd.to_datetime(reformed_df["Most_Recent"])
        ).dt.days
        reformed_df = reformed_df.drop("Most_Recent", axis=1)
        return reformed_df

    """Drop Rows for Easier Data Presentation"""
    upper_df = reshape_and_rename(upper_df)
    lower_df = reshape_and_rename(lower_df)
    abs_df = reshape_and_rename(abs_df)
    walk_df = reshape_and_rename(walk_df)
    with ui.row():
        ui.label("Most Recent Exercises").classes(
            "text-3xl text-bold"
        ).style('font-family : "JetBrainsMono"')
    with ui.row():
        with ui.card():
            ui.label("Upper Body Exercises").classes(
                "text-xl text-bold"
            ).style(
                'font-family : "Atkinson Hyperlegible"'
            )
            ui.separator().classes("w-full h-1").props("color=positive")
            table_c = ui.table(
                columns=[
                    {"name": col, "label": col, "field": col, "headerClasses": "border-b border-secondary",
                     "align": 'left'}
                    for col in upper_df.columns
                ],
                rows=upper_df.to_dict("records"),
            ).style(
                "font-family: JetBrainsMono"
            ).classes("text-lg font-normal")
            table_c.add_slot('body-cell-Days_Since_Last', '''
                <q-td key="Days_Since_Last" :props="props">
                <q-badge :color="props.value  <= 8 ? 'blue' : props.value <= 14 ? 'green' : props.value <= 21 ? 'orange' : 'red'" text-color="black" outline>
                    {{ props.value }}
                </q-badge>
                </q-td>
                ''')
        with ui.card():
            ui.label("Lower Body Exercises").classes(
                "text-xl text-bold"
            ).style(
                'font-family : "Atkinson Hyperlegible"'
            )
            ui.separator().classes("w-full h-1").props("color=positive")
            table_b = ui.table(
                columns=[
                    {"name": col, "label": col, "field": col, "headerClasses": "border-b border-secondary",
                     "align": 'left'}
                    for col in lower_df.columns
                ],
                rows=lower_df.to_dict("records"),
            ).style(
                "font-family: JetBrainsMono"
            ).classes("text-lg font-normal")
            table_b.add_slot('body-cell-Days_Since_Last', '''
                <q-td key="Days_Since_Last" :props="props">
                <q-badge :color="props.value  <= 8 ? 'blue' : props.value <= 14 ? 'green' : props.value <= 21 ? 'orange' :  'red'" text-color="black" outline>
                    {{ props.value }}
                </q-badge>
                </q-td>
                ''')
        with ui.column():
            with ui.card():
                ui.label("Abdominal Exercises").classes(
                    "text-xl text-bold"
                ).style(
                    'font-family : "Atkinson Hyperlegible"'
                )
                ui.separator().classes("w-full h-1").props("color=positive")
                table_a = ui.table(
                    columns=[
                        {"name": col, "label": col, "field": col, "headerClasses": "border-b border-secondary",
                         "align": 'left'}
                        for col in abs_df.columns
                    ],
                    rows=abs_df.to_dict("records"),
                ).style(
                    "font-family: JetBrainsMono"
                ).classes("text-lg font-normal")
                table_a.add_slot('body-cell-Days_Since_Last', '''
                    <q-td key="Days_Since_Last" :props="props">
                    <q-badge :color="props.value  <= 8 ? 'blue' : props.value <= 14 ? 'green' : props.value <= 21 ? 'orange' :  'red'" text-color="black" outline>
                        {{ props.value }}
                    </q-badge>
                    </q-td>
                    ''')
            with ui.card():
                ui.label("Walking").classes("text-xl text-bold").style(
                    'font-family : "Atkinson Hyperlegible"'
                )
                ui.separator().classes("w-full h-1").props("color=positive")
                table = ui.table(
                    columns=[
                        {"name": col, "label": col, "field": col, "headerClasses": "border-b border-secondary",
                         "align": 'left'}
                        for col in walk_df.columns
                    ],
                    rows=walk_df.to_dict("records"),
                ).style(
                    "font-family: JetBrainsMono"
                ).classes()
                table.add_slot('body-cell-Days_Since_Last', '''
                    <q-td key="Days_Since_Last" :props="props">
                    <q-badge :color="props.value  <= 8 ? 'blue' : props.value <= 14 ? 'green' : props.value <= 21 ? 'orange' :  'red'" text-color="black" outline>
                        {{ props.value }}
                    </q-badge>
                    </q-td>
                    ''')


def content() -> None:
    with theme.frame("- DASHBOARD -"):
        fitness()
        ui.separator().classes("w-full h-2").props("color=accent")
        piano()
