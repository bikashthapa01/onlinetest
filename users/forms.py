from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
	first_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':'First Name'}))
	last_name = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
	username = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'placeholder':'Your USN'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
	rpassword = forms.CharField(widget= forms.PasswordInput(attrs={'placeholder':'Re-type Password '}))
	mod = forms.BooleanField(label='Apply For Moderator ?',required=False)

	class Meta:
		model = User
		fields=('first_name','last_name','username','password')


	def clean(self):
		cleaned_data = super(RegisterForm,self).clean()
		usn = cleaned_data.get('username')

		# if User.objects.filter(username=usn).count() != 0 :
		# 	raise forms.ValidationError(' Account Already Exists with this USN')
		#1st16cs710


		if not (usn.startswith('1st') or usn.startswith('1ST')):
			raise forms.ValidationError('Invalid USN (Must Start with 1st ') 

		if usn[5:7] != 'cs':
			raise forms.ValidationError('Invalid USN ( Must be a CS student )') 
		if not usn[7:].isnumeric():
			raise forms.ValidationError('Invalid USN (')

		if len(usn) != 10 :
			raise forms.ValidationError('Invalid USN')


		password = cleaned_data.get('password')
		cpassword = cleaned_data.get('rpassword')
		if password != cpassword:
			raise forms.ValidationError("Password Do Not Match !")


	def save(self,commit=True):
		user = super(RegisterForm,self).save(commit=False)
		user.set_password(self.cleaned_data['password'])
		if commit:
			user.save()
		return user

