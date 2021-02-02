from notes.models import Notes, SharedNotes
from notes.serializers import NotesSerializer, SharedNotesSerializer
from rest_framework import generics
from rest_framework import permissions
from notes.serializers import UserSerializer
from django.contrib.auth.models import User
from notes.permissions import IsOwnerOrReadOnly

#for relations and hyperlinked api
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'notes': reverse('note-list', request=request, format=format)
    })



class NoteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    #perform_create is a default function
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer