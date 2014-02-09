from conf import *
import requests
def send_simple_message(subject, content):
    return requests.post(
            "https://api.mailgun.net/v2/sandbox7930.mailgun.org/messages",
            auth=("api", mailgunkey),
            data={"from": FROM_MAIL,
                  "to": TO_MAIL,
                  "subject": subject,
                  "text": content})

