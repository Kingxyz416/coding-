n = int(input("eneter no ="))
i=0
while(i<11):
    print(f"{n} X {i} = {n*i}")
    i+=1
for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"*(2*i-1),end="")
    print("")
i = n
while i > 0:
    print(" " * (n - i) + "*" * (2 * i - 1))
    i -= 1



   

for i in range(n):
    row = ""
    for j in range(n):
        if i == n // 2 and j == n // 2:
            row += " "
        else:
            row += "*"
    print(row)
    


        
