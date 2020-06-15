from urllib import parse, request
import json
from ptuBusCrawling.Crawler.Util.SendSlcakMsg import SendSlackMeg
import sys

class TrainStationParsing:
    def __init__(self):
        apiKey = 'mxl46U1g52x6aVOUX/p969Zbtq9EZmboho4Jp5WiUlQ'
        self.url = 'https://api.odsay.com/v1/api/trainTerminals?'
        self.query = [('apiKey', apiKey), ('CID', '1220'), ('terminalName', "평택")]
        self.msg = SendSlackMeg()

    def makeURL(self):
        return self.url + parse.urlencode(self.query, encoding='UTF-8', doseq=True)

    def openURL(self):
        url = self.makeURL()
        request_url = request.Request(url)
        response = request.urlopen(request_url)
        return response.read().decode('utf-8')

    def makeDict(self, startStationName, startStationID, endStationName, endStationID):
        ListStr = ["startStationName", "startStationID", "endStationName", "endStationID"]
        dList = [startStationName, startStationID, endStationName, endStationID]
        return dict(zip(ListStr, dList))

    def checkError(self, data):
        if (('error' in data) == True):
            code = data["error"][0]["code"]
            message = data["error"][0]["message"]
            error_status = "code : " + code + "\nmessage : " + message
            print (error_status)
            self.msg.sendMsg(error_status)
            sys.exit()
        elif (not data['result']):
            code = '-8'
            message = "필수 입력 값 형식 및 범위 오류"
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
        startStationID = rDD["result"][0]["stationID"]
        startStationName = rDD["result"][0]["stationName"]
        results = rDD["result"][0]['arrivalTerminals']
        for result in results:
            temp.append(self.makeDict(startStationName, startStationID, result['stationName'], result['stationID']))
        return temp