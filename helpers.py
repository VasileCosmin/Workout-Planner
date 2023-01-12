from flask import redirect, session
from functools import wraps
import json
import requests


def login_required(f):
  """
  Decorate routes to require login.

  https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
  """
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if session.get("user_id") is None:
      return redirect("/login")
    return f(*args, **kwargs)
  return decorated_function



def get_exercises(muscle):
  url = "https://exercises-by-api-ninjas.p.rapidapi.com/v1/exercises"

  querystring = {"muscle": muscle}

  headers = {
    "X-RapidAPI-Key": "5e49e6c529msh539b9a5b3af5adfp15b833jsn725a79513fa1",
    "X-RapidAPI-Host": "exercises-by-api-ninjas.p.rapidapi.com"
  }

  response = json.loads(requests.request("GET", url, headers=headers, params=querystring).text)
  
  return response