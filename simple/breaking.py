import time

con = True
i = 0
shouts = ["what", "who"]
while(con):
	print("hi my name is!")
	"""
		if i == 2:
			break
	"""
	print(shouts[i % 2])
	i += 1
 
	time.sleep(1)

for _ in range(1, 3):
	print('chicka')
 
print("Slim Shady")

# ---------- Expected Output ----------#

# hi my name is!
# what
# hi my name is!
# who
# hi my name is!
# chicka
# chicka
# Slim Shady
