from rest_framework.generics import ListAPIView

from .serializers import CustomerSerializer
from .models import Customer

class CustomerApi(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer