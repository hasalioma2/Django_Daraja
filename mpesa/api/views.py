
from rest_framework.generics import CreateAPIView
# from rest_framework.permissions import IsAdminUser


from mpesa.api.serializers import LNMOnlineSerializer
from mpesa.models import LNMOnline

class LNMOCallbackApiView(CreateAPIView):
    queryset = LNMOnline.objects.all()
    serializer_class = LNMOnlineSerializer
    # permission_classes = [IsAdminUser]

    def create(self, request):
        print (request.data, "This is our data")