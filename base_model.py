class BaseAdvertising:
    def __init__(self):
        self.__clicks = 0
        self.__views = 0
        self.__id = 0

    def getClicks(self) -> int:
        return self.__clicks

    def getViews(self) -> int:
        return self.__views

    def incClicks(self):
        self.__clicks += 1

    def incViews(self):
        self.__views += 1

    @staticmethod
    def describeMe(self):
        print("I\'m the base model for Ad and Advertiser")
