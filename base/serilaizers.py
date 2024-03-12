from rest_framework.serializers import ModelSerializer
from base.models import Advocate

class AdvocateSerializers(ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__' 