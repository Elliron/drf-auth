from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import App_thingieSerializer
from .models import App_thingie

class App_thingieList(ListCreateAPIView):
    queryset = App_thingie.objects.all()
    serializer_class = App_thingieSerializer

class App_thingieDetail(RetrieveUpdateDestroyAPIView):
    queryset = App_thingie.objects.all()
    serializer_class = App_thingieSerializer