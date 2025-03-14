N,X = map(int,input().split())
A = list(map(int,input().split()))
result = [str(num) for num in A if num < X]  # 조건에 맞는 값만 리스트에 저장
print(" ".join(result))  # 리스트를 공백으로 구분하여 출력