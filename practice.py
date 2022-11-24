def find_even_index(arr):
  for i in range(len(arr)):
    if sum(arr[:i])==sum(arr[i+1:]):
      print(arr.index(i))
      return arr.index(i)
  return -1
find_even_index([1,2,3,4,3,2,1])
