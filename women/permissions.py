from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
        методы:
            has_permission - позволяет настраивать прова доступа на уровне всего запроса от клиента;
            has_object_permission - позволяет настраивать прова доступа на уровне одного объекта, или данных;

        SAFE_METHODS - запросы только для чтения данных;
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешение на уровне объекта, чтобы разрешить его редактирование только владельцам объекта.
    Предполагается, что экземпляр модели имеет атрибут «владелец».
    """

    def has_object_permission(self, request, view, obj):
        # Разрешения на чтение предоставляются для любого запроса,
        # поэтому мы всегда разрешаем запросы GET, HEAD или OPTIONS.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Экземпляр должен иметь атрибут с именем «пользователь».
        return obj.user == request.user
