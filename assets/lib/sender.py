from logHelper import *
from messageCard import *

class TeamsSender():
  def __init__(self, webhook:str):
    self.webhook = webhook

  def postCard(self, card: MessageCard):

    data = card.render(filterEmpty=True, asString=True)
    response = requests.post(url=self.webhook, data=data)

    if response.status_code >= 400:
      log.error(response.text)
    else:
      log.info(f'Successfull POST to MS Teams')

    return