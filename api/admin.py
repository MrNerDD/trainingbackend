from django.contrib import admin
from .models import Student, Subject ,Comment
# Register your models here.
#step8 start from here
admin.site.register(Student)  #ye her aik main new proj krna hai bus models name diff hoga
#step9 starts on models.py
admin.site.register(Subject) 
admin.site.register(Comment) 

