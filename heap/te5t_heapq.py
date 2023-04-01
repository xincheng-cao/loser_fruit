import heapq


# min-heap
li=[5,7,9,1,3]
heapq.heapify(li)
print(li)

# push pop
li=[5,7,9,1,3]
heapq.heapify(li)
print(li)

heapq.heappush(li,4)
print(li)

print(heapq.heappop(li))
print(li)

heapq.heappush(li,-100)
print(li)

print(heapq.heappop(li))
print(li)

#push&pop
li=[5,1,9,4,3]
heapq.heapify(li)
print(li)

print(heapq.heappushpop(li,-1))
print(li)

print(heapq.heappushpop(li,1000))
print(li)

print(heapq.heappushpop(li,4))
print(li)

# pop&push

li=[3,5,1,7,9,11,1,3]
heapq.heapify(li)
print(li)
'''
for i in range(len(li)):
    print(heapq.heappop(li))
'''
print(heapq.heapreplace(li,0))
print(li)

print(heapq.heapreplace(li,1))
print(li)

print(heapq.heapreplace(li,10000))
print(li)

print(heapq.heapreplace(li,2))
print(li)


# nlargest
# nsmallest

li=[10,1,3,1000,32,0,-1000,1,1,3000,3000,1]
heapq.heapify(li)
print(li)

print(heapq.nsmallest(len(li),li))
print(heapq.nlargest(len(li),li))
print(li)
