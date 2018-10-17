import json
import sys
import os

class file():
	"""
	Created this class to store the ipynb and py file names
	"""
	def __init__(self,ipynb,py):
		self.ipynb = ipynb
		self.py = py

def retrieve_arguments():
	"""
	Functionality: Takes files user inputs on command line
	and creates file instances with the ipynb and py file extensions
	Ouput: list of file class instances
	"""

	#Takes all files that user inputs on command line
	#sys.argv[0] is the file name so we want to exclude that
	arg_files = sys.argv[1:]

	files = []
	for ipynb in arg_files:
		#Raise error if file is not ipynb extenstion
		if 'ipynb' not in ipynb:
			raise Exception(f'{ipynb} is not an IPython Notebook (.ipynb)')
		#Replaces extension in new py variable
		py = ipynb.replace('ipynb','py')
		new_file = file(ipynb,py)
		files.append(new_file)

	return files

def main():
	"""
	Input: ipynb files from the command line
	Functionality: Converts ipynb files to py files
	Output: n py files in current directory (where n = # of ipynb from command line)
	"""
	#files will contain file instances (which contain ipynb and py file names)
	#for every ipynb file inputed from the command line
	files = retrieve_arguments()

	for file in files:
		#User has to decide if they want to overwrite the file
		if os.path.isfile(file.py):
			#Will not allow you to perform this action
			#on a file with the same name as this python file
			#sys.argv[0] is the current file name
			if file.py == sys.argv[0]:
				print(f'You cannot rewrite {sys.argv[0]}!!!')
				print('Ryan already did this once he had to rewrite the whole thing')
				continue
			user_input = input(f'Do you want to OVERWRITE {file.py}\nProceed ([y]/n)? ')
			if user_input == 'y':
				continue
		#Opens the ipynb file
		#Creates (or overwrites if the user has given consent) the py file
		with open(file.py,'w'),open(file.ipynb,'r') as py,ipynb:
			#creates a json object from ipynb file
			ipynb_json = json.load(ipynb)

			for cell in ipynb_json['cells']:
				#Only writes contents from code cells
				if cell['cell_type'] != 'code':
					continue
				for line in cell['source']:
					#Replaces new line chars because not every line has one
					#By removing new line chars and appending at the end 
					#we create consistent styling in the new file
					line = line.replace('\n','')
					py.write(line)
					py.write('\n')
				#Adds a new line char at the end of each cell to replicate
				#that natural division from cells
				py.write('\n')


if __name__ == '__main__':
	main()
