class BaseAdvertising:
    def __init__(self, id):
        self.__clicks = 0
        self.__views = 0
        self.__id = id

    def getClicks(self) -> int:
        return self.__clicks

    def getViews(self) -> int:
        return self.__views

    def incClicks(self):
        self.__clicks += 1

    def incViews(self):
        self.__views += 1

    @staticmethod
    def describeMe():
        print("I\'m the base model for Ad and Advertiser")
