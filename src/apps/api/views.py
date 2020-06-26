import json

import requests
from django.http import HttpResponse
from django.views import View
from dynaconf import settings
from rest_framework.authtoken.views import ObtainAuthToken as _DrfObtainAuthToken


class ObtainAuthToken(_DrfObtainAuthToken):
    swagger_schema = None


class TelegramView(View):
    def post(self, *args, **kwargs):
        try:
            payload = json.loads(self.request.body)
            message = payload["message"]
            text = message["text"]
            chat_id = message["chat"]["id"]

            r = requests.post(
                f"https://api.telegram.org/bot{settings.TG}/sendMessage",
                json={"chat_id": chat_id, "text": text.upper()},
            )
            print(f"XXX sendMessage resp: {r}")
        except Exception as err:
            print(err)
        return HttpResponse()
