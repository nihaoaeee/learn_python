lst = [1 ,2 ,3, 4, 5]
g = (n for n in lst if n in lst)
lst = [0, 1, 2]
print(list(g))