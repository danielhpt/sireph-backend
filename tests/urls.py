from django.urls import path

from .views import *

urlpatterns = [
    path('', TestsList.as_view(), name="create_test"),
    path('<int:test_id>/', TestDetail.as_view(), name="update_test"),
]
