from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import JsonResponse

from django.views.generic.edit import FormView


class RegisterFormView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()  # form data will be saved
        return super().form_valid(form)


def user_details(request, session_id):
    session = Session.objects.get(session_key=session_id)
    user_id = session.get_decoded()['_auth_user_id']
    user = User.objects.get(pk=user_id)
    return JsonResponse(
        {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "last_login": user.last_login,
        }
    )
