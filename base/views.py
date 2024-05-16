from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import School, Class, Assessment_Areas, Answers, Student, Awards, Subject, Summary
import os
import pandas as pd

files = ['Ganison_dataset_1.csv', 'Ganison_dataset_2.csv', 'Ganison_dataset_3.csv', 'Ganison_dataset_4.csv', 'Ganison_dataset_5.csv', 'Ganison_dataset_6.csv']


def home(request):
    return HttpResponse('<h1>Home</h1>')

# class fileReader:
#     unique_values = []

#     for file in files:
#             file_path = os.path.join('C:\\Users\\Dami Yami\\Desktop\\OctopusBI\\practicaltest\\files', file)
#             df = pd.read_csv(file_path)
#             unique_values.extend(df['Class'].unique())  

#     unique_values = list(set(unique_values))

class fileReader:

    def fileR(self, feild) -> None:
        
        self.unique_values = []

        for file in files:
                file_path = os.path.join('C:\\Users\\Dami Yami\\Desktop\\OctopusBI\\practicaltest\\files', file)
                df = pd.read_csv(file_path)
                self.unique_values.extend(df[feild].unique())  

        self.unique_values = list(set(self.unique_values))


# class view
def allClasses(request):

    if not Class.objects.exists(): 
        fr = fileReader()
        fr.fileR("Class")
        
        for class_name in fr.unique_values:
            if not Class.objects.filter(Name=class_name).exists(): 

                new_class = Class(Name=class_name)
                new_class.save()

    dv = Class.objects.all()
    return render(request, 'dataview.html', {'dv': dv})



# school table
def allSchools(request):

    unique_School = []
    if not School.objects.exists(): 

        for file in files:
            file_path = os.path.join('C:\\Users\\Dami Yami\\Desktop\\OctopusBI\\practicaltest\\files', file)
            df = pd.read_csv(file_path)
            unique_School.extend(df['school_name'].unique())  

        unique_School = list(set(unique_School))


    for school_name in unique_School:
        if not School.objects.filter(Name=school_name).exists(): 

            new_school = School(Name=school_name)
            new_school.save()

    dv = School.objects.all()
    return render(request, 'dataview.html', {'dv': dv})


# Assessment_Areas table
def allAssessment(request):

    unique_Assessment = []
    if not Assessment_Areas.objects.exists(): 
        
        for file in files:
            file_path = os.path.join('C:\\Users\\Dami Yami\\Desktop\\OctopusBI\\practicaltest\\files', file)
            df = pd.read_csv(file_path)
            unique_Assessment.extend(df['Assessment Areas'].unique())  

        unique_Assessment = list(set(unique_Assessment))


    for Assessment_name in unique_Assessment:
        if not Assessment_Areas.objects.filter(Name=Assessment_name).exists(): 

            new_As = Assessment_Areas(Name=Assessment_name)
            new_As.save()

    dv = Assessment_Areas.objects.all()
    return render(request, 'dataview.html', {'dv': dv})



# Answers table
def allAnswers(request):
 
    unique_Answers = []

    for file in files:
        file_path = os.path.join('C:\\Users\\Dami Yami\\Desktop\\OctopusBI\\practicaltest\\files', file)
        df = pd.read_csv(file_path)
        unique_Answers.extend(df['Answers'].unique())  

    # unique_Answers = list(set(unique_Answers))


    for Answer in unique_Answers:
        if not Answers.objects.filter(Answer=Answer).exists(): 

            new_Answer = Answers(Answer=Answer)
            new_Answer.save()

    return HttpResponse('Need to Add HTML View')

# Awards table
def allAwards(request):
 
    unique_Award = []

    for file in files:
        file_path = os.path.join('C:\\Users\\Dami Yami\\Desktop\\OctopusBI\\practicaltest\\files', file)
        df = pd.read_csv(file_path)
        unique_Award.extend(df['award'].unique())  

    unique_Award = list(set(unique_Award))


    for Award_name in unique_Award:
        if not Awards.objects.filter(Name=Award_name).exists(): 

            new_Award = Awards(Name=Award_name)
            new_Award.save()

    return HttpResponse('Need to Add HTML View')



# Subject table
def allSubject(request):
 
    unique_Subject = []

    for file in files:
        file_path = os.path.join('C:\\Users\\Dami Yami\\Desktop\\OctopusBI\\practicaltest\\files', file)
        df = pd.read_csv(file_path)
        unique_Subject.extend(df['Subject'].unique())  

    unique_Subject = list(set(unique_Subject))


    for Sub_name in unique_Subject:
        if not Subject.objects.filter(Subject=Sub_name).exists(): 

            new_sub = Subject(Subject=Sub_name)
            new_sub.save()

    return HttpResponse('Need to Add HTML View')

# Students table
