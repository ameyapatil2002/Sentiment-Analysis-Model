n = 5
sum= 0
prime = True 

for i in range(2,n+1):
    for j in range(2,i):
        if i%j == 0:
            prime= False
        
    if prime:
        sum+=i
    prime = True
print(sum)
