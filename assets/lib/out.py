#!/usr/bin/env python3
import json
import os
import sys

import logging as log
import tempfile

from sender import TeamsSender
from messageCard import *
from logHelper import *

class MSTeamsResource:
  def __init__(self, json_data: str):
    data = json.loads(json_data)

    source = data.get('source', None)
    params = data.get('params', None)

    # Setup log level
    if source.get('log_level', None) != None:
      log.level(source['log_level'])

    # Build Card
    if params != None:
      card = buildCard(params)

      if source.get('url', None) != None:
        self.postCard(source['url'], card)

  def buildCard(self, data):
    m = MessageCard(
      summary=data.get('summary', None),
      themeColor=data.get('themeColor', Color.DEFAULT),
      title=data.get('title', None),
      text=data.get('text', None)
    )

    return m

  def postCard(self, url: str, card: MessageCard):
    sender = TeamsSender(url)
    sender.postCard(card)
    return

    # # We've already redirected STDOUT to STDERR in the bash file ...
    # print(f'command_name: {command_name}')
    # print(f'json_data: {json_data}')



  # def outFunction(self, input:str, dirPath):
  #   payload = json.load(input)

  #   url = payload["source"]["url"]

  #   # teams = TeamsSender(url, self.common)
  #   # teams.sendMessage(dirPath)

  #   outResult = {
  #     "version": {
  #       "timestamp": f"{time.time()}"
  #     }
  #   }

  #   return outResult

  # def __getPayloadParam(self, payload: {}, name: str):
  #   if "params" in payload and name in payload["params"]:
  #     return payload["params"][name]
  #   else:
  #     self.common.setDebugInformation(f"Could not find param {name}")
  #     return None

  # def __getPropertyValue(self, item: {}, key: str):
  #   if key in item:
  #     return item[key]
  #   else:
  #     return None

  # def __addMetadataItem(self, name: str, value):
  #   if value != None:
  #     self.common.buildMetadata[name] = value
  #   else:
  #     self.common.setDebugInformation(f"Did not add {name} because it's value was None")

  # def __getFileContentsAsJson(self, filePath):
  #   results = ""
  #   with open(filePath, "r") as reader:
  #     results = json.load(reader)
  #   return results

if __name__ == "__main__":
  try:
    # print(MSTeamsResource(sys.stdin.read(), sys.argv[1:]))
    MSTeamsResource(sys.argv[1:])
  except Exception as ex:
    log.error(ex)

