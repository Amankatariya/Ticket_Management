from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class TicketSerializer(serializers.ModelSerializer):
    reporter_name = serializers.CharField(source='reporter.name', read_only=True)
    assignee_name = serializers.CharField(source='assignee.name', read_only=True)
    sprint = serializers.CharField(source='sprint.sprint_name', read_only=True)

    class Meta:
        model = Ticket
        fields = '__all__'


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = '__all__'

class MemberSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source='user.name', read_only=True)    
    class Meta:
        model = Member
        fields = ['member_name']
