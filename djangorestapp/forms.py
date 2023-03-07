#forms.py
from django import forms  
from djangorestapp.models import Uav, Users  

class UavForm(forms.ModelForm):  
    class Meta:  
        model = Uav  
        fields = ['UavName', 'UavModel', 'UavWeight', 'UavCategory'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 
            'UavName': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'UavModel': forms.TextInput(attrs={ 'class': 'form-control' }),
            'UavWeight': forms.NumberInput(attrs={ 'class': 'form-control' }),
            'UavCategory': forms.TextInput(attrs={ 'class': 'form-control' }),
      }

class UserForm(forms.ModelForm):  
    class Meta:  
        model = Users  
        fields = ['UserName', 'UserMail', 'UserPassword'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 
            'UserName': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'UserMail': forms.TextInput(attrs={ 'class': 'form-control' }),
            'UserPassword': forms.NumberInput(attrs={ 'class': 'form-control' }),
      }
