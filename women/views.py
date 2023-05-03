from django.forms import model_to_dict
from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from women.models import Women, Category
from women.serializers import WomenSerializer


# class WomenAPIList(generics.ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIUpdate(generics.UpdateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
#
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return self.queryset[:3]
        return self.queryset.filter(pk=pk)

    """
        Создаётся свой собственный метод, с настройками;
        Также добавляется автоматически новый url список routers.urls;
    """
    # для всех записей
    @action(methods=['get'], detail=False)
    def category(self, request):
        cats = Category.objects.all()
        return Response({'cats': [i.name for i in cats]})

    # для одной любой записи по pk
    @action(methods=['get'], detail=True)
    def category_detail(self, request, pk):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})
