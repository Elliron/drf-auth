from rest_framework import serializers
from .models import App_thingie

class App_thingieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at')
        model = App_thingie