import maths # import math

def main():
	print("Me is calculator")
	print("Gib what do")
	print("I can do sin, cos, and tan")
	func = input()

	if func in ["sin", "cos", "tan"]:
		print("Gib Angle")
		angle = input()
		if func == "sin":
			print(maths.sin(angle))
		elif func == "cos":
			print(maths.cos(angle))
		elif func == "tan":
			print(maths.tan(angle))
	else:
		print("Wrong func, pls retry")

if __name__ == "__main__":
	main()