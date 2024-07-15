from django.forms import ModelForm
from .models import Link


class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['original_url']
        exclude = ['shortened_link']
        
