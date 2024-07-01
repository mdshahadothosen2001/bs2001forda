from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from user.models import Doctor
from ..serializers.doctor import DoctorListSerializer


class DoctorListView(APIView):
    permission_classes = [AllowAny]

    def validate_parameter(self, id):
        if id:
            return True
        else:
            return False
    
    def get(self, request):
        id = request.query_params.get("id")
        doctors = Doctor.objects.values()
        if self.validate_parameter(id) is True:
            doctors = doctors.filter(specialization=id)
        serializer = DoctorListSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
