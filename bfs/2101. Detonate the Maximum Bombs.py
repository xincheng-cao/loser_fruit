class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # o n^2 problem i ilike

        bb2bbs = []

        for i in range(len(bombs)):
            bb2bbs.append([])
            for j in range(len(bombs)):
                if i == j: continue
                dis = bombs[i][2]
                act_dis = ((bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2) ** (1 / 2)
                if act_dis <= dis:
                    bb2bbs[i].append(j)

        res = [0] * len(bombs)
        for i in range(len(bombs)):
            q = []
            visited = set()
            q.insert(0, i)
            res[i] += 1
            visited.add(i)
            while len(q) > 0:
                bb = q.pop()

                for other_bb in bb2bbs[bb]:
                    if other_bb not in visited:
                        q.insert(0, other_bb)
                        res[i] += 1
                        visited.add(other_bb)  # adding visited is important right after it is put in queue!!!
        return max(res)