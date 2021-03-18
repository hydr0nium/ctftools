#!/usr/bin/python2
#Written by Sol

def credits():

	print "#"*40 + "\n" +"#                                      #" + "\n"+ "# CTF-Tools Database                   #" + "\n" + "# Written by White Hood                #" + "\n" + "#                                      #" + "\n" + "#"*40    



import os.path
import sys
import os

#Formatting the databasefiles as arrays if needed
def formatDB(databasename):
	with open(os.environ["HOME"] + '/.ctftools/databases/' + databasename,'r') as f:
		data = f.readlines()
		for j in range(len(data)):
			data[j] = data[j].split("\n")[0]
		databaselist = data
		for i in range(len(databaselist)):
			databaselist[i] = databaselist[i].split(":")		
		
			
	return databaselist


#Prints out the name part of a database file
def printDB(data):
	for i in range(len(data)):
		print(str(i+1) + ". " + data[i][0])


#Prints out the description a tool has
def printTools(tool,toolbox):
	with open(os.environ["HOME"] + '/.ctftools/tools/' + toolbox + '/' + tool, 'r') as f:
		data = f.read()
		print "--------------------------------\n" + data

#Prints the help menu
def printhelp():
	print "Usage:\nctftools          |  Look through tool database via toolbox menu\nctftools --add    | adds a new entry into the database\nctftools --remove | removes entry from database\nctftools --help   | Opens the help menu"  


#Adds a entry to the database
def ctfadd():

	try:
		DBlist = formatDB("ctftools.db")
		printDB(DBlist)
		valid = False
		while(valid==False):
			choice = raw_input("Please choose a toolbox you want to add an entry to: ")
			try:
				choice = int(choice)
			except:
				print "Not a valid input"	
			if (choice<=len(DBlist)):
				valid = True
			
		DBtools = formatDB(DBlist[choice-1][1])
		displayname = raw_input("Please enter the display name of the tool: ")
		filename = raw_input("Please enter filename of the tool (ending with .ctft and no spaces | example.ctf): ")
		tool = [displayname,filename]
		DBtools.append(tool)
		print "Please add a explaination file with the name " + filename + " into " + ".ctftools/tools/" + DBlist[choice-1][0]
		writeToDB(DBlist[choice-1][1],displayname,filename) 	
		print "Tool added to database."
	except:
		print "An error has occured"

#Appends and formats the data that someone wants to add to the right file 
def writeToDB(databasename,displayname,filename):
	
	with open(os.environ["HOME"] + '/.ctftools/databases/' + databasename,'a') as f:
		f.write(displayname+":"+filename + "\n")

#Removes entry from database 
def ctfremove():
	try:
		DBlist = formatDB("ctftools.db")
		printDB(DBlist)
		valid = False
		while(valid==False):
			choice = raw_input("Please enter the toolbox you want to remove a tool from: ")
			try:
				choice = int(choice)
			except:
				print "Not a valid input"	
			if (choice<=len(DBlist)):
				valid = True

		with open(os.environ["HOME"] + '/.ctftools/databases/' + DBlist[choice-1][1], 'r') as f:
			lines = f.readlines()
		
		DBtools = formatDB(DBlist[choice-1][1])
		printDB(DBtools)
		valid = False
		while(valid==False):
			toolname = raw_input("Please enter the name of the tool you want to remove (Case-sensitive!): ")
			if(toolname!=""):
				for line in lines:
					if line.split(":")[0]==toolname:
						path = line.split(":")[1]	
						valid = True
		
		with open(os.environ["HOME"] + '/.ctftools/databases/' + DBlist[choice-1][1], 'w') as f:
			for line in lines:
  				if line.split(":")[0]!=toolname:
    					f.write(line)

		print "Removed " + toolname + " from the " + DBlist[choice-1][0] + " toolbox!"
		print "Please remove the explaination file with the name " + path + " from " + ".ctftools/tools/" + DBlist[choice-1][0]
	except:
		print "An error has occured" 	
	
	





#-----------------------------MAIN---------------------------------------

#Checks for arguments 
if(len(sys.argv)>=2):
	if(sys.argv[1]=="--help"):
		printhelp()
	elif(sys.argv[1]=="--add"):
		credits()
		ctfadd()
	elif(sys.argv[1]=="--remove"):
		credits()
		ctfremove()
	else:
		printhelp()

#Checks if no argument is given
elif(len(sys.argv)==1):		
	if (os.path.isfile(os.environ["HOME"] + "/.ctftools/databases/ctftools.db")):
		try:	
			credits()
			DBlist = formatDB("ctftools.db")
			printDB(DBlist)
			valid = False
			while(valid==False):
				choice = raw_input("Please enter a toolboxnumber: ")
				try:
					choice = int(choice)
				except:
					print "Not a valid input"	
				if (choice<=len(DBlist)):
					valid = True
				
			DBtools = formatDB(DBlist[choice-1][1])
			printDB(DBtools)

			valid2 = False
			while(valid2==False):
				choice2 = raw_input("Please enter a toolnumber: ")
				try:
					choice2 = int(choice2)
				except:
					print "Not a valid input"
				if (choice2<=len(DBtools)):
					valid2 = True
			

		
			printTools(DBtools[choice2-1][1],DBlist[choice-1][0])		
		except:
			print "An error has occured"
	else:
		print "CTF-Tools main database file not found. Please check\nyour ./ctftools folder for the ctftools.db file."

else:
	printhelp()
