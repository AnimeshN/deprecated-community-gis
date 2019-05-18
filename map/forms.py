from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Layers
from . fields import RestrictedFileField


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label = '',max_length=30, required=False, help_text='<small>*Optional.</small>',widget = forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter First Name'}))
    last_name = forms.CharField(label = '',max_length=30, required=False, help_text='<small>*Optional.</small>',widget = forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Last Name'}))
    email = forms.EmailField(label = '',max_length=254, help_text='<small>*Required</small>',widget = forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter email address'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def __init__(self,*args,**kwargs):
    	super(SignUpForm,self).__init__(*args,**kwargs)

    	self.fields['username'].widget.attrs['class'] = 'form-control'
    	self.fields['username'].widget.attrs['placeholder'] = 'Enter User Name'
    	self.fields['username'].label = ''
    	self.fields['username'].help_text = '<small>*Required, Letters, digits and @/./+/-/_ only.</small>'


    	self.fields['password1'].widget.attrs['class'] = 'form-control'
    	self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
    	self.fields['password1'].label = ''
    	self.fields['password1'].help_text = """<small><ul>
			<li>Your password can't be too similar to your other personal information.</li>
			<li>Your password must contain at least 8 characters.</li>
			<li>Your password can't be a commonly used password.</li>
			<li>Your password can't be entirely numeric.</li>
		</ul></small>"""

    	self.fields['password2'].widget.attrs['class'] = 'form-control'
    	self.fields['password2'].widget.attrs['placeholder'] = 'Enter Password Again'
    	self.fields['password2'].label = ''
    	self.fields['password2'].help_text = ''




class PassChangeForm(PasswordChangeForm):
	def __init__(self, *args , **kwargs):
		super(PassChangeForm, self).__init__(*args , **kwargs)
		self.fields['old_password'].widget.attrs['class'] = 'form-control'
		self.fields['old_password'].widget.attrs['placeholder'] = 'Enter Old Password'
		self.fields['old_password'].label = ''


		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].help_text = """<small><ul>
			<li>Your password can't be too similar to your other personal information.</li>
			<li>Your password must contain at least 8 characters.</li>
			<li>Your password can't be a commonly used password.</li>
			<li>Your password can't be entirely numeric.</li>
		</ul></small>"""
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Enter New Password'
		self.fields['new_password1'].label = ''




		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Enter New Password Again'
		self.fields['new_password2'].label = ''


select_themes_CHOICES  = (
			('CEN','Census'),
			('EDU','Education'),
			('RUL','Rural'),
			('WAT','Water'),
			('HEL','Health'),
			('OTH','Other'),
		)

class LayersForm(forms.ModelForm):
	
	name_of_layer = forms.CharField(label = '',max_length=30, required=True,widget = forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Layers Name'}))
	description = forms.CharField(label = '',max_length=200, required=True,widget = forms.TextInput(attrs = {'class':'form-control','placeholder':'Description'}))
	# select_theme = forms.ChoiceField(choices=select_themes_CHOICES)
	if_other = forms.CharField(label = '',max_length=50, required=False,help_text='<small>*Optional</small>',widget = forms.TextInput(attrs = {'class':'form-control','placeholder':'Other Theme'}))
	source = forms.CharField(label = '',max_length=50, required=False,help_text='<small>*Optional</small>',widget = forms.TextInput(attrs = {'class':'form-control','placeholder':'Source of Data'}))
	
	tool_used = forms.CharField(label = '',max_length=50, required=False,help_text='<small>*Optional</small>',widget = forms.TextInput(attrs = {'class':'form-control','placeholder':'Tool Used'}))
	layer = RestrictedFileField(label = '',content_types=['image/jpeg','image/png','application/vnd.google-earth.kml+xml','image/tiff','application/gml+xml','text/csv','application/pdf', 'application/zip','application/x-tar','application/geo+json','application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'])
	class Meta:
		model = Layers
		fields = ('name_of_layer','description','select_theme','if_other','source','types','style_file_available','tool_used','layer',)