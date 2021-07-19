#step3 yahan se shuru hoga 
from django.shortcuts import render
from rest_framework.response import Response #ye bhi khud krna hai humne 
#or ye json ki form object ki form main frontend per data bhejta hai
from rest_framework.decorators import api_view
# ab StudentSerializer import krain gy idhr  nechy
from .serializers import StudentSerializer
# Create your views here.
@api_view(['GET']) #khud krna ye
def get_response(request):    #ye function bnaya hai python main
    return Response("bum bum diggy bum") #khud kea ye b
    
    '''
 jo bhi data response ki uper wali  parathensis ( ) ke ander likha jaye gaa wo yahan se 
frontend main chla jaye ga 
step 3 complete here ab urls.py api main jana hai or
function get_response wahan call krna hai
    '''
#step 5 start from here 
@api_view(['POST'])
def post_response(request):
    print(request.data) # frontend se data  backend per post man ke through mangwane keliye
    return Response("tlm 1.0")
#get ka kam hai data backend se frontend per bhejna
#post ka kam hai front end se data backend per lena or backend se data frontend per bhejna
#data post method se frontend se backend per agya hai cmd main print ho chuka hai ab
# woi data wapis backend se frontend per bhejna hai
@api_view(['POST'])
def post_response_to_frontend(request):
    rawdata=request.data #ye variable bnaya hai
    #raw data variable ke ander frontend se jo post ke through data aya hai wo pra hai 
    print(rawdata)    #iss se data fronend se backend per agya hai 
    return Response(rawdata)
#step 6 shuru hoga models.py se ab database per kam krain gy
#............................................................
#step 7 yahan se shuru hoga serializer bnany ke bd yahan kam krna hai
@api_view(['POST'])
def add_student(request): #ye function bnaya hai
    savedata=request.data  #ye variable bnaya hai iss main frontend se any wala data bqackend main save krne klye
    #jo serializer bnaya hai pahly usy import krna hai StudentSerializer ko uper
    save_data_serializer=StudentSerializer(data=savedata)
    if save_data_serializer.is_valid(): 
        #if wali line data check kry gi valid hai ya ni 
        save_data_serializer.save()
        #agr data valid hua tau data save krwady gi 
    #ab data StudentSeralizer pass hai jo frontend se aya hai 
    #or wo ab ye data models main bhejy ga or uska jo result hoga 
    #wo save_data_serializer main ajaye ga 
    return Response(save_data_serializer.data) #.data ana he ana hai jab aisa kam ho
    #ab post man main dekhna hai data frontend se backend per arha hai ya ni
    #step8 admin .py main hoga ,
    #data ko database per show krne keliye models.py ko admin.py main call krna hoga
   

