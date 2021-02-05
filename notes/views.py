from notes.models import Notes, SharedNotes
from notes.serializers import NotesSerializer, SharedNotesSerializer
from rest_framework import generics
from rest_framework import permissions,authentication
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
        'notes': reverse('note-list', request=request, format=format),
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
    authentication_classes = [authentication.TokenAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['POST'])
def shared_notes(request,note_id,viewer_id):
    try:
        note = Notes.objects.get(pk=note_id)
    except note.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        viewer = User.objects.get(pk=viewer_id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    duplicate=SharedNotes.objects.filter(notes=note,viewer=viewer)
    print("hello",duplicate)
    if request.method=='POST':
        
        SharedNotes.objects.create(notes=note, viewer=viewer)
        # return Response(status=status.HTTP_201_CREATED)

    #  serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    # shared_note= SharedNotes.objects.create(notes=note, viewer=viewer)
    


