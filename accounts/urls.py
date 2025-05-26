from django.urls import path, include
from accounts.views import registerView, loginView

urlpatterns = [
    path('accounts/register/', registerView.as_view(), name='Register'),
    path('accounts/login/', loginView.as_view(), name='Login'),
]
