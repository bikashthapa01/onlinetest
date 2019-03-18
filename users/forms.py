from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
	username = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder':'Your USN'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	rpassword = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Re-type Password '}))
	mod = forms.BooleanField(label='Apply For Moderator ?',required=False)

	class Meta:
		model = User
		fields=('username','password')


	def clean(self):
		cleaned_data = super(RegisterForm,self).clean()
		usn = cleaned_data.get('username')

		# if User.objects.filter(username=usn).count() != 0 :
		# 	raise forms.ValidationError(' Account Already Exists with this USN')

		if not (usn.startswith('1st') or usn.startswith('1ST')):
			raise forms.ValidationError('Invalid USN (Must Start with 1st ') 

		if 'cs' not in usn:
			raise forms.ValidationError('Invalid USN ( Must be a CS student )') 

		password = cleaned_data.get('password')
		cpassword = cleaned_data.get('rpassword')
		if password != cpassword:
			raise forms.ValidationError("Password Do Not Match !")
