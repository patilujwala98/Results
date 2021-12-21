m=int(input("Enter math marks"))
p=int(input("Enter physics marks"))
c=int(input("Enter botany marks"))
s=int(input("Enter science marks"))
e=int(input("Enter English marks"))
h=int(input("Enter hindi marks"))

total=m+p+c+s+e+h
per=total/6

print("per=",per)

if per >= 90:
        print("Disctinction")
    
 
elif per >= 80:
    
        print("First class")
    
elif per >= 65:
    
        print("Second class")

elif per >=50:
    
        print("Pass class")

else:
        print("Fail")
    
  
