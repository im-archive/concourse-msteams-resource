from messageCard import *
import json
import pytest

def test_MessageCard():
  m = MessageCard()

  expected = {
    "@type": "MessageCard",
    "@context": "https://schema.org/extensions",
    "summary": None,
    "themeColor": Color.DEFAULT,
    "title": None,
    "text": None,
    "sections": [],
    "potentialAction": []}

  actual = m.render()

  assert actual == expected

  actual = m.render(filterEmpty=True)
  expected = {'themeColor': Color.DEFAULT, '@type': 'MessageCard', '@context': 'https://schema.org/extensions'}

  assert actual == expected

  # Test JSON serialization
  actual = json.loads(m.render(filterEmpty=True, asString=True))
  expected = {
    'themeColor': Color.DEFAULT,
    '@type': 'MessageCard',
    '@context': 'https://schema.org/extensions'}

  assert actual == expected

def test_Section():
  s = Section()

  expected = {
    'title': None,
    'startGroup': False,
    'activityImage': None,
    'activityTitle': None,
    'activitySubtitle': None,
    'activityText': None,
    'heroImage': None,
    'text': None,
    'facts': None,
    'images': None,
    'potentialAction': []}

  actual = s.render()

  assert actual == expected

  expected = {}
  assert s.render(filterEmpty=True) == {'startGroup': False}

def test_CardWithSection():
  m = MessageCard(title='Test', text='This is a test', summary='Summary')
  s = Section(title='Section Title')
  m.addSection(s)

  actual = json.loads(m.render(filterEmpty=True, asString=True))
  expected = {'summary': 'Summary', 'themeColor': Color.DEFAULT, 'title': 'Test', 'text': 'This is a test', 'sections': [{'title': 'Section Title', 'startGroup': False}], '@type': 'MessageCard', '@context': 'https://schema.org/extensions'}

  assert actual == expected

def test_DeserializeCard():
  cardJSON = '{"themeColor": "35495c"}'
  data = json.loads(cardJSON)
  m = MessageCard(**data)

  assert m.themeColor == Color.DEFAULT


