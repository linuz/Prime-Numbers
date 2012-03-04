#!/usr/bin/python
#############################################################
# Prime finder for Python                                   #
# by: Dennis Linuz <dennismald@gmail.com>                   #
# Demonstration of a prime numbers                          #
#############################################################
MIN_NUMBER = 2
MAX_NUMBER = 1000
primeArray = []
for i in range(MIN_NUMBER,MAX_NUMBER):
	result = False
	temp = int(i**0.5)
	while (temp > 1):
		if (i%temp == 0): result = True	
		temp -= 1
	if not result: primeArray.append(i)
print primeArray
print ""
print "There are " + str(len(primeArray)) + " prime numbers between " + str(MIN_NUMBER) + " and " + str(MAX_NUMBER) + "."
