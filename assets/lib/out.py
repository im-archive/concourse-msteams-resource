#!/usr/bin/env python3
import json
import os
import sys

import subprocess

import logging as log
import tempfile

from sender import TeamsSender
from messageCard import *
from logHelper import *
from parseHTML import *

class MSTeamsResource:
  def __init__(self, config, pwd):
    log.info('Initializing MS Teams Resource Type: OUT ...')
    self.pwd = pwd
    log.debug(f'Working Directory: {self.pwd}')

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
      cardString = self.buildCard(params)

      if source.get('url', None) != None:
        log.info('POSTing card ...')
        self.postCard(source['url'], cardString)
      else:
        log.warn(f'No MS TEAMS URI was supplied. No card will be POSTed.')

  def buildCard(self, data):
    log.info('Detecting card sources ... ')

    if 'template' in data:
      log.info('Card source: Template')
      return self.buildTemplate(data)

    elif 'messageCard' in data:
      log.info('Card source: JSON')
      m = json.loads(data['messageCard'])
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

  def __proc(self, cmd):
    proc = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.stdout

  def buildTemplate(self, data):
    template = json.dumps(json.loads(data['template']))
    vs = data.get('vars',{})

    ls = self.__proc(f'cd {self.pwd} && ls -la')
    log.debug(f'cd {self.pwd} && ls -la')
    log.debug(ls)

    for v in vs.keys():
      if 'file' in vs[v]:
        f = open(f'{self.pwd}/{vs[v]["file"]}')
        value = f.read()
        if 'decodeHTML' in vs[v] and vs[v]['decodeHTML'] == True:
          value = parseHTML.decode(value)
          log.debug(f'Decoded: {value}')

        if 'parseHTML' in vs[v] and vs[v]['parseHTML'] == True:
          value = parseHTML.asMarkdown(value)
          log.debug(f'Markdown: {value}')

      if 'value' in vs[v]:
        value = vs[v]
        log.debug(f'Value: {value}')

      template = template.replace(f'{{{v}}}', value)

    return template

  def postCard(self, url: str, card: str):
    sender = TeamsSender(url)
    return sender.postCardJSON(card)

if __name__ == "__main__":
  try:
    log.debug(f'sys.argv: {sys.argv}')
    log.debug(f'sys.argv[1]: {sys.argv[1]}')
    MSTeamsResource(sys.stdin, sys.argv[1])
    print(json.dumps({'version':{}}), file=sys.stdout)
  except Exception as ex:
    log.error(ex)
    sys.exit(1)

