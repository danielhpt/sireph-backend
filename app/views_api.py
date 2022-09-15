import coreapi
import coreschema
from django.contrib.auth import logout, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User as User_Auth
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.schemas import ManualSchema
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.views import APIView, Response, status
from drf_yasg.utils import swagger_auto_schema

from .serializers import *


class Login(APIView):
    """User Login"""
    permission_classes = [AllowAny]

    login_schema = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING),
            'password': openapi.Schema(type=openapi.TYPE_STRING),
        },
        required=['username', 'password']
    )
    login_schema_response = {
        status.HTTP_200_OK: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'token': openapi.Schema(type=openapi.TYPE_STRING),
                "user": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'username': openapi.Schema(type=openapi.TYPE_STRING),
                        'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                        'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                        'email': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                ),
                "is_technician": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                "is_dispatcher": openapi.Schema(type=openapi.TYPE_BOOLEAN),
                "is_hospitalstaff": openapi.Schema(type=openapi.TYPE_BOOLEAN)
            }
        )
    }

    @swagger_auto_schema(request_body=login_schema, responses=login_schema_response)
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = get_object_or_404(User, username=username)
        if not check_password(password, user.password):
            return Response(status=status.HTTP_400_BAD_REQUEST)  # return ValidationError()
        else:
            login(request, user)
            token = Token.objects.get_or_create(user=user)[0].key
            if user.is_superuser:
                is_technician = True
                is_dispatcher = True
                is_hospitalstaff = True
            else:
                try:
                    Technician.objects.get(technician=user)
                    is_technician = True
                except Technician.DoesNotExist:
                    is_technician = False
                try:
                    Dispatcher.objects.get(dispatcher=user)
                    is_dispatcher = True
                except Dispatcher.DoesNotExist:
                    is_dispatcher = False
                try:
                    HospitalStaff.objects.get(employee=user)
                    is_hospitalstaff = True
                except HospitalStaff.DoesNotExist:
                    is_hospitalstaff = False
            data = {
                "token": token,
                "user": UserSimplifiedSerializer(user).data,
                "is_technician": is_technician,
                "is_dispatcher": is_dispatcher,
                "is_hospitalstaff": is_hospitalstaff
            }
            return Response(status=status.HTTP_200_OK, data=data)


class Logout(APIView):
    """User Logout"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):  # todo sem swagger?
        try:
            request.user.auth_token.delete()
        except User_Auth.auth_token.RelatedObjectDoesNotExist:
            pass
        logout(request)
        return Response(status=status.HTTP_200_OK)


# done
class UserDetailByToken(APIView):
    """List the details of an User"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: UserSimplifiedSerializer()})
    def get(self, request):  # working
        serializer = UserSimplifiedSerializer(request.user)

        return Response(serializer.data)


class TechnicianDetailByToken(APIView):
    """List the details of a Technician"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: TechnicianDetailSerializer()})
    def get(self, request):  # working
        try:
            technician = Technician.objects.get(technician=request.user, active=True)
        except Technician.DoesNotExist:
            return HttpResponseNotFound()
        serializer = TechnicianDetailSerializer(technician)

        return Response(serializer.data)


# done
class UserInactive(APIView):
    """List the details of an User"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: UserSimplifiedSerializer(many=True)})
    def get(self, request, user_id):  # working
        user = get_object_or_404(User, pk=user_id)
        actives = TeamTechnician.objects.filter(technician=user, active=True)

        if len(actives) > 0:
            return HttpResponseNotFound()

        serializer = UserSimplifiedSerializer(user)

        return Response(serializer.data)


