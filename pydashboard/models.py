import urllib.request, json
import connection as conn
from django.db import models
import pandas as pd

# Create your models here.
try:
    MeteorData = pd.read_csv('static/csv/dataset.csv', header=0)

    print(MeteorData)
except Exception as ex:
    print(repr(ex))