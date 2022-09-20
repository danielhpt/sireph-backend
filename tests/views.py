from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response, status

from app.models import Occurrence
from .models import *


class TestsList(APIView):
    swagger_schema = None
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

    def put(self, request, test_id):
        data = request.data.copy()
        test = get_object_or_404(Test, id=test_id)
        if "action" in data:
            test_action = TestAction.objects.create(test=test, action=data["action"])
            test_action.save()
            if data["action"] == "end test":
                test_occurrences = TestOccurrence.objects.filter(test_id=test_id)
                for test_occurrence in test_occurrences:
                    occurrence = Occurrence.objects.get(pk=test_occurrence.occurrence_id)
                    if occurrence.active:
                        occurrence.active = False
                        occurrence.save()
                    team = occurrence.team
                    if team.active:
                        team.active = False
                        team.save()
                        for t in team.team_technicians.reverse():
                            if t.active:
                                t.active = False
                                t.save()
        if "occurrence_id" in data:
            test_occurrence = TestOccurrence.objects.create(test=test, occurrence_id=data["occurrence_id"])
            test_occurrence.save()
        return Response(status=status.HTTP_200_OK)
