import random

def rgPass():
	rSeed = random.seed()
	rSeed = random.seed(rSeed)
	rValue = str(round(random.random()))
	rPass = rValue
	i = 0
	while True:
		rInt = random.randrange(9)
		rPass = str(rPass) + str(rInt)
		i += 1
		if i > 9:
			return rPass

