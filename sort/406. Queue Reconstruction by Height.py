class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if len(people) <= 1: return people

        '''
        [7,0]  [7,1]  [6,1] [5,0] [5,2] [4,4] 

        [7,0]  [7,1].  [6,1] [5,0] [5,2] [4,4] top-2 sorted
        [7,0]  [6,1] [7,1]. [5,0] [5,2] [4,4] top-3 sorted
        [5,0] [7,0]  [6,1] [7,1]. [5,2] [4,4] top-4 sorted
        [5,0] [7,0] [5,2] [6,1] [7,1]. [4,4] top-5 sorted
        [5,0] [7,0] [5,2] [6,1] [4,4] [7,1]. top-6 sorted
        '''

        def partition(nums, start_idx, end_idx):
            left_part_end_idx = start_idx - 1
            right_part_start_idx = end_idx + 1

            i = start_idx + 1
            std_val = nums[start_idx]
            while i < right_part_start_idx:
                if nums[i][0] > std_val[0]:
                    left_part_end_idx += 1
                    nums[i], nums[left_part_end_idx] = nums[left_part_end_idx], nums[i]
                    i += 1
                elif nums[i][0] < std_val[0]:
                    right_part_start_idx -= 1
                    nums[i], nums[right_part_start_idx] = nums[right_part_start_idx], nums[i]
                else:
                    if nums[i][1] < std_val[1]:
                        left_part_end_idx += 1
                        nums[i], nums[left_part_end_idx] = nums[left_part_end_idx], nums[i]
                        i += 1
                    elif nums[i][1] > std_val[1]:
                        right_part_start_idx -= 1
                        nums[i], nums[right_part_start_idx] = nums[right_part_start_idx], nums[i]
                    else:
                        i += 1

            return left_part_end_idx, right_part_start_idx

        def quick_sort(nums, start_idx, end_idx):
            # print(start_idx,end_idx)
            if end_idx <= start_idx: return
            left_part_end_idx, right_part_start_idx = partition(nums, start_idx, end_idx)

            quick_sort(nums, start_idx, left_part_end_idx)
            quick_sort(nums, right_part_start_idx, end_idx)

        quick_sort(people, 0, len(people) - 1)

        # flag=True
        for i in range(1, len(people)):
            if people[i][1] != i:
                # flag=False
                break
        # if flag: return people
        # print(people)

        ans = people[:i]
        for j in range(i, len(people)):
            if people[j][1] != j:
                ans.insert(people[j][1], people[j])
            else:
                ans.append(people[j])

        return ans


















