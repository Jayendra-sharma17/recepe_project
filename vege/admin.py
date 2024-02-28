from django.contrib import admin
from .models import *
from django.db.models import Sum
admin.site.register(Receipe)
# Register your models here.
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)

admin.site.register(Subject)
# admin.site.register(SubjectMarks)

class SubjectMarkAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']
admin.site.register(SubjectMarks, SubjectMarkAdmin)

class Rankstudentadmin(admin.ModelAdmin):
    list_display=['student','student_rank','total_marks','student_rank_generation_date']
    ordering=['student_rank']
    def total_marks(self,obj):
        subject_marks=SubjectMarks.objects.filter(student=obj.student)
        marks=(subject_marks.aggregate(marks=Sum('marks')))
        
        return marks['marks']
admin.site.register(Rankstudnet,Rankstudentadmin)