class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True

        if hand.__len__() % groupSize != 0:
            return False

        hand.sort()
        for k in range(len(hand) // groupSize):
            temp = []
            res = [hand.pop(0)]
            while len(res) < groupSize and len(hand) > 0:
                a = hand.pop(0)
                if a == res[-1] + 1:
                    res.append(a)
                else:
                    temp.append(a)
            if len(res) != groupSize:  # important!
                return False
            hand = temp + hand

        return len(hand) == 0