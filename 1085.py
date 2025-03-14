x,y,w,h=map(int,input().split())
if 1 <= w <= 1000 and 1 <= h <= 1000 and 1 <= x <= w-1 and 1 <= y <= h-1:
    print(f"{min(x,y,w-x,h-y)}")
else:
    print("다시입력하세요.")