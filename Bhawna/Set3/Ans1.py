def double(x):
    return x * 2

l = [1,2,3,4,5,6,7]

# A map applies a function to each item in an iterable(eg-list)
# map(function,iterable)

result = map(double,l)

print(list(result))
