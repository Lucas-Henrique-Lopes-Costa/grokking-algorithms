def binary_search(list, item):
  low = 0
  high = len(list)-1
  while low <= high:
    mid = (low + high)
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None

my_list = [1, 2, 3, 5, 7, 9, 10, 14, 16, 18, 20]

print(binary_search(my_list, 9))

# EXERCISES
# 1.1 Suppose you have a sorted list of 128 names, and you're searching through it using binary search. Wha€s the maximum number of steps it would take?

# Log2(128) = 7

# 1.2 Suppose you double the size of the list. What's the maximum number of steps now?

# Log2(256) = 8

# 1.3 You have a name, and you want to find the person's Phone number in the Phone book.

# O(log n)

# 1.4 You have a Phone number, and you want to find the person's name in the Phone book. (Hint: You'll have to search through the whole book!)

# O(n)

# 1.5 You want to read the numbers of every person in the Phone book.

# O(n)

# 1.6 You want to read the numbers of just the As. (This is a tricky one! It involves concepts that are covered more in  hapter 4. Read the answer—you may be surprised!)

# O(n/26)