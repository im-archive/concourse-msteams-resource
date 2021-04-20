#!/usr/bin/env python3
import json
import os
import sys

from sender import TeamsSender
from messageCard import *

class Out:
  def __init__(self, *args):
    self.args = args
    for each arg in args:
      print(f'arg: {arg}')

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
    out = Out(sys.stdin.read(), sys.argv[1:])
  except Exception as ex:
    print(str(ex))

