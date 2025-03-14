a= [int(input()) for _ in range(9)]
max_value = max(a)
max_index = a.index(max_value)+1
print(max_value,max_index)
