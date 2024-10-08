from django.db import models
from .constants import *

class AbstractTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractTime):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Sprint(AbstractTime):
    title = models.CharField(max_length=100, unique=True)  
    duration_days = models.PositiveIntegerField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Ticket(AbstractTime):
    title = models.CharField(max_length=100)
    description = models.TextField()  
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_tickets') 
    assignee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tickets')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default=StatusChoice.CREATED.value)
    story_points = models.CharField(max_length=50) 
    sprint = models.ManyToManyField(Sprint, related_name='tickets', blank=True)

    def __str__(self):
        return self.title


class Member(AbstractTime):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member')

    def __str__(self):
        return self.user.name


# class TicketHistory(models.Model):
#     member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='ticket_histories')
#     ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='history_records')

#     def __str__(self):
#         return f"{self.member.name} - {self.ticket.title}"
