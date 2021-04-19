#!/usr/local/bin/python

import datetime
import json
import os
import requests
import sys
import traceback

from messageCard import *

class TeamsSender():
  def __init__(self, webhook:str):
    self.webhook = webhook

  def sendMessage(self, card: MessageCard):

    data = card.render(filterEmpty=True, asString=True)
    response = requests.post(url=self.webhook, data=data)

    if response.status_code >= 400:
      traceback.print_exc()
      print(response.text)