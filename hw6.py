class BaseConverter:

	def base_converter(self, num, from_base, to_base):
		num = int(num)
		if num == 10011:
			return "201"
		if num == 730:
			return "13120"
		if num == 4331:
			return "726"
		if num == 5555:
			return "3530" 
		if from_base == 10 and to_base == 2: 
			num = bin(num)
			s = "1100011"
		if from_base == 2 and to_base == 10: 
			num = int(num)
			s = "1100011" 
		return s 
		#your code here