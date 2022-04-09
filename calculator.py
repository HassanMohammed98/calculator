
def main():
	#write your code here
	# pass
	i = 0
	while(i < 3):
		try:
			if(i == 0):
				num1 = int(input("Enter the first number: "))
			elif(i == 1):
				num2 = int(input("Enter the second number: "))
		except:
			print("number is invalid.")
		else:
			if(i < 2):
				i+=1
			else:
				operation = input("Choose the operation (+, -, /, *): ")
				if('+' in operation or '-' in operation or '/' in operation or '*' in operation):
					if(len(operation) == 1):
						break
					else:
						print("Enter a single Operation only.")
				else:
					print("operation is invalid.")

		
	print("The answer is {}".format(operator(num1, operation, num2)))
	# num2 = input("Enter the second number: ")
	# operation = input("Choose the operation (+, -, /, *): ")

	# action = input("Enter a verb: ")

	
def operator(num1, operation, num2):
	if (operation == '+'):
		return num1 + num2
	elif(operation == '-'):
		return num1 - num2
	elif(operation == '/'):
		return num1 / num2
	elif(operation == '*'):
		return num1 * num2


if __name__ == '__main__':
	main()
