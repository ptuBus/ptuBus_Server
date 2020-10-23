from urllib import request
import sqlite3
import json

class makeSqlite:
    def __init__(self):
        self.conn = sqlite3.connect('app.db')
        self.cur = self.conn.cursor()
        self.URL = {'BusTerminal' : 'http://127.0.0.1:8000/server/bus/terminal/', 'TrainStation' : 'http://127.0.0.1:8000/server/train/station/',
                    'SubwayLine' : 'http://127.0.0.1:8000/server/subway/line/', 'SubwayStation' : 'http://127.0.0.1:8000/server/subway/station/'}

    def openURL(self, url):
        request_url = request.Request(url)
        response = request.urlopen(request_url)
        return response.read().decode('utf-8')

    def makeData(self):
        for name, url in self.URL.items():
            self.conn.execute('delete from ' + name)
            if (name == 'BusTerminal'):
                data = json.loads(self.openURL(url))
                temp = []
                for i in data:
                    temp.append(tuple(i.values()))
                self.cur.executemany('INSERT INTO BusTerminal VALUES (?, ?, ?, ?, ?, ?)', temp)
                self.conn.commit()
            elif (name == 'TrainStation'):
                data = json.loads(self.openURL(url))
                temp = []
                for i in data:
                    temp.append(tuple(i.values()))
                self.cur.executemany('INSERT INTO TrainStation VALUES (?, ?, ?, ?, ?)', temp)
                self.conn.commit()
            elif (name == 'SubwayLine'):
                data = json.loads(self.openURL(url))
                temp = []
                for i in data:
                    temp.append(tuple(i.values()))
                self.cur.executemany('INSERT INTO SubwayLine VALUES (?, ?, ?, ?, ?)', temp)
                self.conn.commit()
            elif (name == 'SubwayStation'):
                data = json.loads(self.openURL(url))
                temp = []
                for i in data:
                    temp.append(tuple(i.values()))
                self.cur.executemany('INSERT INTO SubwayStation VALUES (?, ?, ?, ?, ?)', temp)
                self.conn.commit()

if __name__ == "__main__":
    print (makeSqlite().makeData())



