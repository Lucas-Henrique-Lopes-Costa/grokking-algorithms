def greet2(name):
  print("how are you, " + name + "?")

def bye():
  print("ok bye!")

def greet(name):
 print("hello, " + name + "!")
 greet2(name)
 print("getting ready to say bye...")
 bye()

print(greet("lucas"))

# 3.1 Suppose I show you a call stack like this. What information can you give me, just based on this call stack? Now let’s see the call stack in action with a recursive function.

# This process is in 2 step, and fist call fucntion set variable name to maggie, só second also recive it. But, the processo in second function didn't finish.

