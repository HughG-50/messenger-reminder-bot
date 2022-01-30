# messenger-reminder-bot

Bot to send reminders in messenger

### Running the program

`pipenv run python3 main.py`

Example main.py logic

```
import requests

response = requests.get('https://httpbin.org/ip')

print('Your IP is {0}'.format(response.json()['origin']))
```
