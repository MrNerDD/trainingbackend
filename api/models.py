#step 6 from here
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=True, blank=True, default=0)
    roll_no = models.IntegerField( unique=True)
    subject=models.ManyToManyField("Subject") #subject waly model ko yahan relate kea gya hai
        #step 9 starts from here
    '''
    admin dashboard main student object 1 or studentobject2 jo likha  arha hai uski jaga
    student ka name kese aye ab uska code likhna hai 
    
    '''
    def __str__(self):
        return self.name

#step 9 ends here
#step 7 serializers bnany hain 
class Subject(models.Model):      #ye table bnaya hai table per kam hoga 
    name = models.CharField(max_length=200)  #ab ye jo Subject hai ye line 9 per bulaya gya hai 
                                            #Subject ko Student se relate krne keliye

    def __str__(self):
        return self.name
class Comment(models.Model):
    comment=models.CharField(max_length=1000)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)

    
    
    
    def __str__(self):
        return self.name
'''
jab bhi database main changing kro or databse bnao tau 
cmd main ye 2 command run krni hain
(1) python manage.py makemigrations
(2) python manage.py migrate
'''

