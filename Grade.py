per=int(input("enter your percentage"))
if per<40 and per>0 :
    print("you are awarded an F")

elif per<50:
    print("you are awarded an E")

elif per<60:
    print("You are awarded an D")

elif per<70:
    print("You are awarded an C")   

elif per<80:
    print("you gen a B")

elif per>80 and per<100:
    print("You get an A")  

else :
    print("your grade entred is wrong")
