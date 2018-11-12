import os
def scan():
	# BASE_DIR1 = os.path.dirname(os.path.abspath('__file__'))
	# BASE_DIR = os.path.join(BASE_DIR1,"tmp")
	BASE_DIR = '/tmp/'
	txtfiles=[]
	for file in os.listdir(BASE_DIR):
	    if file.endswith(".TXT"):
	    	txtfiles.append(file)
	print(txtfiles)
	return txtfiles