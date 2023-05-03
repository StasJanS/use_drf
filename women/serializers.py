from rest_framework import serializers

from women.models import Women


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # автоматически связывает новую запись в БД с пользователем, который её добавил

    class Meta:
        model = Women
        fields = '__all__'
