# messenger-reminder-bot

Bot to send reminders in messenger

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
