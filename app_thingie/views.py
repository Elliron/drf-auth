from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import App_thingieSerializer
from .models import App_thingie
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class App_thingieList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly)
    queryset = App_thingie.objects.all()
    serializer_class = App_thingieSerializer

class App_thingieDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = App_thingie.objects.all()
    serializer_class = App_thingieSerializer