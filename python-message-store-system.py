#Message store

messages=[]
import time

while True:
    print("1)Send message:")
    print("2)Show history:")
    print("3)Filter by user:")
    print("4)Exit:")

    ch=input("Choose:")

    if ch=="1":
        name=input("Enter the name:")
        message=input("Enter the message:")

        current_time = time.strftime("%H:%M:%S")

        chat={"Name":name,"MSG":message,"Time":current_time}

        messages.append(chat)
    if ch=="2":
    	print("History:",messages)
    if ch=="3":
    	name=input("Enter the name:")
    	for m in messages:
    		if m["Name"]==name:
    			print(m)
    		else:
    			print("No name!")
    		
    if ch=="4":
    	print("Bye!!")
    	break
