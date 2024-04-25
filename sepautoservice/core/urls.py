from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from .views import (
    user_login,
    
    CalendarView,
    DayView,
    event,
    generate_pdf,
    delete
)
app_name = 'core'

urlpatterns = [
    # post views
    #path('', index, name='index'),
    #path('', user_login, name='login'),
    
    path('accounts/profile/', CalendarView.as_view(), name='calendar'),
    path('event/new/', event, name='event_new'),
    path('event/delete/<int:event_id>/', delete, name='delete'),
    path('', auth_views.LoginView.as_view(template_name="registration/login.html")),
    
    path('event/edit/<int:event_id>/', event, name='event_edit'),
    path('generate_pdf/<int:day>/<int:month>/<int:year>', generate_pdf, name='generate_pdf'),
    #path('day/edit/<day><month><year>/', date_edit, name='date_edit'),
    path('day/edit/<int:day>/<int:month>/<int:year>', DayView.as_view(), name='day'),
]


