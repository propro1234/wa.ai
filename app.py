import openai
import os
import sys
from flask import Flask, request, app, render_template
from twilio.twiml.messaging_response import MessagingResponse
from vdo_to_mp3 import yt_download
import re

app = Flask(__name__)

openai.api_key = os.environ.get('OPENAI_API_KEY')
# # acc_sid = os.getenv('TWILIO_ACCOUNT_SID')
# # auth_tok = os.environ.get('TWILIO_AUTH_TOKEN')

def user_Q(ureq):
    req = openai.Completion.create(
        model = "text-davinci-003",
        prompt = ureq,
        max_tokens = 4000,
        temperature = 0,
        frequency_penalty = 0.5,
        presence_penalty = 0
    )
    return req['choices'][0]['text'].strip()
@app.route("/")
def index():
    return "hello world"
# def index():
#    return render_template("index.html")

@app.route("/chat",methods=['POST'])
def chat():
    in_que = request.form.get('Body')
    
#---------------------------------------------youtube----------------------------------------------
    if 'yt' in in_que:
        match = re.search(' ', in_que)
        if match:
            res = in_que[match.end():]
            in_que = in_que.lstrip('yt.')
            msg = MessagingResponse()
            
            try:
                msg.message("Downloading...")
                media_url=[yt_download(in_que,res)]
                msg.message(":::Download Completed:::")
            except Exception as e:
                msg.message(f"its not working because of {e}")
        else:
            msg = MessagingResponse()
            msg.message("Please add a space before resolution")
    else:
        msg = MessagingResponse()
        msg.message("Please add 'yt.' before link")

#------------------------------------------------Youtube----------------------------------------------
    # return render_template("index.html",in_msg = f"message from whatsapp: {in_que}")
    ans = user_Q(in_que)

    msg = MessagingResponse()# creates an object of MessagingResponse
    # msg.message(f"You said: {in_que}")# creates an instance of that object
    msg.message(ans)
    # wa_msg.body(ans)#with that object we keeping the ans on the body
    
    return str(msg) #because of the framework can only detect/read the json object


if __name__ == '__main__':
    app.run(debug=True)
