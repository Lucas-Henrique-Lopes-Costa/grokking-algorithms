# Write out the code for the earlier sum function

def sum(arr):
  if arr == []:
    return 0
  return arr[0] + sum(arr[1:])

print(sum([1, 2]))