import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from women.models import Women


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

# # кодирование и декотирование данных, которые представляются в виде json-формата
#
# def encode():
#     model = WomenModel('Stas', 'Content: Super Class')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Stas","content":"Content: Super Class"}')
#     new_data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=new_data)
#     serializer.is_valid()
#     print(serializer.validated_data)