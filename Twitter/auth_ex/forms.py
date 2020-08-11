from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.contrib.auth import get_user_model


class UserCreationForm(DjangoUserCreationForm):

    class Meta(DjangoUserCreationForm.Meta):
        model = get_user_model()