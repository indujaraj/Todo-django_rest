from django.urls import path
from snippets import views


urlpatterns =[
    path('todos/',views.TodosView.as_view()),
    path('todos/<int:id>',views.TodoDetailView.as_view()),
    path('accounts/signup',views.UserRegistrationView.as_view()),
    path('accounts/signin',views.LoginView.as_view()),
    path('accounts/logout',views.Logout.as_view())
]