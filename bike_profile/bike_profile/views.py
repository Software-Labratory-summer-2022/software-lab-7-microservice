from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        score = 10000  # API call to external service payment
        user = {
            "username": "derfanian",
            "first_name": "Danial",
            "last_name": "Erfanian",
        }

        return {
            "score": score,
            "user": user
        }
