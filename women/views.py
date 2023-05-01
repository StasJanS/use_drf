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
        return Response({'posts': WomenSerializer(all_w, many=True).data})

    def post(self, request):

        # валидация
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': "Метод PUT невозможен!!!"})

        try:
            ins_tance = Women.objects.get(pk=pk)
        except:
            return Response({'error': "Объект ненайден!!!"})

        serializer = WomenSerializer(data=request.data, instance=ins_tance)
        # TODO есть пояснение
        """ где:
            request.data - данные, которые нужно внести
            ins_tance - тот объект, который мы будем менять
            Метод save() (ниже) автоматически вызовет метод update()
        """
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    # def delete(self, request):
    #     Women.objects.get(id=request.data["person_id"]).delete()
    #     return Response({'del': f'Удалена запись №{request.data["person_id"]}'})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({'error': "Метод DELETE невозможен!!!"})

        try:
            ins_tance = Women.objects.get(pk=pk)
        except:
            return Response({'error': "Объект ненайден!!!"})

        ins_tance.delete()
        return Response({'post': f'Удалена запись №{pk}!!!'})
