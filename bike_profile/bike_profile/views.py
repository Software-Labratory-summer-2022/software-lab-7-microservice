import requests
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        user = self.get_user_data()  # API call to external auth service
        score = 10000  # API call to external service payment

        return {
            "score": score,
            "user": user
        }

    def get_user_data(self):
        session_id = self.request.session.session_key
        print("session_id =", session_id)
        resp = requests.get(f"http://localhost:9000/user_details/{session_id}")
        return resp.json()
