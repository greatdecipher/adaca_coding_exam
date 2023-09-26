from datetime import datetime
from django.http import HttpResponse


class ResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = datetime.now()
        response = self.get_response(request)
        end_time = datetime.now()
        
        time_taken = end_time - start_time
        response['X-Time-Taken'] = str(time_taken)
        return response