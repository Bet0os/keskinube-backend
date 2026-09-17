from django.urls import path
from .views import BusinessCreateView

urlpatterns = [
    path('', BusinessCreateView.as_view(), name='business-create'),
]