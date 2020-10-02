for i in range(1,100):
        print("#####################################")
        print("#    		                    #")
        print("#           My Smartphone           #")
        print("# 	Python Application	    #")
        print("#			            #")
        print("#####################################")
        print("#		                    #")
        print("#  	  Select an application     #")
        print("# 		  to run	    #")
        print("#			            #")
        print("#####################################")
        print("#	     [Options]		    #")
        print("#####################################")
        print("#			 	    #")
        print("#	 Enter '1' for Payroll      #")
        print("#	 Enter '2' for Calculator   #")
        print("#        Enter '3' for Flip a coin  #")
        print("#        Enter '4' for Grocery list #")
        print("#        Enter '5' to exit          #")
        print("#####################################")
        op = int(input("Select a number: "))
        while op == 1:
                hours = round(40,2)
                print("One Stop Shop Payroll Calculator")
                user = str(input("\nPlease enter your name or type '0' to quit: "))
                if user == "0":
                        print("End of Report")
                        break
                else:
                        hours = (float(input("Please enter hours worked: ", )))
                        payrate =(float(input("Please enter your payrate: $", )))
                if hours <= 40:
                        print("Employee's name: ", user)
                        print("Overtime hours: 0")
                        print("Overtime Pay: $0.00")
                        regularpay = round(hours * payrate, 2)
                        print("Gross Pay: $", regularpay)
                elif hours > 40:
                        overtimehours = round(hours - 40.00,2)
                        print("Overtime hours: ", overtimehours)
                        print("Employee's name: ", user)
                        regularpay = round(hours * payrate,2)
                        overtimerate = round(payrate * 1.5, 2)
                        overtimepay = round(overtimehours * overtimerate)
                        grosspay = round(regularpay+overtimepay,2)
                        print("Regular Pay: $", regularpay)
                        print("Overtime Pay: $",overtimepay)
                        print("Gross Pay: $", grosspay)
        while op == 2: # Calculator
                num1 = float(input("Press 0 to exit\nEnter the first number: "))
                if num1 == 0:
                        break
                num2 = float(input("Enter the second number: "))
                operator = input("What calculation would you like to perform?\nEnter '+' to add\nEnter '/' to divide\nEnter '+' to add\nEnter '*' to multiply\nEnter '**' to square a number by another number\n##########################\n")
                mult = num1 * num2
                div = num1 / num2
                diff = num1 - num2
                total = num1 + num2
                power = num1 ** num2
                if operator == '*':
                        print(num1, "multiplied by", num2, "equals", mult)
                elif operator == '+':
                        print(num1, "plus", num2, "equals", total)
                elif operator == '-':
                        print(num1, "minus", num2, "equals", diff)
                elif operator == '/':
                        print(num1, "divided by", num2, "equals", div)
                elif operator == '**':
                        print(num1, "to the power of", num2, "equals", power)
                else:
                        print("Invalid input! ")
        while op == 3: # Heads or Tails
                import random
                var = int(input("How many times would you like to flip the coin? "))
                var2 = random.random() * var
                if var2 < 0.5:
                    print('Heads! ')
                elif var2 > 0.5:
                    print('Tails!')
                    break
        while op == 4: # Grocery list 
                shopList = []
                maxLength = 50
                for i in range(1, 100):
                    print('###############################')
                    print('#                             #')
                    print('#   Welcome to my Grocery     #')
                    print('#                             #')
                    print('#_____________________________#')
                    print('# Please enter in what action #')
                    print('#       you wish to do        #')
                    print('#_____________________________#')
                    print('#                             #')
                    print('#          [Options]          #')
                    print('#   Enter "1" to add an item  #')
                    print('# Enter "2" to remove an item #')
                    print('# Enter "3" to clear the list #')
                    print('# Enter "4" to exit this menu #')
                    print('# Enter "5" to list your list #')
                    print('#                             #')
                    print('###############################')
                    Enter1 = int(input('Select a number 1-5: ')) # Enter1 will allow us to ask for input from the user for a response in the menu given to them.
                    if Enter1 == 1:
                        var2 = str(input('What item would you like to add to the list? '))
                        if len(shopList) > maxLength:
                            break
                        shopList.append(var2)
                        var5 = str(input("Would you like to add another item to the list? Respond with 'y' for yes, and 'n' for no: "))
                        while var5 == 'y':
                            print("Your current shopping list is", shopList, '\n#################################')
                            var6 = str(input("Press 'E' to exit this menu\nWhat else would you like to add to your list? "))
                            if var6 == 'E':
                                break
                            else:
                                print("Your current shopping list is: ", shopList)
                                shopList.append(var6)
                        if var5 == 'n':
                            break
                            print("Your current shopping list is", shopList)
                    elif Enter1 == 2:
                        var3 = str(input('What item would you like to remove from the list? '))
                        shopList.remove(var3)
                        print("Your current shopping list is: ", shopList)
                    elif Enter1 == 3:
                        var4 = print("Clearing list...")
                        shopList[:] = []
                    elif Enter1 == 4:
                        print("Goodbye! ")
                        break
                    elif Enter1 == 5:
                        print("Your current shopping list is: ", shopList)
                    else:
                        print("Invalid input!")
        while op == 5:
                print("Goodbye!", exit, exit())
                break
