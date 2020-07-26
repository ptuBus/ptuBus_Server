import json
from urllib import parse, request
from ptuBusCrawling.Crawler.Util.SendSlcakMsg import SendSlackMeg
from ptuBusServer.Models import BusTimeTableModel, BusTerminalModel

class BusTimeTableParsing:
    def __init__ (self):
        self.pData = BusTerminalModel.objects.all()
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

    def min2hour(self, time):
        if (time.find(':') == -1):
            time = int(time)
            hour = time // 60
            min = time % 60
            return str(hour).zfill(2) + ":" + str(min).zfill(2)
        else:
            return time

    def parsing(self):
        count = 1
        specialFare = 0
        nightschedule = '0'
        for pData in self.pData:
            if pData.isExpress == 0:
                url = self.url[0]
                special = 0
            elif pData.isExpress == 1:
                url = self.url[1]
                special = 1
            query = [('apiKey', self.apiKey), ('startStationID', pData.startStationID),
                     ('endStationID', pData.endStationID)]
            data = self.openURL(url, query)
            rDD = self.checkError(json.loads(data))
            schedules = self.cleanSchedule(rDD["result"]["station"][0]['schedule'])

            if (special == 1):
                specialFare = rDD["result"]["station"][0]['specialFare']

            if rDD["result"]["station"][0]['nightSchedule'] != "":
                nightschedule = rDD["result"]["station"][0]['nightSchedule']

            for schedule in schedules:
                BusTimeTableModel(id = count,
                                  startStationName = pData.startStationName,
                                  startStationID =  pData.startStationID,
                                  endStationName = pData.endStationName,
                                  endStationID = pData.endStationID,
                                  wasteTime = self.min2hour(rDD["result"]["station"][0]['wasteTime']),
                                  normalFare = rDD["result"]["station"][0]['normalFare'],
                                  specialFare = specialFare,
                                  nightFare = rDD["result"]["station"][0]['nightFare'],
                                  schedule = schedule,
                                  nightschedule = nightschedule,
                                  isExpress = pData.isExpress
                                  ).save()
                count += 1

if __name__ == "__main__":
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from BusTerminalParsing import BusTerminalParsing
    else:
        from .BusTerminalParsing import BusTerminalParsing
    print (BusTimeTableParsing(BusTerminalParsing().parsing()).parsing())