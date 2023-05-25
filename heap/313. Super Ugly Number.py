class Solution:
    def nthSuperUglyNumber2(self, n: int, primes: List[int]) -> int:
        import heapq
        max_32_bit_signed_int = pow(2, 32 - 1)
        seen = set()

        my_heap = [1]
        seen.add(1)
        if n == 1: return 1

        for i in range(1, n):
            cur = heapq.heappop(my_heap)
            # print(cur)
            for pri in primes:  # All the values of primes are unique and sorted in ascending order.
                tt = cur * pri
                if tt > max_32_bit_signed_int:
                    break
                else:
                    if tt not in seen:
                        heapq.heappush(my_heap, tt)
                        seen.add(tt)
                # if cur%pri==0:break

        return heapq.heappop(my_heap)

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        max_32_bit_signed_int = pow(2, 32 - 1)

        my_heap = [1]
        if n == 1: return 1

        for i in range(1, n):
            cur = heapq.heappop(my_heap)
            # print(cur)
            for pri in primes:  # All the values of primes are unique and sorted in ascending order.
                if cur * pri > max_32_bit_signed_int:
                    break
                else:
                    heapq.heappush(my_heap, cur * pri)
                if cur % pri == 0: break

        return heapq.heappop(my_heap)




