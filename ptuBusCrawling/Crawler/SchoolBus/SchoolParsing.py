from ptuBusCrawling.Crawler.Util.WebParsing import WebParsing

class SchoolParsing:
    def __init__(self):
        url = "https://www.ptu.ac.kr/contents/www/cor/traffic_2.html"
        self.wp = WebParsing(url)

    def cleanList(self, all_list):
        pDataList = []
        toSchool = []
        toSubway = []

        all_list = ' '.join(all_list).split()
        for i in range(len(all_list)):
            if ((i % 4) < 2):
                toSchool.append(all_list[i].zfill(5))
            else:
                toSubway.append(all_list[i].zfill(5))

        toSchool.sort()
        toSubway.sort()
        pDataList.append(toSchool)
        pDataList.append(toSubway)
        return pDataList

    def makeDict(self, pDataList):
        temp = []
        toSchool = []
        toSubway = []
        ListStr = ["arrTime", "startStationID", "startStationNm", "endStationID", "endStationNm", "upDownTypeCode"]
        for i in range(len(pDataList)):
            #상행
            if i == 0:
                for j in range(len(pDataList[0])):
                    dList = [str(pDataList[0][j]), '0', '롯데', '1', '평택대학교', 'U']
                    zipbObj = zip(ListStr, dList)
                    toSchool.append(dict(zipbObj))
            elif i == 1:
                for j in range(len(pDataList[1])):
                    dList = [str(pDataList[1][j]), '1', '평택대학교', '0', '롯데', 'D']
                    zipbObj = zip(ListStr, dList)
                    toSubway.append(dict(zipbObj))
        temp.append(toSchool)
        temp.append(toSubway)
        return temp

    def parsingData(self):
        all_list = []
        tr_list = self.wp.parsingSelector('div > div.table7 > table > tbody > tr > td')
        for i in range(2, len(tr_list)):
            all_list.append(tr_list[i].text.strip())
        return self.makeDict(self.cleanList(all_list))

if __name__ == "__main__":
    print (SchoolParsing().parsingData())