#MAKE A TO DO LIST
list=[]
while True:
    print("1.Add task")
    print("2.view")
    print("3.remove")
    print("exit")
    choice=input("enter choice")
    if choice=="1":
        a=input("enter task")
        list.append(a)
        print("task added")
    elif choice =="2":
        if not list:
            print("no task available")
        else:
            print("your task")
            for i, list in enumerate(list ,start=1):
                print(i, list)
    elif choice=="3":
        if not list:
            print("no task to remove")
        else:
            a1=input("enter the task which you want to want to remove")
            if 0<a1<=len(list):
                remove=list.pop(a1-1)
                print("task remove")
    elif choice=="4":
        print("thanks for using to do list")
    else:
        print("invalid choice")

        
                
                

