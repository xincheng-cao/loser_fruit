from collections import OrderedDict
from sortedcontainers import SortedList


class ExamRoom_outoftime:

    def __init__(self, n: int):
        self._seat=OrderedDict()
        self._seat_len=n
        for i in range(n):
            self._seat[i]=0


    def seat(self) -> int:
        seat_list=[]
        for k,v in self._seat.items():
            if v==1:
                seat_list.append(k)
        #print(seat_list)

        if len(seat_list)==0:
            self._seat[0]=1
            return 0
        if len(seat_list)==1:
            if seat_list[0]==0:
                self._seat[self._seat_len-1]=1
                return self._seat_len-1
            elif seat_list[0]==self._seat_len-1:
                self._seat[0]=1
                return 0
            else:
                if seat_list[0]==self._seat_len-1-seat_list[0]:
                    self._seat[0] = 1
                    return 0
                elif seat_list[0]>self._seat_len-1-seat_list[0]:
                    self._seat[0] = 1
                    return 0
                else:
                    self._seat[self._seat_len - 1] = 1
                    return self._seat_len-1
        #max_len=float('-inf')
        #selected_seat=-1
        if seat_list[0]>0:
            selected_seat=0
            max_len=seat_list[0]
        else:
            max_len = float('-inf')
            selected_seat = None

        for i in range(len(seat_list)-1):
            if (seat_list[i+1]-seat_list[i])//2>max_len:
                max_len=(seat_list[i+1]-seat_list[i])//2
                selected_seat=max_len+seat_list[i]

        if seat_list[-1]<self._seat_len-1:
            if self._seat_len-1-seat_list[-1]>max_len:
                max_len=self._seat_len-1-seat_list[-1]
                selected_seat=self._seat_len-1

        self._seat[selected_seat]=1



        return selected_seat


    def leave(self, p: int) -> None:
        self._seat[p]=0


class ExamRoom:

    def __init__(self, n: int):
        #self._seat=OrderedDict()
        self._seat_len=n
        self._sorted_list=SortedList()
        #for i in range(n):
        #    self._seat[i]=0


    def seat(self) -> int:
        seat_list=[]
        for k in self._sorted_list:
            seat_list.append(k)
        #print(seat_list)

        if len(seat_list)==0:
            #self._seat[0]=1
            self._sorted_list.add(0)
            return 0
        if len(seat_list)==1:
            if seat_list[0]==0:
                #self._seat[self._seat_len-1]=1
                self._sorted_list.add(self._seat_len-1)
                return self._seat_len-1
            elif seat_list[0]==self._seat_len-1:
                #self._seat[0]=1
                self._sorted_list.add(0)
                return 0
            else:
                if seat_list[0]==self._seat_len-1-seat_list[0]:
                    #self._seat[0] = 1
                    self._sorted_list.add(0)
                    return 0
                elif seat_list[0]>self._seat_len-1-seat_list[0]:
                    #self._seat[0] = 1
                    self._sorted_list.add(0)
                    return 0
                else:
                    #self._seat[self._seat_len - 1] = 1
                    self._sorted_list.add(self._seat_len - 1)
                    return self._seat_len-1
        #max_len=float('-inf')
        #selected_seat=-1
        if seat_list[0]>0:
            selected_seat=0
            max_len=seat_list[0]
        else:
            max_len = float('-inf')
            selected_seat = None

        for i in range(len(seat_list)-1):
            if (seat_list[i+1]-seat_list[i])//2>max_len:
                max_len=(seat_list[i+1]-seat_list[i])//2
                selected_seat=max_len+seat_list[i]

        if seat_list[-1]<self._seat_len-1:
            if self._seat_len-1-seat_list[-1]>max_len:
                max_len=self._seat_len-1-seat_list[-1]
                selected_seat=self._seat_len-1

        #self._seat[selected_seat]=1
        self._sorted_list.add(selected_seat)



        return selected_seat


    def leave(self, p: int) -> None:
        #self._seat[p]=0
        self._sorted_list.remove(p)


# Your ExamRoom object will be instantiated and called as such:
'''
obj = ExamRoom(10)
print( obj.seat())
print( obj.seat())
print( obj.seat())
obj.leave(0)
obj.leave(4)
print( obj.seat())
print( obj.seat())
print( obj.seat())
print( obj.seat())
print( obj.seat())
print( obj.seat())
print( obj.seat())
print( obj.seat())
print( obj.seat())
obj.leave(0)
obj.leave(4)
print( obj.seat())
print( obj.seat())
obj.leave(7)
print( obj.seat())
obj.leave(3)
print( obj.seat())
obj.leave(3)
print( obj.seat())
obj.leave(9)
print( obj.seat())
obj.leave(0)
obj.leave(8)
print( obj.seat())
'''
