# messenger-reminder-bot

Bot to send reminders in messenger

### Setting up a virtual env with pipenv

https://docs.python-guide.org/dev/virtualenvs/

```
cd <your_project_directory>
pipenv install <package>
```

### Installing dependencies and using pipenv

pipenv is like a package manager for a python project. Need to install packages with it, e.g.

`pipenv install selenium`

If using virtualenv like pipenv, make sure that VSCode is using the virtualenv as your python interpreter, otherwise it will not be able to pick up the packages that you installed inside this virtualenv.

To do so, click on the Python interpreter in your bottom bar, you should get a list of possible python interpreters including your virtualenv.

### Installing Selenium and Chromedriver

Updgrade Chrome to latest version, then:

`brew upgrade cask chromedriver`

`xattr -d com.apple.quarantine /usr/local/bin/chromedriver`

https://www.kenst.com/2015/03/installing-chromedriver-on-mac-osx/#:~:text=The%20easiest%20way%20to%20install,seeing%20it%20returns%20a%20version.

**With Docker**
https://www.kenst.com/2018/09/how-to-run-your-selenium-tests-headlessly-in-docker/

### Running the program

`pipenv run python3 main.py`

Example main.py logic

```
import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))
```

### Virtual env shell

`pipenv shell`

- launches subshell in virtual env (e.g. the one defined by the Pipfile)

`exit`

- exit the virtual env shell

`pipenv --rm`

- removes the pipenv shell defined by the Pipfile (only works if you haven't deleted the Pipfile, otherwise you need to delete the activation file)

**Running script manually on Heroku**

`heroku run python main.py`

## Deploying to Heroku

1. Create new app in Heroku
2. Update settings > Add Buildpack > Python
3. Setup `Procfile`

```
web: python <your_script_name.py>
worker: python <your_script_name.py>
```

- web - use when deploying web apps or HTTP request related scripts
- worker - use when deploying normal scripts

4. Setup `requirements.txt` file

https://drgabrielharris.medium.com/python-how-create-requirements-txt-using-pipenv-2c22bbb533af

```
pipenv lock -r > requirements.txt
```

Or just from global packages

```
pip3 freeze > requirements.txt
```

5. Setup heroku with code
   1. `heroku login`
   2. `heroku git:remote -a <name_of_heroku_app>`
   3. Make a commit then push, `git push heroku master`

### Installing Chrome and Chrome driver on Heroku

https://www.andressevilla.com/running-chromedriver-with-python-selenium-on-heroku/

1. Add the following to the config for using Chromedrive in your python script

```
options = webdriver.ChromeOptions()
options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
options.add_argument("--headless")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=options)
```

2. Add the buildpacks to Heroku needed for Chromedriver

- Go to settings > Add Buildpack > Then paste in the URL of the Buildpack you need
- https://github.com/heroku/heroku-buildpack-google-chrome
- https://github.com/heroku/heroku-buildpack-chromedriver

3. Add config needed Chromedriver config vars to Heroku

`CHROMEDRIVER_PATH` = `/app/.chromedriver/bin/chromedriver`
`GOOGLE_CHROME_BIN` = `/app/.apt/usr/bin/google-chrome`

### Checking Heroku logs

https://devcenter.heroku.com/articles/logging

`heroku logs –app <your_app_name> —-tail`

- `--tail` option gives us a real time live stream of logs from the app

### Running script on a schedule

https://devcenter.heroku.com/articles/scheduler

1. Install the Heroku Scheduler add on

`heroku addons:create scheduler:standard`

Resources > Add ons > Heroku Scheduler

2. Open scheduler dashbaord

`heroku addons:open scheduler`

## Setting up Cron job on Mac

https://blog.dennisokeeffe.com/blog/2021-01-19-running-cronjobs-on-your-local-mac

https://stackoverflow.com/questions/48990067/how-to-run-a-cron-job-with-pipenv

- Issues with running a script with crontab with pipenv shell, note answer which tells you how to run it
- Get the path to the virtual env e.g.
  `~/.local/share/virtualenvs/messenger-reminder-bot-BsQ_qW-P/bin`
  and fix your shell script like the example:

```
#!/bin/bash
#or whatever shell you use
cd /Users/X/Code/python/example
. /<path>/<to>/<virtualenv>/bin/activate
# you should specifiy the python version in the below command
#python2.7 start.py >> /Users/X/Code/python/example/log.txt 2>&1
python3 start.py >> /Users/X/Code/python/example/log.txt 2>&1
```

### Setting up a basic shell script

```
# Create the .scripts folder at the root
mkdir ~/.scripts
# Change into the folder
cd ~/.scripts
# Create the file ~/.scripts/hello.sh
touch hello.sh
# Ensure we enable execution permissions for the file
chmod u+x ./hello.sh
```

### Crontab

```
 +---------------- minute (0 - 59)
 |  +------------- hour (0 - 23)
 |  |  +---------- day of month (1 - 31)
 |  |  |  +------- month (1 - 12)
 |  |  |  |  +---- day of week (0 - 6) (Sunday=0 or 7)
 |  |  |  |  |
 *  *  *  *  *  command to be executed
```

https://crontab.guru/examples.html

At 6pm on Sunday's

```
0 18 * * SUN cd ~/.scripts && ./my_script.sh
```

### Logging crontab output

https://stackoverflow.com/questions/24957734/start-python-script-with-cron-and-output-print-to-a-file

```
*/3 * * * * /home/ubuntu/my_script.sh >> /home/ubuntu/Logs.txt 2>&1
```

## Using launchd to run scripts on Mac

- launchd is a more advanced featured tool/framework for starting, stopping and managing daemons, applications, processes, and scripts on Mac
- a daemon is a program running in the background without requiring user input, daemon is root user level, whereas agent runs on behalf of logged in user
- launchd is better than crontab because if your computer is off when scheduled to run, launchd will run once computer boots up, it will also wake up sleeping computer

### Launchd configuration

https://medium.com/@chetcorcos/a-simple-launchd-tutorial-9fecfcf2dbb3

We need to create plist files for each script that we want to be run with launchd.
(Did not take this approach because XML much more complicated than crontab to figure out)

- plist files are Apple's custom XML format for configurations

**Creating a launchd configuration plist file**

```
touch ~/Library/LaunchAgents/com.demo.daemon.plist
```

- plists in `~/Library/LaunchAgents` folder are automatically loaded into launchd when you log in

The following script:

- runs whenever the user logs in
- executes every 20 seconds
- output to some log files
- sets the environment path

```

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
  <dict>

    <key>Label</key>
    <string>com.demo.daemon.plist</string>

    <key>RunAtLoad</key>
    <true/>

    <key>StartInterval</key>
    <integer>20</integer>

    <key>StandardErrorPath</key>
    <string>/Users/chet/demo/stderr.log</string>

    <key>StandardOutPath</key>
    <string>/Users/chet/demo/stdout.log</string>

    <key>EnvironmentVariables</key>
    <dict>
      <key>PATH</key>
      <string><![CDATA[/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin]]></string>
    </dict>

    <key>WorkingDirectory</key>
    <string>/Users/chet/demo</string>

    <key>ProgramArguments</key>
    <array>
      <string>/usr/local/bin/node</string>
      <string>main.js</string>
    </array>

  </dict>
</plist>
```

**Running launchd**

```
launchctl load ~/Library/LaunchAgents/com.demo.daemon.plist
```

## Shell

`$(date)` gives you the current time and date

Permissions issue for cron
https://stackoverflow.com/questions/58844669/trying-to-run-a-python-script-with-cron-getting-errno-1-operation-not-permitt
