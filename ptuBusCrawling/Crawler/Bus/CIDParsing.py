from ptuBusCrawling.Crawler.Util.WebParsing import WebParsing

class CIDParsing:
    def __init__(self):
        url = 'https://lab.odsay.com/guide/releaseReference#CID'
        self.wp = WebParsing(url)

    def makeDict(self, all_list):
        temp = []
        pCID = all_list[::2]
        pName = all_list[1::2]
        ListStr = ['CID', 'Name']
        for i in range(len(pCID)):
            dList = [pCID[i], pName[i]]
            zipbObj = zip(ListStr, dList)
            temp.append(dict(zipbObj))
        return temp

    def parsingData(self):
        all_list = []
        tr_list = self.wp.parsingSelector('#defineCode > div:nth-child(13) > table > tr > td')
        for i in range(len(tr_list)):
            all_list.append(tr_list[i].text.strip())
        return self.makeDict(all_list)

if __name__ == "__main__":
    print (CIDParsing().parsingData())