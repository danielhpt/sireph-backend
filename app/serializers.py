from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import *


class UserSimplifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class CentralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Central
        fields = ['id', 'designation', 'address', 'area_of_action', 'contact', 'is_administrative']


class TechnicianSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = UserSimplifiedSerializer(source='technician')

    class Meta:
        model = Technician
        fields = ['id', 'user', 'active']


class TechnicianDetailSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    user = UserSimplifiedSerializer(source='technician')
    central = CentralSerializer()

    class Meta:
        model = Technician
        fields = ['id', 'user', 'active', 'central']


class TeamTechnicianSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='technician.id')
    user = UserSimplifiedSerializer(source='technician.technician', read_only=True)

    class Meta:
        model = TeamTechnician
        fields = ['id', 'user', 'active', 'team_leader']


class TeamSerializer(serializers.ModelSerializer):
    technicians = TeamTechnicianSerializer(many=True, source='team_technicians')
    central = CentralSerializer(read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'technicians', 'central', 'active']

    def create(self, validated_data):
        validated_data = self.data.serializer.initial_data
        technicians_data = validated_data.pop('technicians')
        team = Team.objects.create()
        for technician_data in technicians_data:
            technician = Technician.objects.get(pk=technician_data['id'])
            teamTechnician = TeamTechnician()
            teamTechnician.team = team
            teamTechnician.technician = technician
            teamTechnician.active = technician_data['active']
            teamTechnician.team_leader = technician_data['team_leader']
            if teamTechnician.team_leader:
                team.central = technician.central
            teamTechnician.save()
        if team.central is None:
            team.central = Technician.objects.get(pk=technicians_data[0]['id']).central
        if team.central is None:
            team.central = Central.objects.get(pk=validated_data["central"]["id"])
        team.save()
        return team

    def update(self, instance, validated_data):
        validated_data = self.data.serializer.initial_data
        teamTechniciansOld = TeamTechnician.objects.filter(team_id=instance.id)
        teamTechniciansNew = validated_data.pop('technicians')

        for ttOld in teamTechniciansOld:
            for ttNew in teamTechniciansNew:
                if ttOld.technician_id == ttNew['id']:
                    if ttNew['active'] is not None:
                        ttOld.active = ttNew['active']
            ttOld.save()

        return instance


class DispatcherSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='dispatcher.id')
    username = serializers.ReadOnlyField(source='dispatcher.username')
    first_name = serializers.ReadOnlyField(source='dispatcher.first_name')
    last_name = serializers.ReadOnlyField(source='dispatcher.last_name')

    class Meta:
        model = Dispatcher
        fields = ['id', 'username', 'first_name', 'last_name', 'active', 'central']


class DispatcherDetailSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='dispatcher.id')
    username = serializers.ReadOnlyField(source='dispatcher.username')
    first_name = serializers.ReadOnlyField(source='dispatcher.first_name')
    last_name = serializers.ReadOnlyField(source='dispatcher.last_name')
    central = CentralSerializer(read_only=True)

    class Meta:
        model = Dispatcher
        fields = ['id', 'username', 'first_name', 'last_name', 'active', 'central']


class HospitalStaffSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='employee.id')
    username = serializers.ReadOnlyField(source='employee.username')
    first_name = serializers.ReadOnlyField(source='employee.first_name')
    last_name = serializers.ReadOnlyField(source='employee.last_name')

    class Meta:
        model = HospitalStaff
        fields = ['id', 'username', 'first_name', 'last_name', 'active', 'hospital']


class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = ['id', 'occurrence_number', 'entity', 'mean_of_assistance', 'motive', 'number_of_victims', 'local',
                  'gps_coordinates',
                  'parish', 'municipality', 'active', 'alert_mode', 'created_by', 'created_on', 'team', 'central']


#  def create(self, validated_data):
#      validated_data = self.data.serializer.initial_data
#      del validated_data['id']
#      del validated_data['states']
#      del validated_data['victims']
#      occurrence = Occurrence.objects.create(**validated_data)
#      return occurrence


class VictimIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Victim
        fields = ['id']


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['id', 'state']


class OccurrenceStateSerializer(serializers.ModelSerializer):
    state = StateSerializer(read_only=True)

    class Meta:
        model = OccurrenceState
        fields = ['id', 'state', 'longitude', 'latitude', 'date_time']

    def create(self, validated_data):
        validated_data = self.data.serializer.initial_data
        occurrance_state = OccurrenceState.objects.create(occurrence=validated_data["occurrence"], state=validated_data["state"],
                                                          longitude=validated_data["longitude"], latitude=validated_data["latitude"],
                                                          date_time=validated_data["date_time"])
        occurrance_state.save()
        return occurrance_state


class OccurrenceSimplifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occurrence
        fields = ['id', 'occurrence_number']


class TypeOfTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfTransport
        fields = ['id', 'type_of_transport']


class NonTransportReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = NonTransportReason
        fields = ['id', 'non_transport_reason']


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['id', 'name', 'address', 'capacity', 'current_capacity', 'contact', 'image_url']


class HospitalStaffDetailSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField(source='employee.id')
    username = serializers.ReadOnlyField(source='employee.username')
    first_name = serializers.ReadOnlyField(source='employee.first_name')
    last_name = serializers.ReadOnlyField(source='employee.last_name')
    hospital = HospitalSerializer(read_only=True)

    class Meta:
        model = HospitalStaff
        fields = ['id', 'username', 'first_name', 'last_name', 'active', 'hospital']


class VictimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Victim
        fields = ['id', 'name', 'birthdate', 'age', 'gender', 'identity_number', 'address', 'circumstances',
                  'disease_history', 'allergies', 'last_meal', 'last_meal_time', 'usual_medication', 'risk_situation',
                  'medical_followup', 'hospital_checkin_date', 'episode_number', 'comments',
                  'type_of_emergency', 'type_of_transport', 'non_transport_reason', 'occurrence', 'hospital']

    def create(self, validated_data):
        validated_data = self.data.serializer.initial_data
        if 'type_of_transport' in validated_data:
            if validated_data['type_of_transport'] is not None:
                validated_data['type_of_transport'] = TypeOfTransport.objects.get(type_of_transport=validated_data['type_of_transport'])
        if 'non_transport_reason' in validated_data:
            if validated_data['non_transport_reason'] is not None:
                validated_data['non_transport_reason'] = NonTransportReason.objects.get(non_transport_reason=validated_data['non_transport_reason'])
        if 'hospital' in validated_data:
            if validated_data['hospital'] is not None:
                validated_data['hospital'] = Hospital.objects.get(pk=validated_data['hospital'])
        occurrence_id = validated_data['occurrence']
        del validated_data['occurrence']
        victim = Victim.objects.create(occurrence_id=occurrence_id, **validated_data)
        return victim


class OccurrenceDetailSerializer(serializers.ModelSerializer):
    victims = VictimSerializer(many=True, read_only=True)
    states = OccurrenceStateSerializer(many=True, read_only=True, source="occurrence_states")
    team = TeamSerializer(read_only=True)
    central = CentralSerializer(read_only=True)

    class Meta:
        model = Occurrence
        fields = ['id', 'occurrence_number', 'entity', 'mean_of_assistance', 'motive', 'number_of_victims', 'local',
                  'gps_coordinates',
                  'parish', 'municipality', 'active', 'alert_mode', 'created_on', 'central', 'team', 'victims',
                  'states']


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['id', 'time', 'pharmacy', 'dose', 'route', 'adverse_effect', 'victim']


class PharmacyDetailSerializer(serializers.ModelSerializer):
    victim = VictimIdSerializer(read_only=True)

    class Meta:
        model = Pharmacy
        fields = ['id', 'time', 'pharmacy', 'dose', 'route', 'adverse_effect', 'victim']

    def create(self, validated_data):
        validated_data = self.data.serializer.initial_data
        victim = validated_data["victim"]
        del validated_data["victim"]
        pharmacy = Pharmacy.objects.create(victim=victim, **validated_data)
        return pharmacy


class ProcedureScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureScale
        fields = ['cincinatti', 'PROACS', 'RTS', 'MGAP', 'RACE', 'victim']

    def create(self, validated_data):
        validated_data = self.data.serializer.initial_data
        victim = validated_data["victim"]
        del validated_data["victim"]
        procedureScale = ProcedureScale.objects.create(victim_id=victim, **validated_data)
        return procedureScale

    def update(self, instance, validated_data):
        instance.cincinatti = validated_data.get('cincinatti', instance.cincinatti)
        instance.PROACS = validated_data.get('PROACS', instance.PROACS)
        instance.RTS = validated_data.get('RTS', instance.RTS)
        instance.MGAP = validated_data.get('MGAP', instance.MGAP)
        instance.RACE = validated_data.get('RACE', instance.RACE)

        instance.save()

        return instance


class ProcedureCirculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureCirculation
        fields = ['temperature_monitoring', 'compression', 'tourniquet', 'pelvic_belt', 'venous_access', 'patch',
                  'ecg', 'victim']

    def create(self, validated_data):
        validated_data = self.data.serializer.initial_data
        victim = validated_data["victim"]
        del validated_data["victim"]
        procedureCirculation = ProcedureCirculation.objects.create(victim_id=victim, **validated_data)
        return procedureCirculation

    def update(self, instance, validated_data):
        instance.temperature_monitoring = validated_data.get('temperature_monitoring', instance.temperature_monitoring)
        instance.compression = validated_data.get('compression', instance.compression)
        instance.tourniquet = validated_data.get('tourniquet', instance.tourniquet)
        instance.pelvic_belt = validated_data.get('pelvic_belt', instance.pelvic_belt)
        instance.venous_access = validated_data.get('venous_access', instance.venous_access)
        instance.patch = validated_data.get('patch', instance.patch)
        instance.ecg = validated_data.get('ecg', instance.ecg)

        instance.save()

        return instance


class GlasgowScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlasgowScale
        fields = ['eyes', 'verbal', 'motor', 'total']


class EvaluationSerializer(serializers.ModelSerializer):
    glasgow_scale = GlasgowScaleSerializer(allow_null=True)

    class Meta:
        model = Evaluation
        fields = ['id', 'hours', 'avds', 'ventilation', 'spo2', 'o2', 'etco2', 'pulse', 'ecg', 'skin', 'temperature',
                  'systolic_blood_pressure', 'diastolic_blood_pressure', 'pupils', 'pain', 'glycemia', 'news', 'victim', 'glasgow_scale']


class EvaluationDetailSerializer(serializers.ModelSerializer):
    victim = VictimIdSerializer(read_only=True)
    glasgow_scale = GlasgowScaleSerializer(allow_null=True)

    class Meta:
        model = Evaluation
        fields = ['id', 'hours', 'avds', 'ventilation', 'spo2', 'o2', 'etco2', 'pulse', 'ecg', 'skin', 'temperature',
                  'systolic_blood_pressure', 'diastolic_blood_pressure', 'pupils', 'pain', 'glycemia', 'news', 'victim', 'glasgow_scale']

    def create(self, validated_data):
        glasgow_scale = None
        validated_data = self.data.serializer.initial_data
        victim = validated_data["victim"]
        del validated_data["victim"]
        if validated_data['glasgow_scale']:
            glasgow_scale = validated_data['glasgow_scale']
            del validated_data['glasgow_scale']
        evaluation = Evaluation.objects.create(victim=victim, **validated_data)
        if glasgow_scale:
            GlasgowScale.objects.create(evaluation=evaluation, **glasgow_scale)
        return evaluation


class TraumaSerializaer(serializers.ModelSerializer):
    class Meta:
        model = Trauma
        fields = ['id', 'body_part', 'type_of_injury', 'closed', 'burn_degree']


class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = ['comments', 'victim', 'total_burn_area']


class SymptomDetailsSerializer(serializers.ModelSerializer):
    traumas = TraumaSerializaer(many=True, read_only=True)

    class Meta:
        model = Symptom
        fields = ['comments', 'traumas', 'victim', 'total_burn_area']

    def create(self, validated_data):
        validated_data = self.data.serializer.initial_data
        victim = validated_data["victim"]
        del validated_data["victim"]
        symptom = Symptom.objects.create(victim_id=victim, **validated_data)
        return symptom


class TraumaDetailsSerializaer(serializers.ModelSerializer):
    symptom = SymptomSerializer(read_only=True)

    class Meta:
        model = Trauma
        fields = ['id', 'body_part', 'type_of_injury', 'closed', 'burn_degree', 'symptom']

    def create(self, validated_data):
        validated_data = self.data.serializer.initial_data
        symptom = validated_data["symptom"]
        del validated_data["symptom"]
        trauma = Trauma.objects.create(**validated_data, symptom=symptom)
        return trauma


class ProcedureRCPSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureRCP
        fields = ['witnessed', 'SBV_DAE', 'SIV_SAV', 'first_rhythm', 'nr_shocks', 'recovery', 'downtime',
                  'mechanical_compressions', 'not_performed', 'victim']

    def create(self, validated_data):
        validated_data = self.data.serializer.initial_data
        victim = validated_data["victim"]
        del validated_data["victim"]
        procedureRCP = ProcedureRCP.objects.create(victim_id=victim, **validated_data)
        return procedureRCP

    def update(self, instance, validated_data):
        instance.witnessed = validated_data.get('witnessed', instance.witnessed)
        instance.SBV_DAE = validated_data.get('SBV_DAE', instance.SBV_DAE)
        instance.SIV_SAV = validated_data.get('SIV_SAV', instance.SIV_SAV)
        instance.first_rhythm = validated_data.get('first_rhythm', instance.first_rhythm)
        instance.nr_shocks = validated_data.get('nr_shocks', instance.nr_shocks)
        instance.recovery = validated_data.get('recovery', instance.recovery)
        instance.downtime = validated_data.get('downtime', instance.downtime)
        instance.mechanical_compressions = validated_data.get('mechanical_compressions', instance.mechanical_compressions)
        instance.not_performed = validated_data.get('not_performed', instance.not_performed)

        instance.save()

        return instance


class ProcedureVentilationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureVentilation
        fields = ['clearance', 'oropharyngeal', 'laryngeal_tube', 'endotracheal', 'laryngeal_mask',
                  'mechanical_ventilation', 'cpap', 'victim']

    def create(self, validated_data):
        validated_data = self.data.serializer.initial_data
        victim = validated_data["victim"]
        del validated_data["victim"]
        procedureVentilation = ProcedureVentilation.objects.create(victim_id=victim, **validated_data)
        return procedureVentilation

    def update(self, instance, validated_data):
        instance.clearance = validated_data.get('clearance', instance.clearance)
        instance.oropharyngeal = validated_data.get('oropharyngeal', instance.oropharyngeal)
        instance.laryngeal_tube = validated_data.get('laryngeal_tube', instance.laryngeal_tube)
        instance.endotracheal = validated_data.get('endotracheal', instance.endotracheal)
        instance.laryngeal_mask = validated_data.get('laryngeal_mask', instance.laryngeal_mask)
        instance.mechanical_ventilation = validated_data.get('mechanical_ventilation', instance.mechanical_ventilation)
        instance.cpap = validated_data.get('cpap', instance.cpap)

        instance.save()

        return instance


class ProcedureProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureProtocol
        fields = ['immobilization', 'TEPH', 'SIV', 'VV_AVC', 'VV_coronary', 'VV_sepsis', 'VV_trauma', 'VV_PCR',
                  'victim']

    def create(self, validated_data):
        validated_data = self.data.serializer.initial_data
        victim = validated_data["victim"]
        del validated_data["victim"]
        procedureProtocol = ProcedureProtocol.objects.create(victim_id=victim, **validated_data)
        return procedureProtocol

    def update(self, instance, validated_data):
        instance.immobilization = validated_data.get('immobilization', instance.immobilization)
        instance.TEPH = validated_data.get('TEPH', instance.TEPH)
        instance.SIV = validated_data.get('SIV', instance.SIV)
        instance.VV_AVC = validated_data.get('VV_AVC', instance.VV_AVC)
        instance.VV_coronary = validated_data.get('VV_coronary', instance.VV_coronary)
        instance.VV_sepsis = validated_data.get('VV_sepsis', instance.VV_sepsis)
        instance.VV_trauma = validated_data.get('VV_trauma', instance.VV_trauma)
        instance.VV_PCR = validated_data.get('VV_PCR', instance.VV_PCR)

        instance.save()

        return instance


class VictimDetailsSerializer(serializers.ModelSerializer):
    type_of_transport = serializers.ReadOnlyField(source='type_of_transport.type_of_transport')
    non_transport_reason = serializers.ReadOnlyField(source='non_transport_reason.non_transport_reason')
    occurrence = OccurrenceSimplifiedSerializer(read_only=True)
    evaluations = EvaluationSerializer(read_only=True, many=True)
    pharmacies = PharmacySerializer(many=True, read_only=True)
    procedure_rcp = ProcedureRCPSerializer(read_only=True)
    procedure_ventilation = ProcedureVentilationSerializer(read_only=True)
    procedure_protocol = ProcedureProtocolSerializer(read_only=True)
    procedure_circulation = ProcedureCirculationSerializer(read_only=True)
    procedure_scale = ProcedureScaleSerializer(read_only=True)
    symptom = SymptomDetailsSerializer(read_only=True)

    class Meta:
        model = Victim
        fields = ['id', 'name', 'birthdate', 'age', 'gender', 'identity_number', 'address', 'circumstances',
                  'disease_history', 'allergies', 'last_meal', 'last_meal_time', 'usual_medication', 'risk_situation',
                  'medical_followup', 'hospital_checkin_date', 'episode_number', 'comments',
                  'type_of_emergency', 'type_of_transport', 'non_transport_reason', 'occurrence', 'evaluations',
                  'symptom', 'procedure_rcp', 'procedure_ventilation', 'procedure_protocol',
                  'procedure_circulation', 'procedure_scale', 'pharmacies', 'hospital']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']

    def create(self, validated_data):
        validated_data = self.data.serializer.initial_data
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=make_password(validated_data['password'])
        )
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)

        instance.save()

        return instance


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'image_url']


