#step 2 start from here .by defualt this page is blank 
#or ye page hmain khud bnana hota hai 


from django.urls import path 
from .views import get_response, post_response,post_response_to_frontend,add_student # ye step 4 hai... function ko import kea hai yahan
urlpatterns = [
                    
     path('',get_response),         #ab yahan function call krna pry ga magar 
                        #function bnana views.py main hai
    #get ka path hai /api/
     path('post/',post_response),       
     #post ka path hai /api/post/   
     path('posttofrontend/',post_response_to_frontend),  
     path('addstudent/',add_student),       

               
]


#step3 ab views.py main hoga shuru
#step4 krlia hai or function call hogya hai ab postman main check krna hai 
#ke data frontend pe gya hai ya ni
#step 5 ab post ki req bnayen gy views.py main
'''
    jab bhi project per kam krna hai tau app ka name settings.py ko btana hota hai
    iss project main hmari app ka name api hai    
    '''