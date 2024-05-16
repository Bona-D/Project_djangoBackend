from django.db import models

# Create your models here.
class School(models.Model):
    # id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

class Class(models.Model):
    # id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

class Assessment_Areas(models.Model):
    # id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

class Student(models.Model):
    # id = models.AutoField(primary_key=True)
    Fullname = models.CharField(max_length=255)

class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    Answer = models.CharField(max_length=10)

class Awards(models.Model):
    # id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)

class Subject(models.Model):
    # id = models.AutoField(primary_key=True)
    Subject = models.CharField(max_length=255)
    Subject_score = models.IntegerField(null=True)

class Summary(models.Model):
    # School_id = models.AutoField(primary_key=True)
    sydney_participants = models.IntegerField(null=True)
    sydney_percentile = models.IntegerField(null=True)
    Assessment_Areas_Id = models.IntegerField(null=True)
    Awards_Id = models.IntegerField(null=True)
    Class_Id = models.IntegerField(null=True)
    Correct_answer_percentage_per_class = models.IntegerField(null=True)
    Correct_Answer = models.CharField(max_length=10)
    Student_Id = models.IntegerField(null=True)
    Participants = models.IntegerField(null=True)
    Student_Score = models.IntegerField(null=True)
    Subject_Id = models.IntegerField(null=True)
    Category_Id = models.IntegerField(null=True)
    Year_level_name = models.CharField(max_length=100)
    Answer_Id = models.IntegerField(null=True)
    Correct_asnwer_Id = models.IntegerField(null=True)