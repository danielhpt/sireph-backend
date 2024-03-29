from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.datetime_safe import datetime
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Central(models.Model):
    designation = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    area_of_action = models.CharField(max_length=50)
    contact = models.IntegerField()
    is_administrative = models.BooleanField()

    def __str__(self):
        return self.designation


class Team(models.Model):
    central = models.ForeignKey(
        Central,
        on_delete=models.RESTRICT,
        related_name="central_team",
        blank=True,
        null=True,
    )
    active = models.BooleanField(default=True)

    # def __str__(self):
    # if self.team_technicians.filter(team_leader=True)[0]:
    #    return str(self.id) + ' - ' + self.team_technicians.filter(team_leader=True)[0].technician.get_username()
    # return str(self.id)


class Technician(models.Model):
    technician = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='technician_user'
    )
    central = models.ForeignKey(
        Central,
        on_delete=models.RESTRICT,
        related_name="central_technician"
    )
    active = models.BooleanField(default=True)

    models.UniqueConstraint(
        fields=['technician'],
        name='uniqueUser'
    )

    def __str__(self):
        return self.technician.get_username()


class TeamTechnician(models.Model):
    team = models.ForeignKey(
        Team,
        on_delete=models.RESTRICT,
        related_name="team_technicians"
    )
    technician = models.ForeignKey(
        Technician,
        on_delete=models.RESTRICT,
        related_name="technician_teams"
    )
    active = models.BooleanField(default=True)
    team_leader = models.BooleanField(default=False)

    models.UniqueConstraint(
        fields=['team', 'technician'],
        name='unique1'
    )

    def __str__(self):
        if self.active:
            active = ' active: 1'
        else:
            active = ' active: 0'
        if self.team_leader:
            team_leader = ' leader: 1'
        else:
            team_leader = ' leader: 0'
        return str(self.team.id) + ' - ' + self.technician.technician.get_username() + active + team_leader


class Occurrence(models.Model):
    occurrence_number = models.IntegerField()
    entity = models.CharField(max_length=50, null=True, blank=True)
    mean_of_assistance = models.CharField(max_length=50, null=True, blank=True)
    motive = models.CharField(max_length=50)
    number_of_victims = models.IntegerField()
    local = models.CharField(max_length=100)
    gps_coordinates = models.CharField(max_length=100, null=True, blank=True)
    parish = models.CharField(max_length=50, null=True, blank=True)  # freguesia
    municipality = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(default=True)
    alert_mode = models.BooleanField(default=False)
    created_by = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(null=True, blank=True)
    team = models.ForeignKey(
        Team,
        related_name="occurrences",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
    )
    central = models.ForeignKey(
        Central,
        related_name="occurrences",
        on_delete=models.RESTRICT,
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.id) + ' - ' + str(self.occurrence_number)


class Dispatcher(models.Model):
    dispatcher = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name='dispatcher_user'
    )
    central = models.ForeignKey(
        Central,
        on_delete=models.RESTRICT,
        related_name="central_user"
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.dispatcher.get_username()


class State(models.Model):
    state = models.CharField(max_length=25)

    def __str__(self):
        return self.state


class OccurrenceState(models.Model):
    occurrence = models.ForeignKey(
        Occurrence,
        on_delete=models.RESTRICT,
        related_name="occurrence_states"
    )
    state = models.ForeignKey(
        State,
        on_delete=models.RESTRICT,
        related_name="state_occurrences"
    )
    longitude = models.DecimalField(max_digits=15, decimal_places=7)
    latitude = models.DecimalField(max_digits=15, decimal_places=7)
    date_time = models.DateTimeField()

    models.UniqueConstraint(fields=['occurrence', 'state'], name='unique2')

    def __str__(self):
        return str(self.occurrence.id) + ' - ' + self.state.state


class TypeOfTransport(models.Model):
    type_of_transport = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.type_of_transport


class NonTransportReason(models.Model):
    non_transport_reason = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.non_transport_reason


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    capacity = models.IntegerField()
    current_capacity = models.IntegerField()
    contact = models.IntegerField()
    image_url = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class HospitalStaff(models.Model):
    employee = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        related_name="staff_user"
    )
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.RESTRICT,
        related_name="hospital_employee"
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.employee.get_username()


