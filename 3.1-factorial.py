def fact(x):
 if x == 1:
  return 1
 else:
  return x * fact(x-1)
 
print(fact(3))

# 3.2 Suppose you accidentally write a recursive function that runs forever. As you saw, your computer allocates memory on the stack for each function call. What happens to the stack when your recursive function runs forever?

# It's going forever, until the program chash, call it stack overflow