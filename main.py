print("Welcome to the tip calculator!")

# Ask about the total bill and convert it to float
bill = input("What was the total bill? $")
bill_as_float = float(bill)

# Ask about the percentage of the tip and convert it to int
bill_tip = input("How much tip would you like to give? e.g. 10, 12, or 15? %")
bill_tip_as_int = int(bill_tip)

# Ask about the number of people and convert it to int
number_of_people = input("How many people to split the bill? ")
number_of_people_as_int = int(number_of_people)

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
