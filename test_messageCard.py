from lib import messageCard as lib
import json

def test_MessageCard():
  m = lib.MessageCard()

  expected = {
    "@type": "MessageCard",
    "@context": "https://schema.org/extensions",
    "summary": None,
    "themeColor": lib.Color.DEFAULT,
    "title": None,
    "text": None,
    "sections": [],
    "potentialAction": []}

  actual = m.render()

  assert actual == expected

  actual = m.render(filterEmpty=True)
  expected = {'themeColor': lib.Color.DEFAULT, '@type': 'MessageCard', '@context': 'https://schema.org/extensions'}

  assert actual == expected

  # Test JSON serialization
  actual = json.loads(m.render(filterEmpty=True, asString=True))
  expected = {
    'themeColor': lib.Color.DEFAULT,
    '@type': 'MessageCard',
    '@context': 'https://schema.org/extensions'}

  assert actual == expected

def test_Section():
  s = lib.Section()

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
  m = lib.MessageCard(title='Test', text='This is a test', summary='Summary')
  s = lib.Section(title='Section Title')
  m.addSection(s)

  actual = json.loads(m.render(filterEmpty=True, asString=True))
  expected = {'summary': 'Summary', 'themeColor': lib.Color.DEFAULT, 'title': 'Test', 'text': 'This is a test', 'sections': [{'title': 'Section Title', 'startGroup': False}], '@type': 'MessageCard', '@context': 'https://schema.org/extensions'}

  assert actual == expected
