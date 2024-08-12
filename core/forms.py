from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Exercise

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].widget.attrs.update({'class': 'form-control'})

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your username',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter your password',
        })

class PromptForm(forms.Form):
    prompt = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ask your questions...', 'class':'form-control'}))

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['exercise', 'weight', 'sets', 'reps']
    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)

        # Add 'form-control' class to all fields
        for field_name in self.fields:
            if not isinstance(self.fields[field_name].widget, (forms.CheckboxInput, forms.CheckboxSelectMultiple, forms.RadioSelect)):
                self.fields[field_name].widget.attrs['class'] = 'form-control'

class DateSelectionForm(forms.Form):
    selected_date = forms.DateField(widget=forms.SelectDateWidget)

from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['gender', 'weight', 'height']
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
     # Add 'form-control' class to all fields
        for field_name in self.fields:
            if not isinstance(self.fields[field_name].widget, (forms.CheckboxInput, forms.CheckboxSelectMultiple, forms.DateField)):
                self.fields[field_name].widget.attrs['class'] = 'form-control'