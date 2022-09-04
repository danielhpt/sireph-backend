from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.safestring import mark_safe
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


class TraumaInline(admin.TabularInline):
    model = Trauma


class SymptomAdmin(admin.ModelAdmin):
    inlines = [TraumaInline]
    model = Symptom


class SymptomInline(admin.StackedInline):
    model = Symptom
    show_change_link = True


class PharmacyInline(admin.TabularInline):
    model = Pharmacy


class GlasgowScaleInline(admin.StackedInline):
    model = GlasgowScale


class EvaluationAdmin(admin.ModelAdmin):
    inlines = [GlasgowScaleInline]
    model = Evaluation


class EvaluationInline(admin.TabularInline):
    model = Evaluation
    show_change_link = True


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
        PharmacyInline
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


class NewsAdmin(admin.ModelAdmin):
    model = News


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Evaluation, EvaluationAdmin)
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
admin.site.register(News, NewsAdmin)
