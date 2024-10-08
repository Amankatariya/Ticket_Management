from django.contrib import admin
from .models import User, Sprint, Ticket, Member

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'email']

@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration_days', 'start_date' ,'end_date']

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'reporter', 'assignee',
        'start_date', 'end_date', 'status', 'story_points'
    ]
    list_filter = ['status', 'sprint']
    search_fields = ['title', 'description']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['user']

