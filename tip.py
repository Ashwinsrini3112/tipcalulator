print("Welcome to the tip calculator!")
bill = int(input("What is the dollar bill? $"))
tip = int(input("How much tip would you like to give ? 10 ,12 , 15? "))
people = int(input("how much people have come together ?"))

billwithtip = tip / 100 * bill + bill
tipaspercent = tip /100
totaltipamount = bill * tipaspercent
totalbill = bill + totaltipamount
billperperson = totalbill / people
finalamount = "{:.2f}".format(billperperson)
print(f"Each person should pay: ${finalamount}")