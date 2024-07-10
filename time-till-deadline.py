from datetime import datetime

user_input = input("Please input your Goal and deadline(like: Learn Python:01.05-2025) and it will show how many days are left!: ")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

print(f"Your goal is: {goal} and deadline is: {deadline}")

deadline_date = datetime.strptime(deadline, '%d.%m.%Y') 
today_date = datetime.today()

final_result = deadline_date - today_date

print(f"You have {final_result.days} days left to fulfill your goal, Hurry up!!")

print("Thanks for using our app! Hope you have enjoied it :")