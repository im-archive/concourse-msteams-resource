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
  def __init__(self, config, sources):
    log.info('Initializing MS Teams Resource Type: OUT ...')

    data = json.load(config)

    log.debug(f'config: {json.dumps(data)}')

    source = data.get('source', None)
    params = data.get('params', None)

    # Setup log level
    if source.get('log_level', None) != None:
      log.level(source['log_level'])
      log.debug(f'Log level set to {source["log_level"]}')

    # Build Card
    if params != None:
      card = self.buildCard(params)

      if source.get('url', None) != None:
        log.info('POSTing card ...')
        self.postCard(source['url'], card)

  def buildCard(self, data):
    log.info('Detecting card sources ... ')

    if 'messageCard' in data.get('messageCard', ''):
      log.info('Card source: JSON')
      m = data['messageCard']
      return json.dumps(m)

    else:
      log.info('Card source: params')
      m = MessageCard(
        summary=data.get('summary', None),
        themeColor=data.get('themeColor', Color.DEFAULT),
        title=data.get('title', None),
        text=data.get('text', None)
      )
      log.info('Card built')
      return m.render(asString=True, filterEmpty=True)

  def postCard(self, url: str, card: str):
    sender = TeamsSender(url)
    sender.postCardJSON(card)
    return

if __name__ == "__main__":
  try:
    # print(MSTeamsResource(sys.stdin.read(), sys.argv[1:]))
    MSTeamsResource(sys.stdin, sys.argv[0])
    print(json.dumps({'version':{}}), file=sys.stdout)
  except Exception as ex:
    log.error(ex)
    sys.exit(1)

