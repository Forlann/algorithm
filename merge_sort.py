import random
import time

start_time = time.time()

def merge(a, b):
  c = []

  while len(a) > 0 and len(b) > 0:   
    if a[0] > b[0]:
      c.append(b[0])
      b.pop(0)
      
    else:
      c.append(a[0])
      a.pop(0)
  
  while len(a) > 0:
    c.append(a[0])
    a.pop(0)

  while len(b) > 0:
    c.append(b[0])
    b.pop(0)
    
  return c

def mergeSort(alist):
  if len(alist) == 1:
    return alist
  
  mid = len(alist)//2
  lefthalf = alist[:mid]
  righthalf = alist[mid:]

  lefthalf = mergeSort(lefthalf)
  righthalf = mergeSort(righthalf)
  return merge(lefthalf, righthalf)


alist = random.sample(range(1, 1000000), 100000)
# print(f'Unsorted list:{alist}')
sorted_list = mergeSort(alist)
# print(f'Sorted list: {mergeSort(alist)}')

print("--- %s seconds ---" % (time.time() - start_time))
