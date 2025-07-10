
user_info = input("enter ID")
print(user_info)

score = int(input("Enter your score:"))
if 70 <= score <= 100:
	print('A')
elif 60 <= score <= 69:
	print('B')
elif 50 <= score <= 59:
	print('C')
elif 45 <= score <= 49:
	print('D')
elif 40 <= score <= 44:
	print('E')
elif 0<= score <= 39:
	print('F')

#Create user message
print("Results assigned.")
