import unittest
from Function_Examples import gcd_recursive, gcd_iterative

'''
The unittest package defines the TestCase class, which is primarily designed for writing unit tests.
To start writing your test cases, import the class and subclass it.
Then add individual methods whose names begin with "test_".
These methods will test a given unit of code using different inputs and check for the expected results.
'''

class FunctionTests(unittest.TestCase):
	"""
	A test case class for testing the functions in Function_Examples module.
	"""

	def test_gcd_recursive(self):
		"""
		Test the gcd function with known inputs.
		"""
		self.assertEqual(gcd_recursive(12, 8), 4, msg = "The GCF of 12 and 8 is 4.")
		self.assertEqual(gcd_recursive(42, 14), 14, msg = "The GCF of 42 and 14 is 14.")

	def test_gcd_recursive_2(self):
		"""
		Test the gcd function with different inputs.
		"""
		self.assertEqual(gcd_recursive(25, 15), 5, msg = "The GCF of 25 and 15 is 5.")

	def test_gcd_iterative_primes(self):
		"""
		Test the gcd function with prime numbers.
		"""
		self.assertEqual(gcd_iterative(7, 5), 1, msg = "The GCF of 7 and 5 is 1.")
		self.assertEqual(gcd_iterative(13, 11), 1, msg = "The GCF of 13 and 11 is 1.")


if __name__ == "__main__":
	'''
	Among other arguments, the main() function takes a verbosity level.
	With this argument, you can tweak the output's verbosity, which has three possible values:

	0 -> quiet
	1 -> normal
	2 -> verbose detail
	'''
	unittest.main(verbosity=2)