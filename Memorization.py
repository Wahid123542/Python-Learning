#Memorization in python
import functools
def factorial(n, cache={}):
  if n in cache:
    return cache[n]
  elif n==1 or n==0:
    return 1
  else:
    cache[n]=n*factorial(n-1)
    return cache[n]
factorial(3)
