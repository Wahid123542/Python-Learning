#knowing what is first class function
def square(n):
  return n*n
square(6)

my_function=square
my_function(6)

print(id(square))
print(id(my_function))

#it gives same memory location 
