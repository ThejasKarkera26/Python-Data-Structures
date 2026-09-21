#RAILWAY WAITING LIST

waiting_list = []

while True:
    print("\n------ RAILWAY WAITING LIST------")
    print("1. Add Passenger\n2. Confirm Ticket\n3. Display Waiting List\n4. View First Passenger\n5. Search Passenger\n6. Cancel Passenger")
    print("7. Count Passengers\n8. Exit")
    print('-'*37)

    choice = int(input("Enter your choice: "))


    if choice == 1:
        name = input("Enter passenger name: ")
        waiting_list.append(name)
        print(name, "has been added to the waiting list.")


    elif choice == 2:
        if len(waiting_list) == 0:
            print("Waiting list is empty.")
        else:
            name = waiting_list.pop(0)
            print("Ticket confirmed for:", name)


    elif choice == 3:
        if len(waiting_list) == 0:
            print("Waiting list is empty.")
        else:
            print("\n--- Waiting List ---")

            for i in range(len(waiting_list)):
                print(i + 1, ".", waiting_list[i])


    elif choice == 4:
        if len(waiting_list) == 0:
            print("Waiting list is empty.")
        else:
            print("First passenger:", waiting_list[0])


    elif choice == 5:
        name = input("Enter passenger name to search: ")

        if name in waiting_list:
            position = waiting_list.index(name) + 1
            print(name, "is in the waiting list.")
            print("Waiting position:", position)
        else:
            print(name, "is not in the waiting list.")


    elif choice == 6:
        name = input("Enter passenger name to cancel: ")

        if name in waiting_list:
            waiting_list.remove(name)
            print(name, "has been removed from the waiting list.")
        else:
            print(name, "is not in the waiting list.")


    elif choice == 7:
        print("Total passengers waiting:", len(waiting_list))


    elif choice == 8:
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")