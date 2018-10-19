from flask import Flask, request, Response, jsonify, json
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)


class Comment(Resource):
    @staticmethod
    def verify_recaptcha(recaptcha_response):
        check_dict = {"secret": "6LfT63QUAAAAAGmXVd4HpJGquD9ODc0owB6GINei", "response": recaptcha_response}
        r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=check_dict)
        print(r.status_code)
        return r.text

    def post(self):
        message = request.form
        for item in message:
            print(item + " " + message[item])
        is_okay = json.loads(self.verify_recaptcha(message["g-recaptcha-response"]))
        if is_okay["success"]:
            return Response("<a href=\"http://127.0.0.1\">Home</a><br><h1>You got this!</h1>",
                            mimetype="text/html")
        else:
            return Response("<a href=\"http://127.0.0.1\">Home</a><br><h1>Get outta here robot!!!</h1>",
                            mimetype="text/html")


api.add_resource(Comment, '/comment')  # Route_1

if __name__ == '__main__':
    app.run(port='5002')
