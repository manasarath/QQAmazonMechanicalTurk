import sys
import csv

def textMaker(filename):
	questions = []
	authrater1num = []
	authrater2num = []
	authrater3num = []
	authvoted = []
	clear1num = []
	clear2num = []
	clear3num = []
	clearvoted = []
	comprater1num = []
	comprater2num = []
	comprater3num = []
	compvoted = []
	corater1num = []
	corater2num = []
	corater3num = []
	covoted = []
	obrater1num = []
	obrater2num = []
	obrater3num = []
	obvoted = []
	rdrater1num = []
	rdrater2num = []
	rdrater3num = []
	rdvoted = []
	rlrater1num = []
	rlrater2num = []
	rlrater3num = []
	rlvoted = []
	trater1num = []
	trater2num = []
	trater3num = []
	tvoted = []
	categories = ["Authentic", "Clear", "Complete", "Correct", "Objective", "Readable", "Reliable", "Trustworthy"]
	search = ["authentic.", "clear.", "complete.", "correct.", "objective.", "readable.", "reliable.", "trustworthy."]

	with open(filename,'rU') as csvfile:
	    reader = csv.reader(csvfile, delimiter=',')
	    for row in reader:
	    	if row[0].split(" ")[-1] == "authentic.":
	    		questions.append(" ".join(row[0].split(" ")[:-7]))
	    		authrater1num.append(row[1])
	    		authrater2num.append(row[2])
	    		authrater3num.append(row[3])
	    		authvoted.append(row[4])
	    	if row[0].split(" ")[-1] == "clear.":
	    		clear1num.append(row[1])
	    		clear2num.append(row[2])
	    		clear3num.append(row[3])
	    		clearvoted.append(row[4])
	    	if row[0].split(" ")[-1] == "complete.":
	    		comprater1num.append(row[1])
	    		comprater2num.append(row[2])
	    		comprater3num.append(row[3])
	    		compvoted.append(row[4])
	    	if row[0].split(" ")[-1] == "correct.":
	    		corater1num.append(row[1])
	    		corater2num.append(row[2])
	    		corater3num.append(row[3])
	    		covoted.append(row[4])
	    	if row[0].split(" ")[-1] == "objective.":
	    		obrater1num.append(row[1])
	    		obrater2num.append(row[2])
	    		obrater3num.append(row[3])
	    		obvoted.append(row[4])
	    	if row[0].split(" ")[-1] == "objective.":
	    		rdrater1num.append(row[1])
	    		rdrater2num.append(row[2])
	    		rdrater3num.append(row[3])
	    		rdvoted.append(row[4])
	    	if row[0].split(" ")[-1] == "reliable.":
	    		rlrater1num.append(row[1])
	    		rlrater2num.append(row[2])
	    		rlrater3num.append(row[3])
	    		rlvoted.append(row[4])
	    	if row[0].split(" ")[-1] == "trustworthy.":
	    		trater1num.append(row[1])
	    		trater2num.append(row[2])
	    		trater3num.append(row[3])
	    		tvoted.append(row[4])
	    data = [['Question', 'Category', "Rater 1", "Rater 2", "Rater 3", "Voted Response", 
	    		'Category', "Rater 1", "Rater 2", "Rater 3", "Voted Response",
	    		'Category', "Rater 1", "Rater 2", "Rater 3", "Voted Response",
	    		'Category', 'rater1', 'rater2', 'rater3', 'Voted Response',
	    		'Category', 'rater1', 'rater2', 'rater3', 'Voted Response',
	    		'Category', 'rater1', 'rater2', 'rater3', 'Voted Response',
	    		'Category', 'rater1', 'rater2', 'rater3', 'Voted Response',
	    		'Category', 'rater1', 'rater2', 'rater3', 'Voted Response']]
	    datafile = open("TESTING.csv", 'w')
	    with datafile:
	    	writer = csv.writer(datafile)
	    	writer.writerows(data)
	    	for i in range(len(questions)):
	    		ratedata = [[questions[i], categories[0], authrater1num[i], authrater2num[i], authrater3num[i], authvoted[i],
	    					categories[1], clear1num[i], clear2num[i], clear3num[i], clearvoted[i],
	    					categories[2], comprater1num[i], comprater2num[i], comprater3num[i], compvoted[i],
	    					categories[3], corater1num[i], corater2num[i], corater3num[i], covoted[i],
	    					categories[4], obrater1num[i], obrater2num[i], obrater3num[i], obvoted[i],
	    					categories[5], rdrater1num[i], rdrater2num[i], rdrater3num[i], rdvoted[i],
	    					categories[6], rlrater1num[i], rlrater2num[i], rlrater3num[i], rlvoted[i],
	    					categories[7], trater1num[i], trater2num[i], trater3num[i], tvoted[i]]]
	    		writer.writerows(ratedata)

textMaker(sys.argv[1])