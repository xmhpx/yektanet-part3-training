from base_model import BaseAdvertising


class Advertiser(BaseAdvertising):
    __totalClicks = 0

    def __init__(self, id, name):
        super(Advertiser, self).__init__()
        self.__id = id
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    @staticmethod
    def help():
        print("I\'m helping")

    @staticmethod
    def describeMe():
        print("I\'m the Advertiser class")

    @staticmethod
    def getTotalClicks():
        return Advertiser.__totalClicks

    def incClicks(self):
        super(Advertiser, self).incClicks()
        Advertiser.__totalClicks += 1