# done
class UserList(APIView):
    """List all Users"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: UserSimplifiedSerializer(many=True)})
    def get(self, request):  # working
        users = User.objects.all()
        serializer = UserSimplifiedSerializer(users, many=True)

        return Response(serializer.data)


# done
# class UserDetail(APIView):
# """List the details of an User"""
#  authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
#   permission_classes = [IsAuthenticated]
#    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

# @swagger_auto_schema(manual_parameters=[auth], responses={200: UserSimplifiedSerializer(many=True)})
# def get(self, request, user_id):  # working
#     user = get_object_or_404(User, pk=user_id)
#      serializer = UserSimplifiedSerializer(user)

#       return Response(serializer.data)


# done
class UserTeamList(APIView):  # todo Existem 2 funções de get user
    """List the teams of an User"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: TeamSerializer(many=False)})
    def get(self, request, user_id):  # working
        user = get_object_or_404(User, pk=user_id)
        teams = Team.objects.filter(team_technicians__technician=user)
        serializer = TeamSerializer(teams, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=TeamSerializer)
    def post(self, request, user_id):  # working todo maybe
        serializer = TeamSerializer(data=request.data.copy())

        if serializer.is_valid():
            serializer.save()
            result = TeamSerializer(Team.objects.get(pk=serializer.instance.id))
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserActiveOccurrence(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     @swagger_auto_schema(responses={200: OccurrenceSerializer(many=True)})
#     def get(self, request, user_id):  # working
#         user = get_object_or_404(User, pk=user_id)
#         occurrences = Occurrence.objects.filter(team__team_technicians__technician=user, active=True)
#
#         if len(occurrences) > 0:
#             serializer = OccurrenceSerializer(occurrences[0])
#             return Response(serializer.data)
#
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def put(self, request, user_id):
#         user = get_object_or_404(User, pk=user_id)
#         occurrences = Occurrence.objects.filter(team__team_technicians__technician=user, active=True)
#
#         if len(occurrences) > 0:
#             occurrences[0].active = False
#             occurrences[0].save()
#             return Response(status=status.HTTP_200_OK)
#
#         return Response(status=status.HTTP_400_BAD_REQUEST)


class TechnicianActiveOccurrence(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: OccurrenceAllDetailsSerializer(many=False)})
    def get(self, request, technician_id):  # working
        technician = get_object_or_404(Technician, pk=technician_id)
        occurrences = Occurrence.objects.filter(team__team_technicians__technician=technician, active=True)

        if len(occurrences) > 0:
            serializer = OccurrenceAllDetailsSerializer(occurrences[0])
            return Response(serializer.data)

        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(manual_parameters=[auth], request_body=OccurrenceAllDetailsSerializer)
    def put(self, request, technician_id):
        technician = get_object_or_404(Technician, pk=technician_id)
        data = request.data.copy()
        occurrence = get_object_or_404(Occurrence, pk=data.get("id"))
        occurrences = Occurrence.objects.filter(team__team_technicians__technician=technician, active=True)
        if len(occurrences) > 0:
            for o in occurrences:
                if o.id == occurrence.id:
                    serializer = OccurrenceAllDetailsSerializer(occurrence, data=data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


# done
# class UserOccurrenceList(APIView):
#     """List the occurrences of an User"""
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     @swagger_auto_schema(responses={200: OccurrenceSerializer(many=True)})
#     def get(self, request, user_id):  # working
#         user = get_object_or_404(User, pk=user_id)
#         occurrences = Occurrence.objects.filter(team__team_technicians__technician=user)
#         serializer = OccurrenceSerializer(occurrences, many=True)
#
#         return Response(serializer.data)


class TechnicianOccurrenceList(APIView):
    """List the occurrences of an Technician"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: OccurrenceAllDetailsSerializer(many=True)})
    def get(self, request, technician_id):
        technician = get_object_or_404(Technician, pk=technician_id)
        occurrences = Occurrence.objects.filter(team__team_technicians__technician=technician)
        serializer = OccurrenceAllDetailsSerializer(occurrences, many=True)

        return Response(serializer.data)


# done
class TeamList(APIView):
    """List all Teams"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]  # Alteração
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: TeamSerializer(many=True)})
    def get(self, request):  # working
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[auth], request_body=TeamSerializer)
    def post(self, request):  # working
        serializer = TeamSerializer(data=request.data.copy())

        if serializer.is_valid():
            serializer.save()
            result = TeamSerializer(Team.objects.get(pk=serializer.instance.id))
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# done
class TeamDetail(APIView):
    """List the details of a Team"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: TeamSerializer(many=False)})
    def get(self, request, team_id):  # working
        team = get_object_or_404(Team, pk=team_id)
        serializer = TeamSerializer(team)

        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[auth], request_body=TeamSerializer)
    def put(self, request, team_id):  # working
        team = get_object_or_404(Team, pk=team_id)
        data = request.data.copy()
        serializer = TeamSerializer(team, data=data)

        if serializer.is_valid():
            serializer.save()
            result = TeamSerializer(Team.objects.get(pk=serializer.instance.id))
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# done
class TeamOccurrencesList(APIView):
    """List all Occurrences for a specific Team"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: OccurrenceSerializer(many=True)})
    def get(self, request, team_id):  # working
        team = get_object_or_404(Team, pk=team_id)
        occurrence = Occurrence.objects.filter(team=team)
        serializer = OccurrenceSerializer(occurrence, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[auth], request_body=OccurrenceSerializer)
    def post(self, request, team_id):  # working
        team = get_object_or_404(Team, pk=team_id)

        data = request.data.copy()
        data['team'] = team

        serializer = OccurrenceSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            result = OccurrenceSerializer(serializer.instance)
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserTeamActive(APIView):
#     """List the active Team of an User"""
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     @swagger_auto_schema(responses={200: TeamSerializer(many=True)})
#     def get(self, request, user_id):  # working
#         user = get_object_or_404(User, pk=user_id)
#         teams = Team.objects.filter(team_technicians__technician=user, team_technicians__active=True)
#
#         if len(teams) != 0:
#             team = teams[0]
#             serializer = TeamSerializer(team)
#
#             return Response(serializer.data)
#
#         return HttpResponseNotFound()


