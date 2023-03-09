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

import pandas as pd
import wx
import wx.html
import wx.html2
import wx.lib.scrolledpanel as scrolled

date = datetime.datetime.now().strftime("%Y_%m_%d-%H%M%S_%p")
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


dataBasePath = Path(USER_DIR).joinpath('Fitness/workoutLog.db')
if __name__ == '__main__':
    dataBasePath = Path(USER_DIR).joinpath('Fitness/workoutLog.db')
    create_connection(dataBasePath)


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
    return conn


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
    conn.close()


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
    conn.close()
    conn = create_connection(dataBasePath)
    if conn is not None:
        create_table(conn, sql_create_lowerbody_table)
    else:
        print("Error! cannot create the database connection.")
    conn.close()


if __name__ == '__main__':
    main()


class MyBrowser(wx.Dialog):
    def __init__(self, *args, **kwds):
        wx.Dialog.__init__(self, *args, **kwds)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.browser = wx.html2.WebView.New(self)
        sizer.Add(self.browser, 1, wx.EXPAND, 10)
        self.SetSizer(sizer)
        self.SetSize((1600, 1200))


class upperBody(scrolled.ScrolledPanel):
    """

    """

    def __init__(
            self,
            parent
            ):
        scrolled.ScrolledPanel.__init__(
                self,
                parent,
                -1
                )
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(
                wx.StaticLine(
                        self,
                        -1,
                        size = (750,
                                -1)
                        ),
                0,
                wx.ALL,
                5
                )
        vbox.Add(
                wx.StaticLine(
                        self,
                        -1,
                        size = (-1,
                                750)
                        ),
                0,
                wx.ALL,
                5
                )
        vbox.Add(
                (20,
                 20)
                )
        self.SetSizer(vbox)
        self.SetupScrolling()
        self.SetBackgroundColour(
                wx.Colour(
                        255,
                        153,
                        153
                        )
                )
        self.SetFont(
                wx.Font(
                        12,
                        wx.MODERN,
                        wx.NORMAL,
                        wx.NORMAL,
                        False,
                        u'JetBrains Mono NL'
                        )
                )
        ######### Panel title
        wx.StaticText(
                self,
                -1,
                "UPPER BODY WORKOUT",
                pos = (200,
                       20)
                )

        ######### Date
        wx.StaticText(
                self,
                -1,
                "Date" + '.' * (55 - len("Date")),
                pos = (30,
                       50)
                )
        self.date = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       50),
                size = (320,
                        25)
                )
        self.date.SetHint('YYYY-MM-DD')

        ######### Frontline POW Raise
        wx.StaticText(
                self,
                -1,
                "Frontline Raise" + '.' * (55 - len("Frontline Raise")),
                pos = (30,
                       80)
                )
        self.frontlineRaiseReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       80),
                size = (100,
                        25)
                )
        self.frontlineRaiseReps.SetHint('Reps')

        self.frontlineRaiseSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       80),
                size = (100,
                        25)
                )
        self.frontlineRaiseSets.SetHint('Sets')

        self.frontlineRaiseWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (520,
                       80),
                size = (100,
                        25)
                )
        self.frontlineRaiseWeight.SetHint('Weight')

        ######### Downward Dog to Pushup
        wx.StaticText(
                self,
                -1,
                "Downward Dog to Pushup" + '.' * (45 - len("Downward Dog to Pushup")),
                pos = (30,
                       110)
                )
        self.downdogPushupReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       110),
                size = (100,
                        25)
                )
        self.downdogPushupReps.SetHint('Reps')

        self.downdogPushupSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       110),
                size = (100,
                        25)
                )
        self.downdogPushupSets.SetHint('Sets')

        ######### Seated Shoulder Z Press
        wx.StaticText(
                self,
                -1,
                "Shoulder Z Press" + '.' * (55 - len("Shoulder Z Press")),
                pos = (30,
                       140)
                )
        self.shoulderPressReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       140),
                size = (100,
                        25)
                )
        self.shoulderPressReps.SetHint('Reps')

        self.shoulderPressSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       140),
                size = (100,
                        25)
                )
        self.shoulderPressSets.SetHint('Sets')

        self.shoulderPressWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (520,
                       140),
                size = (100,
                        25)
                )
        self.shoulderPressWeight.SetHint('Weight')

        ######### Single Arm Elbow Out Row
        wx.StaticText(
                self,
                -1,
                "Elbow Out Row" + '.' * (55 - len("Elbow Out Row")),
                pos = (30,
                       170)
                )
        self.elbowOutRowReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       170),
                size = (100,
                        25)
                )
        self.elbowOutRowReps.SetHint('Reps')

        self.elbowOutRowSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       170),
                size = (100,
                        25)
                )
        self.elbowOutRowSets.SetHint('Sets')

        self.elbowOutRowWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (520,
                       170),
                size = (100,
                        25)
                )
        self.elbowOutRowWeight.SetHint('Weight')

        ######### Supinating Bicep Curl
        wx.StaticText(
                self,
                -1,
                "Supinating Bicep Curl" + '.' * (55 - len("Supinating Bicep Curl")),
                pos = (30,
                       200)
                )
        self.bicepCurlReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       200),
                size = (100,
                        25)
                )
        self.bicepCurlReps.SetHint('Reps')

        self.bicepCurlSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       200),
                size = (100,
                        25)
                )
        self.bicepCurlSets.SetHint('Sets')

        self.bicepCurlWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (520,
                       200),
                size = (100,
                        25)
                )
        self.bicepCurlWeight.SetHint('Weight')

        ######### Close Grip Pushups
        wx.StaticText(
                self,
                -1,
                "Close Grip Pushup" + '.' * (55 - len("Close Grip Pushup")),
                pos = (30,
                       230)
                )
        self.closeGripPushupReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       230),
                size = (100,
                        25)
                )
        self.closeGripPushupReps.SetHint('Reps')

        self.closeGripPushupSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       230),
                size = (100,
                        25)
                )
        self.closeGripPushupSets.SetHint('Sets')

        self.closeGripPushupWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (520,
                       230),
                size = (100,
                        25)
                )
        self.closeGripPushupWeight.SetHint('Stair')

        ######### Seated Rear Delt Fly
        wx.StaticText(
                self,
                -1,
                "Seated Rear Delt Fly" + '.' * (55 - len("Seated Rear Delt Fly")),
                pos = (30,
                       260)
                )
        self.rearDeltFlyReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       260),
                size = (100,
                        25)
                )
        self.rearDeltFlyReps.SetHint('Reps')

        self.rearDeltFlySets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       260),
                size = (100,
                        25)
                )
        self.rearDeltFlySets.SetHint('Sets')

        self.rearDeltFlyWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (520,
                       260),
                size = (100,
                        25)
                )
        self.rearDeltFlyWeight.SetHint('Weight')

        ######### Standing Side Bend
        wx.StaticText(
                self,
                -1,
                "Standing Side Bend" + '.' * (55 - len("Standing Side Bend")),
                pos = (30,
                       290)
                )
        self.sideBendReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       290),
                size = (100,
                        25)
                )
        self.sideBendReps.SetHint('Reps')

        self.sideBendSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       290),
                size = (100,
                        25)
                )
        self.sideBendSets.SetHint('Sets')

        self.sideBendWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (520,
                       290),
                size = (100,
                        25)
                )
        self.sideBendWeight.SetHint('Weight')

        ######### Lateral Raise
        wx.StaticText(
                self,
                -1,
                "Lateral Raise" + '.' * (55 - len("Lateral Raise")),
                pos = (30,
                       320)
                )
        self.lateralRaiseReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       320),
                size = (100,
                        25)
                )
        self.lateralRaiseReps.SetHint('Reps')

        self.lateralRaiseSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       320),
                size = (100,
                        25)
                )
        self.lateralRaiseSets.SetHint('Sets')

        self.lateralRaiseWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (520,
                       320),
                size = (100,
                        25)
                )
        self.lateralRaiseWeight.SetHint('Weight')

        ########## Buttons
        self.btn = wx.Button(
                self,
                201,
                "SAVE",
                pos = (250,
                       400),
                size = (70,
                        30)
                )
        self.Bind(
                wx.EVT_BUTTON,
                self.save,
                id = 201
                )
        self.btn2 = wx.Button(
                self,
                203,
                "SHOW",
                pos = (330,
                       400),
                size = (70,
                        30)
                )
        self.Bind(
                wx.EVT_BUTTON,
                self.show,
                id = 203
                )
        self.btn1 = wx.Button(
                self,
                202,
                "EXIT",
                pos = (410,
                       400),
                size = (70,
                        30)
                )
        self.Bind(
                wx.EVT_BUTTON,
                self.exit,
                id = 202
                )

    @staticmethod
    def exit(event):
        """

        :param event:
        :type event:
        """
        wx.Exit()

    def show(self, event):
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
        dfAsStringU = df.to_html(index = False)

        Find = '<table border="1" class="dataframe">'
        Replace = '<table border="1" class="dataframe">\n<colgroup>\n<col span="1" style="background-color:white">\n<col span="3" style="background-color:LightGrey">\n<col span="2" ' \
                  'style="background-color:white">\n<col span="3" style="background-color:LightGrey">\n<col span="3" style="background-color:white">\n<col span="3" style="background-color:LightGrey">\n<col ' \
                  'span="3" style="background-color:white">\n<col span="3" style="background-color:LightGrey">\n<col span="3" style="background-color:white">\n<col span="3" style="background-color:LightGrey">'
        dfAsStringU = dfAsStringU.replace(Find, Replace)
        Find = '<tr style="text-align: right;">'
        Replace = '<tr style="text-align: center;">'
        dfAsStringU = dfAsStringU.replace(Find, Replace)
        Find = '<td>'
        Replace = '<td align="center">'
        dfAsStringU = dfAsStringU.replace(Find, Replace)
        html = wx.html2.WebView.New(
                self,
                -1,
                size = (
                        1200,
                        800
                        )
                )
        dialog = MyBrowser(None, -1)
        dialog.browser.SetPage(dfAsStringU, "")
        dialog.Show()

    def save(
            self,
            event
            ):
        """

        :param event:
        :type event:
        """
        date = self.date.GetValue()
        frontlineRaiseReps = self.frontlineRaiseReps.GetValue()
        frontlineRaiseSets = self.frontlineRaiseReps.GetValue()
        frontlineRaiseWeight = self.frontlineRaiseReps.GetValue()
        downdogPushupReps = self.downdogPushupReps.GetValue()
        downdogPushupSets = self.downdogPushupSets.GetValue()
        downdogPushupWeight = self.downdogPushupWeight.GetValue()
        shoulderPressReps = self.shoulderPressReps.GetValue()
        shoulderPressSets = self.shoulderPressSets.GetValue
        shoulderPressWeight = self.shoulderPressWeight.GetValue()
        elbowOutRowReps = self.elbowOutRowReps.GetValue()
        elbowOutRowSets = self.elbowOutRowSets.GetValue()
        elbowOutRowWeight = self.elbowOutRowWeight.GetValue()
        bicepCurlReps = self.bicepCurlReps.GetValue()
        bicepCurlSets = self.bicepCurlSets.GetValue()
        bicepCurlWeight = self.bicepCurlWeight.GetValue()
        closeGripPushupReps = self.closeGripPushupReps.GetValue()
        closeGripPushupSets = self.frontlineRaiseReps.GetValue
        closeGripPushupWeight = self.closeGripPushupWeight.GetValue()
        rearDeltFlyReps = self.rearDeltFlyReps.GetValue()
        rearDeltFlySets = self.rearDeltFlySets.GetValue()
        rearDeltFlyWeight = self.rearDeltFlyWeight.GetValue()
        sideBendReps = self.sideBendReps.GetValue()
        sideBendSets = self.sideBendSets.GetValue()
        sideBendWeight = self.sideBendWeight.GetValue()
        lateralRaiseReps = self.lateralRaiseReps.GetValue()
        lateralRaiseSets = self.lateralRaiseSets.GetValue()
        lateralRaiseWeight = self.lateralRaiseWeight.GetValue()

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
                                downdogPushupWeight,
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
            conn.close()

            self.dial = wx.MessageDialog(
                    None,
                    'Uploaded Successfully!',
                    'Info',
                    wx.OK
                    )
            self.dial.ShowModal()

        data_entry()


