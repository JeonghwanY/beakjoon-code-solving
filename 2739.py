n=int(input())
if 1<=n<10:
    i=1
    while i<=9:
        print(f"{n} * {i} = {n*i}")
        i+=1
else:
    print("다시 입력하세요")