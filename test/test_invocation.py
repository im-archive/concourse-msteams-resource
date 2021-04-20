import json
import subprocess

import pytest
from helpers import cmd

def test_out(httpbin):
  """Test OUT action with minimal input."""
  data = {
    'source': {
      'uri': httpbin + '/status/200',
    },
    'version': {}
  }
  subprocess.check_output('/opt/resource/out', input=json.dumps(data).encode())
  # subprocess.run(['/opt/resource/out', json.dumps(data).encode()], capture_output=True)
