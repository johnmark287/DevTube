from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from django.urls import path
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
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
]
