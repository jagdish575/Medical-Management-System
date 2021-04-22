from django import forms
from django.contrib.auth.models import User
from .models import (
    Dealer, Medicine, Employee,
    Customer, Purchase,
)
from django.contrib.auth.forms import UserCreationForm,\
    AuthenticationForm


class AddDealerForm(forms.ModelForm):
    """"
    This class creates a dealer.
    """
    class Meta:
        model = Dealer
        fields = ['fname', 'lname', 'address', 'phone_number', 'email']
        widgets = {
            'fname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomFirstName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'lname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationCustomLastName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                }
            ),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationPhoneNumber',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "tel"
                }
            ),
            'email': forms.TextInput(attrs={
                'class': 'form-control user_input',
                'id': 'validationEmail',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "email"
                }
            ),
        }


class AddMedicineForm(forms.ModelForm):
    
    class Meta:
        model = Medicine
        fields = [
            "med_code", "med_name", "dealer_name",
            "price", "stock", "description"
        ]
        widgets = {
            'med_code': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationMedCode',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'med_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationMedName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'dealer_name': forms.Select(attrs={
                'class': 'form-control',
                'id': 'validationMedName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationPrice',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
            'stock': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationStock',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                }
            ),
        }


class AddEmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = [
            "fname", "lname", "address",
            "salary", "phone_number", "email"
        ]
        widgets = {
            'fname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationFirstName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'lname': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationLastName',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                }
            ),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                }
            ),
            'salary': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationPrice',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "number"
                }
            ),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationStock',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': "tel"
                }
            ),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'validationEmail',
                'aria-describedby': 'inputGroupPrepend',
                'required': "true",
                'type': 'email'
                }
            ),
        }


class CreateUserForm(UserCreationForm):
    """
    A form that inherits from the base *UserCreationForm*,
    and creates a user, with no privileges, from the given 
    username and password.
    """
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control password_input',
            'id': 'confirmPassword1',
            'required': 'true',
            }
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control password_input',
            'id': 'confirmPassword2',
            'required': 'true',
            }
        ),
    )
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
        'username': forms.TextInput(attrs={
            'autocomplete': 'username',
            'class': 'form-control user_input',
            'id': 'validationCustomUsername',
            'aria-describedby': 'inputGroupPrepend',
            'required': 'true',
            }
        ),
    }


class LogUserForm(forms.Form):
    """
    A form that inherits from the base *Form* class,
    and logs a user, with no privileges, from the given 
    username and password.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autocomplete': 'username',
            'class': 'form-control user_input',
            'id': 'validationCustomUsername',
            'aria-describedby': 'inputGroupPrepend',
            'required': 'true',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'form-control password_input',
            'id': 'confirmPassword1',
            'required': 'true',
            }
        )
    )


# class UpdateProfileForm(forms.ModelForm):
#     """
#     This form updates a user profile, from the given 
#     bio and profile_picture fields.
#     """
#     profile_picture = forms.FileField()
#     class Meta:
#         model = Profile
#         fields = ['bio', 'profile_picture']
#         widgets = {
#             'bio': forms.Textarea(attrs={
#                 'class': 'form-control edit_textarea',
#                 'id': 'editBio',
#                 'rows': '3',
#             }
#         )
#     }


class UpdateUserForm(forms.ModelForm):
    """
    This form updates a user, from the given 
    username field.
    """
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={
            'autocomplete': 'username',
            'class': 'form-control user_input',
            'id': 'validationCustomUsername',
            'aria-describedby': 'inputGroupPrepend',
            'required': 'true',
            }
        )
    }