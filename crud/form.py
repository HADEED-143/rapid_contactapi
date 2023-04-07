from django.forms import ModelForm
from . models import contact

class Contact_form(ModelForm):
    class Meta:
        model = contact
        fields = '__all__'