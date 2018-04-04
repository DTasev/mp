from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.
from .serializers import ListMapSerializer, MapCreatorSerializer, SingleMapSerializer
from .models import Map


class MapViewSet(viewsets.ModelViewSet):
    serializer_class = ListMapSerializer
    queryset = Map.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        # GET tanks/maps/<int:pk> - retrieve a single map's data with all the terrain information
        if self.action == 'retrieve':
            return SingleMapSerializer
        # POST tanks/maps - create a new map with overridden create method in the serializer
        elif self.action == 'create':
            return MapCreatorSerializer

        # GET tanks/maps/ - return all maps
        return ListMapSerializer
