from base_model import BaseAdvertising


class Advertiser(BaseAdvertising):
    __totalClicks = 0

    def __int__(self, id, name):
        self.__id = id
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    @staticmethod
    def help(self):
        print("I\'m helping")

    @staticmethod
    def describeMe(self):
        print("I\'m the Advertiser class")

    @staticmethod
    def getTotalClicks(self):
        return Advertiser.__totalClicks

    def incClicks(self):
        super(Advertiser, self).incClicks()
        Advertiser.__totalClicks += 1
