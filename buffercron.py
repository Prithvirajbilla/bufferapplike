from email import send_simple_message
from conf import *
import glob
import os
import shutil
import datetime
def get_files(directory):
	os.chdir(directory)
	lsfiles = glob.glob("*.txt")
	return lsfiles

def get_now_files(files):
	result = []
	for i in files:
		filename = i.split(".")[0]	#assuming only one . that too after txt
		filename = filename.split("|")[0].strip()
		current_datetime = datetime.datetime.now()
		filedatetime = datetime.datetime.strptime( filename, "%Y-%m-%d %H:%M")
		delta = filedatetime - current_datetime
		minutes = divmod(delta.days * 86400 + delta.seconds, 60)[0]
		if minutes < 30:
			result += [i]
	return result



def buffer_post(directory):
	files = get_files(directory)
	archived_directory = directory+"/archives"
	real_files = get_now_files(files)
	for i in real_files:
		filename = directory+"/"+i
		f = open(filename,"r")
		line = f.readlines()
		subject = line[0]
		message = ""
		try:
			for k in line[1:]:
				message =message+k
		except Exception,e:
			print e
		send_simple_message(subject,message)
		# print subject,message
		shutil.move(filename,archived_directory+"/"+i)



# buffer_post("/home/madhukar/bufferapplike")