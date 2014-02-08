import requests
import json

class HackerNews:
	url = "https://community-hnify.p.mashape.com/"
	def __init__(self,key)
		self.key = key
	
	def getResult(self,which):
		extra = "get/"+which
		r=requests.get(self.url+extra, headers={"X-Mashape-Authorization":self.key});
		if r.status_code = 200:
			try:
				return r.json()["stories"]
			except Exception,e:
				return False
				
		else:
			return False

