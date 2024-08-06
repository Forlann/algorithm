import random
import time

start_time = time.time()

def bubble_sort(n_list):
  n = len(n_list)
  
  for i in range(n):
    swaped = False
    for j in range(n-i-1):
      num = n_list[j]
      next_num = n_list[j + 1]

      if num > next_num:
        n_list[j], n_list[j + 1] = next_num, num
        swaped = True
        
    if not swaped:
      break

      
  return n_list

n_list = random.sample(range(1, 1000000), 100000)
# print("Unsorted list:", n_list)
sorted_list = bubble_sort(n_list)
# print("Sorted list:", sorted_list)

print("--- %s seconds ---" % (time.time() - start_time))
