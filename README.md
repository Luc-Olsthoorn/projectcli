# projectcli

## About

This package allows you to simply add command line instructions to any of your projects

Functional, but still largely in development 

## Run

pip instal -e . 

projectcli add <path to your JSON>

projectcli yourCommand yoursubcommand

## Sample JSON file 

```
{
	"name":"raveBox",
	"subCommands":[
		{
			"name":"display",
			"command": "sudo ls",
			"numArgs": 0
		},
		{
			"name":"open",
			"command":"cd",
			"numArgs": 1
		},
		{
			"name":"toto",
			"command": "open /Users/lucolsthoorn/Desktop/toto.mp3",
			"numArgs": 0
		}
	]
}
```

In this example running 
```
projectcli add <path to your JSON>
projectcli raveBox display 
```

Would simply sudo list in the terminal.