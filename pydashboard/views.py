from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

def FetchData():
    # Create your models here.
    try:
        MeteorData = pd.read_csv('http://pydashboard.pushprojects.live/static/csv/Crime_data_2017_2021.csv', header=0)

        return MeteorData
    except Exception as ex:
        print(repr(ex))

# Create your views here.
def dashboard(request):
    try:
        data = FetchData()
        df = pd.DataFrame(data)
        context = {
            'number_rows': len(df.axes[0]),
            'number_cols': len(df.axes[0]),
        }

        return render(request, 'index.html', context)
    except Exception as ex:
        print(repr(ex))



def data_description(request):
    return render(request,'index.html')

def descriptive_analytics(request):
    return render(request,'index.html')