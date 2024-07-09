n = int(input("Termos da série: "))

if n == 1:
    print("0")
elif n == 2:
    print("0, 1")
elif n > 2:
    n0 = 1  
    n1 = 1 
    
    print("1, 1", end="")
    
    for count in range(2, n):
        termo = n0 + n1
        n0 = n1
        n1 = termo
      
        print(f", {termo}", end="")
    
    print()
