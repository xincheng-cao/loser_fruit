'''
[1,3,1,2,3,1,]
[0,1,3,]
'''

def intersection_fn(set_a:set,list_b:list)->set:
    #return set(list_a).intersection(set(list_b))
    #set_a
    ans=set()
    for e in list_b:
        if e in set_a:
            ans.add(e)
    return ans


def multi_intersection_fn(matrix,)->set:
    ans_set=set(matrix[0])
    for i in range(1,len(matrix)):
        ans_set=intersection_fn(ans_set,matrix[i])
    return ans_set