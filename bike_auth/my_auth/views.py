from django.contrib.auth.forms import UserCreationForm

from django.views.generic.edit import FormView


class RegisterFormView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        form.save()  # form data will be saved
        return super().form_valid(form)
