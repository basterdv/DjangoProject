from django.contrib.auth.forms import UserCreationForm, forms, UserChangeForm

from users.models import CustomUser


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        labels = {
            'username': 'username',
            'email': 'Email',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match')
        return password2

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email is None:
            raise forms.ValidationError('This field is required')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            # 'class': 'form-control',
            'required': 'true',
            'name': 'username',
            'id': 'username',
            'type': 'text',
            # 'class': 'form-control block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
            'class': 'form-control block w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Username',
        })

        self.fields['email'].widget.attrs.update({
            'required': 'true',
            'name': 'email',
            'id': 'email',
            'type': 'email',
            'class': 'form-control block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Email',
        })

        self.fields['password1'].widget.attrs.update({
            'required': 'true',
            'name': 'password1',
            'id': 'password1',
            'type': 'password',
            'class': 'form-control block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Password',
        })

        self.fields['password2'].widget.attrs.update({
            'required': 'true',
            'name': 'password2',
            'id': 'password2',
            'type': 'password',
            'class':'form-control block w-full pl-10 pr-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
            'placeholder': 'Password confirmation',
        })

    # def __init__(self, *args, **kwargs):
    #     super(RegisterUserForm, self).__init__(*args, **kwargs)
    #     # class="block w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
    #     # placeholder="Иван" required=""
    #     self.fields['username'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['password1'].widget.attrs['class'] = 'form-control'
    #     self.fields['password2'].widget.attrs['class'] = 'form-control'

    # self.fields['username'].widget.attrs.update({'class':'form-control'})

class ProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = [

            'username',
            'email',

        ]

