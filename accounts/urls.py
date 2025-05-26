from django.urls import path, include
from accounts.views import registerView, loginView, logoutView, perfilView

urlpatterns = [
    path('accounts/register/', registerView.as_view(), name='Register'),
    path('accounts/login/', loginView.as_view(), name='Login'),
    path('accounts/logout/', logoutView.as_view(), name='Logout'),
    path('accounts/perfil/', perfilView.as_view(), name='Perfil'),
]
