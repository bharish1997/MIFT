from .models import User
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class UserRegistrationForm(UserCreationForm):
    # gender = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=GENDER_CHOICES)

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['gender'].required = True
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['address'].label = "Address"
        self.fields['phno'].label = "Phone Number"

        # self.fields['gender'].widget = forms.CheckboxInput()

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        self.fields['address'].widget.attrs.update(
            {
                'placeholder': 'Address',
            }
        )
        self.fields['phno'].widget.attrs.update(
            {
                'placeholder': 'Phone Number',
            }
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'gender','address','phno']
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            },
            'gender': {
                'required': 'Gender is required'
            },
            'phno': {
                'required': 'phone number is required'
            }
        }

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "user"
        if commit:
            user.save()
        return user


class NgoRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(NgoRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "NGO Name"
        self.fields['last_name'].label = "Chair person"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"
        self.fields['account_no'].label = "Account Number"
        self.fields['ifsc'].label = "IFSC code"
        self.fields['account_holder_name'].label = "Account Holder Name"
        self.fields['address'].label = "Address"
        self.fields['phno'].label = "Phone Number"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter NGO Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter chair person name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        self.fields['account_no'].widget.attrs.update(
            {
                'placeholder': 'Account Number',
            }
        )
        self.fields['ifsc'].widget.attrs.update(
            {
                'placeholder': 'IFSC Code',
            }
        )
        self.fields['account_holder_name'].widget.attrs.update(
            {
                'placeholder': 'Account Holder Name',
            }
        )
        self.fields['address'].widget.attrs.update(
            {
                'placeholder': 'Address',
            }
        )
        self.fields['phno'].widget.attrs.update(
            {
                'placeholder': 'Phone Number',
            }
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2','account_no','ifsc','account_holder_name','address','phno']
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            },
            'account_no':{
                'required': 'Account Number is required',
                'min_length': 'Invalid account number'
            }
            
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "ngo"
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password'})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("User Does Not Exist.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not self.user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


class UserProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['address'].widget.attrs.update(
            {
                'placeholder': 'Address',
            }
        )
        self.fields['phno'].widget.attrs.update(
            {
                'placeholder': 'Phone Number',
            }
        )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "gender","email","address","phno"]


class NgoProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(NgoProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )

        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email Id',
            }
        )
        self.fields['account_no'].widget.attrs.update(
            {
                'placeholder': 'Account Number',
            }
        )
        self.fields['ifsc'].widget.attrs.update(
            {
                'placeholder': 'IFSC Code',
            }
        )
        self.fields['account_holder_name'].widget.attrs.update(
            {
                'placeholder': 'Account Holder Name',
            }
        )
        self.fields['address'].widget.attrs.update(
            {
                'placeholder': 'Address',
            }
        )
        self.fields['phno'].widget.attrs.update(
            {
                'placeholder': 'Phone Number',
            }
        )

    class Meta:
        model = User
        fields = ["first_name","email",'account_no','ifsc','account_holder_name','address','phno']

