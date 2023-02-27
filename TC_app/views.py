from django.shortcuts import render
from . import forms
from datetime import datetime
import pandas as pd
import numpy as np
from datetime import datetime
import json
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    try:
        if request.method == 'POST':
            textfile =request.FILES['myfile'].readlines()
            date_dict={'result':textfile}
            return render(request,'TC_app\index.html',context=date_dict)
        else:
            return render(request,'TC_app\index.html')
    except Exception as e:
        error={'error':e}
        return render(request,'TC_app\error.html',context=error)

def search_dates(request, pk=''):
    try:
        if request.method == "GET": # select dates in calendar
            form = forms.DateForm()
            form1 = forms.Sot()
            return render(request, 'TC_app\date.html',{"form":form,"form1":form1} )
        if request.method == "POST": # create cart from selected dates
            form = forms.DateForm(request.POST)
            form1 = forms.Sot(request.POST)
            if form.is_valid():
                start = form.cleaned_data['start_date']
                end = form.cleaned_data['end_date']
                s= form1.data['S']
                start_date = datetime.strftime(start, "%Y-%m-%d")
                end_date = datetime.strftime(end, "%Y-%m-%d")
                startd=start_date+' 00:00:00'
                endd=end_date+' 23:00:00'
                df = pd.read_csv(r':\speridian\django v1 Deploy\TC_project\media\retreaver.csv')
                df=df[['Timestamp','RecordingURL']]
                df['Timestamp1']=pd.to_datetime(df['Timestamp'], format='%Y-%m-%d')
                df.sort_values(by=['Timestamp1'])      
                start_datetime = datetime.strptime(startd, '%Y-%m-%d %H:%M:%S')
                end_datetime = datetime.strptime(endd, '%Y-%m-%d %H:%M:%S')

                dff=df.loc[(df['Timestamp1'] >= start_datetime) & (df['Timestamp1'] <= end_datetime)]
                if s == 'sortaz':
                    dff=dff.sort_values(by=['Timestamp1'])
                json_records = dff.reset_index().to_json(orient ='records')
                arr = []
                arr = json.loads(json_records)

                        
        return render(request, 'TC_app\date.html', {"form":form,"form1":form1,'d': arr,})
    except Exception as e:
        error={'error':e}
        return render(request,'TC_app\error.html',context=error)


def uploadfile(request):
    try:
        if request.method == "POST":
            # if the post request has a file under the input name 'document', then save the file.
            request_file = request.FILES['document'] if 'document' in request.FILES else None
            if request_file:
                    # save attached file

                    # create a new instance of FileSystemStorage
                    fs = FileSystemStorage()
                    file = fs.save(request_file.name, request_file)
                    # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
                    fileurl = fs.url(file)

        return render(request, "TC_app\\upload.html")

    except Exception as e:
        error={'error':e}
        return render(request,'TC_app\error.html',context=error)