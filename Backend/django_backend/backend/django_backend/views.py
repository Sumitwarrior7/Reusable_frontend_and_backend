from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from . import models
from . import serializers


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetNotes(request):
    user = request.user
    notes = user.note_set.all()
    # notes = models.Note.objects.all()
    serializer = serializers.NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def GetNote(request, note_id):
    try:
        note = models.Note.objects.get(id=note_id)
    except ObjectDoesNotExist:
        error_message = "Note not found"
        return JsonResponse({'error': error_message}, status=404)
    else:
        serializer = serializers.NoteSerializer(note)
        return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def CreateNote(request):
    data = request.data
    print(data)
    print("User :", request.user)
    created_note = models.Note.objects.create(user=request.user, body=data["body"])
    serializer = serializers.NoteSerializer(created_note, many=False)
    return Response(serializer.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def UpdateNote(request, note_id):
    try:
        note = models.Note.objects.get(id=note_id)
        print("Note, i want to edit", note)
    except ObjectDoesNotExist:
        error_message = "Note not found"
        return JsonResponse({'error': error_message}, status=404)
    else:
        new_data = request.data
        print("Updated data :", new_data)
        # Here in serializer, first argument is a model instance, and second argument is a dictionary <{body:"updated body value"}> we are getting from frontend
        serializer = serializers.NoteSerializer(instance=note, data=new_data)
        print("Serializer :", serializer)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def DeleteNote(request, note_id):
    note = models.Note.objects.get(id=note_id)
    print(note)
    note.delete()
    return Response("Note was deleted")