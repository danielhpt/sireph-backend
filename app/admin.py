from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from rest_framework.authtoken.admin import TokenAdmin

from .models import *

admin.site.site_header = "SIREPH Administrator Page"

TokenAdmin.raw_id_fields = ['user']


class TokenInline(admin.StackedInline):
    model = Token


class UserAdmin(AuthUserAdmin):
    inlines = [TokenInline]


class TechnicianAdmin(admin.ModelAdmin):
    model = Technician


class TeamTechnicianInline(admin.TabularInline):
    model = TeamTechnician


class ProcedureScaleInline(admin.StackedInline):
    model = ProcedureScale


class ProcedureCirculationInline(admin.StackedInline):
    model = ProcedureCirculation


class ProcedureProtocolInline(admin.StackedInline):
    model = ProcedureProtocol


class ProcedureVentilationInline(admin.StackedInline):
    model = ProcedureVentilation


class ProcedureRCPInline(admin.StackedInline):
    model = ProcedureRCP


class SymptomInline(admin.StackedInline):
    model = Symptom


class PharmacyInline(admin.TabularInline):
    model = Pharmacy


class EvaluationInline(admin.TabularInline):
    model = Evaluation


class HospitalAdmin(admin.ModelAdmin):
    model = Hospital


class VictimAdmin(admin.ModelAdmin):
    inlines = [
        EvaluationInline,
        SymptomInline,
        ProcedureRCPInline,
        ProcedureVentilationInline,
        ProcedureCirculationInline,
        ProcedureProtocolInline,
        ProcedureScaleInline,
        PharmacyInline,
    ]


class CentralAdmin(admin.ModelAdmin):
    model = Central


class OccurrenceStateInline(admin.TabularInline):
    model = OccurrenceState


class OccurrenceAdmin(admin.ModelAdmin):
    inlines = [
        OccurrenceStateInline
    ]


class TeamAdmin(admin.ModelAdmin):
    inlines = [
        TeamTechnicianInline,
    ]


class DispatcherAdmin(admin.ModelAdmin):
    model = Dispatcher


class HospitalStaffAdmin(admin.ModelAdmin):
    model = HospitalStaff


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Victim, VictimAdmin)
admin.site.register(Occurrence, OccurrenceAdmin)
admin.site.register(State)
admin.site.register(NonTransportReason)
admin.site.register(TypeOfTransport)
admin.site.register(Team, TeamAdmin)
admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Central, CentralAdmin)
admin.site.register(HospitalStaff, HospitalStaffAdmin)
admin.site.register(Dispatcher, DispatcherAdmin)
admin.site.register(Technician, TechnicianAdmin)
