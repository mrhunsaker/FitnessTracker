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
import pandas as pd
import datetime

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
            with ui.tabs() as tabs:
                ui.tab("PIANO INPUT")
                ui.tab("PRACTICE DATA")
            with ui.tab_panels(tabs, value="PIANO INPUT"):
                with ui.tab_panel("PIANO INPUT"):
                    u_today_date = (
                    ui.date()
                    .classes("hidden")
                    .style('font-family : "Atkinson Hyperlegible"')
                    )
                    u_piano= (
                    ui.number()
                    .classes("hidden")
                    .style('font-family : "Atkinson Hyperlegible"')
                    )
                    u_lesson = (
                    ui.input()
                    .classes("hidden")
                    .style('font-family : "Atkinson Hyperlegible"')
                    )
                    u_recital = (
                    ui.input()
                    .classes("hidden")
                    .style('font-family : "Atkinson Hyperlegible"')
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
                        -s------
                        None

                        Examples
                        --------
                        >>> save(some_event)
                        """

                        today_date = u_today_date.value
                        piano = int(u_piano.value)
                        lesson = str(u_lesson.value)
                        recital = str(u_recital.value)

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
                                        """INSERT INTO PIANO (
                                        DATE,
                                        PIANO,
                                        LESSON,
                                        RECITAL
                                        )
                                        VALUES (
                                        ?,
                                        ?,
                                        ?,
                                        ?
                                        )
                                        """,
                                    ( 
                                        today_date,
                                        piano,
                                        lesson,
                                        recital,
                                    ),
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

                    with ui.row().classes("w-full no-wrap"):
                        ui.date(
                        value="f{datenow}",
                        on_change=lambda e: u_today_date.set_value(e.value),
                        ).classes("w-1/2")
                    with ui.row().classes("w-full no-wrap py-4"):
                        ui.label("PIANO PRACTICE").classes("text-2xl").style(
                        'font-family : "Atkinson Hyperlegible"'
                        )
                    with ui.row().classes("w-full no-wrap"):
                        ui.label("Practice").classes("w-1/4 text-base").style(
                        'font-family : "Atkinson Hyperlegible"'
                        )
                        ui.number(
                        label="Practice",
                        value="",
                        on_change=lambda e: u_piano.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                        'aria-label=Practice'
                        ).style('font-family : "Atkinson Hyperlegible"')
                        ui.input(
                        label="LESSON SONG",
                        value="",
                        on_change=lambda e: u_lesson.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                        'aria-label="Lesson"'
                        ).style('font-family : "Atkinson Hyperlegible"')
                        ui.input(
                        label="RECITAL SONG",
                        value="",
                        on_change=lambda e: u_recital.set_value(e.value),
                        ).classes("w-1/4 text-base").props(
                        'aria-label="Recital"'
                        ).style('font-family : "Atkinson Hyperlegible"')
                    with ui.row().classes("w-full no-wrap"):
                        ui.button("SAVE", on_click=save).props('color=secondary')
                        ui.button("EXIT", on_click=app.shutdown).props('color=secondary')
                        
            with ui.tab_panels(tabs, value="PRACTICE DATA"):
                with ui.tab_panel("PRACTICE DATA"):
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
                            "DATE"  : "Date",
                            "PIANO" : "Practiced" 
                        }
                    )
                    df = df.rename(
                        columns={
                            "DATE": "Date",
                            "PIANO" : "Practiced",
                            "LESSON" : "Lesson",
                            "RECITAL" : "Recital"
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
                        melted_df = melted_df[melted_df["value"] != 0 & melted_df["value"].notna()]
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
                            table=ui.table(
                                columns=[
                                    {"name": col, "label": col, "field": col, "headerClasses":"border-b border-secondary",
                                "align": 'left'}
                                    for col in piano_df.columns
                                ],
                                rows=piano_df.to_dict("records"),
                            ).style(
                                "font-family: JeBrainsMono"
                            ).classes("text-lg font-normal")
                            table.add_slot('body-cell-Days_Since_Last', '''
                <q-td key="Days_Since_Last" :props="props">
                <q-badge :color="props.value  <= 2 ? 'green-5' : props.value <= 3? 'yellow-5' : props.value <= 4? 'orange-5' : 'red-5'">
                    {{ props.value }}
                </q-badge>
                </q-td>
                ''')
                    with ui.row():
                        ui.label("Cumulative Practice Log").classes(
                            "text-3xl text-bold"
                        ).style(
                            'font-family : "Atkinson Hypelegible"'
                        )
                    with ui.row():
                        ui.table(
                            columns=[
                                {"name": col, 
                                "label": col, 
                                "field": col, 
                                "headerClasses":"border-b border-secondary",
                                "align": 'left'}
                                for col in df.columns
                            ],
                            rows=df.to_dict("records"),
                        ).style('font-family: JetBrainsMono').classes()
