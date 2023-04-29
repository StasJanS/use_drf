from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women
from women.serializers import WomenSerializer


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

class WomenAPIView(APIView):

    def get(self, request):
        all_w = Women.objects.all().values()
        return Response({'posts': list(all_w)})

    def post(self, request):
        post_new = Women.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            cat_id=request.data["cat_id"]
        )
        return Response({'post': model_to_dict(post_new)})

    def delete(self, request):
        Women.objects.get(id=request.data["person_id"]).delete()
        return Response({'del': f'Удалена запись №{request.data["person_id"]}'})
