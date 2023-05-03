from rest_framework import routers


# Свой собственный class routers
class MyCustomRouter(routers.SimpleRouter):
    """
        routes - список маршрутов;
        Route - класс роутеров;
        url - шаблон маршрута;
        mapping - связывает тип запроса с соответствующим методом ViewSet;
        name - название маршрута;
        detail - определяет список или отдельная запись;
        initkwargs - доп.аргументы для kwargs, которые передаются конкретному определению при срабатывании маршрута;
    """
    routes = [
        routers.Route(
            url=r'^{prefix}/$',
            mapping={'get': 'list'},
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        ),
        routers.Route(
            url=r'^{prefix}/{lookup}/$',
            mapping={'get': 'retrieve'},
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix': 'Detail'}
        )
    ]
