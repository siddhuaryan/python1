
per=int(input("Enter your percentage") )

if per<40 and per>0: 
	print("You are fail") 

elif per<60: 
	print("you are pass") 

elif per<70 : 
	print("merit") 

elif per>70 and per<100 :
    print("distinction")    

else: 
	print("your percentage should be in between 0-100") 
