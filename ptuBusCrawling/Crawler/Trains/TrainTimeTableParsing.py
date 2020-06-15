from urllib import parse, request
import json
from ptuBusCrawling.Crawler.Util.SendSlcakMsg import SendSlackMeg
import sys

class TrainTimeTableParsing:
    def __init__(self, data):
        self.pData = data
        self.apiKey = 'mxl46U1g52x6aVOUX/p969Zbtq9EZmboho4Jp5WiUlQ'
        self.url = 'https://api.odsay.com/v1/api/trainServiceTime?'
        self.msg = SendSlackMeg()

    def makeURL(self, query):
        return self.url + parse.urlencode(query, encoding='UTF-8', doseq=True)

    def openURL(self, query):
        url = self.makeURL(query)
        request_url = request.Request(url)
        response = request.urlopen(request_url)
        return response.read().decode('utf-8')

    def makeDict(self, startStationName, startStationID, endStationName, endStationID, railName, trainClass,
                 departureTime, arrivalTime, wasteTime, runDay):
        ListStr = ["startStationName", "startStationID", "endStationName", "endStationID", "railName", "trainClass",
                 "departureTime", "arrivalTime", "wasteTime", "runDay"]
        dList = [startStationName, startStationID, endStationName, endStationID, railName, trainClass,
                 departureTime, arrivalTime, wasteTime, runDay]
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
            query = [('apiKey', self.apiKey), ('startStationID', pData['startStationID']),
                     ('endStationID', pData['endStationID'])]
            data = self.openURL(query)
            rDD = self.checkError(json.loads(data))
            startStationName = rDD["result"]["startStationName"]
            startStationID = rDD["result"]["startStationID"]
            endStationName = rDD["result"]["endStationName"]
            endStationID = rDD["result"]["endStationID"]
            results = rDD['result']['station']
            for result in results:
                temp.append(self.makeDict(startStationName, startStationID, endStationName, endStationID,
                                          result['railName'],
                                          result['trainClass'], result['departureTime'], result['arrivalTime'],
                                          result['wasteTime']
                                          , result['runDay']))
            return temp