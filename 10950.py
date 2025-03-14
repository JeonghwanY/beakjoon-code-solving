n=int(input())
add=[]
for _ in range(n):
    a,b=map(int,input().split())
    add.append((a+b))
print("\n".join(map(str,add)))
