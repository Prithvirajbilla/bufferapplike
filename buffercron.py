from email import send_simple_message
from conf import *
import glob
import os
def get_files(directory):
	os.chdir(directory)
	lsfiles = glob.glob("*.txt")
	return lsfiles

def get_now_files(files):
	pass


def buffer_post(directory):
	files = get_files(directory)
	real_files = get_now_files(files)

