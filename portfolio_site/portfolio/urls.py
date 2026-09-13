from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact/", views.contact_submit, name="contact_submit"),
    path("resume/download/", views.download_resume, name="download_resume"),
    # A couple of friendly aliases some visitors/search engines might try.
    path("resume/", RedirectView.as_view(pattern_name="download_resume")),
]
