from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from . import models
from . import serializers
from . import api



@api_view(["POST"])
def GetResponse(request):
    data_dict = request.data
    print(data_dict)
    # res = api.openai_func(data_dict)
    return Response(data_dict["name"])



@api_view(["GET"])
def GetNote(request, note_id):
    try:
        note = models.Note.objects.get(id=note_id)
    except ObjectDoesNotExist:
        error_message = "Note not found"
        return JsonResponse({'error': error_message}, status=404)
    else:
        serializer = serializers.NoteSerializer(note)
        return Response(serializer.data)




@api_view(["PUT"])
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






