from flask import Flask, request, Response
import base64
import requests


app = Flask(__name__)

webhook_url = None


def send_webhook(identifier):
    if not webhook_url:
        return

    payload = {
        'username': 'Pixel Tracker',
        'content': 'The email with the identifier **{}** has been opened.'.format(identifier)
    }
    requests.post(webhook_url, data=payload)


@app.route('/pixel.gif')
def pixel():
    identifier = request.args.get('identifier')
    send_webhook(identifier)

    pixel_data = base64.b64decode("R0lGODlhAQABAIAAAP8AAP8AACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==")
    return Response(pixel_data, mimetype='image/gif')


if __name__ == '__main__':
    app.run()