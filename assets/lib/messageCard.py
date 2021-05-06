# https://docs.microsoft.com/en-us/outlook/actionable-messages/message-card-reference

import json
import inspect
from typing import TypedDict, List
# import html2markdown

class Fact(TypedDict):
  name: str
  value: str

Facts = List[Fact]

class Image(TypedDict):
  image: str
  title: str

Images = List[Image]

class Os:
  DEFAULT = 'default'
  IOS = 'iOS'
  ANDROID = 'android'
  WINDOWS = 'windows'

class Target(TypedDict):
  os: Os
  uri: str

# TODO: In order for potentialActions to render, they need to have a @type property set.
class ActionOpenUri(TypedDict):
  name: str
  targets: List[Target]

class Renderable:
  def render(self, asString:bool = False, indent:int = None, filterEmpty:bool = False):
    data = self.__dict__.copy()
    if 'self' in data.keys():
      del data['self']

    if filterEmpty == True:
      c = {}
      for key in data.keys():
        # print(f'type of "{key}": {type(data[key])}')
        # print(f'{key} is ... ', end='')
        if isinstance(data[key], str) and len(data[key].strip()) > 0:
          # print(f'string')
          c[key] = data[key]
        elif isinstance(data[key], dict) and len(data[key].keys()) > 0:
          c[key] = data[key]
        elif isinstance(data[key], Renderable):
          # print(f'Renderable')
          c[key] = data[key].render(asString=False, filterEmpty=filterEmpty)
        elif isinstance(data[key], list) and len(data[key]) > 0:
          # print(f'list')
          c[key] = []
          for item in data[key]:
            if isinstance(item, Renderable):
              c[key].append(item.render(asString=False, filterEmpty=filterEmpty))
            else:
              c[key].append(item)
        elif isinstance(data[key], (int, float, bool)):
          # print('int/float/bool')
          c[key] = data[key]
      data = c

    if asString == True:
      return json.dumps(data, indent=indent, sort_keys=True)
    else:
      return data

class Color:
  DEFAULT = "35495c"
  RED = "d00001"
  GREEN = "33cd34"
  BLUE = "0034d1"
  ORANGE = "d16900"
  YELLOW = "f8ce43"

# class Image(Renderable):
#   def __init__(self, image: str = None, title: str = None):
#     self.__dict__ = locals()

class Section(Renderable):
  def __init__(self,
    title: str = None,
    startGroup: bool = False,
    activityImage: str = None,
    activityTitle: str = None,
    activitySubtitle: str = None,
    activityText: str = None,
    heroImage: Image = None,
    text: str = None,
    facts: Facts = None,
    images: Images = None,
    potentialAction: List[TypedDict] = []):

    self.__dict__ = locals()

Sections = List[Section]

class MessageCard(Renderable):

  """
  Defines a legacy Message Card.

  See https://docs.microsoft.com/en-us/outlook/actionable-messages/message-card-reference for additional details.
  """

  def __init__(self,
    summary: str = None,
    themeColor: str = Color.DEFAULT,
    title: str = None,
    text: str = None,
    sections: Sections = [],
    potentialAction: List[TypedDict] = []):

    locals()["@type"] = 'MessageCard'
    locals()["@context"] = 'https://schema.org/extensions'

    self.__dict__ = locals()

  def addSection(self, section):
    self.sections.append(section)

  def addAction(self, action):
    self.potentialAction.append(action)

# NOT YET IMPLEMENTED
# class ActionHttpPOST:
# class ActionCard:
# class ActionInvokeAddInCommand:

