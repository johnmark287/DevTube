from django.urls import include, path

urlpatterns = [
    # dj-rest-auth common endpoints
    path("auth/", include("dj_rest_auth.urls")),
    # dj-rest-auth registration endpoints
    path("auth/registration/", include("dj_rest_auth.registration.urls")),
]
