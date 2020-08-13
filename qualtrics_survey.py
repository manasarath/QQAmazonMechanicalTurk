import sys
import csv
import random

questions = []
categories = []
choices = []

pseudo = ["When day is Christmas?", "Type in the number 5", "Name a fruit", "Name a vegetable",
			"Name a country that starts with C", "Name an ocean", "Type the number 56", "Name an animal",
			"What month does Halloween fall under?", "Type the word hello", "Who is the current president?"]

def textMaker(filename):
	with open(filename,'rU') as csvfile:
	    reader = csv.reader(csvfile, delimiter=',')
	    for row in reader:
	      questions.append(row[0])
	      categories.append(row[1])
	      choices.append(row[2])

	f = open("template.txt", "w")
	f.write("[[AdvancedFormat]]\n\n")
	for i in range(0, len(questions) - 1):
		f.write("[[Block]]\n")
		if ((i + 1) % 5 == 0):
			f.write("[[Question:TextEntry:SingleLine]]\n")
			random.shuffle(pseudo);
			f.write(pseudo[0] + "\n");
		else:
			f.write("[[Question:Matrix]]\n")
			f.write(questions[i + 1] + ".\n\n")
			f.write("[[Choices]]\n")
			choices_temp = choices[i + 1].split(",")
			random.shuffle(choices_temp)
			for choice in choices_temp:
				f.write(choice.strip() + "\n")
			f.write("[[AdvancedAnswers]]\n")
			cat_temp = categories[i + 1].split(",")
			random.shuffle(cat_temp)
			for cat in cat_temp:
				f.write("[[Answer]]\n")
				f.write(cat.strip() + "\n")
		f.write("\n")
		

textMaker(sys.argv[1])