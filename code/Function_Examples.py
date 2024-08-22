'''
The following functions use type hints and docstrings to provide information about the function.
The functions are deterministic and non-deterministic.
Deterministic functions can be tested and further documented using doctests.
'''

def gcd_iterative(a: int, b: int) -> int:
	"""
	Returns the greatest common factor (GCF) of two numbers
	using the iterative version of Euclid's algorithm.

	Parameters:
	a (int): The first number.
	b (int): The second number.

	Returns:
	int: The GCF of the two numbers.

	Examples:
	This function is deterministic, so we can provide examples as doctests.

	>>> gcd_iterative(12, 8)
	4
	>>> gcd_iterative(25, 15)
	5
	>>> gcd_iterative(7, 5)
	1
	"""

	while b != 0:					# Loop until b is 0
		a, b = b, a % b				# assign b to a and the remainder of a divided by b to b
		''' 
		# BUGGY CODE - Uncomment to see the error in tests
		a = b
		b = a % b
		'''
	return a						# Return the GCF

def gcd_recursive(a: int, b: int) -> int:
	"""
	Returns the greatest common factor (GCF) of two numbers 
	using the recursive version of Euclid's algorithm.

	Parameters:
	a (int): The first number.
	b (int): The second number.

	Returns:
	int: The GCF of the two numbers.

	Examples:
	This function is deterministic, so we can provide examples as doctests.

	>>> gcd_recursive(12, 8)
	4
	>>> gcd_recursive(25, 15)
	5
	>>> gcd_recursive(7, 5)
	1
	"""

	if b == 0:							# Base case
		return a						# Return the GCF
	else:								# Recursive case
		return gcd_recursive(b, a % b)	# Reduce problem size and recurse
	
def spongebobify(text: str) -> str:
	"""
	Returns the input text with 50% alternating capitalization.

	Parameters:
	text (str): The text to spongebobify.

	Returns:
	text (str): The spongebobified text.

	Examples:
	This function is not deterministic, so examples will not be provided
	as doctests do not provide the ability to test non-deterministic functions.
	You need to employ other testing methods to verify the correctness.
	We will do this externally in the test file.

	"""
	from random import randint										# Import randint function
	fifty_percent	= len(text) // 2								# Calculate 50% of the text length
	used_indices	= set()											# Create an empty set to store used indices

	while len(used_indices) < fifty_percent:						# Loop until 50% of the text is capitalized
		index = randint(0, len(text) - 1)							# Generate a random index within range of 0 to length of text
		char = text[index]											# Get the character at the index
		if char.isalpha() and index not in used_indices:			# Check if the character is a letter and the index is not used
			used_indices.add(index)									# Add the index to the used indices
			text = text[:index] + char.upper() + text[index + 1:]	# Capitalize the character at the index
			
	return text														# Return the spongebobified text


if __name__ == "__main__":

	dt = gcd_recursive.__doc__			# Get the docstring of the function
	print(dt) 							# Print the docstring

	'''
	Example usage of the spongebobify function. This technique is commonly
	used to test functions but relies on user verification of output correctness. 
	Many times our eyes can be deceiving, so it is important to have a test file to verify
	'''
	# phrases to spongebobify
	phrases = [	
		"With imagination, you can be anything you want.",
		"If you believe in yourself and with a tiny pinch of magic, all your dreams can come true.", 
		"Too bad SpongeBob's not here to enjoy Spongebob not being here.",
		"Always follow your heart unless your heart is bad with directions."
	]

	for phrase in phrases:				# Iterate over the phrases
		print(spongebobify(phrase))		# Spongebobify the phrase and print the result