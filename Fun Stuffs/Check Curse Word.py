import time
import urllib

def read_txt():
	
	
	print("NOTE:Please enclose your query with double quotes \"your_query_here\"")
	file_address = str(input("Drag the txt file  here:"))
																
	if file_address.endswith(".txt"):
		print("...processing")
		time.sleep(3) # time sleep for 3 secs
		process_file(file_address)
	else:
		print("This program only accepts .txt files")
		read_txt()

def process_file(file_address):
	#Open and read the contentst of the file then close it
	open_file = open(file_address)
	get_file_contents = open_file.read()
	print(get_file_contents)# prints the value of get_file_contents
	open_file.close()
	
	#Open a connection using urlopen
	get_connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+get_file_contents)
	#Read the output from the connection and store it to get_output variable
	get_output = get_connection.read()
	
	#Checks if there's a bad word in the result
	if "false"  in get_output:
		print("--All Clean--")
	else:
		print("--Bad word Detected!--")
	get_connection.close()
	
read_txt()