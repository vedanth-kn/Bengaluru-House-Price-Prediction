# views.py in prediction app

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . import util

def index(request):
    return render(request, 'prediction/app.html')

def get_location_names(request):
    locations = util.get_location_names()
    return JsonResponse({'locations': locations})

@csrf_exempt
def predict_home_price(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total_sqft = float(data['total_sqft'])
        location = data['location']
        bhk = int(data['bhk'])
        bath = int(data['bath'])

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        return JsonResponse({'estimated_price': estimated_price})

    return JsonResponse({'error': 'Invalid HTTP method'}, status=400)