class Victim(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=25, null=True, blank=True)
    identity_number = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    circumstances = models.CharField(max_length=100, null=True, blank=True)
    disease_history = models.CharField(max_length=200, null=True, blank=True)
    allergies = models.CharField(max_length=100, null=True, blank=True)
    last_meal = models.CharField(max_length=50, null=True, blank=True)
    last_meal_time = models.DateTimeField(null=True, blank=True)
    usual_medication = models.CharField(max_length=100, null=True, blank=True)
    risk_situation = models.CharField(max_length=50, null=True, blank=True)
    medical_followup = models.BooleanField(default=False)
    hospital_checkin_date = models.DateTimeField(max_length=100, null=True, blank=True)
    episode_number = models.PositiveIntegerField(null=True, blank=True)
    comments = models.CharField(max_length=400, null=True, blank=True)
    type_of_emergency = models.CharField(max_length=100, null=True, blank=True)
    type_of_transport = models.ForeignKey(
        TypeOfTransport,
        on_delete=models.RESTRICT,
        null=True,
        blank=True
    )
    non_transport_reason = models.ForeignKey(
        NonTransportReason,
        on_delete=models.RESTRICT,
        null=True,
        blank=True
    )
    occurrence = models.ForeignKey(
        Occurrence,
        on_delete=models.RESTRICT,
        related_name='victims',
        null=True,
        blank=True
    )
    hospital = models.ForeignKey(
        Hospital,
        on_delete=models.RESTRICT,
        related_name='victim_hospital',
        null=True,
        blank=True
    )

    def __str__(self):
        if self.name:
            return str(self.id) + ' - ' + self.name
        return str(self.id)


class Pharmacy(models.Model):
    victim = models.ForeignKey(
        Victim,
        on_delete=models.RESTRICT,
        related_name="pharmacies"
    )
    time = models.DateTimeField(null=True, blank=True)
    pharmacy = models.CharField(max_length=50)
    dose = models.CharField(max_length=50, null=True, blank=True)
    route = models.CharField(max_length=50, null=True, blank=True)
    adverse_effect = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Pharmacies"

    def __str__(self):
        return str(self.victim.id) + ' - ' + self.pharmacy


class ProcedureScale(models.Model):
    victim = models.OneToOneField(
        Victim,
        on_delete=models.RESTRICT,
        primary_key=True,
        related_name='procedure_scale'
    )
    cincinatti = models.PositiveSmallIntegerField(null=True, blank=True)
    PROACS = models.PositiveSmallIntegerField(null=True, blank=True)
    RTS = models.PositiveSmallIntegerField(null=True, blank=True)
    MGAP = models.PositiveSmallIntegerField(null=True, blank=True)
    RACE = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.victim.id) + ' - Scale procedures'


class ProcedureCirculation(models.Model):
    victim = models.OneToOneField(
        Victim,
        on_delete=models.RESTRICT,
        primary_key=True,
        related_name='procedure_circulation'
    )
    temperature_monitoring = models.BooleanField()
    compression = models.BooleanField()
    tourniquet = models.BooleanField()
    pelvic_belt = models.BooleanField()
    venous_access = models.BooleanField()
    patch = models.BooleanField()
    ecg = models.BooleanField()

    def __str__(self):
        return str(self.victim.id) + ' - Circulation procedures'


class Evaluation(models.Model):
    victim = models.ForeignKey(
        Victim,
        on_delete=models.RESTRICT,
        related_name="evaluations"
    )
    hours = models.DateTimeField()
    avds = models.CharField(max_length=1, null=True, blank=True)
    ventilation = models.PositiveSmallIntegerField(null=True, blank=True)
    spo2 = models.PositiveSmallIntegerField(null=True, blank=True)
    o2 = models.PositiveSmallIntegerField(null=True, blank=True)
    etco2 = models.PositiveSmallIntegerField(null=True, blank=True)
    pulse = models.PositiveSmallIntegerField(null=True, blank=True)
    ecg = models.BooleanField(default=False)
    skin = models.CharField(max_length=50, null=True, blank=True)
    temperature = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    systolic_blood_pressure = models.PositiveSmallIntegerField(null=True, blank=True)
    diastolic_blood_pressure = models.PositiveSmallIntegerField(null=True, blank=True)
    pupils = models.CharField(max_length=50, null=True, blank=True)
    pain = models.PositiveSmallIntegerField(null=True, blank=True, validators=[MaxValueValidator(10)])
    glycemia = models.PositiveSmallIntegerField(null=True, blank=True)
    news = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.victim.id) + ' - ' + str(self.hours)


