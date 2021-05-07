from logHelper import *
from messageCard import *

import requests

class TeamsSender():
  def __init__(self, webhook:str):
    self.webhook = webhook

  def postCard(self, card: MessageCard):
    data = card.render(filterEmpty=True, asString=True)
    postCardJSON(data)
    return

  def postCardJSON(self, card: str):
    log.info(f'TeamsSender: POSTing card')
    log.debug(f'URL:\t{self.webhook}')
    log.debug(f'DATA:\t{data}')
    response = requests.post(url=self.webhook, data=data)

    if response.status_code >= 400:
      log.error(f'{response.status_code} - {response.text}')
    else:
      log.success(f'TeamsSender: Success')

    return