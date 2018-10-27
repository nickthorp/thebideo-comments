from flask import Flask, request, Response, json
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)


class Comment(Resource):
    @staticmethod
    def verify_recaptcha(recaptcha_response):
        check_dict = {"secret": "6LfT63QUAAAAAGmXVd4HpJGquD9ODc0owB6GINei", "response": recaptcha_response}
        r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=check_dict)
        return r.text

    def post(self):
        message = request.form
        is_okay = json.loads(self.verify_recaptcha(message["g-recaptcha-response"]))
        if is_okay["success"]:
            r = self.mailgun(message["from"], "nickthorp20@gmail.com", message["subject"], message["text"])
            if r == "failed":
                return Response("<a href=\"http://127.0.0.1\">Home</a><br><h1>There was a problem submitting "
                                "your comment. Please try again later.</h1>",
                                mimetype="text/html")
            return Response("<a href=\"http://127.0.0.1\">Home</a><br><h1>Your comment has been submitted!</h1>",
                            mimetype="text/html")
        else:
            return Response("<a href=\"http://127.0.0.1\">Home</a><br><h1>Get outta here robot!!!</h1>",
                            mimetype="text/html")

    @staticmethod
    def mailgun(from_who, to_email, subject, text):
        our_email = "comments@thebideo.com"
        user = 'api'
        password = '59232a7ee7c8297f71725eb03553365b-bd350f28-4af382c7'
        url = "https://api.mailgun.net/v3/mg.thebideo.com/messages"
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
