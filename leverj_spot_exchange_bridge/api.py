#!/usr/bin/env python

import json
import os
import sys
from subprocess import *
from Naked.toolshed.shell import *

api_js=os.path.join(os.path.dirname(__file__), 'api.js')

def run_js(command, arguments_as_dictionary):
  arguments_as_json = json.dumps(arguments_as_dictionary)
  node_command = f"{api_js} --command={command} --args='{arguments_as_json}'"
  result = muterun_js(node_command)
  if result.exitcode == 0:
    return json.loads(result.stdout)
  else:
    sys.stderr.write(result.stderr.decode('utf-8'))
