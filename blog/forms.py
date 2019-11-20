from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Event, Comment, Address
from django.forms.widgets import FileInput
#from datetimepicker.widgets import DateTimePicker
from bootstrap_datepicker_plus import DatePickerInput, DateTimePickerInput

#class DateForm(forms.Form):
#    date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

class NewPostForm(forms.ModelForm):
    image = forms.ImageField(label=('Image'),required=False,
                                    error_messages ={'invalid':("Image files only")},
                                    widget= FileInput)
    class Meta:
        model = Post
        fields = ('title', 'content', 'image')

class NewEventForm(forms.ModelForm):
    image = forms.ImageField(label=('Image'),required=False,
                                    error_messages ={'invalid':("Image files only")},
                                    widget= FileInput),
    class Meta:
        model = Event
        fields = ['title', 'details', 'dateTime', 'image',]
        labels = {
            'dateTime': 'Date and Time of Event:',
        }
        widgets = {
            'dateTime': DateTimePickerInput(), # default date-format %m/%d/%Y will be used

            #'details' : forms.Textarea,
        }

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class AddAdressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('addressLine1', 'addressLine2', 'suburbCity', 'country', 'stateProvince', 'zipCode', 'latitude', 'longitude')
