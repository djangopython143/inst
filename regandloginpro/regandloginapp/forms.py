from django import forms

class RegistrationForm(forms.Form):
    firstname=forms.CharField(label='Enter Your First Name:',
                              widget=forms.TextInput(
                                  attrs={'class':'form-control','placeholder':'Your First Name'}))
    lastname = forms.CharField(label='Enter Your Last Name:',
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Your Last Name'}))
    username=forms.CharField(label='Enter Your User Name:',
                              widget=forms.TextInput(
                                  attrs={'class':'form-control','placeholder':'Your User Name'}))
    password=forms.CharField(label='Enter Your Password:',
                              widget=forms.PasswordInput(
                                  attrs={'class':'form-control','placeholder':'Your Password'}))
    mobile=forms.IntegerField(label='Enter Your Mobile Number:',
                              widget=forms.NumberInput(
                                  attrs={'class':'form-control','placeholder':'Mobile Number'}))
    email=forms.CharField(label='Enter Your Email-Id',
                          widget=forms.EmailInput(
                              attrs={'class':'form-control','placeholder':'Your Email-Id'}))
    gender_choice=(('MALE','Male'),('FEMALE','Female'))
    gender=forms.ChoiceField(label='Select Your gender',
                             widget=forms.RadioSelect(attrs={'class':'RadioSelect-control'}),choices=gender_choice)
    y=range(2020,1960,-1)
    date_of_birth=forms.DateField(label='Date of Birth',
                                  widget=forms.SelectDateWidget(years=y))

class LoginForm(forms.Form):
    username=forms.CharField(label='User Name',widget=forms.TextInput(
        attrs={'placeholder':'Username','class':'form-control'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(
        attrs={'placeholder':'password','class':'form-control'}
    ))