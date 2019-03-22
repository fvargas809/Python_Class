class CC:

	def __init__(self,card_number):
		self.card_number = str(card_number)
		self.length = len(card_number)
		self.card_type = self.determine_card_type()

	def determine_card_type(self):
		visa = "4"
		mastercard = ("51","52","53","54","55")
		amex = ("34","37")
		discover = "6011"

		if self.card_number[0] == visa and self.length == 16:
			return "Visa"
		elif self.card_number[0:2:1] in mastercard and self.length == 16:
			return "Mastercard"
		elif self.card_number[0:2:1] in amex and self.length == 15:
			return "AMEX"
		elif self.card_number[0:4:1] == discover and self.length == 16:
			return "Discover"
		else:
			return "Unknown"

		
	def validate(self):
		# Convert string into list
		numbers = list(self.card_number)

		# Change string to integers
		numbers = [ int(x) for x in numbers ]

		# Mulitply every second digit from the right by 2
		for x in range(-2,-(self.length)-1,-2):
			numbers[x] *= 2

		# Add up all numbers in list and split any 2-digit numbers
		total = 0
		for x in range(0,self.length,1):
			if numbers[x] >= 10:
				temp = str(numbers[x])
				left_digit = int(temp[0])
				right_digit = int(temp[1])
				total = total + left_digit + right_digit
			else:
				total = total + numbers[x]

		# Return True if result is divisible by 10, else: False
		if total % 10 == 0:
			return True
		else:
			return False
				

# Sample uses

new_card = CC(input("Enter a card number: "))

if new_card.validate():
	print("This card number is valid.")
	print("Card type:", new_card.card_type)
else:
	print("This card number is invalid.")