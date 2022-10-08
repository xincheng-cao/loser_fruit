class UndergroundSystem:

    def __init__(self):
        self.enter=dict()
        self.history=dict()


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id in self.enter:
            return
        else:
            self.enter[id]=(stationName,t)


    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.enter:
            temp=self.enter.pop(id)
            #a sep is important!! bc there cant be aa+b and a+ab
            key=temp[0]+'\x01'+stationName
            if key in self.history:
                self.history[key].append(t-temp[1])
            else:
                self.history[key]=[t-temp[1]]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key= startStation+'\x01'+endStation
        if key in self.history:
            return sum(self.history[key])/self.history[key].__len__()


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)