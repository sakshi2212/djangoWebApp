from django import forms  
from app.models import Abc  
class AbcForm(forms.ModelForm):  
    class Meta:  
        model = Abc  
        fields = "__all__"  