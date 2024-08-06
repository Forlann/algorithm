import math


def dist(p1, p2):
    return math.sqrt(((p1[0] - p2[0])**2)
                     + ((p1[1] - p2[1])**2))
    
def closest_pair(points):
  min_d = float('inf')
  for i in range(len(points)):
    p1 = points[i]
    for j in range(i, len(points) - 1):
      p2 = points[j + 1]
      d = dist(p1, p2)
      # print(f'({p1}, {p2}), i:{i} d: {round(d, 2)}')
      
      if min_d > d:
        coordenate = [p1, p2]
        min_d = d
        
  return coordenate, round(min_d, 2)
      
    
points = [[10, 2], [6, 1], [3, 4], [25, 60], [0, 10], [34, 44]]

closest_pair, diff = closest_pair(points)

print(f"Cordenadas: {closest_pair}\nDistância: {diff}")