from rest_framework import serializers
from .models import stud_detail

class serializ_stud(serializers.ModelSerializer):
    class Meta:
        model=stud_detail
        fields='__all__'
