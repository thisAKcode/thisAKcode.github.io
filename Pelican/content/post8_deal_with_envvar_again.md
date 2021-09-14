title: Private Parameters Loading With Dotenv
date: 2021-04-06 23:00
author: Alex

# Setting Environment Variables

Nice people from the Internet wrote here about how to use dotenv to pass around credentials that you want to keep private:  <https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/>. So I feel that it make sense and for different projects from now on I used [python dotenv](https://pypi.org/project/python-dotenv/). 


# Set of steps to follow
1. create venv in your project directory `python -m venv venv && venv\Scripts\activate.bat`
2. Install python-dotenv into your virtualenv:
`pip install python-dotenv`
3. Set my `PRIVATE_VARIABLE='test'`:
`vim .env`
4. Inside .env add a variable and assign the value 'test' to it:
```
# myapp settings
PRIVATE_VARIABLE='test'
```
We populated this `PRIVATE_VARIABLE` with `test` which I consider to keep secret.
This will be an environment variable to pass around within venv

5. The variable inside `.dotenv` retrieved in app.py as follows:
```python
from dotenv import dotenv_values

DOTENV_CONFIG = dotenv_values(".env")  # access dict object {"PRIVATE_VARIABLE": "test"}
API_URL = DOTENV_CONFIG['AWS_ENDPOINT']
```
## Additional step to fix variable "privacy"
6. I want to keep it away from others but available for python within this particular venv. 
I want to add .env to my .gitignore. This way when I post my code to Github I keep `.env` private (away from vcs).
In `.gitignore` I add the following:
```
.env
```

