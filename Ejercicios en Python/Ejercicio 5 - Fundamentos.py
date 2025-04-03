def primos(l,n):
    if n!=-1:
        l.append(n)
        while n!=-1:
            n = int(input("número? "))
            if n!=-1:
                l.append(n)
        primo=0
        print(l)
        for i in l:
            no_primo=0
            for j in range(2,i):
                if i%j==0:
                    no_primo+=1
            if no_primo==0:
                primo+=1
        return primo
l = []
n = int(input("número? "))
print("Hay",primos(l,n),"números primos")