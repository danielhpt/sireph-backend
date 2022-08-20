from django.urls import path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from .views_api import *

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
   ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # API
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('token/', obtain_auth_token),

    path('user/', UserCreate.as_view()),
    path('user/<int:user_id>/dispatcher/', DispatcherDetail.as_view(), name="user_dispatcher_detail"),
    path('user/', UserDetailByToken.as_view(), name="user_detail_by_token"),
    path('user/<int:user_id>/', UserInactive.as_view(), name="user_inactive"),
    path('user/<int:user_id>/occurrence/', UserActiveOccurrence.as_view(), name="user_active_occurrence"),

    path('users/', UserList.as_view(), name="user_list"),  # admin only
    path('users/<int:user_id>/', UserDetail.as_view(), name="user_detail"),
    path('users/<int:user_id>/teams/', UserTeamList.as_view(), name="user_team_list"),
    path('users/dispatchers/', DispatcherList.as_view(), name="user_dispatcher_list"),
    path('users/employees/', HospitalStaffList.as_view(), name="user_employee_list"),
    path('users/<int:user_id>/occurrences/', UserOccurrenceList.as_view(), name="user_occurrences_list"),

    path('teams/', TeamList.as_view(), name="team_list"),  # admin only
    path('teams/<int:team_id>/', TeamDetail.as_view(), name="team_detail"),
    path('teams/<int:team_id>/occurrences/', TeamOccurrencesList.as_view(), name="team_occurrences_list"),

    path('team/active/<int:user_id>/', UserTeamActive.as_view(), name="team_user_active"),

    path('occurrences/', OccurrenceList.as_view(), name="occurrence_list"),  # admin only
    path('occurrences/<int:occurrence_id>/', OccurrenceDetails.as_view(), name="occurrence_detail"),
    path('occurrences/<int:occurrence_id>/victims/', OccurrenceVictimsList.as_view(), name="occurrence_victims_list"),
    path('occurrences/<int:occurrence_id>/states/', OccurrenceStateList.as_view(), name="occurrence_states_list"),

    path('victims/<int:victim_id>/', VictimDetails.as_view(), name="victim_detail"),
    path('victims/<int:victim_id>/pharmacies/', VictimPharmacyList.as_view(), name="victim_pharmacy_list"),
    path('victims/<int:victim_id>/pharmacies/<int:pharmacy_id>/', VictimPharmacyDetail.as_view(),
         name="victim_pharmacy_detail"),
    path('victims/<int:victim_id>/evaluations/', VictimEvaluationList.as_view(), name="victim_evaluation_list"),
    path('victims/<int:victim_id>/evaluations/<int:evaluation_id>/', VictimEvaluationDetail.as_view(),
         name="victim_evaluation_detail"),
    path('victims/<int:victim_id>/symptom/', VictimSymptom.as_view(), name="victim_symptom"),
    path('victims/<int:victim_id>/procedure_rcp/', VictimProcedureRCP.as_view(), name="victim_procedure_rcp"),
    path('victims/<int:victim_id>/procedure_ventilation/', VictimProcedureVentilation.as_view(),
         name="victim_procedure_ventilation"),
    path('victims/<int:victim_id>/procedure_protocol/', VictimProcedureProtocol.as_view(),
         name="victim_procedure_protocol"),
    path('victims/<int:victim_id>/procedure_circulation/', VictimProcedureCirculation.as_view(),
         name="victim_procedure_circulation"),
    path('victims/<int:victim_id>/procedure_scale/', VictimProcedureScale.as_view(), name="victim_procedure_scale"),

    path('hospitals/', HospitalList.as_view(), name="hospital_list"),
    path('hospitals/victims/', HospitalVictimsList.as_view(), name="hospital_victims_list"),
    path('centrals/', CentralList.as_view(), name="central_list"),
    path('centrals/<int:central_id>/occurrences/', CentralOccurrencesList.as_view(), name="central_occurrences_list"),

    path('victim/<int:user_id>/occurrences', VictimOccurrences.as_view(), name="victim_occurrences"),
]