class lowerBody(scrolled.ScrolledPanel):
    """

    """

    def __init__(
            self,
            parent
            ):
        scrolled.ScrolledPanel.__init__(
                self,
                parent,
                -1
                )
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(
                wx.StaticLine(
                        self,
                        -1,
                        size = (750,
                                -1)
                        ),
                0,
                wx.ALL,
                5
                )
        vbox.Add(
                wx.StaticLine(
                        self,
                        -1,
                        size = (-1,
                                750)
                        ),
                0,
                wx.ALL,
                5
                )
        vbox.Add(
                (20,
                 20)
                )
        self.SetSizer(vbox)
        self.SetupScrolling()
        self.SetBackgroundColour(
                wx.Colour(
                        255,
                        153,
                        153
                        )
                )
        self.SetFont(
                wx.Font(
                        12,
                        wx.MODERN,
                        wx.NORMAL,
                        wx.NORMAL,
                        False,
                        u'JetBrains Mono NL'
                        )
                )

        ########## Panel title
        wx.StaticText(
                self,
                -1,
                "LOWER BODY WORKOUT",
                pos = (200,
                       20)
                )

        ######### Date
        wx.StaticText(
                self,
                -1,
                "Date" + '.' * (55 - len("Date")),
                pos = (30,
                       50)
                )
        self.date = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       50),
                size = (320,
                        25)
                )
        self.date.SetHint('YYYY-MM-DD')

        ######### Single Leg Bridge
        wx.StaticText(
                self,
                -1,
                "Single Leg Bridge" + '.' * (45 - len("Single Leg Bridge")),
                pos = (30,
                       80)
                )
        self.singleLegBridgeReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       80),
                size = (100,
                        25)
                )
        self.singleLegBridgeReps.SetHint('Reps')

        self.singleLegBridgeSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       80),
                size = (100,
                        25)
                )
        self.singleLegBridgeSets.SetHint('Sets')

        ######### World's Greatest Stretch
        wx.StaticText(
                self,
                -1,
                "World's Greatest Stretch" + '.' * (45 - len("World's Greatest Stretch")),
                pos = (30,
                       110)
                )
        self.worldsGreatestReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       110),
                size = (100,
                        25)
                )
        self.worldsGreatestReps.SetHint('Reps')

        self.worldsGreatestSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       110),
                size = (100,
                        25)
                )
        self.worldsGreatestSets.SetHint('Sets')

        ######### Stiff Leg RDL
        wx.StaticText(
                self,
                -1,
                "Stiff Leg RDL" + '.' * (55 - len("Stiff Leg RDL")),
                pos = (30,
                       140)
                )
        self.stiffLegRDLReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       140),
                size = (100,
                        25)
                )
        self.stiffLegRDLReps.SetHint('Reps')

        self.stiffLegRDLSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       140),
                size = (100,
                        25)
                )
        self.stiffLegRDLSets.SetHint('Sets')

        self.stiffLegRDLWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (520,
                       140),
                size = (100,
                        25)
                )
        self.stiffLegRDLWeight.SetHint('Weight')

        ######### Slider Hamstring Curl
        wx.StaticText(
                self,
                -1,
                "Slider Hanstring Curl" + '.' * (45 - len("Slider Hanstring Curl")),
                pos = (30,
                       170)
                )
        self.hamstringCurlReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       170),
                size = (100,
                        25)
                )
        self.hamstringCurlReps.SetHint('Reps')

        self.hamstringCurlSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       170),
                size = (100,
                        25)
                )
        self.hamstringCurlSets.SetHint('Sets')

        ######### Hip Thruster
        wx.StaticText(
                self,
                -1,
                "Supinating Bicep Curl" + '.' * (55 - len("Supinating Bicep Curl")),
                pos = (30,
                       200)
                )
        self.hipThrusterReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       200),
                size = (100,
                        25)
                )
        self.hipThrusterReps.SetHint('Reps')

        self.hipThrusterSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       200),
                size = (100,
                        25)
                )
        self.hipThrusterSets.SetHint('Sets')

        self.hipThrusterWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       200),
                size = (100,
                        25)
                )
        self.hipThrusterWeight.SetHint('Sets')

        ######### Forward Squat
        wx.StaticText(
                self,
                -1,
                "Forward Squat" + '.' * (55 - len("Forward Squat")),
                pos = (30,
                       230)
                )
        self.frontSquatReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       230),
                size = (100,
                        25)
                )
        self.frontSquatReps.SetHint('Reps')

        self.frontSquatSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       230),
                size = (100,
                        25)
                )
        self.frontSquatSets.SetHint('Sets')

        self.frontSquatWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (520,
                       230),
                size = (100,
                        25)
                )
        self.frontSquatWeight.SetHint('Weight')

        ######### Forward Lunge
        wx.StaticText(
                self,
                -1,
                "Forward lunge" + '.' * (55 - len("Forward Lunge")),
                pos = (30,
                       260)
                )
        self.forwardLungeReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       260),
                size = (100,
                        25)
                )
        self.forwardLungeReps.SetHint('Reps')

        self.forwardLungeSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       260),
                size = (100,
                        25)
                )
        self.forwardLungeSets.SetHint('Sets')

        self.forwardLungeWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (520,
                       260),
                size = (100,
                        25)
                )
        self.forwardLungeWeight.SetHint('Weight')

        ######### Cyclist Squat
        wx.StaticText(
                self,
                -1,
                "Cyclist Squat" + '.' * (55 - len("Cyclist Squat")),
                pos = (30,
                       290)
                )
        self.cyclistSquatReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       290),
                size = (100,
                        25)
                )
        self.cyclistSquatReps.SetHint('Reps')

        self.cyclistSquatSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       290),
                size = (100,
                        25)
                )
        self.cyclistSquatSets.SetHint('Sets')

        self.cyclistSquatWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (520,
                       290),
                size = (100,
                        25)
                )
        self.cyclistSquatWeight.SetHint('Weight')

        ######### Single Leg Calf Raise
        wx.StaticText(
                self,
                -1,
                "Single Leg Calf Raise" + '.' * (55 - len("Single Leg Calf Raise")),
                pos = (30,
                       320)
                )
        self.calfRaiseReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       320),
                size = (100,
                        25)
                )
        self.calfRaiseReps.SetHint('Reps')

        self.calfRaiseSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       320),
                size = (100,
                        25)
                )
        self.calfRaiseSets.SetHint('Sets')

        self.calfRaiseWeight = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (520,
                       320),
                size = (100,
                        25)
                )
        self.calfRaiseWeight.SetHint('Weight')

        ######### Long Lever Crunches
        wx.StaticText(
                self,
                -1,
                "Long Lever Crunches" + '.' * (55 - len("Long Lever Crunches")),
                pos = (30,
                       320)
                )
        self.longLeverReps = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (300,
                       320),
                size = (100,
                        25)
                )
        self.longLeverReps.SetHint('Reps')

        self.longLeverSets = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (410,
                       320),
                size = (100,
                        25)
                )
        self.longLeverSets.SetHint('Sets')

        ########## Buttons
        self.btn = wx.Button(
                self,
                201,
                "SAVE",
                pos = (250,
                       400),
                size = (70,
                        30)
                )
        self.Bind(
                wx.EVT_BUTTON,
                self.save,
                id = 201
                )
        self.btn2 = wx.Button(
                self,
                203,
                "SHOW",
                pos = (330,
                       400),
                size = (70,
                        30)
                )
        self.Bind(
                wx.EVT_BUTTON,
                self.show,
                id = 203
                )
        self.btn1 = wx.Button(
                self,
                202,
                "EXIT",
                pos = (410,
                       400),
                size = (70,
                        30)
                )
        self.Bind(
                wx.EVT_BUTTON,
                self.exit,
                id = 202
                )

    @staticmethod
    def exit(event):
        """

        :param event:
        :type event:
        """
        wx.Exit()

    def show(self, event):
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
                        'LONGLEVERCRUNCHES_REPS':   'Long Lever Crunshes reps',
                        'LONGLEVERCRUNCHES_SETS':   'Long Lever Crunches sets'
                        }
                )
        dfAsStringL = df.to_html(index = False)
        print(dfAsStringL)
        Find = '<table border="1" class="dataframe">'
        Replace = '<table border="1" class="dataframe">\n<colgroup>\n<col span="1" style="background-color:white">\n<col span="2" style="background-color:LightGrey">\n<col span="2" ' \
                  'style="background-color:white">\n<col span="3" style="background-color:LightGrey">\n<col span="2" style="background-color:white">\n<col span="3" style="background-color:LightGrey">\n<col ' \
                  'span="3" style="background-color:white">\n<col span="3" style="background-color:LightGrey">\n<col span="2" style="background-color:white">\n<col span="2" ' \
                  'style="background-color:LightGrey">\n<col span="2" style="background-color:white">'
        dfAsStringL = dfAsStringL.replace(Find, Replace)
        Find = '<tr style="text-align: right;">'
        Replace = '<tr style="text-align: center;">'
        dfAsStringL = dfAsStringL.replace(Find, Replace)
        Find = '<td>'
        Replace = '<td align="center">'
        dfAsStringL = dfAsStringL.replace(Find, Replace)
        html = wx.html2.WebView.New(self, -1, size = (1200, 800))
        dialog = MyBrowser(None, -1)
        dialog.browser.SetPage(dfAsStringL, "")
        dialog.Show()

    def save(
            self,
            event
            ):
        """
        :param event:
        :type event:
        """
        date = self.date.GetValue()
        singleLegBridgeReps = self.singleLegBridgeReps.GetValue()
        singleLegBridgeSets = self.singleLegBridgeSets.GetValue()
        worldsGreatestReps = self.worldsGreatestReps.GetValue()
        worldsGreatestSets = self.worldsGreatestSets.GetValue()
        worldsGreatestWeight = self.worldsGreatestWeight.GetValue()
        stiffLegRDLReps = self.stiffLegRDLReps.GetValue()
        stiffLegRDLSets = self.stiffLegRDLSets.GetValue()
        stiffLegRDLWeight = self.stiffLegRDLWeight.GetValue()
        hamstringCurlReps = self.hamstringCurlReps.GetValue()
        hamstringCurlSets = self.hamstringCurlSets.GetValue()
        hipThrusterReps = self.hipThrusterReps.GetValue()
        hipThrusterSets = self.hipThrusterSets.GetValue()
        hipThrusterWeight = self.hipThrusterWeight.GetValue()
        frontSquatReps = self.frontSquatReps.GetValue()
        frontSquatSets = self.frontSquatSets.GetValue()
        frontSquatWeight = self.frontSquatWeight.GetValue()
        forwardLungeReps = self.forwardLungeReps.GetValue()
        forwardLungeSets = self.forwardLungeSets.GetValue()
        forwardLungeWeight = self.forwardLungeWeight.GetValue()
        cyclistSquatReps = self.cyclistSquatReps.GetValue()
        cyclistSquatSets = self.cyclistSquatSets.GetValue()
        cyclistSquatWeight = self.cyclistSquatWeight.GetValue()
        calfRaiseReps = self.calfRaiseReps.GetValue()
        calfRaiseSets = self.calfRaiseSets.GetValue()
        calfRaiseWeight = self.calfRaiseWeight.GetValue()
        longLeverReps = self.longLeverReps.GetValue()
        longLeverSets = self.longLeverSets.GetValue()
        longLeverWeight = self.longLeverWeight.GetValue()

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
                            worldsGreatestWeight,
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
                            cyclistSquatWeight,
                            calfRaiseReps,
                            calfRaiseSets,
                            calfRaiseWeight,
                            longLeverReps,
                            longLeverSets,
                            longLeverWeight
                            )
                    )
            conn.commit()
            conn.close()

            self.dial = wx.MessageDialog(
                    None,
                    'Uploaded Successfully!',
                    'Info',
                    wx.OK
                    )
            self.dial.ShowModal()

        data_entry()


class WorkoutLogBook(
        wx.Frame,
        wx.Accessible
        ):
    """

    """

    def __init__(
            self,
            parent,
            title
            ):
        super(
                WorkoutLogBook,
                self
                ).__init__(
                parent,
                title = "Data Entry Form",
                size = (
                        1130,
                        1000
                        )
                )
        self.SetBackgroundColour(
                wx.Colour(
                        224,
                        224,
                        224
                        )
                )
        self.SetFont(
                wx.Font(
                        12,
                        wx.MODERN,
                        wx.NORMAL,
                        wx.NORMAL,
                        False,
                        u'JetBrains Mono NL'
                        )
                )
        self.initui()

    def initui(self):
        """

        """
        nb = wx.Notebook(self)
        nb.AddPage(
                upperBody(nb),
                "UPPER BODY"
                )
        nb.AddPage(
                lowerBody(nb),
                "LOWER BODY"
                )

        self.Centre()
        self.Show(True)


app = wx.App()
frame = WorkoutLogBook(
        None,
        'Workout Logs'
        )
frame.Centre()
frame.Show()
app.MainLoop()
