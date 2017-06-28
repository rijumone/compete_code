class Difference:

	maximumDifference = 0
	__elements = []

	def __init__(self, a):
		self.__elements = a
	# Add your code here
	def computeDifference(self):
		for k in self.__elements:
			for j in self.__elements:
				if j != k :
					diff = (j-k) if (j-k) >= 0 else (j-k)*-1
					if diff > self.maximumDifference:
						self.maximumDifference = diff

# End of Difference class

_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.computeDifference()

# print d.maximumDifference        