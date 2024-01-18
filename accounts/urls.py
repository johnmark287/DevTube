from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    # dj-rest-auth common endpoints
    path("auth/", include("dj_rest_auth.urls")),
    # dj-rest-auth registration endpoints
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
    # password reset
    path(
        "password-reset/confirm/<uidb64>/<token>/",
        TemplateView.as_view(template_name="password_reset_confirm.html"),
        name="password_reset_confirm",
    ),
]
