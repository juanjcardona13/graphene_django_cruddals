import base64
import json

from django.test import Client as BaseClient
from django.urls import reverse


def decode_bytes(value):
    if isinstance(value, list):
        return [decode_bytes(v) for v in value]
    if isinstance(value, dict):
        return {k: decode_bytes(v) for k, v in value.items()}
    if isinstance(value, bytes):
        return base64.b64encode(value).decode("utf-8")
    return value


class Client(BaseClient):
    url = reverse("graphql")

    def query(self, query, variables=None):
        data = {"query": query}
        if variables is not None:
            for key, value in variables.items():
                variables[key] = decode_bytes(value)
            data["variables"] = json.dumps(variables)
        response = self.post(path=self.url, data=data)
        return response
