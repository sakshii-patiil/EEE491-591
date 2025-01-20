n = int (input("Enter number of prime number:"))
k=1
count=0

my_prime_list=[]
while count!=n:
    c=0
    for j in range(1,k):
        if k%j==0:
            c+=1
    if c==1:
        my_prime_list.append(k)
        count+=1
    k+=1

print(my_prime_list)
            
