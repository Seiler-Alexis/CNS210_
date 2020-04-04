import argparse
import os

def fibi(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibi(n-1) + fibi(n-2)

def newname(file):
	while os.path.exists(file + ".txt"):
		exists = input("this file has already been created, would you like to overwrite it? y/n ")
		if exists == "y":
			break
		elif exists == "n":
			file = input("Please enter a new file name.")
	f = open(file + ".txt", "w")
	 
def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("num", help="please input the number you seek.", type=int, default=True)
	parser.add_argument("file", help="Please input the name of the file to be called", type=str, default=True)
	
	args = parser.parse_args()
	results = fibi(args.num)
	print("The fibinocci number is" + str(results))
	file = (args.file)
	while os.path.exists(file + ".txt"):
		exists = input("this file has already been created, would you like to overwrite it? y/n ")
		if exists == "y":
			break
		elif exists == "n":
			file = input("Please enter a new file name.")
	f = open(file + ".txt", "w")
	f.write("The fibinocci number is " + str(results))
	f.close()
main()