#!/opt/thebideo-comments/bin/python3

from flask import Flask, request, Response, json
from flask_restful import Resource, Api
import requests
import yaml

# Load up our configuration file
with open("config.yml", 'r') as yaml_file:
    cfg = yaml.load(yaml_file)

app = Flask(__name__)
api = Api(app)


class Comment(Resource):
    @staticmethod
    def verify_recaptcha(recaptcha_response):
        check_dict = {"secret": cfg['recaptcha::secret'], "response": recaptcha_response}
        r = requests.post(cfg['recaptcha::url'], data=check_dict)
        return r.text

    def post(self):
        message = request.form
        is_okay = json.loads(self.verify_recaptcha(message["g-recaptcha-response"]))
        if is_okay["success"]:
            r = self.mailgun(message["from"], cfg['email::to'], message["subject"], message["text"])
            if r == "failed":
                return Response("<a href=\"" + cfg['thebideo::url'] + "\">Home</a><br><h1>There was a problem "
                                "submitting your comment. Please try again later.</h1>",
                                mimetype="text/html")
            return Response("<a href=\"" + cfg['thebideo::url'] + "\">Home</a><br><h1>Your comment has been "
                            "submitted!</h1>",
                            mimetype="text/html")
        else:
            return Response("<a href=\"" + cfg['thebideo::url'] + "\">Home</a><br><h1>Get outta here robot!!!</h1>",
                            mimetype="text/html")

    @staticmethod
    def mailgun(from_who, to_email, subject, text):
        our_email = cfg['mailgun::from']
        user = cfg['mailgun::user']
        password = cfg['mailgun::secret']
        url = cfg['mailgun::url']
        full_text = text + "\n\n" + from_who
        email = {"from": our_email,
                 "to": to_email,
                 "subject": subject,
                 "text": full_text}
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }
        s = requests.Session()
        s.auth = (user, password)
        r = s.post(url, data=email, headers=headers)
        if r.status_code != 200:
            return "failed"
        print(r.status_code)
        print(r.text)
        message = json.loads(r.text)
        print(message["message"])
        return message["message"]


api.add_resource(Comment, '/comment')  # Route_1

if __name__ == '__main__':
    app.run(port='5002')
