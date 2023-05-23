# Django imports
from django.http import HttpResponse, JsonResponse
# DRF imports
from rest_framework.decorators import api_view, permission_classes
# python default imports
import json
from home.models import College
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def get_colleges(request):
    query = request.GET.get('query')

    if query == 'USA' or query == 'INDIA':
        colleges = College.objects.filter(country=query)
    elif query:
        print(query)
        colleges = College.objects.filter(name__icontains=query)
    else:
        colleges = College.objects.all()
    res = {
        "colleges": list(colleges.values())
    }
    return JsonResponse(res, status=200)


@api_view(['GET'])
def by_name(request, name):
    college = College.objects.get(name=name)
    res = college.to_dict()
    return JsonResponse(res, status=200)
