from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from users.models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Введите имя"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Введите фамилию"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Введите имя пользователя"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': "Введите электронную почту"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Введите пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Введите пароль повторно"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control py-4'

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control py-4'

    class Meta:
        model = User
        fields = ('username', 'password')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваша фамилия'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Логин'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }),
            'image': forms.FileInput(attrs={
                'class': 'custom-file-input'
            })
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Ограничиваем размер файла (например, до 5 МБ)
            if image.size > 5 * 1024 * 1024:
                raise forms.ValidationError("Изображение слишком большое (максимум 5 МБ).")
        return image

# Форма для добавления упражнений

class FavouriteExerciseForm(forms.Form):
    exercise_id = forms.IntegerField(widget=forms.HiddenInput())