import json

import paho.mqtt.client as paho

from app.notifiers.utils import NotifierUtils


class MqttNotifier(NotifierUtils):

    def __init__(self, **kwargs):
        self._host = kwargs['host']
        self._port = kwargs['port']

        self.client = paho.Client()
        if kwargs.get(
                'username') is not None and kwargs.get('password') is not None:
            self.client.username_pw_set(
                kwargs.get('username'), kwargs.get('password'))

    def connect(self):
        self.client.connect(self._host, self._port)

    def notify(self, exchange, key, time_span, message):
        topic = '/%s/%s/%s/' % exchange, key, time_span
        self.client.publish(topic, json.dumps(message), retain=True)

    def disconnect(self):
        self.client.disconnect()
