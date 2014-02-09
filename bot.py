from conf import *
from hackernews import *
from email import *

def auto_post():
	hn = HackerNews(key=XMashapeAuthorization)

	js = hn.getResult("best")
	if js:
		for i in range(5):
			try:
				message = js[i]["title"]+"\n"
				message+= "Comments link: "+js[i]["comments_link"]+"\n"
				message+= "Published "+ js[i]["published_time"]+"\n"
				message+= "Category:Best Links"
				subject = js[i]["link"]
				send_simple_message(subject, message)
			except Exception,e:
				pass

	js = hn.getResult("top")
	if js:
		for i in range(5):
			try:
				message = js[i]["title"]+"\n"
				message+= "Comments link: "+js[i]["comments_link"]+"\n"
				message+= "Published "+ js[i]["published_time"]+"\n"
				message+= "Category:Top links"
				subject = js[i]["link"]
				send_simple_message(subject, message)
			except Exception,e:
				pass

	js = hn.getResult("newest")
	if js:
		for i in range(5):
			try:
				message = js[i]["title"]+"\n"
				message+= "Comments link: "+js[i]["comments_link"]+"\n"
				message+= "Published "+ js[i]["published_time"]+"\n"
				message+= "Category:Newest links"
				subject = js[i]["link"]
				send_simple_message(subject, message)
			except Exception,e:
				pass

auto_post()