class VictimAllDetailsSerializer(serializers.ModelSerializer):
    type_of_transport = serializers.ReadOnlyField(source='type_of_transport.type_of_transport')
    non_transport_reason = serializers.ReadOnlyField(source='non_transport_reason.non_transport_reason')
    occurrence = OccurrenceSimplifiedSerializer(read_only=True)
    evaluations = EvaluationSerializer(read_only=True, many=True)
    pharmacies = PharmacySerializer(many=True, read_only=True)
    procedure_rcp = ProcedureRCPSerializer(read_only=True)
    procedure_ventilation = ProcedureVentilationSerializer(read_only=True)
    procedure_protocol = ProcedureProtocolSerializer(read_only=True)
    procedure_circulation = ProcedureCirculationSerializer(read_only=True)
    procedure_scale = ProcedureScaleSerializer(read_only=True)
    symptom = SymptomDetailsSerializer(read_only=True)
    hospital = HospitalSerializer(read_only=True)

    class Meta:
        model = Victim
        fields = ['id', 'name', 'birthdate', 'age', 'gender', 'identity_number', 'address', 'circumstances',
                  'disease_history', 'allergies', 'last_meal', 'last_meal_time', 'usual_medication', 'risk_situation',
                  'medical_followup', 'hospital_checkin_date', 'episode_number', 'comments',
                  'type_of_emergency', 'type_of_transport', 'non_transport_reason', 'occurrence', 'evaluations',
                  'symptom', 'procedure_rcp', 'procedure_ventilation', 'procedure_protocol',
                  'procedure_circulation', 'procedure_scale', 'pharmacies', 'hospital']


class OccurrenceAllDetailsSerializer(serializers.ModelSerializer):
    victims = VictimAllDetailsSerializer(many=True, read_only=True)
    states = OccurrenceStateSerializer(many=True, read_only=True, source="occurrence_states")
    team = TeamSerializer(read_only=True)
    central = CentralSerializer(read_only=True)

    class Meta:
        model = Occurrence
        fields = ['id', 'occurrence_number', 'entity', 'mean_of_assistance', 'motive', 'number_of_victims', 'local',
                  'gps_coordinates',
                  'parish', 'municipality', 'active', 'alert_mode', 'created_on', 'central', 'team', 'victims',
                  'states']


class VictimTransportSerializer(serializers.ModelSerializer):
    type_of_transport = serializers.IntegerField(source='type_of_transport.id', allow_null=True)
    non_transport_reason = serializers.IntegerField(source='non_transport_reason.id', allow_null=True)
    hospital = serializers.IntegerField(source="hospital.id", allow_null=True)

    class Meta:
        model = Victim
        fields = ['id', 'medical_followup', 'episode_number', 'type_of_transport', 'non_transport_reason', 'hospital']

    def update(self, instance, validated_data):
        instance.medical_followup = validated_data.get('medical_followup', instance.medical_followup)
        instance.episode_number = validated_data.get('episode_number', instance.episode_number)

        if validated_data.get('type_of_transport')['id']:
            instance.type_of_transport = TypeOfTransport.objects.get(pk=validated_data.get('type_of_transport')['id'])
        else:
            instance.type_of_transport = None
        if validated_data.get('non_transport_reason')['id']:
            instance.non_transport_reason = NonTransportReason.objects.get(pk=validated_data.get('non_transport_reason')['id'])
        else:
            instance.non_transport_reason = None
        if validated_data.get('hospital')['id']:
            instance.hospital = Hospital.objects.get(pk=validated_data.get('hospital')['id'])
        else:
            instance.hospital = None

        instance.save()

        return instance