class GlasgowScale(models.Model):
    evaluation = models.OneToOneField(
        Evaluation,
        on_delete=models.RESTRICT,
        primary_key=True,
        related_name="glasgow_scale"
    )
    eyes = models.PositiveSmallIntegerField(null=True, blank=True)
    verbal = models.PositiveSmallIntegerField(null=True, blank=True)
    motor = models.PositiveSmallIntegerField(null=True, blank=True)
    total = models.PositiveSmallIntegerField(null=True, blank=True)


class Symptom(models.Model):
    victim = models.OneToOneField(
        Victim,
        on_delete=models.RESTRICT,
        primary_key=True,
        related_name='symptom'
    )
    comments = models.CharField(max_length=400, null=True, blank=True)
    total_burn_area = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)

    def __str__(self):
        return str(self.victim.id) + ' - Symptoms'


class Trauma(models.Model):
    symptom = models.ForeignKey(
        Symptom,
        on_delete=models.RESTRICT,
        related_name='traumas'
    )
    body_part = models.CharField(max_length=20, null=True, blank=True)
    type_of_injury = models.CharField(max_length=1, null=True, blank=True)
    closed = models.BooleanField(default=False)
    burn_degree = models.CharField(max_length=2, null=True, blank=True)


class ProcedureRCP(models.Model):
    witnessed = models.BooleanField(default=False)
    SBV_DAE = models.DateTimeField(null=True, blank=True)
    SIV_SAV = models.DateTimeField(null=True, blank=True)
    first_rhythm = models.CharField(max_length=25, null=True, blank=True)
    nr_shocks = models.PositiveIntegerField(null=True, blank=True)
    recovery = models.DateTimeField(null=True, blank=True)
    downtime = models.DateTimeField(null=True, blank=True)
    mechanical_compressions = models.BooleanField(default=False)
    not_performed = models.BooleanField(default=False)
    victim = models.OneToOneField(
        Victim,
        on_delete=models.RESTRICT,
        primary_key=True,
        related_name='procedure_rcp'
    )

    def __str__(self):
        return str(self.victim.id) + ' - RCP procedures'


class ProcedureVentilation(models.Model):
    victim = models.OneToOneField(
        Victim,
        on_delete=models.RESTRICT,
        primary_key=True,
        related_name='procedure_ventilation'
    )
    clearance = models.BooleanField(default=False)
    oropharyngeal = models.BooleanField(default=False)
    laryngeal_tube = models.BooleanField(default=False)
    endotracheal = models.BooleanField(default=False)
    laryngeal_mask = models.BooleanField(default=False)
    mechanical_ventilation = models.BooleanField(default=False)
    cpap = models.BooleanField(default=False)

    def __str__(self):
        return str(self.victim.id) + ' - Ventilation procedures'


class ProcedureProtocol(models.Model):
    immobilization = models.BooleanField(default=False)
    TEPH = models.BooleanField(default=False)
    SIV = models.BooleanField(default=False)
    VV_AVC = models.BooleanField(default=False)
    VV_coronary = models.BooleanField(default=False)
    VV_sepsis = models.BooleanField(default=False)
    VV_trauma = models.BooleanField(default=False)
    VV_PCR = models.BooleanField(default=False)
    victim = models.OneToOneField(
        Victim,
        on_delete=models.RESTRICT,
        primary_key=True,
        related_name='procedure_protocol'
    )

    def __str__(self):
        return str(self.victim.id) + ' - Protocol procedures'


class News(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    image_url = models.CharField(max_length=500, null=True, blank=True)
