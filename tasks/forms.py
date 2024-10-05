from django import forms
from .models import  Tasks,FeedFile
        
class TaskForm(forms.ModelForm):
   
    class Meta:
        model = Tasks
        fields = ['title', 'description','completed','priority','due_date','created_at',]
    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['placeholder'] = 'Enter Title'
      
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'text-black'

from django.forms import ClearableFileInput
...
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
    
class FileModelForm(forms.ModelForm):
    
    image = MultipleFileField(label='Select files', required=False)
    
    class Meta:
        model = FeedFile
        fields = ['image']
       