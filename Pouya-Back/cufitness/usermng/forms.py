from django import forms
from .models import CustomUser


class UserRegistrationAdminForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        # email = self.cleaned_data.get('email')
        # password = self.cleaned_data.get('password')
        # user = CustomUser.objects.create_user(email=email, password=password)

        if commit:
            instance.save()
        return instance