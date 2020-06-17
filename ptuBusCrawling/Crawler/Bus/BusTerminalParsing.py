import json
from urllib import parse, request
from ptuBusCrawling.Crawler.Util.SendSlcakMsg import SendSlackMeg
import sys

class BusTerminalParsing:
    def __init__(self, CID='1220'):
        apiKey = 'PNsB3fNkDcbHCx6LK4YWprIVdIhoyc8EL7W1b8v1jyE'
        self.url = [{'url' : 'https://api.odsay.com/v1/api/intercityBusTerminals?', 'isExpress': 0},
                    {'url' : 'https://api.odsay.com/v1/api/expressBusTerminals?', 'isExpress': 1}]
        self.query = [('apiKey', apiKey), ('CID', CID)]
        self.msg = SendSlackMeg()

    def makeURL(self, url):
        return url + parse.urlencode(self.query, encoding='UTF-8', doseq=True)

    def openURL(self, url):
        url = self.makeURL(url)
        request_url = request.Request(url)
        response = request.urlopen(request_url)
        return response.read().decode('utf-8')

    def makeDict(self, startStationID, startStationName,endStationID, endStationName, isExpress):
        ListStr = ["startStationID", "startStationName", "endStationID", "endStationName", "isExpress"]
        dList = [startStationID, startStationName, endStationID, endStationName, isExpress]
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
        for Type in self.url:
            data = self.openURL(Type['url'])
            rDD = self.checkError(json.loads(data))
            isExpress = Type['isExpress']
            t = rDD["result"]
            for i in range(len(t)):
                if (rDD["result"][i]['stationName'] == '평택시외버스터미널' or rDD["result"][i][
                    'stationName'] == '평택고속버스터미널'):
                    startStationID = rDD["result"][i]['stationID']
                    startStationName = rDD["result"][i]['stationName']
                    results = rDD["result"][i]['destinationTerminals']
                    for result in results:
                        temp.append(self.makeDict(startStationID, startStationName, result['stationID'],
                            result['stationName'], isExpress))
            return temp