menuChoice = -7

while menuChoice != 0:
    print("1) Calculate circumference\n2) Calculate area\nEnter 1,2, or 0 to exit: ")
    menuChoice = int(input())
    if menuChoice == 1:
        print("Please enter the radius: ")
        userRadius = int(input())
        circumference = (userRadius * 2) * 3.14
        print("The circumference of the circle is " + str(circumference))
    if menuChoice == 2:
        print("Please enter the radius: ")
        userRadius = int(input())
        area = (userRadius * userRadius) * 3.14
        print("The area of the circle is " + str(area))
    if menuChoice == 0:
        print("Have a nice day!")