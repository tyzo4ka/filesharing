from django.urls import path
from webapp.views import IndexView, FileView, FileCreate, FileUpdate, FileDelete
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('file/<int:pk>/', FileView.as_view(), name="file_detail"),
    path('file/create/', FileCreate.as_view(), name="file_create"),
    path('file/<int:pk>/update/', FileUpdate.as_view(), name="file_update"),
    path('file/<int:pk>/delete/', FileDelete.as_view(), name="file_delete"),
]