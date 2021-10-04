import base_model
import advertiser


class Ad(base_model.BaseAdvertising):
    def __int__(self, id, title, imgUrl, link, adv: advertiser.Advertiser):
        self.__id = id
        self.__title = title
        self.__imgUrl = imgUrl
        self.__link = link
        self.__adv = adv

    def getTitle(self):
        return self.__title

    def setTitle(self, title):
        self.__title = title

    def getImgUrl(self):
        return self.__imgUrl

    def setImgUrl(self, imgUrl):
        self.__imgUrl = imgUrl

    def getLink(self):
        return self.__link

    def setLink(self, link):
        self.__link = link

    def setAdvertiser(self, adv):
        self.__adv = adv

    @staticmethod
    def describeMe(self):
        print("I\'m the Ad class")

    def incClicks(self):
        super(Ad, self).incClicks()
        self.__adv.incClicks()

    def incViews(self):
        super(Ad, self).incViews()
        self.__adv.incViews()
