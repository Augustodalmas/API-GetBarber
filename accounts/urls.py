from django.urls import path, include
from accounts.views import registerView, loginView, logoutView, perfilView, employeeView, employeeUpdateView

urlpatterns = [
    path('accounts/register/', registerView.as_view(), name='Register'),
    path('accounts/login/', loginView.as_view(), name='Login'),
    path('accounts/logout/', logoutView.as_view(), name='Logout'),
    path('accounts/perfil/', perfilView.as_view(), name='Perfil'),
    path('accounts/employee/', employeeView.as_view(), name='employee'),
    path('accounts/employee/<int:pk>/',
         employeeUpdateView.as_view(), name='employee_update'),
]
