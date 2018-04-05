import sys
import json
from json import dumps
from subprocess import call

import os 
# for file io 
import pickle 
import pkg_resources 
#TODO make persistent af
from pkg_resources import resource_filename

filepath = resource_filename('projectcli', 'resources/commandsList.txt')

with open (filepath, 'rb') as fp:
  try:
    commandsList = pickle.load(fp)
  except EOFError:
    commandsList = []
print(commandsList)
def parseCommand(data, args, argNumber):
  #breadth first traversal 
  name = getCurrentName(data)
  if isCorrectArgument(name, args[argNumber]):
    if isFinalCommand(data):
      if isCorrectNumArgs(data, args, argNumber):
        return data["command"]
      else:
        raise Exception("Wrong number of args")
        return 0
    elif hasSubCommands(data): 
      for subCommand in data["subCommands"]:
        result = parseCommand(subCommand, args, argNumber+1)
        if result != 0:
          return result
    else:
      raise Exception("Broken, no command or subcommand found under " + name)
      return 0
  #raise Exception( "Incorrect argument " + args[argNumber] + " does not match " + name)
  return 0
def getCurrentName(data):
  return data["name"]
def hasSubCommands(data):
  if "subCommands" in data:
    return True
  else:
    return False
def isCorrectArgument(name, arg):
  if name == arg:
    return True
  else:
    return False
def isFinalCommand(data):
  if "command" in data:
    return True
  else:
    return False
  
def isCorrectNumArgs(data, args, currentArg):
  argsLeft = len(args) - currentArg - 1
  if data["numArgs"] == argsLeft:
      return True
  else:
    return False
def checkValidStructure(Path):
  #TODO: write this function
  return True
def add(args):
  if len(args) < 3:
    raise Exception("Not enough arguments")
  else:
    for path in args[2:]:
      if path in commandsList:
        raise Exception("Path: " + path + " is already in the commands list")
      elif checkValidStructure(path):
        commandsList.append(path)
        print(commandsList)
        with open(filepath, 'wb') as fp:
          pickle.dump(commandsList, fp)
      else:
        raise Exception("Path: " + path + " is not a valid path")
def listAllCommands():
  total = ""
  for path in commandsList:
    data = json.load(open(path))
    total += getCurrentName(data)
  return total
def main():
  #TODO verbose arguments
  verbose = True
  if len(sys.argv) == 1:
    print("Not enough arguments")
  elif(sys.argv[1] == "add"):
    try:
      add(sys.argv)
    except Exception as e:
      print ("Add error:")
      print (e)
  elif(sys.argv[1]=="remove"):
    print("removing")
  elif(sys.argv[1] == "list"):
    print(listAllCommands())
  else:
    result = 0
    for path in commandsList:
        data = json.load(open(path))
        try:
          result = parseCommand(data, sys.argv, 1)
          print (result)
          if result != 0:
            os.system(result)
        except Exception as e:
          print("Couldn't find command " + sys.argv[1])
          if verbose:
            print (e)

      