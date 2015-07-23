import random

def rgPass():
	rgSeed = random.seed()
	rgSeed = random.seed(rSeed)
	rgValue = str(round(random.random()))
	rgPass = rgValue
	i = 0
	while True:
		rgInt = random.randrange(9)
		rgPass = str(rgPass) + str(rgInt)
		i += 1
		if i > 9:
			return rgPass

