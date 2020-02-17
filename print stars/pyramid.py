n = eval(input())

blank = n-1
for i in range(1, n+1) :
    for j in range(1, blank+1) :
        print(" ", end="")
    for j in range(1, i+1) :
        if j != i :
            print("* ", end="")
        else :
            print("*")

    blank -= 1
  
    
    
