import openai
import os
import sys
from flask import Flask, request, app, render_template
from twilio.twiml.messaging_response import MessagingResponse
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
            in_que = in_que.lstrip(res)
            msg = MessagingResponse()

            url = "https://all-media-downloader-v2.p.rapidapi.com/dl"

            payload = { "url": in_que }
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": os.getenv('XRapidAPIKey'),
                "X-RapidAPI-Host": "all-media-downloader-v2.p.rapidapi.com"
            }

            response = req.post(url, json=payload, headers=headers)

            video = response.json()
            
            try:
                msg.message("Download here")
                if response.status_code == 200:
                    # print('youtube',response.status_code)
                    preference = 'video'
                    if preference == 'video':
                        single_or_playlist = 'single'
                        if single_or_playlist == 'single':
                            qua=[0]*len(video['formats'])
                            extension=[0]*len(video['formats'])
                            # print("Video Details:------->>")
                            title = video['title']
                            duration = video['duration_string']
                            
                            
                            for i in range(len(video['formats'])):
                                qua[i] = video['formats'][i]['format_note']
                                extension[i] = video['formats'][i]['ext']
                            #     print(qua[i])
                            #     print(extension[i])
                            for j in range(len(video['formats'])):
                                # print(qua[j], quality)    
                                if qua[j] == res and extension[j] == 'mp4':
                                    # print("if")
                                    video_dl_link = video['formats'][j]['url'].encode()

                                    msg.message(title+'-->'+' '+duration+' '+video_dl_link.decode('utf-8'))
                                else:
                                    # print("else")
                                    msg.message("quality not exit")
                        else: #if choice is playlist
                            print("playlist")
                    else:#if choice is audio
                        print("audio")
                    return render_template('index.html',ti = title, ex = extension, q = quality, d = duration)

                else:
                    print(f"failed with error code {response.status_code}")

            except Exception as e:
                msg.message("its not working")
        else:
            msg = MessagingResponse()
            msg.message("Please add a space before resolution")
    else:
        msg = MessagingResponse()
        msg.message("Please add 'yt.' before link")

    return render_template('index.html')
            

#------------------------------------------------Youtube----------------------------------------------
    # return render_template("index.html",in_msg = f"message from whatsapp: {in_que}")
    # ans = user_Q(in_que)

    # msg = MessagingResponse()# creates an object of MessagingResponse
    # # msg.message(f"You said: {in_que}")# creates an instance of that object
    # msg.message(ans)
    # wa_msg.body(ans)#with that object we keeping the ans on the body
    
    return str(msg) #because of the framework can only detect/read the json object


if __name__ == '__main__':
    app.run(debug=True)

