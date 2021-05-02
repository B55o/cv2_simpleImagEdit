import os
from os import path
from src.functions import funcErode, funcBinary, funcDilate, funcBoxFilter, funcMedian

how_many_pic = input("how many pictures you want to analyse: ")
all_pics = []
for i in range(0, int(how_many_pic)):
	pic = input("directory of file you want to edit: ")
	while not os.path.isfile(pic):
		pic = input("there is no such directory or file, try another: ")
		print(pic)
	else:
		if pic.find(".jpg") > 0:
			all_pics.append(pic)
		elif pic.find(".png") > 0:
			all_pics.append(pic)
		elif pic.find(".tif") > 0:
			all_pics.append(pic)
		elif pic.find(".jfif") > 0:
			all_pics.append(pic)
		else:
			print("your file format is not supported...")

print(all_pics)

print("first operation you want to execute: ")
more = True
while more:
	operation_name = int(input("\n1 - Erode\n2 - Binary\n3 - Dilate\n4 - BoxFilter\n5 - Median\n"))
	while operation_name < 1 or operation_name > 5:
		print(f"{operation_name} this number is out of range.. ")
		operation_name = int(input("\n1 - Erode\n2 - Binary\n3 - Dilate\n4 - BoxFilter\n5 - Median\n"))
	if operation_name == 1:
		for pic in all_pics:
			funcErode(pic)
	elif operation_name == 2:
		for pic in all_pics:
			funcBinary(pic)
	elif operation_name == 3:
		for pic in all_pics:
			funcDilate(pic)
	elif operation_name == 4:
		for pic in all_pics:
			funcBoxFilter(pic)
	elif operation_name == 5:
		for pic in all_pics:
			funcMedian(pic)

	count = input("You want to try more operations? y/n\n")
	if count != "y":
		break
