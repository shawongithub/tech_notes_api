from django.contrib.auth.models import User
from rest_framework import serializers
from notes.models import Notes, SharedNotes




class NotesSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Notes
        fields = ['id', 'title', 'body','shared','publish_date','author']


class SharedNotesSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Notes.objects.all())
    viewer=serializers.ReadOnlyField(source='viewer.username')
    class Meta:
        model = SharedNotes
        fields = ['id', 'notes', 'viewer']

# class UserSerializer(serializers.ModelSerializer):
#     notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Notes.objects.all())

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'notes']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.HyperlinkedRelatedField(many=True, view_name='note-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'notes']

