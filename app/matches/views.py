from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from matches.models import Match
from matches.serializer import MatchSerializer
from rest_framework.decorators import api_view


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'matches/index.html'

    def get(self, request):
        queryset = Match.objects.all()
        return Response({'matches': queryset})

class individual_match(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'matches/individual_match.html'

    def get(self, request, id):
        queryset = Match.objects.filter(id=id)
        return Response({'matches': queryset})

@api_view(['GET', 'POST', 'DELETE'])
def matches_list(request):
    if request.method == 'GET':
        matches = Match.objects.all()
        matches_serializer = MatchSerializer(matches, many=True)
        return JsonResponse(matches_serializer.data, safe=False)
    
    elif request.method == 'POST':
        match_data = JSONParser().parse(request)
        match_serializer = MatchSerializer(data=match_data)
        if match_serializer.is_valid():
            match_serializer.save()
            return JsonResponse(match_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(match_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Match.objects.all().delete()
        return JsonResponse(
            {
                'message': f'{count[0]} matches were deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )

@api_view(['GET', 'DELETE', 'PATCH'])
def individual_match_api(request, id):
    try:
        match = Match.objects.get(pk=id)
    except Match.DoesNotExist:
        return JsonResponse({'message': 'The match does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        match_serializer = MatchSerializer(match)
        return JsonResponse(match_serializer.data)
    
    elif request.method == 'PUT':
        match_data = JSONParser().parse(request)
        match_serializer = MatchSerializer(match, data=match_data)
        if match_serializer.is_valid():
            match_serializer.save()
            return JsonResponse(match_serializer.data)
        return JsonResponse(match_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        match.delete()
        return JsonResponse({'message': 'Match was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)