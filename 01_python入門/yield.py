def myfunc():
    yield 'one'
    yield 'two'
    yield 'three'

x = myfunc()
y = myfunc()

print(x.__next__())  # one  
print(x.__next__())  # two  
print(x.__next__())  # three

print(next(y)) # one  
print(next(y)) # two  
print(next(y)) # three

