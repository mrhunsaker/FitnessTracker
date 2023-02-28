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


dataBasePath = Path(USER_DIR).joinpath('Fitness/workouts.db')
if __name__ == '__main__':
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
        ID	        INTEGER PRIMARY KEY AUTOINCREMENT,
        DATE	        TEXT NOT NULL,
        FRONTLINE       INTEGER NOT NULL,
        SHOULDERPRESS	INTEGER NOT NULL,
        CHAIRROW	INTEGER NOT NULL,
        SUPINECURL	INTEGER NOT NULL,
        REARDELTFLY	INTEGER NOT NULL,
        SIDEBEND	INTEGER NOT NULL,
        LATERALRAISE	INTEGER NOT NULL
    );"""

    sql_create_lowerbody_table = """CREATE TABLE IF NOT EXISTS LOWERBODY (
        ID	        INTEGER PRIMARY KEY AUTOINCREMENT,
        DATE	        TEXT NOT NULL,
        STIFFLEGRDL	INTEGER NOT NULL,
        HIPTHRUSTER	INTEGER NOT NULL,
        FORWARDSQUAT	INTEGER NOT NULL,
        FORWARDLUNGE	INTEGER NOT NULL
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
        # dialog = MyBrowser(None, -1)
        # dialog.browser.LoadURL(f"URL")
        # dialog.Show()


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
        wx.StaticText(
                self,
                -1,
                "UPPER BODY WEIGHTS",
                pos = (200,
                       20)
                )
        wx.StaticText(
                self,
                -1,
                "Date" + '.' * (90 - len("Date")),
                pos = (30,
                       50)
                )
        self.trial01 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (650,
                       50),
                size = (300,
                        25)
                )
        self.trial01.SetHint('YYYY-MM-DD')
        wx.StaticText(
                self,
                -1,
                "Frontline Raise" + '.' * (90 - len("Frontline Raise")),
                pos = (30,
                       80)
                )
        self.trial11 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (650,
                       80),
                size = (300,
                        25)
                )
        self.trial11.SetHint('Weight per Arm')
        wx.StaticText(
                self,
                -1,
                "Shoulder Press" + '.' * (90 - len("Shoulder Press")),
                pos = (30,
                       110)
                )
        self.trial12 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (650,
                       110),
                size = (300,
                        25)
                )
        self.trial12.SetHint('Weight per Arm')
        wx.StaticText(
                self,
                -1,
                "Chair Single Arm Row" + '.' * (90 - len("Chair Single Arm Row")),
                pos = (30,
                       140)
                )
        self.trial13 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (650,
                       140),
                size = (300,
                        25)
                )
        self.trial13.SetHint('Weight per Arm')
        wx.StaticText(
                self,
                -1,
                "Supine Curl" + '.' * (90 - len("Supine Curl")),
                pos = (30,
                       170)
                )
        self.trial14 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (650,
                       170),
                size = (300,
                        25)
                )
        self.trial14.SetHint('Weight per Arm')
        wx.StaticText(
                self,
                -1,
                "Rear Delt Fly" + '.' * (90 - len("Rear Delt Fly")),
                pos = (30,
                       200)
                )
        self.trial21 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (650,
                       200),
                size = (300,
                        25)
                )
        self.trial21.SetHint('Weight per Arm')
        wx.StaticText(
                self,
                -1,
                "Side Bend" + '.' * (90 - len("Side Bend")),
                pos = (30,
                       230)
                )
        self.trial22 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (650,
                       230),
                size = (300,
                        25)
                )
        self.trial22.SetHint('Weight per Arm')
        wx.StaticText(
                self,
                -1,
                "Lateral Raise" + '.' * (90 - len("Lateral Raise")),
                pos = (30,
                       260)
                )
        self.trial23 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (650,
                       260),
                size = (300,
                        25)
                )
        self.trial23.SetHint('Weight per Arm')
        self.btn = wx.Button(
                self,
                201,
                "SAVE",
                pos = (450,
                       830),
                size = (70,
                        30)
                )
        self.Bind(
                wx.EVT_BUTTON,
                self.save,
                id = 201
                )
        self.btn1 = wx.Button(
                self,
                202,
                "EXIT",
                pos = (550,
                       830),
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

    def save(
            self,
            event
            ):
        """

        :param event:
        :type event:
        """
        trial01 = self.trial01.GetValue()
        trial11 = self.trial11.GetValue()
        trial12 = self.trial12.GetValue()
        trial13 = self.trial13.GetValue()
        trial14 = self.trial14.GetValue()
        trial21 = self.trial21.GetValue()
        trial22 = self.trial22.GetValue()
        trial23 = self.trial23.GetValue()

        def data_entry():
            """

            """
            conn = sqlite3.connect(dataBasePath)
            if conn is not None:
                c = conn.cursor()
                c.execute(
                        """INSERT INTO UPPERBODY (
                    DATE,
                    FRONTLINE,
                    SHOULDERPRESS,
                    CHAIRROW,
                    SUPINECURL,
                    REARDELTFLY,
                    SIDEBEND,
                    LATERALRAISE
                    )
                    VALUES (
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
                                trial01,
                                trial11,
                                trial12,
                                trial13,
                                trial14,
                                trial21,
                                trial22,
                                trial23
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
            conn = sqlite3.connect(dataBasePath)
            dfSQL = pd.read_sql_query("SELECT * FROM UPPERBODY", conn)
            conn.close()
            df = dfSQL.drop(columns = ['ID'])
            df = df.rename(
                    columns = {
                            'frontline':     'Frontline POW Raise',
                            'shoulderpress': 'Shoulder Press',
                            'chairrow':      'Chair Side Row',
                            'supinecurl':    'Supine Curl',
                            'reardeltfly':   'Rear Delt Fly',
                            'sidebend':      'Standing Side Bend',
                            'lateralraise':  'Lateral Raise'
                            }
                    )
            dfAsStringU = df.to_html(index = False)
            Find = '<th>'
            Replace = '<th style="width:12.5%">'
            dfAsStringU = dfAsStringU.replace(Find, Replace)
            Find = '<tr style="text-align: right;">'
            Replace = '<tr style="text-align: center;">'
            dfAsStringU = dfAsStringU.replace(Find, Replace)
            Find = '<table border="1" class="dataframe">'
            Replace = '<table border="1" class="dataframe" style="width:1000px">'
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
            # html.SetPage(dfAsStringU, "")
            dialog = MyBrowser(None, -1)
            dialog.browser.SetPage(dfAsStringU, "")
            dialog.Show()

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
        wx.StaticText(
                self,
                -1,
                "LOWER BODY WEIGHTS",
                pos = (200,
                       20)
                )
        wx.StaticText(
                self,
                -1,
                "Date" + '.' * (90 - len("Date")),
                pos = (30,
                       50)
                )
        self.trial01 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (650,
                       50),
                size = (300,
                        25)
                )
        self.trial01.SetHint('YYYY-MM-DD')
        wx.StaticText(
                self,
                -1,
                "Stiff Leg RDL (Total Weight)" + '.' * (90 - len("Stiff Leg RDL (Total Weight)")),
                pos = (30,
                       80)
                )
        self.trial11 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (650,
                       80),
                size = (300,
                        25)
                )
        self.trial11.SetHint('Total Weight')
        wx.StaticText(
                self,
                -1,
                "Hip Thruster" + '.' * (90 - len("Hip Thruster")),
                pos = (30,
                       110)
                )
        self.trial12 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (650,
                       110),
                size = (300,
                        25)
                )
        self.trial12.SetHint('Total Weight')
        wx.StaticText(
                self,
                -1,
                "Forward Squat (Total Weight)" + '.' * (90 - len("Forward Squat (Total Weight)")),
                pos = (30,
                       140)
                )
        self.trial13 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (650,
                       140),
                size = (300,
                        25)
                )
        self.trial13.SetHint('Total Weight')
        wx.StaticText(
                self,
                -1,
                "Forward Lunge (Total Weight)" + '.' * (90 - len("Forward Lunge (Total Weight)")),
                pos = (30,
                       170)
                )
        self.trial14 = wx.TextCtrl(
                self,
                -1,
                "",
                pos = (650,
                       170),
                size = (300,
                        25)
                )
        self.trial14.SetHint('Total Weight')
        self.btn = wx.Button(
                self,
                201,
                "SAVE",
                pos = (450,
                       830),
                size = (70,
                        30)
                )
        self.Bind(
                wx.EVT_BUTTON,
                self.save,
                id = 201
                )
        self.btn1 = wx.Button(
                self,
                202,
                "EXIT",
                pos = (550,
                       830),
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

    def save(
            self,
            event
            ):
        """
        :param event:
        :type event:
        """
        trial01 = self.trial01.GetValue()
        trial11 = self.trial11.GetValue()
        trial12 = self.trial12.GetValue()
        trial13 = self.trial13.GetValue()
        trial14 = self.trial14.GetValue()

        def data_entry():
            """

            """
            conn = sqlite3.connect(dataBasePath)
            c = conn.cursor()
            c.execute(
                    """INSERT INTO LOWERBODY (
                DATE,
                STIFFLEGRDL,
                HIPTHRUSTER,
                FORWARDSQUAT,
                FORWARDLUNGE
                )
                VALUES (
                ?,
                ?,
                ?,
                ?,
                ?
                )
                """,
                    (
                            trial01,
                            trial11,
                            trial12,
                            trial13,
                            trial14
                            )
                    )
            conn.commit()
            conn.close

            self.dial = wx.MessageDialog(
                    None,
                    'Uploaded Successfully!',
                    'Info',
                    wx.OK
                    )
            self.dial.ShowModal()
            conn = sqlite3.connect(dataBasePath)
            dfSQL = pd.read_sql_query("SELECT * FROM LOWERBODY", conn)
            conn.close()

            df = dfSQL.drop(columns = ['ID'])
            df = df.rename(
                    columns = {
                            'stifflegrdl':  'Stiff Leg RDL',
                            'hipthruster':  'Hip Thruster',
                            'forwardsquat': 'Forward Squat',
                            'forwardlunge': 'Forward lunge'
                            }
                    )
            dfAsStringL = df.to_html(index = False)
            Find = '<th>'
            Replace = '<th style="width:20%">'
            dfAsStringL = dfAsStringL.replace(Find, Replace)
            Find = '<tr style="text-align: right;">'
            Replace = '<tr style="text-align: center;">'
            dfAsStringL = dfAsStringL.replace(Find, Replace)
            Find = '<table border="1" class="dataframe">'
            Replace = '<table border="1" class="dataframe" style="width:1000px">'
            dfAsStringL = dfAsStringL.replace(Find, Replace)
            Find = '<td>'
            Replace = '<td align="center">'
            dfAsStringL = dfAsStringL.replace(Find, Replace)
            html = wx.html2.WebView.New(self, -1, size = (1200, 800))
            dialog = MyBrowser(None, -1)
            dialog.browser.SetPage(dfAsStringL, "")
            dialog.Show()

        data_entry()


# class upperBodyTable(scrolled.ScrolledPanel):
#     """
#
#     """
#
#     def __init__(
#             self,
#             parent
#             ):
#         scrolled.ScrolledPanel.__init__(
#                 self,
#                 parent,
#                 -1
#                 )
#         vbox = wx.BoxSizer(wx.VERTICAL)
#         vbox.Add(
#                 wx.StaticLine(
#                         self,
#                         -1,
#                         size=(1500,
#                               -1)
#                         ),
#                 0,
#                 wx.ALL,
#                 5
#                 )
#         vbox.Add(
#                 wx.StaticLine(
#                         self,
#                         -1,
#                         size=(-1,
#                               1500)
#                         ),
#                 0,
#                 wx.ALL,
#                 5
#                 )
#         vbox.Add(
#                 (20,
#                  20)
#                 )
#         self.SetSizer(vbox)
#         self.SetupScrolling()
#         self.SetBackgroundColour(
#                 wx.Colour(
#                         255,
#                         153,
#                         153
#                         )
#                 )
#         self.SetFont(
#                 wx.Font(
#                     12,
#                     wx.MODERN,
#                     wx.NORMAL,
#                     wx.NORMAL,
#                     False,
#                     u'JetBrains Mono NL'
#                     )
#                 )
#         wx.StaticText(
#                 self,
#                 -1,
#                 "UPPER BODY TABLE",
#                 pos=(170,
#                      20)
#                 )
#         self.btn1 = wx.Button(
#                 self,
#                 202,
#                 "EXIT",
#                 pos=(450,
#                      830),
#                 size=(70,
#                       30)
#                 )
#         self.Bind(
#                 wx.EVT_BUTTON,
#                 self.exit,
#                 id=202
#                 )
#         self.btn2 = wx.Button(
#                 self,
#                 203,
#                 "REFRESH",
#                 pos=(550,
#                      830),
#                 size=(70,
#                       30)
#                 )
#         self.Bind(
#                 wx.EVT_BUTTON,
#                 self.refresh,
#                 id=203
#                 )
#
#     def refresh(self, event):
#         try:
#             html
#         except NameError:
#             html = None
#
#         if html is None:
#             conn = sqlite3.connect(dataBasePath)
#             dfSQL = pd.read_sql_query("SELECT * FROM UPPERBODY", conn)
#             conn.close()
#             df = dfSQL.drop(columns=['ID'])
#             df = df.rename(columns={'frontline':'Frontline POW Raise', 'shoulderpress':'Shoulder Press', 'chairrow':'Chair Side Row','supinecurl':'Supine Curl','reardeltfly':'Rear Delt Fly','sidebend':'Standing Side Bend', 'lateralraise':'Lateral Raise'})
#             dfAsStringU = df.to_html(index=False)
#             Find = '<th>'
#             Replace = '<th style="width:12.5%">'
#             dfAsStringU = dfAsStringU.replace(Find, Replace)
#             Find = '<tr style="text-align: right;">'
#             Replace = '<tr style="text-align: center;">'
#             dfAsStringU = dfAsStringU.replace(Find, Replace)
#             Find = '<table border="1" class="dataframe">'
#             Replace = '<table border="1" class="dataframe" style="width:1000px">'
#             dfAsStringU = dfAsStringU.replace(Find, Replace)
#             Find = '<td>'
#             Replace = '<td align="center">'
#             dfAsStringU = dfAsStringU.replace(Find, Replace)
#             html = wx.html2.WebView.New(
#                     self,
#                     -1,
#                     size=(
#                         1200,
#                         800
#                         )
#                     )
#             html.SetPage(dfAsStringU, "")
#         else:
#             html.Reload(wx.html2.WEBVIEW_RELOAD_NO_CACHE)
#
#     @staticmethod
#     def exit(event):
#         """
#
#         :param event:
#         :type event:
#         """
#         wx.Exit()
#
#
# class lowerBodyTable(scrolled.ScrolledPanel):
#     """
#
#     """
#
#     def __init__(
#             self,
#             parent
#             ):
#         scrolled.ScrolledPanel.__init__(
#                 self,
#                 parent,
#                 -1
#                 )
#
#         vbox = wx.BoxSizer(wx.VERTICAL)
#         vbox.Add(
#                 wx.StaticLine(
#                         self,
#                         -1,
#                         size=(750,
#                               -1)
#                         ),
#                 0,
#                 wx.ALL,
#                 5
#                 )
#         vbox.Add(
#                 wx.StaticLine(
#                         self,
#                         -1,
#                         size=(-1,
#                               750)
#                         ),
#                 0,
#                 wx.ALL,
#                 5
#                 )
#         vbox.Add(
#                 (20,
#                  20)
#                 )
#         self.SetSizer(vbox)
#         self.SetupScrolling()
#         self.SetBackgroundColour(
#                 wx.Colour(
#                         255,
#                         153,
#                         153
#                         )
#                 )
#         self.SetFont(
#                 wx.Font(
#                     12,
#                     wx.MODERN,
#                     wx.NORMAL,
#                     wx.NORMAL,
#                     False,
#                     u'JetBrains Mono NL'
#                     )
#                 )
#         wx.StaticText(
#                 self,
#                 -1,
#                 "LOWER BODY TABLE",
#                 pos=(170,
#                      20)
#                 )
#         self.btn1 = wx.Button(
#                 self,
#                 202,
#                 "EXIT",
#                 pos=(450,
#                      830),
#                 size=(70,
#                       30)
#                 )
#         self.Bind(
#                 wx.EVT_BUTTON,
#                 self.exit,
#                 id=202
#                 )
#         self.btn2 = wx.Button(
#                 self,
#                 203,
#                 "REFRESH",
#                 pos=(550,
#                      830),
#                 size=(70,
#                       30)
#                 )
#         self.Bind(
#                 wx.EVT_BUTTON,
#                 self.refresh,
#                 id=203
#                 )
#
#     def refresh(self, event):
#         try:
#             html
#         except NameError:
#             html = None
#
#         if html is None:
#             conn = sqlite3.connect(dataBasePath)
#             dfSQL = pd.read_sql_query("SELECT * FROM LOWERBODY", conn)
#             conn.close()
#
#             df = dfSQL.drop(columns=['ID'])
#             df = df.rename(columns={
#                 'stifflegrdl': 'Stiff Leg RDL',
#                 'hipthruster': 'Hip Thruster',
#                 'forwardsquat': 'Forward Squat',
#                 'forwardlunge': 'Forward lunge'
#                 }
#                            )
#             dfAsStringL = df.to_html(index=False)
#             Find = '<th>'
#             Replace = '<th style="width:20%">'
#             dfAsStringL = dfAsStringL.replace(Find, Replace)
#             Find = '<tr style="text-align: right;">'
#             Replace = '<tr style="text-align: center;">'
#             dfAsStringL = dfAsStringL.replace(Find, Replace)
#             Find = '<table border="1" class="dataframe">'
#             Replace = '<table border="1" class="dataframe" style="width:1000px">'
#             dfAsStringL = dfAsStringL.replace(Find, Replace)
#             Find = '<td>'
#             Replace = '<td align="center">'
#             dfAsStringL = dfAsStringL.replace(Find, Replace)
#
#             html = wx.html2.WebView.New(self, -1, size=(1200, 800))
#             html.SetPage(dfAsStringL, "")
#         else:
#             html.Reload(wx.html2.WEBVIEW_RELOAD_NO_CACHE)
#
#     @staticmethod
#     def exit(event):
#         """
#
#         :param event:
#         :type event:
#         """
#         wx.Exit()


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
                        u'Atkinson Hyperlegible'
                        )
                )
        self.initui()

    def initui(self):
        """

        """
        nb = wx.Notebook(self)
        nb.AddPage(
                lowerBody(nb),
                "LOWER BODY"
                )
        # nb.AddPage(
        # lowerBodyTable(nb),
        # "LOWER BODY TABLE"
        # )
        nb.AddPage(
                upperBody(nb),
                "UPPER BODY"
                )
        # nb.AddPage(
        # upperBodyTable(nb),
        # "UPPER BODY TABLE"
        # )
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
