#step 6 from here
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200, unique=True)
    age = models.IntegerField(null=True, blank=True, default=0)
    roll_no = models.IntegerField( unique=True)
    #step 9 starts from here
    '''
    admin dashboard main student object 1 or studentobject2 jo likha  arha hai uski jaga
    student ka name kese aye ab uska code likhna hai 
    '''
    def __str__(self):
        return self.name
#step 9 ends here
#step 7 serializers bnany hain 

'''
jab bhi database main changing kro or databse bnao tau 
cmd main ye 2 command run krni hain
(1) python manage.py makemigrations
(2) python manage.py migrate
'''