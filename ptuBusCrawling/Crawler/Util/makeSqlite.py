from urllib import request
import sqlite3
import json
import time
from ptuBusCrawling.Crawler.Util.SendSlcakMsg import SendSlackMeg
from ptuBusServer.Models.AppDB.AppDBModel import AppDBModel

now = time.localtime()


class makeSqlite:
    def __init__(self):
        self.msg = SendSlackMeg()
        self.conn = sqlite3.connect("app.db")
        self.cur = self.conn.cursor()
        self.URL = {
            "BusTerminal": "http://127.0.0.1:8000/server/bus/terminal/",
            "TrainStation": "http://127.0.0.1:8000/server/train/station/",
            "SubwayLine": "http://127.0.0.1:8000/server/subway/line/",
            "SubwayStation": "http://127.0.0.1:8000/server/subway/station/",
        }

    def openURL(self, name):
        request_url = request.Request(self.URL[name])
        response = request.urlopen(request_url)
        readData = response.read().decode("utf-8")
        data = json.loads(readData)
        temp = []
        for value in data:
            temp.append(tuple(value.values()))
        return temp

    def deleteTables(self):
        for name in self.URL.keys():
            self.conn.execute("delete from " + name)

    def makeDataBase(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS BusTerminal (id integer PRIMARY KEY, startStationName text, startStationID text,"
            "endStationName text,endStationID text, isExpress integer)"
        )
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS TrainStation (id integer PRIMARY KEY, startStationName text, startStationID text,"
            "endStationName text,endStationID text)"
        )
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS SubwayLine (id integer PRIMARY KEY, lineName text, lineCode text, lineColorCode text,"
            "lineSaidName text)"
        )
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS SubwayStation (id integer PRIMARY KEY, stationName text, stationCode text,"
            "lineCode text, railLineCode text)"
        )

    def diffDataBase(self):
        for name in self.URL:
            data = self.openURL(name)
            self.cur.execute("SELECT * FROM " + name)
            rows = self.cur.fetchall()
            if data != rows:
                self.msg.sendMsg(name + "에서 새로운 값이 검출되었습니다.")
                self.makeData()
                break

    def makeData(self):
        self.deleteTables()
        self.makeDataBase()
        for name in self.URL:
            data = self.openURL(name)
            if name == "BusTerminal":
                self.cur.executemany(
                    "INSERT INTO BusTerminal VALUES (?, ?, ?, ?, ?, ?)", data
                )
            elif name == "TrainStation":
                self.cur.executemany(
                    "INSERT INTO TrainStation VALUES (?, ?, ?, ?, ?)", data
                )
            elif name == "SubwayLine":
                self.cur.executemany(
                    "INSERT INTO SubwayLine VALUES (?, ?, ?, ?, ?)", data
                )
            elif name == "SubwayStation":
                self.cur.executemany(
                    "INSERT INTO SubwayStation VALUES (?, ?, ?, ?, ?)", data
                )
        self.conn.commit()
        fileKey = "{0}{1}{2}{3}{4}{5}".format(
            now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec
        )
        AppDBModel(fileKey=fileKey).save()
        self.msg.sendMsg("File Key = " + fileKey)


if __name__ == "__main__":
    print(makeSqlite().diffDataBase())