class TechnicianTeamActive(APIView):
    """List the active Team of a Technician"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: TeamSerializer(many=False)})
    def get(self, request, technician_id):  # working
        technician = get_object_or_404(Technician, pk=technician_id)
        teams = Team.objects.filter(team_technicians__technician=technician, team_technicians__active=True, active=True)

        if len(teams) != 0:
            team = teams[0]
            serializer = TeamSerializer(team)

            return Response(serializer.data)

        return HttpResponseNotFound()


# done
class OccurrenceList(APIView):
    """List all Occurrences"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: OccurrenceSerializer(many=True)})
    def get(self, request):  # working
        occurrences = Occurrence.objects.all()
        serializer = OccurrenceSerializer(occurrences, many=True)

        return Response(serializer.data)


# done
class OccurrenceDetails(APIView):
    """List the details of an Occurrence"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: OccurrenceDetailSerializer(many=False)})
    def get(self, request, occurrence_id):  # working
        occurrence = get_object_or_404(Occurrence, pk=occurrence_id)
        serializer = OccurrenceDetailSerializer(occurrence)

        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[auth], request_body=OccurrenceDetailSerializer(many=False))
    def post(self, request, occurrence_id):  # working
        occurrence = get_object_or_404(Occurrence, pk=occurrence_id)
        data = request.data.copy()
        serializer = OccurrenceDetailSerializer(occurrence, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)


# done
class OccurrenceVictimsList(APIView):
    """List all victims of an Occurrence"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: VictimSerializer(many=True)})
    def get(self, request, occurrence_id):  # working
        occurrence = get_object_or_404(Occurrence, pk=occurrence_id)
        victims = Victim.objects.filter(occurrence=occurrence)
        serializer = VictimSerializer(victims, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[auth], request_body=VictimSerializer(many=True))
    def post(self, request, occurrence_id):  # working
        occurrence = get_object_or_404(Occurrence, pk=occurrence_id)

        data = request.data.copy()
        data['occurrence'] = occurrence.id
        if 'evaluations' in data:
            del data['evaluations']
        if 'pharmacies' in data:
            del data['pharmacies']
        serializer = VictimSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            result = VictimSerializer(serializer.instance)
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CentralOccurrencesList(APIView):
    """List all Occurrences of a Central"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: OccurrenceDetailSerializer(many=True)})
    def get(self, request, central_id):
        central = get_object_or_404(Central, pk=central_id)
        occurrences = Occurrence.objects.filter(central=central)
        serializer = OccurrenceDetailSerializer(occurrences, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[auth], request_body=OccurrenceDetailSerializer)
    def post(self, request):
        serializer = OccurrenceDetailSerializer(data=request.data.copy())

        if serializer.is_valid():
            serializer.save()
            result = OccurrenceDetailSerializer(serializer.instance)
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# done
class OccurrenceStateList(APIView):
    """List all States of an Occurrence"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: OccurrenceStateSerializer(many=True)})
    def get(self, request, occurrence_id):  # working
        occurrence = Occurrence.objects.get(pk=occurrence_id)
        occurrence_states = OccurrenceState.objects.filter(occurrence=occurrence)
        serializer = OccurrenceStateSerializer(occurrence_states, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[auth], request_body=OccurrenceStateSerializer)
    def post(self, request, occurrence_id):  # working
        occurrence = get_object_or_404(Occurrence, pk=occurrence_id)
        data = request.data.copy()
        data['occurrence'] = occurrence
        data['state'] = State.objects.get(pk=data['state']['id'])

        serializer = OccurrenceStateSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            result = OccurrenceStateSerializer(serializer.instance)
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# done

