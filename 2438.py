n=int(input())
if 1<=n<=100:
    for i in range(1, n + 1):  # 1부터 n까지 반복
        print("*" * i)  # i 개수만큼 별 출력