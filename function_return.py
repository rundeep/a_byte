def empty_function():
    pass

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print maximum(2, 3)
print empty_function()