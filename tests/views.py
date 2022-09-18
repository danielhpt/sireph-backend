from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, status

from .models import *


class TestsList(APIView):
    swagger_schema = None
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data.copy()
        test = Test.objects.create(type=data["type"])
        test.save()
        if "action" in data:
            test_action = TestAction.objects.create(test=test, action=data["action"])
            test_action.save()
        if "occurrence_id" in data:
            test_occurrence = TestOccurrence.objects.create(test=test, occurrence_id=data["occurrence_id"])
            test_occurrence.save()
        response = {
            "test_id": test.id
        }
        return Response(data=response, status=status.HTTP_201_CREATED)


class TestDetail(APIView):
    swagger_schema = None
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, test_id):
        data = request.data.copy()
        test = get_object_or_404(Test, id=test_id)
        if "action" in data:
            test_action = TestAction.objects.create(test=test, action=data["action"])
            test_action.save()
        if "occurrence_id" in data:
            test_occurrence = TestOccurrence.objects.create(test=test, occurrence_id=data["occurrence_id"])
            test_occurrence.save()
        return Response(status=status.HTTP_200_OK)
