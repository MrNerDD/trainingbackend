#step 7 start from here 
# by default ye page blank hota hai or bna bhi ni 
# serializers.py khud create krna hota hai
from django.db.models import fields
from api.models import Student
from rest_framework.serializers import ModelSerializer
#jis name se model bnaya hoga usi name se serializer hoga 
class StudentSerializer(ModelSerializer):
# ye ab student model ka serializer ban gya hai
    class Meta:
        model=Student # ye student woi model hai jo models main bnaya hai
        fields="__all__"
#step 8 ab views.py main shuru hoga

