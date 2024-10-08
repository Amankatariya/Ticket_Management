from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import *
from .models import *

class MemberAPIView(APIView):
    def get(self, request):
        obj = Member.objects.all()
        serializer = MemberSerializer(obj, many=True)
        return Response({'data': serializer.data},status=status.HTTP_200_OK)

class TicketAPIView(APIView):
    def get(self, request):
        obj = Ticket.objects.all()
        serializer = TicketSerializer(obj, many=True)
        return Response({'data': serializer.data})
    
    def post(self, request):
        data = request.data
        serializer = TicketSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'SUCCESS': 'YOUR DATA IS SAVED..'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            ticket = Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            return Response({'ERROR': 'Ticket not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TicketSerializer(ticket, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'SUCCESS': 'Ticket updated successfully.'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            ticket = Ticket.objects.get(pk=pk)
            ticket.delete()
            return Response({'SUCCESS': 'Ticket deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
        except Ticket.DoesNotExist:
            return Response({'ERROR': 'Ticket not found.'}, status=status.HTTP_404_NOT_FOUND)