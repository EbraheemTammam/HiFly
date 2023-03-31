from django.urls import path

from .views import (
    login_api_view,
    logout_api_view,
    user_list_api_view,
    user_detail_api_view,
)

app_name = 'accounts'

urlpatterns = [
    path('', user_list_api_view),
    path('<int:pk>/', user_detail_api_view),
    path('login/', login_api_view),
    path('logout/', logout_api_view),
]