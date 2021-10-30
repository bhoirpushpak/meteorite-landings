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


        context = {
            'number_rows': len(Crime_Df.axes[0]),
            'number_cols': len(Crime_Df.axes[0]),
        }

        return render(request, 'index.html', context)
    except Exception as ex:
        print(repr(ex))



def data_description(request):

    Crime_Df = FetchData()
    Data_head =  Crime_Df.head()
    Data_tail = Crime_Df.tail()
    Data_describe =  Crime_Df.describe()
    context = {
        'data_head' : Data_head,
        'data_tail' : Data_tail,
        'data_describe' : Data_describe,
    }

    return render(request,'data-description.html',context)

def descriptive_analytics(request):
    return render(request,'index.html')