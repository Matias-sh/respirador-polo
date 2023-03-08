from rest_framework import serializers
from .models import Personas

class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Personas

        fields = ('__all__')

        

