from urllib import parse, request
import json
from ptuBusCrawling.Crawler.Util.SendSlcakMsg import SendSlackMeg
from ptuBusCrawling.Models import TrainTimeTableModel, TrainStationModel

class TrainTimeTableParsing:
    def __init__(self):
        self.pData = TrainStationModel.objects.all()
        self.apiKey = 'mxl46U1g52x6aVOUX/p969Zbtq9EZmboho4Jp5WiUlQ'
        self.url = 'https://api.odsay.com/v1/api/trainServiceTime?'
        self.msg = SendSlackMeg()
        self.trainTypeCode = ['KTX', '무궁화', '새마을', 'ITX-새마을', '누리로', '통근']
                                # 0      1        2         3          4      5
        self.dailyTypeCode = ['토', '금토일', '토일', '화수목금토일', '월화수목토일', '금', '금토', '금일', '월', '매일', '월화수목금토', '월화수목금', '월화수목']
                              #0      1       2         3            4       5     6      7     8     9         10
    def makeURL(self, query):
        return self.url + parse.urlencode(query, encoding='UTF-8', doseq=True)

    def openURL(self, query):
        url = self.makeURL(query)
        request_url = request.Request(url)
        response = request.urlopen(request_url)
        return response.read().decode('utf-8')

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
        count = 1
        for parsingData in self.pData:
            query = [('apiKey', self.apiKey), ('startStationID', parsingData.startStationID),
                     ('endStationID', parsingData.endStationID)]
            data = self.openURL(query)
            rDD = self.checkError(json.loads(data))
            startStationName = rDD["result"]["startStationName"]
            startStationID = rDD["result"]["startStationID"]
            endStationName = rDD["result"]["endStationName"]
            endStationID = rDD["result"]["endStationID"]
            results = rDD['result']['station']
            for result in results:
                TrainTimeTableModel(id = count,
                                    startStationName = startStationName,
                                    startStationID = startStationID,
                                    endStationName = endStationName,
                                    endStationID = endStationID,
                                    railName = result['railName'],
                                    trainClass = self.trainTypeCode.index(result['trainClass']),
                                    departureTime = result['departureTime'],
                                    arrivalTime = result['arrivalTime'],
                                    wasteTime = result['wasteTime'],
                                    runDay = self.dailyTypeCode.index(result['runDay'])
                ).save()
                count += 1

if __name__ == "__main__":
    if __package__ is None:
        import sys
        from os import path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
        from TrainStationParsing import TrainStationParsing
    else:
        from .TrainStationParsing import TrainStationParsing
    sample = TrainTimeTableParsing(TrainStationParsing().parsing()).parsing()