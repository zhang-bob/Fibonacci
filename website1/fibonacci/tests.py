from django.test import TestCase

# Create your tests here.
from fibonacci.models import Fibonacci
from fibonacci.serializers import FibonacciSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO

fibonacci_instance = Fibonacci(code='foo = "bar"\n')
fibonacci_instance.save()

fibonacci_instance = Fibonacci(code='print "hello, Bob"\n')
fibonacci_instance.save()

serializer = FibonacciSerializer(fibonacci_instance)
serializer.data

content = JSONRenderer().render(serializer.data)
content


#deserialize
stream = BytesIO(content)
data = JSONParser().parse(stream)

serializer = Fibonacci(data=data)
serializer.is_valid()
# True
serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print "hello, world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save()
# <Snippet: Snippet object>
