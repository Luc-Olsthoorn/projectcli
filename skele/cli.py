import sys
from . import __version__ as VERSION
import json
from pprint import pprint
from json import dumps
from subprocess import call

commandsList =["/Users/lucolsthoorn/Programming/cliproject/skele-cli/skele/commands/userCommand.json"]




def main():
  print(sys.argv)
  for path in commandsList:
      data = json.load(open(path))
      print (sys.argv[1])
      print (list(data)[0])
      name = list(data)[0]
      if sys.argv[1] == name:
        subCommandsNames = list(data[name])
        call(data[name][subCommandsNames[0]])
    #call([)