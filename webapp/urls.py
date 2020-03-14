from django.urls import path
from webapp.views import IndexView, FileView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('file/<int:pk>/', FileView.as_view(), name="file_detail")
    # path('ad/photo/create/', PhotoCreateView.as_view(), name='photo_create')
    # path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout')
]