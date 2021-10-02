#!/usr/bin/python
'''
Files Organiser
Author: Shanmukha Vishnu
gitub: @iam-shanmukha
twitter: @iam_shanmukha
'''
import os
import shutil

doc_extensions=[".txt",".docx",".doc",".xls",".xls",".csv"]
compress_ext =[".zip",".rar",".zst",".gz",".xz"]
vids_ext=[".mp4",".avi",".mkv"]
pic_ext=[".png",".jpg",".jpeg"]
softwares_ext = [".AppImage",".deb"]

#list present working directory files and folders
#ls = files+folders
ls=os.listdir()
def create_dirs():
	directories = ["Pdfs", "Pictures", "Videos", "compressed_Files", "Documents", "Py_files", "softwares"]
	for directory in directories:	
		if directory in ls:
			print(f"{directory} directory exists...skipping ")
		else:
			print(f"Creating {directory} Directory")
			os.mkdir(directory)
create_dirs()

for file in ls:
	try:

		if file.endswith(".pdf"):
			shutil.move(file, "Pdfs")
			print(f"{file} files moved successfully")
		elif file.endswith(tuple(pic_ext)):
			shutil.move(file, "Pictures")
			print(f"{file} files moved successfully")
		elif file.endswith(tuple(vids_ext)):
			shutil.move(file, "Videos")
			print(f"{file} files moved successfully")
		elif file.endswith(tuple(compress_ext)):
			shutil.move(file, "compressed_Files")
			print(f"{file} files moved successfully")
		elif file.endswith(tuple(doc_extensions)):
			shutil.move(file, "compressed_Files")
			print(f"{file} files moved successfully")
		elif file.endswith(tuple(softwares_ext)):
			shutil.move(file, "softwares")
			print(f"{file} files moved successfully")
		elif file.endswith(".py"):
			if file == "organiser.py":
				continue
			shutil.move(file, "Py_files")
			print(f"{file} files moved successfully")
	except shutil.Error as E:
		print("ERROR",E)
		continue