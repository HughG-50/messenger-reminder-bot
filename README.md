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