class VictimList(APIView):
    """List all Victims"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: VictimSerializer(many=True)})
    def get(self, request):  # working
        victims = Victim.objects.all()
        serializer = VictimSerializer(victims, many=True)

        return Response(serializer.data)

    # def post(self, request):
    #     serializer = VictimSerializer(data=request.data.copy())
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         result = VictimSerializer(Victim.objects.get(pk=serializer.instance.id))
    #         return Response(data=result.data,
    #                         status=status.HTTP_201_CREATED)
    #
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VictimDetails(APIView):
    """List the details of a Victim"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: VictimDetailsSerializer(many=False)})
    def get(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        serializer = VictimDetailsSerializer(victim)

        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[auth], request_body=VictimDetailsSerializer)
    def put(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        data = request.data.copy()
        serializer = VictimDetailsSerializer(victim, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# done
class VictimPharmacyList(APIView):
    """List the pharmacies of a Victim"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: PharmacySerializer(many=True)})
    def get(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        pharmacies = Pharmacy.objects.filter(victim=victim)
        serializer = PharmacySerializer(pharmacies, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[auth], request_body=PharmacyDetailSerializer)
    def post(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        data = request.data.copy()
        data['victim'] = victim
        serializer = PharmacyDetailSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            result = PharmacySerializer(serializer.instance)
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# done
class VictimPharmacyDetail(APIView):
    """List the details of a pharmacies of a Victim"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: PharmacySerializer(many=True)})
    def get(self, request, victim_id, pharmacy_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        pharmacy = get_object_or_404(Pharmacy, pk=pharmacy_id, victim=victim)
        serializer = PharmacySerializer(pharmacy)

        return Response(serializer.data)


# done
class VictimEvaluationList(APIView):
    """List the evaluations of a Victim"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: EvaluationSerializer(many=True)})
    def get(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        evaluations = Evaluation.objects.filter(victim=victim)
        serializer = EvaluationSerializer(evaluations, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(manual_parameters=[auth], request_body=EvaluationDetailSerializer)
    def post(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        data = request.data.copy()
        data['victim'] = victim
        serializer = EvaluationDetailSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            result = EvaluationSerializer(serializer.instance)
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# done
class VictimEvaluationDetail(APIView):
    """List the details of an evaluation of a Victim"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: EvaluationSerializer(many=True)})
    def get(self, request, victim_id, evaluation_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        evaluation = get_object_or_404(Evaluation, pk=evaluation_id, victim=victim)
        serializer = EvaluationSerializer(evaluation)

        return Response(serializer.data)


# done
class VictimSymptom(APIView):
    """List the Symptons of a Victim"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], request_body=SymptomDetailsSerializer)
    def post(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        data = request.data.copy()
        data['victim'] = victim.id
        serializer = SymptomSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            result = SymptomDetailsSerializer(serializer.instance)
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[auth], request_body=SymptomDetailsSerializer)
    def put(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        symptom = get_object_or_404(Symptom, pk=victim)
        data = request.data.copy()
        data['victim'] = victim.id
        serializer = SymptomSerializer(symptom, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# done
class VictimProcedureRCP(APIView):
    """List the RCP Procedures of a Victim"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], request_body=ProcedureRCPSerializer)
    def post(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        data = request.data.copy()
        data['victim'] = victim.id
        serializer = ProcedureRCPSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            result = ProcedureRCPSerializer(serializer.instance)
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[auth], request_body=ProcedureRCPSerializer)
    def put(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        procedureRCP = get_object_or_404(ProcedureRCP, pk=victim)
        data = request.data.copy()
        data['victim'] = victim.id
        serializer = ProcedureRCPSerializer(procedureRCP, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# done
class VictimProcedureVentilation(APIView):
    """List the Ventilation Procedures of a Victim"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], request_body=ProcedureVentilationSerializer)
    def post(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        data = request.data.copy()
        data['victim'] = victim.id
        serializer = ProcedureVentilationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            result = ProcedureVentilationSerializer(serializer.instance)
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[auth], request_body=ProcedureVentilationSerializer)
    def put(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        procedureVentilation = get_object_or_404(ProcedureVentilation, pk=victim)
        data = request.data.copy()
        data['victim'] = victim.id
        serializer = ProcedureVentilationSerializer(procedureVentilation, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# done
class VictimProcedureProtocol(APIView):
    """List the Protocol Procedures of a Victim"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], request_body=ProcedureProtocolSerializer)
    def post(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        data = request.data.copy()
        data['victim'] = victim.id
        serializer = ProcedureProtocolSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            result = ProcedureProtocolSerializer(serializer.instance)
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[auth], request_body=ProcedureProtocolSerializer)
    def put(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        procedureProtocol = get_object_or_404(ProcedureProtocol, pk=victim)
        data = request.data.copy()
        data['victim'] = victim.id
        serializer = ProcedureProtocolSerializer(procedureProtocol, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# done
class VictimProcedureCirculation(APIView):
    """List the Circulation Procedures of a Victim"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], request_body=ProcedureCirculationSerializer)
    def post(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        data = request.data.copy()
        data['victim'] = victim.id
        serializer = ProcedureCirculationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            result = ProcedureCirculationSerializer(serializer.instance)
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[auth], request_body=ProcedureCirculationSerializer)
    def put(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        procedureCirculation = get_object_or_404(ProcedureCirculation, pk=victim)
        data = request.data.copy()
        data['victim'] = victim.id
        serializer = ProcedureCirculationSerializer(procedureCirculation, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# done
class VictimProcedureScale(APIView):
    """List the Scale Procedures of a Victim"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], request_body=ProcedureScaleSerializer)
    def post(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        data = request.data.copy()
        data['victim'] = victim.id
        serializer = ProcedureScaleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            result = ProcedureScaleSerializer(serializer.instance)
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(manual_parameters=[auth], request_body=ProcedureScaleSerializer)
    def put(self, request, victim_id):  # working
        victim = get_object_or_404(Victim, pk=victim_id)
        procedureScale = get_object_or_404(ProcedureScale, pk=victim)
        data = request.data.copy()
        data['victim'] = victim.id
        serializer = ProcedureScaleSerializer(procedureScale, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HospitalVictimsList(APIView):
    """List all Victims of an Hospital"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: VictimSerializer(many=True)})
    def get(self, request, hospital_id):
        hospital = get_object_or_404(Hospital, pk=hospital_id)
        victims = Victim.objects.filter(hospital=hospital)
        serializer = VictimSerializer(victims, many=True)

        return Response(serializer.data)


class TypeOfTransportList(APIView):
    """List all Type of transports"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: TypeOfTransportSerializer(many=True)})
    def get(self, request):
        transports_type = TypeOfTransport.objects.all()
        serializer = TypeOfTransportSerializer(transports_type, many=True)

        return Response(serializer.data)


class NonTransportReasonList(APIView):
    """List all non transport reasons"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: NonTransportReasonSerializer(many=True)})
    def get(self, request):
        non_transport_reason = NonTransportReason.objects.all()
        serializer = NonTransportReasonSerializer(non_transport_reason)

        return Response(serializer.data)


class StateList(APIView):
    """List all States"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: StateSerializer(many=True)})
    def get(self, request):
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)

        return Response(serializer.data)


class HospitalList(APIView):
    """List all Hospitals"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: HospitalSerializer(many=True)})
    def get(self, request):
        hospitals = Hospital.objects.all()
        serializer = HospitalSerializer(hospitals, many=True)

        return Response(serializer.data)


class CentralList(APIView):
    """List all Emergency Stations"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: CentralSerializer(many=True)})
    def get(self, request):
        centrals = Central.objects.all()
        serializer = CentralSerializer(centrals, many=True)

        return Response(serializer.data)


class DispatcherList(APIView):
    """List all Dispatchers"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: DispatcherSerializer(many=True)})
    def get(self, request):
        dispatchers = Dispatcher.objects.all()
        serializer = DispatcherSerializer(dispatchers, many=True)

        return Response(serializer.data)


class DispatcherDetail(APIView):
    """List a specific User that is a Dispatcher"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: DispatcherSerializer(many=True)})
    def get(self, request, user_id):  # working
        user = get_object_or_404(User, pk=user_id)
        dispatchers = Dispatcher.objects.filter(dispatcher=user)
        serializer = DispatcherSerializer(dispatchers, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class HospitalStaffList(APIView):
    """List all Hospital Staff Users"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: HospitalStaffSerializer(many=True)})
    def get(self, request):
        employees = HospitalStaff.objects.all()
        serializer = HospitalStaffSerializer(employees, many=True)

        return Response(serializer.data)


class UserCreate(APIView):
    """Create or Update a SIREPH User"""  # On use by Alves

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):  # working
        serializer = UserSerializer(data=request.data.copy())
        user = User.objects.filter(username=serializer.initial_data['username'])

        if user:
            return Response(status=status.HTTP_226_IM_USED)

        if serializer.is_valid():
            serializer.save()
            result = UserSerializer(User.objects.get(pk=serializer.instance.id))
            return Response(data=result.data,
                            status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CentralActiveTechniciansList(APIView):
    """List the active Technicians of a Central"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: TechnicianSerializer(many=True)})
    def get(self, request, central_id):
        central = get_object_or_404(Central, pk=central_id)
        technicians = Technician.objects.filter(central=central, active=True)
        serializer = TechnicianSerializer(technicians, many=True)

        return Response(serializer.data)


class VictimOccurrences(APIView):
    """List all Occurrences of a Victim"""  # On use by Alves
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: OccurrenceDetailSerializer(many=True)})
    def get(self, request, user_id):  #
        user = get_object_or_404(User, pk=user_id)
        occurrences = Occurrence.objects.filter(created_by=user_id)

        serializer = OccurrenceDetailSerializer(occurrences, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class NewsList(APIView):
    """List all News"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: NewsSerializer(many=True)})
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)

        return Response(serializer.data)


class VictimObject(APIView):
    """Create or Update a Victim"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], request_body=VictimSerializer)
    def post(self, request):
        data = request.data.copy()
        if data['id']:
            victim = Victim.objects.get(pk=data['id'])
            serializer = VictimSerializer(victim, data=data)
        else:
            serializer = VictimSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OccurrenceObject(APIView):
    """Create or Update an Occurrence"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], request_body=OccurrenceSerializer)
    def post(self, request):
        data = request.data.copy()
        if data['id']:
            occurrence = Occurrence.objects.get(pk=data['id'])
            serializer = OccurrenceSerializer(occurrence, data=data)
        else:
            serializer = OccurrenceSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EvaluationObject(APIView):
    """Create or Update an Evaluation"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], request_body=EvaluationSerializer)
    def post(self, request):
        data = request.data.copy()
        if data['id']:
            evaluation = Evaluation.objects.get(pk=data['id'])
            serializer = EvaluationSerializer(evaluation, data=data)
        else:
            serializer = EvaluationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PharmacyObject(APIView):
    """Create or Update a Pharmacy"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], request_body=PharmacySerializer)
    def post(self, request):
        data = request.data.copy()
        if data['id']:
            pharmacy = Pharmacy.objects.get(pk=data['id'])
            serializer = PharmacySerializer(pharmacy, data=data)
        else:
            serializer = PharmacySerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActiveUserCentral(APIView):
    """Lists the Central of a User"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: DispatcherDetailSerializer(many=True)})
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        dispatchers = Dispatcher.objects.filter(dispatcher=user, active=True)
        serializer = DispatcherDetailSerializer(dispatchers, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ActiveUserHospital(APIView):
    """Lists the hospital of the current user"""
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], responses={200: HospitalStaffDetailSerializer(many=True)})
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        staffs = HospitalStaff.objects.filter(employee=user, active=True)
        serializer = HospitalStaffDetailSerializer(staffs, many=True)

        return Response(serializer.data)


# class CentralTeamList(APIView):
#     """List all Teams for a specific Central"""
#     authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
#     permission_classes = [IsAuthenticated]
#     auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)
#
#     @swagger_auto_schema(manual_parameters=[auth], responses={200: TeamSerializer(many=True)})
#     def get(self, request, central_id):  # working
#         central = get_object_or_404(Central, pk=central_id)
#         team = Team.objects.filter(central=central)
#         serializer = TeamSerializer(team, many=True)
#
#         return Response(serializer.data)


class VictimSymptomTraumasList(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], request_body=TraumaSerializaer, responses={201: TraumaDetailsSerializaer()})
    def post(self, request, victim_id):
        data = request.data.copy()
        victim = get_object_or_404(Victim, pk=victim_id)
        symptom = Symptom.objects.get_or_create(victim=victim)[0]
        data["symptom"] = symptom
        serializer = TraumaDetailsSerializaer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED, data=serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VictimTransport(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    auth = openapi.Parameter('Authorization', openapi.IN_HEADER, type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[auth], request_body=VictimTransportSerializer)
    def put(self, request, victim_id):
        data = request.data.copy()
        victim = get_object_or_404(Victim, pk=victim_id)

        serializer = VictimTransportSerializer(victim, data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


