#Zapay Challenge - spacex

This is a CLI for Zapy Challenge which participants had to build code to access Space X API to retrieve information about Space X launches.

User should be able to choose between PAST, NEXT, LATESTS and UPCOMING launches on an interface and see the results on the screen.

###CLI Installation (Ubuntu only)

First, copy the repository to your machine with the command:

`$ git clone https://github.com/sergiomafra/zapay-challenge`

Then change to it's directory:

`$ cd zapay-challenge`

####Through Script (execute)
`$ ./install`

####Manually (copy and paste on terminal)
`$ LOCAL=/usr/local/bin && USER="$(whoami)" && sudo cp space-x.py $LOCAL/spacex && sudo chmod 0500 $LOCAL/spacex && sudo chown $USER: $LOCAL/spacex`

###Usage
`-n` or `--next`
Shows on screen information about the next launch

`-l` or `--lastest`
Shows on screen information about the latest launch

`-u` or `--upcoming`
Shows on screen information about the upcoming launches

` -p` or `--past`
Shows on screen information about the past launches

`-h` or `--help`
Shows spacex usage and help about the commands on terminal screen