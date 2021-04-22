import json
import subprocess

import pytest
from helpers import cmd

# Generic OUT input

# {
#   "params": {
#     "uri": "The webhook URI for MS Teams",
#     "somethingelse": "Some other param"
#   },
#   # Comes from creating an instance of the resource
#   "source": {
#     "url": "" # Webhook to MS Teams
#   }
# }

def test_OUT(httpbin):
  """Test action with no params."""

  data = {
    'params': {
      # empty on purpose
    },
    'source': {
      'url': httpbin + '/post'
    }
  }

  result, debug = cmd('out', data)
  assert result['version'] == {}

def test_OUT_simple_card(httpbin):
  """Test action with a simple card."""

  data = {
    'params': {
      'summary': 'Card Summary',
      'title': 'Card Title',
      'text': 'Card text.',
    },
    'source': {
      'url': httpbin + '/post',
    }
  }

  result, debug = cmd('out', data)
  assert result['version'] == {}

def test_OUT_malformed_card(httpbin):
  """Test action with a malformed card."""

  data = {
    'params': {
    },
    'source': {
      'url': httpbin + '/status/404',
    }
  }

  result, debug = cmd('out', data)
  assert result['version'] == {}
  assert 'ERROR: ' in debug

# def test_OUT_json(httpbin):
#   """JSON should be passed as JSON content."""

#   source = {
#     'uri': httpbin + '/post',
#     'method': 'POST',
#     'json': {
#       'test': 123,
#     },
#     'version': {}
#   }

#   output = cmd('out', source)

#   assert output['json']['test'] == 123
#   assert output['version'] == {}

def test_CHECK_empty():
  """CHECK must return an empty response but not nothing."""

  result, debug = cmd('check', {})
  assert result == []

def test_IN_empty():
  """IN must return an empty version response but not nothing."""

  result, debug = cmd('in', {})
  assert result['version'] == {}
