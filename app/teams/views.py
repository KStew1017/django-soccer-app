from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from teams.models import Team
from teams.serializer import TeamSerializer
from rest_framework.decorators import api_view


def index(request):
    print("Here")
    queryset = Team.objects.all()
    return render(request, 'teams/index.html', {'teams': queryset})

class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'teams/index.html'

    def get(self, request):
        queryset = Team.objects.all()
        return Response({'teams': queryset})

class list_all_teams(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'teams/team_list.html'

    def get(self, request):
        queryset = Team.objects.all()
        return Response({'teams': queryset})

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def teams_list(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        team_serializer = TeamSerializer(teams, many=True)
        return JsonResponse(team_serializer.data, safe=False)
    
    elif request.method == 'POST':
        team_data = JSONParser().parse(request)
        team_serializer = TeamSerializer(data=team_data)
        if team_serializer.is_valid():
            team_serializer.save()
            return JsonResponse(team_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Team.objects.all().delete()
        return JsonResponse(
            {
                'message': f'{count[0]} Teams were deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )

@api_view(['GET', 'DELETE', 'POST', 'PATCH'])
def individual_team(request, id):
    try:
        team = Team.objects.get(pk=id)
    except Team.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        team_serializer = TeamSerializer(team)
        return JsonResponse(team_serializer.data)
    
    elif request.method == 'PUT':
        team_data = JSONParser().parse(request)
        team_serializer = TeamSerializer(team, data=team_data)
        if team_serializer.is_valid():
            team_serializer.save()
            return JsonResponse(team_serializer.data)
        return JsonResponse(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        team.delete()
        return JsonResponse({'message': 'Team was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)