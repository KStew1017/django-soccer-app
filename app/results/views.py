from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from results.models import Result
from results.serializer import ResultSerializer
from rest_framework.decorators import api_view


def index(request):
    print("Here")
    queryset = Result.objects.all()
    return render(request, 'results/index.html', {'results': queryset})

class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'results/index.html'

    def get(self, request):
        queryset = Result.objects.all()
        return Response({'results': queryset})

class list_all_results(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'results/result_list.html'

    def get(self, request):
        queryset = Result.objects.all()
        return Response({'results': queryset})

# Create your views here.
@api_view(['GET', 'POST', 'DELETE'])
def results_list(request):
    if request.method == 'GET':
        results = Result.objects.all()
        result_serializer = ResultSerializer(results, many=True)
        return JsonResponse(result_serializer.data, safe=False)
    
    elif request.method == 'POST':
        result_data = JSONParser().parse(request)
        result_serializer = ResultSerializer(data=result_data)
        if result_serializer.is_valid():
            result_serializer.save()
            return JsonResponse(result_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(result_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Result.objects.all().delete()
        return JsonResponse(
            {
                'message': f'{count[0]} results were deleted successfully'
            },
            status=status.HTTP_204_NO_CONTENT
        )

@api_view(['GET', 'DELETE', 'PATCH'])
def individual_result(request, id):
    try:
        result = Result.objects.get(pk=id)
    except Result.DoesNotExist:
        return JsonResponse({'message': 'The result does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        result_serializer = ResultSerializer(result)
        return JsonResponse(result_serializer.data)
    
    elif request.method == 'PATCH':
        result_data = JSONParser().parse(request)
        result_serializer = ResultSerializer(result, data=result_data)
        if result_serializer.is_valid():
            result_serializer.save()
            return JsonResponse(result_serializer.data)
        return JsonResponse(result_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        result.delete()
        return JsonResponse({'message': 'result was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)