from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name= "index"),
    path("login", views.login_view, name= "login"),
    path("logout", views.logout_view, name="logout"),
    path("image/<int:id>", views.image_page,name='image'),
    path("profile/<int:id>", views.profile_page,name ='profile'),
    path("signup", views.signup, name = "signup"),

    # API paths
    path("filter/<str:system>", views.tissue_filter, name="tissue_filter"),
    path("comment/<int:slide_id>", views.comment, name="comment")
]