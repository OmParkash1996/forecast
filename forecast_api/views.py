from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import json
from urllib.request import urlopen
from forecast_api.models import Forecast
from forecast_api.serializer import UserSerializer
from django.utils import timezone
from datetime import timedelta
from django.conf import settings

class GetForecastAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        current_time = timezone.now()
        span_5 = current_time - timedelta(minutes = 5)
        if Forecast.objects.filter(user=request.user,requested_on__gte=span_5,requested_on__lte=current_time).count() < 3:
            api_key = settings.API_KEY
            response = urlopen('https://ipinfo.io/')
            data = json.load(response)
            data=data['loc'].split(',')
            lat,long=data[0],data[-1]
            forecast_response = urlopen('https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=hourly,minutely&appid={}'.format(lat,long,api_key))
            forecast_response = json.load(forecast_response)
            forecast_obj = Forecast.objects.create(user=request.user,forecast=forecast_response)
            return Response(forecast_response)
        else:
            return Response({'error': 'User can access forecasting 3 times in span of 5 minutes', 'error_code': 'E001'}, status=400)

class CreateUser(APIView):
    def post(self, request):
        try:
            serialized = UserSerializer(data = request.data)
            if serialized.is_valid():
                user_obj = serialized.save()
                return Response({'error': '', 'error_code': '', 'data': {'id':user_obj.id}}, status=200)
            else:
                error = ', '.join(['{0}:{1}'.format(k, str(v[0])) for k, v in serialized.errors.items()])
                return Response({'error': error, 'error_code': 'HS002', 'data': {}}, status=200)
        except Exception as error:
            return Response({'error': repr(error), 'error_code': 'H007', 'matched': 'N', 'data': {}}, status=400)
