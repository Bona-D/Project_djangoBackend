from django.contrib import admin
from .models import School, Class, Assessment_Areas, Answers, Student, Awards, Subject, Summary

# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = "id", "Name"

class ClassAdmin(admin.ModelAdmin):
    list_display = "id", "Name"

class AnswersAdmin(admin.ModelAdmin):
    list_display = "id", "Answer"

class AssessmentAdmin(admin.ModelAdmin):
    list_display = "id", "Name"

class StudentAdmin(admin.ModelAdmin):
    list_display = "id", "Fullname"

class AwardsAdmin(admin.ModelAdmin):
    list_display = "id", "Name"

class SubjectAdmin(admin.ModelAdmin):
    list_display = "id", "Subject", "Subject_score"

# class SummaryAdmin(admin.ModelAdmin):
#     list_display = "School_id", "class_name"

admin.site.register(School, SchoolAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(Answers, AnswersAdmin)
admin.site.register(Assessment_Areas, AssessmentAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Awards, AwardsAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Summary)
