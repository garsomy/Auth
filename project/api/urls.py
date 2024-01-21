from django.urls import path
from .views import MessageList, MessageUpdate, MessageDestroy, Register, Login, Logout


urlpatterns = [
    path('', MessageList.as_view()),
    path('update/<int:pk>', MessageUpdate.as_view()),
    path('delete/<int:pk>', MessageDestroy.as_view()),
    path('reg/', Register.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view())
]