from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from pprint import pprint

def FetchData():
    # Create your models here.
    try:
        CrimeData = pd.read_csv('http://pydashboard.pushprojects.live/static/csv/Bos_Crime_Data.csv', header=0, low_memory = False)
        Crime_Df = pd.DataFrame(CrimeData)
        return Crime_Df
    except Exception as ex:
        print(repr(ex))

# Create your views here.
def dashboard(request):
    try:
        Crime_Df = FetchData()

        shooting_days = Crime_Df[Crime_Df.SHOOTING == 1]
        Offences = Crime_Df.groupby(['OFFENSE_DESCRIPTION'])['SHOOTING'].count().reset_index(
            name='Count').sort_values(['Count'], ascending=False)
        Lat_Long = Crime_Df[['Lat', 'Long']]
        Lat_Long = Lat_Long.head(2000)
        latlong_list = Lat_Long.to_json(orient="records")

        context = {
            'offence': Offences['Count'][0],
            'lat_long': latlong_list,
            'shootings': len(shooting_days),
            'number_rows': len(Crime_Df.axes[0])
        }
        return render(request, 'index.html', context)
    except Exception as ex:
        print(repr(ex))



def data_description(request):

    return render(request,'data-description.html')

def descriptive_analytics(request):
    return render(request,'descriptive.html')

def data_visualzation(request):
    return render(request, 'data-visual.html')

def prediction_model(request):
    return render(request, 'predictive.html')

def downloader(request):
    return render(request, 'download.html')
