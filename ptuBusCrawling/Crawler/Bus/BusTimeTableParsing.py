import json
from urllib import parse, request
from ptuBusCrawling.Crawler.Util.SendSlcakMsg import SendSlackMeg
import sys
from ptuBusCrawling.Crawler.Bus.BusTerminalParsing import BusTerminalParsing

class BusTimeTableParsing:
    def __init__ (self, data):
        self.pData = data
        self.apiKey = 'mxl46U1g52x6aVOUX/p969Zbtq9EZmboho4Jp5WiUlQ'
        self.url = ['https://api.odsay.com/v1/api/intercityServiceTime?',
                    'https://api.odsay.com/v1/api/expressServiceTime?']
        self.msg = SendSlackMeg()

    def makeURL(self, url, query):
        return url + parse.urlencode(query, encoding='UTF-8', doseq=True)

    def openURL(self, url_type, query):
        url = self.makeURL(url_type, query)
        request_url = request.Request(url)
        response = request.urlopen(request_url)
        return response.read().decode('utf-8')

    def cleanSchedule(self, schedule):
        replaceAll = schedule.replace("/", " ")
        return ''.join(replaceAll).split()

    def makeDict(self, startStationID, startStationName, endStationID, endStationName, wasteTime, normalFare, specialFare ,nightFare,
                 schedule, nightschedule):
        ListStr = ["startStationID", "startStationName", "endStationID", "endStationName", "wasteTime", "normalFare", "specialFare",
                   "nightFare", "schedule", "nightschedule"]
        dList = [startStationID, startStationName, endStationID, endStationName, wasteTime, normalFare, specialFare, nightFare, schedule ,nightschedule]
        return dict(zip(ListStr, dList))

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
        for pData in self.pData:
            if pData['isExpress'] == 0:
                url = self.url[0]
                special = 0
            elif pData['isExpress'] == 1:
                url = self.url[1]
                special = 1
            query = [('apiKey', self.apiKey), ('startStationID', pData['startStationID']),
                     ('endStationID', pData['endStationID'])]

            data = self.openURL(url, query)
            rDD = self.checkError(json.loads(data))
            startStationID = pData['startStationID']
            startStationName = pData['startStationName']
            endStationName = pData["endStationName"]
            endStationID = pData["endStationID"]
            wasteTime = rDD["result"]["station"][0]['wasteTime']
            normalFare = rDD["result"]["station"][0]['normalFare']
            if (special == 0):
                specialFare = 0
            elif (special == 1):
                specialFare = rDD["result"]["station"][0]['specialFare']
            nightFare = rDD["result"]["station"][0]['nightFare']
            schedules = self.cleanSchedule(rDD["result"]["station"][0]['schedule'])
            if (rDD["result"]["station"][0]['nightSchedule'] == ""):
                nightschedule = '0'
            else:
                nightschedule = rDD["result"]["station"][0]['nightSchedule']
            for schedule in schedules:
                temp.append(self.makeDict(startStationID,
                                          startStationName,
                                          endStationID,
                                          endStationName,
                                          wasteTime,
                                          normalFare,
                                          specialFare,
                                          nightFare,
                                          schedule,
                                          nightschedule))
        return temp