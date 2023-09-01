from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field, Div


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    
    # def __init__(self, *args, **kwargs):
     
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Field('username', placeholder='username')
    #     )

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=65)
#     password = forms.CharField(max_length=65, widget=forms.PasswordInput)
#     def __init__(self, *args, **kwargs):
     
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Field('username', placeholder='username')
#         )

