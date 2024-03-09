
from django.contrib import admin
from django.urls import path
from .views import RecipesDetailView, RecipesListView, RecipesPostView, UserListView, RecipesUpdateView, \
    UserCreateView, UserLoginView, UserLogoutView

urlpatterns = [
    path('recipes/create/', RecipesPostView.as_view()),
    path('recipes/', RecipesListView.as_view()),
    path('recipes/<int:id>/', RecipesDetailView.as_view()),
    path('recipes/<int:id>/update/', RecipesUpdateView.as_view()),
    path('recipes/users/', UserListView.as_view()),
    path('recipes/users/register/', UserCreateView.as_view()),
    path('recipes/<int:id>/delete/', RecipesPostView.as_view()),
    path('recipes/users/login/', UserLoginView.as_view()),
    path('recipes/users/logout/', UserLogoutView.as_view()),
]
