numbers=[]

for i in range(5):
    user=int(input("Enter Numbers: "))
    numbers.append(user)
    print()
    
while True:
    print("1. Original List")
    print("2. Ascending order")
    print("3. Descending order\n")
    
    UsEr=input("Enter Order (1-3): ")
    print()
    if UsEr=="1":
        print(f"Original list: {numbers}\n")

    elif UsEr=="2":
        print(f"Original list: {numbers}\n")
        numbers.sort()
        print(f"Ascending order: {numbers}\n")

    elif UsEr=="3":
        print(f"Original list: {numbers}\n")
        numbers.sort(reverse=True)
        print(f"Descending order: {numbers}\n")

    elif UsEr=="exit".lower():    
        exit()
   


