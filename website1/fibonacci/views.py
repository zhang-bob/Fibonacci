from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from fibonacci.models import Fibonacci
from fibonacci.serializers import FibonacciSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from fibonacci.fibonacciArray import FibonacciArray

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def fibonacci_show(request, number=None, format=None):
    """
    List a number of fibonacci
    """
    fibonacci_instance = FibonacciArray()
    if request.method == 'GET':
        #(status, message) = fibonacci_instance.generate_fibonacci_string(number)
        (status, message) = fibonacci_instance.generate_fibonacci_string(number)
        if status == 0:
            return JSONResponse({'Fibonacci string is': message})
        else:
            return JSONResponse({'Error':message})
