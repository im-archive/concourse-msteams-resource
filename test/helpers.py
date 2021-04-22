import json
import os
import subprocess
import sys

ENVIRONMENT = {
  'BUILD_NAME': '1',
  'BUILD_JOB_NAME': 'test-job',
  'BUILD_PIPELINE_NAME': 'test-pipeline',
  'BUILD_ID': '123',
  'TEST': 'true',
}

def cmd(cmd_name, data):
  """Wrap command interaction for easier use with python objects."""

  data = json.dumps(data)

  command = f'/opt/resource/{cmd_name}'
  environment = dict(os.environ, **ENVIRONMENT)
  result = subprocess.run(command, input=data, env=environment, capture_output=True, text=True)
  print(f'*** STDOUT: **{result.stdout}**', file=sys.stderr)
  return json.loads(result.stdout), result.stderr