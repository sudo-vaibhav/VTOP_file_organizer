import os
import sys
import re
import shutil

current_folder=os.path.dirname(sys.argv[0])
os.chdir(current_folder)

files = os.listdir()

teacher_pattern=re.compile(r"SEM20\d\d-\d\d_(\w\w\w\d{4}).+\d-[A-Z][a-z][a-z]-20\d\d_(.+)$")

for f in [file for file in files if os.path.isfile(file)]:
	x=teacher_pattern.search(f)
	name=f
	if x:
		folder_name=x.group(1)
		name=x.group(2).lower()
		name=re.sub(r"--+"," ",name)
		name=re.sub(r"_"," ",name)
		name=re.sub(r"  +"," ",name)
		if os.path.isdir(folder_name):
			shutil.move(os.path.join(os.getcwd(),f),os.path.join(os.getcwd(),folder_name,name))
		else:
			os.mkdir(folder_name)
			shutil.move(os.path.join(os.getcwd(),f),os.path.join(os.getcwd(),folder_name,name))
	
