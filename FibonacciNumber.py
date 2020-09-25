#Fibonacci dizisi kendinden bir önceki sayının toplamıyla devam eden bir dizidir. 
# Yani örnek vermek gerekirse:

#0,1,1,2,3,5,8,13,21,34, … olarak devam eder. 

def Fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(7))

####
