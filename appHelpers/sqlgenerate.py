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

import sqlite3
from sqlite3 import Error

from nicegui import ui

from appHelpers.helpers import dataBasePath


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
    >>> # Use db_connection for database operations
    >>> # ...

    Note
    ----
    It is recommended to close the database connection after usage by calling the `close` method
    on the returned connection object.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        ui.notify(
            e,
            position="center",
            type="negative",
            close_button="OK",
        )
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
        The SQL statement for creating the table

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
        ui.notify(
            e,
            position="center",
            type="negative",
            close_button="OK",
        )
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
        ABDOMINALS                  INTEGER,
        WALK                        INTEGER,
        WALK_DISTANCE               INTEGER
    );"""

    conn = sqlite3.connect(dataBasePath)
    if conn is not None:
        create_table(conn, sql_create_workout_table)
    else:
        print("Error! cannot create the database connection.")
    conn.close()
