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
from nicegui import ui, app

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
        reformed_df["Days_Ago"] = (
                datetime.datetime.now()
                - pd.to_datetime(reformed_df["Most_Recent"])
        ).dt.days
        reformed_df = reformed_df.drop("Most_Recent", axis=1)
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
                "font-family: JetBrainsMono; background-color: #f5f5f5"
            ).classes("text-lg font-normal  my-table")
            table_p.add_slot('body-cell-Days_Ago', '''
                <q-td key="Days_Ago" :props="props">
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
            datetime.datetime.now() - pd.to_datetime(reformed_df["Most_Recent"])
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

def content() -> None:
    with theme.frame("- DASHBOARD -"):
        fitness()
        ui.separator().classes("w-full h-2").props("color=accent")
        piano()
