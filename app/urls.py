from django.urls import path,include
from .views import *

urlpatterns = [
    path('member/',MemberAPIView.as_view()),
    path('ticket/',TicketAPIView.as_view(), name='ticket-list'),
    path('ticket/<pk>/',TicketAPIView.as_view(), name='ticket-detail'),
]