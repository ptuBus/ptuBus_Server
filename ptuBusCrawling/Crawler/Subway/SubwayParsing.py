import json
from operator import itemgetter
from urllib import parse, request
from ptuBusCrawling.Crawler.Util.SendSlcakMsg import SendSlackMeg
import sys

class SubwayParsing:
    def __init__(self, stationID = '1404'):
        apiKey = 'mxl46U1g52x6aVOUX/p969Zbtq9EZmboho4Jp5WiUlQ'
        self.url ='https://api.odsay.com/v1/api/subwayTimeTable?'
        self.query = [('apiKey', apiKey), ('stationID', stationID), ('showExpressTime', 1),
                      ('sepExpressTime', 1)]
        self.stationNm = ""
        self.dailyType = ['OrdList', 'SatList', 'SunList']
        self.wayCode = ['up', 'down']
        self.msg = SendSlackMeg()

    def makeURL(self):
        return self.url + parse.urlencode(self.query, encoding='UTF-8', doseq=True)

    def openURL(self):
        url = self.makeURL()
        request_url = request.Request(url)
        response = request.urlopen(request_url)
        return response.read().decode('utf-8')

    def makeDict(self, hour, min, dailyType, wayCode, ifExp):
        startIndex = min.find('(')
        newWord = min[:startIndex]
        ListStr = ["startStationName", "endStationName", "dailyTypeCode", "upDownTypeCode", "arrTime", "isExpress"]
        arrTime = str(hour).zfill(2) + ":" + str(newWord)
        endStation = str(min[startIndex + 1: -1])
        dList = [self.stationNm, endStation, dailyType, wayCode, arrTime, ifExp]
        return dict(zip(ListStr, dList))

    def sortDict(self, jData, dailyType, wayCode):
        temp = []
        hour = jData['Idx']
        min = ''.join((jData['list'])).split()
        for j in range(len(min)):
            temp.append(self.makeDict(hour, min[j], dailyType, wayCode, 0))
        if 'expList' in jData:
            min = ''.join((jData['expList'])).split()
            for j in range(len(min)):
                temp.append(self.makeDict(hour, min[j], dailyType, wayCode, 1))
        return sorted(temp, key=itemgetter('arrTime'))

    def checkError(self, data):
        if (('error' in data) == True):
            code = data["error"][0]["code"]
            message = data["error"][0]["message"]
            error_status = "code : " + code + "\nmessage : " + message
            print (error_status)
            self.msg.sendMsg(error_status)
            sys.exit()
        else:
            return data

    def parsing(self):
        temp = []
        data = self.openURL()
        rDD = self.checkError(json.loads(data))
        self.stationNm = rDD["result"]["stationName"]
        for dailyType in self.dailyType:
            typeList = []
            for wayCode in self.wayCode:
                jData = rDD["result"][dailyType][wayCode]["time"]
                for i in range(len(jData)):
                    typeList.extend(self.sortDict(jData[i], dailyType, wayCode))
            temp.append(typeList)
        return temp

if __name__ == "__main__":
    print (SubwayParsing().parsing())