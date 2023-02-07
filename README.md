# SIREPH API


<a name="overview"></a>
## Overview
External Service to Integrated Pre-Hospital Emergency Response System (SIREPH)


### Version information
*Version* : v1


### URI scheme
*Host* : 127.0.0.1:8000  
*BasePath* : /api  
*Schemes* : HTTP


### Consumes

* `application/json`


### Produces

* `application/json`




<a name="paths"></a>
## Paths

<a name="centrals_list"></a>
### GET /centrals/

#### Description
List all Emergency Stations


#### Parameters

| Type       | Name                              | Schema |
|------------|-----------------------------------|--------|
| **Header** | **Authorization**  <br>*optional* | string |


#### Responses

| HTTP Code | Schema                        |
|-----------|-------------------------------|
| **200**   | < [Central](#central) > array |


#### Tags

* centrals


#### Example HTTP request

##### Request path
```
/centrals/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "designation" : "string",
  "address" : "string",
  "area_of_action" : "string",
  "contact" : 0,
  "is_administrative" : true
} ]
```


<a name="centrals_occurrences_create"></a>
### POST /centrals/{central_id}/occurrences/

#### Description
List all Occurrences of a Central


#### Parameters

| Type       | Name                              | Schema                                |
|------------|-----------------------------------|---------------------------------------|
| **Header** | **Authorization**  <br>*optional* | string                                |
| **Path**   | **central_id**  <br>*required*    | string                                |
| **Body**   | **data**  <br>*required*          | [OccurrenceDetail](#occurrencedetail) |


#### Responses

| HTTP Code | Schema                                |
|-----------|---------------------------------------|
| **201**   | [OccurrenceDetail](#occurrencedetail) |


#### Tags

* centrals


#### Example HTTP request

##### Request path
```
/centrals/string/occurrences/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_on" : "1970-01-01T00:00:00Z",
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "team" : {
    "id" : 0,
    "technicians" : [ {
      "id" : "string",
      "user" : {
        "id" : 0,
        "username" : "string",
        "first_name" : "string",
        "last_name" : "string",
        "email" : "email@example.com"
      },
      "active" : true,
      "team_leader" : true
    } ],
    "central" : {
      "id" : 0,
      "designation" : "string",
      "address" : "string",
      "area_of_action" : "string",
      "contact" : 0,
      "is_administrative" : true
    },
    "active" : true
  },
  "victims" : [ {
    "id" : 0,
    "name" : "string",
    "birthdate" : "1970-01-01",
    "age" : 0,
    "gender" : "string",
    "identity_number" : "string",
    "address" : "string",
    "circumstances" : "string",
    "disease_history" : "string",
    "allergies" : "string",
    "last_meal" : "string",
    "last_meal_time" : "1970-01-01T00:00:00Z",
    "usual_medication" : "string",
    "risk_situation" : "string",
    "medical_followup" : true,
    "hospital_checkin_date" : "1970-01-01T00:00:00Z",
    "episode_number" : 0,
    "comments" : "string",
    "type_of_emergency" : "string",
    "type_of_transport" : 0,
    "non_transport_reason" : 0,
    "occurrence" : 0,
    "hospital" : 0
  } ],
  "states" : [ {
    "id" : 0,
    "state" : {
      "id" : 0,
      "state" : "string"
    },
    "longitude" : "string",
    "latitude" : "string",
    "date_time" : "1970-01-01T00:00:00Z"
  } ]
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_on" : "1970-01-01T00:00:00Z",
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "team" : {
    "id" : 0,
    "technicians" : [ {
      "id" : "string",
      "user" : {
        "id" : 0,
        "username" : "string",
        "first_name" : "string",
        "last_name" : "string",
        "email" : "email@example.com"
      },
      "active" : true,
      "team_leader" : true
    } ],
    "central" : {
      "id" : 0,
      "designation" : "string",
      "address" : "string",
      "area_of_action" : "string",
      "contact" : 0,
      "is_administrative" : true
    },
    "active" : true
  },
  "victims" : [ {
    "id" : 0,
    "name" : "string",
    "birthdate" : "1970-01-01",
    "age" : 0,
    "gender" : "string",
    "identity_number" : "string",
    "address" : "string",
    "circumstances" : "string",
    "disease_history" : "string",
    "allergies" : "string",
    "last_meal" : "string",
    "last_meal_time" : "1970-01-01T00:00:00Z",
    "usual_medication" : "string",
    "risk_situation" : "string",
    "medical_followup" : true,
    "hospital_checkin_date" : "1970-01-01T00:00:00Z",
    "episode_number" : 0,
    "comments" : "string",
    "type_of_emergency" : "string",
    "type_of_transport" : 0,
    "non_transport_reason" : 0,
    "occurrence" : 0,
    "hospital" : 0
  } ],
  "states" : [ {
    "id" : 0,
    "state" : {
      "id" : 0,
      "state" : "string"
    },
    "longitude" : "string",
    "latitude" : "string",
    "date_time" : "1970-01-01T00:00:00Z"
  } ]
}
```


<a name="centrals_occurrences_list"></a>
### GET /centrals/{central_id}/occurrences/

#### Description
List all Occurrences of a Central


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**central_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [OccurrenceDetail](#occurrencedetail) > array|


#### Tags

* centrals


#### Example HTTP request

##### Request path
```
/centrals/string/occurrences/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_on" : "1970-01-01T00:00:00Z",
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "team" : {
    "id" : 0,
    "technicians" : [ {
      "id" : "string",
      "user" : {
        "id" : 0,
        "username" : "string",
        "first_name" : "string",
        "last_name" : "string",
        "email" : "email@example.com"
      },
      "active" : true,
      "team_leader" : true
    } ],
    "central" : {
      "id" : 0,
      "designation" : "string",
      "address" : "string",
      "area_of_action" : "string",
      "contact" : 0,
      "is_administrative" : true
    },
    "active" : true
  },
  "victims" : [ {
    "id" : 0,
    "name" : "string",
    "birthdate" : "1970-01-01",
    "age" : 0,
    "gender" : "string",
    "identity_number" : "string",
    "address" : "string",
    "circumstances" : "string",
    "disease_history" : "string",
    "allergies" : "string",
    "last_meal" : "string",
    "last_meal_time" : "1970-01-01T00:00:00Z",
    "usual_medication" : "string",
    "risk_situation" : "string",
    "medical_followup" : true,
    "hospital_checkin_date" : "1970-01-01T00:00:00Z",
    "episode_number" : 0,
    "comments" : "string",
    "type_of_emergency" : "string",
    "type_of_transport" : 0,
    "non_transport_reason" : 0,
    "occurrence" : 0,
    "hospital" : 0
  } ],
  "states" : [ {
    "id" : 0,
    "state" : {
      "id" : 0,
      "state" : "string"
    },
    "longitude" : "string",
    "latitude" : "string",
    "date_time" : "1970-01-01T00:00:00Z"
  } ]
} ]
```


<a name="centrals_technicians_list"></a>
### GET /centrals/{central_id}/technicians/

#### Description
List the active Technicians of a Central


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**central_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Technician](#technician) > array|


#### Tags

* centrals


#### Example HTTP request

##### Request path
```
/centrals/string/technicians/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : "string",
  "user" : {
    "id" : 0,
    "username" : "string",
    "first_name" : "string",
    "last_name" : "string",
    "email" : "email@example.com"
  },
  "active" : true
} ]
```


<a name="evaluation_create"></a>
### POST /evaluation/

#### Description
Create or Update an Evaluation


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Body**|**data**  <br>*required*|[Evaluation](#evaluation)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[Evaluation](#evaluation)|


#### Tags

* evaluation


#### Example HTTP request

##### Request path
```
/evaluation/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "hours" : "1970-01-01T00:00:00Z",
  "avds" : "string",
  "ventilation" : 0,
  "spo2" : 0,
  "o2" : 0,
  "etco2" : 0,
  "pulse" : 0,
  "ecg" : true,
  "skin" : "string",
  "temperature" : "string",
  "systolic_blood_pressure" : 0,
  "diastolic_blood_pressure" : 0,
  "pupils" : "string",
  "pain" : 0,
  "glycemia" : 0,
  "news" : 0,
  "victim" : 0,
  "glasgow_scale" : {
    "eyes" : 0,
    "verbal" : 0,
    "motor" : 0,
    "total" : 0
  }
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "hours" : "1970-01-01T00:00:00Z",
  "avds" : "string",
  "ventilation" : 0,
  "spo2" : 0,
  "o2" : 0,
  "etco2" : 0,
  "pulse" : 0,
  "ecg" : true,
  "skin" : "string",
  "temperature" : "string",
  "systolic_blood_pressure" : 0,
  "diastolic_blood_pressure" : 0,
  "pupils" : "string",
  "pain" : 0,
  "glycemia" : 0,
  "news" : 0,
  "victim" : 0,
  "glasgow_scale" : {
    "eyes" : 0,
    "verbal" : 0,
    "motor" : 0,
    "total" : 0
  }
}
```


<a name="hospitals_list"></a>
### GET /hospitals/

#### Description
List all Hospitals


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Hospital](#hospital) > array|


#### Tags

* hospitals


#### Example HTTP request

##### Request path
```
/hospitals/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "name" : "string",
  "address" : "string",
  "capacity" : 0,
  "current_capacity" : 0,
  "contact" : 0,
  "image_url" : "string"
} ]
```


<a name="hospitals_victims_list"></a>
### GET /hospitals/victims/

#### Description
List all Victims of a Hospital


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Victim](#victim) > array|


#### Tags

* hospitals


#### Example HTTP request

##### Request path
```
/hospitals/victims/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "name" : "string",
  "birthdate" : "1970-01-01",
  "age" : 0,
  "gender" : "string",
  "identity_number" : "string",
  "address" : "string",
  "circumstances" : "string",
  "disease_history" : "string",
  "allergies" : "string",
  "last_meal" : "string",
  "last_meal_time" : "1970-01-01T00:00:00Z",
  "usual_medication" : "string",
  "risk_situation" : "string",
  "medical_followup" : true,
  "hospital_checkin_date" : "1970-01-01T00:00:00Z",
  "episode_number" : 0,
  "comments" : "string",
  "type_of_emergency" : "string",
  "type_of_transport" : 0,
  "non_transport_reason" : 0,
  "occurrence" : 0,
  "hospital" : 0
} ]
```


<a name="login_create"></a>
### POST /login/

#### Description
User Login


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Body**|**data**  <br>*required*|[data](#login_create-data)|

<a name="login_create-data"></a>
**data**

| Name                         | Description              | Schema |
|------------------------------|--------------------------|--------|
| **password**  <br>*required* | **Example** : `"string"` | string |
| **username**  <br>*required* | **Example** : `"string"` | string |


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[Response 200](#login_create-response-200)|

<a name="login_create-response-200"></a>
**Response 200**

|Name|Description|Schema|
|---|---|---|
|**is_dispatcher**  <br>*optional*|**Example** : `true`|boolean|
|**is_hospitalstaff**  <br>*optional*|**Example** : `true`|boolean|
|**is_technician**  <br>*optional*|**Example** : `true`|boolean|
|**token**  <br>*optional*|**Example** : `"string"`|string|
|**user**  <br>*optional*|**Example** : `"object"`|[user](#login-post-user)|

<a name="login-post-user"></a>
**user**

|Name|Description|Schema|
|---|---|---|
|**email**  <br>*optional*|**Example** : `"string"`|string|
|**first_name**  <br>*optional*|**Example** : `"string"`|string|
|**id**  <br>*optional*|**Example** : `0`|integer|
|**last_name**  <br>*optional*|**Example** : `"string"`|string|
|**username**  <br>*optional*|**Example** : `"string"`|string|


#### Tags

* login


#### Example HTTP request

##### Request path
```
/login/
```


##### Request body
```json
{
  "username" : "string",
  "password" : "string"
}
```


#### Example HTTP response

##### Response 200
```json
{
  "token" : "string",
  "user" : "object",
  "is_technician" : true,
  "is_dispatcher" : true,
  "is_hospitalstaff" : true
}
```


<a name="logout_list"></a>
### GET /logout/

#### Description
User Logout


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|No Content|


#### Tags

* logout


#### Example HTTP request

##### Request path
```
/logout/
```


##### Request header
```json
Authorization:"string"
```


<a name="news_list"></a>
### GET /news/

#### Description
List all News


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [News](#news) > array|


#### Tags

* news


#### Example HTTP request

##### Request path
```
/news/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "title" : "string",
  "description" : "string",
  "image_url" : "string"
} ]
```


<a name="occurrence_create"></a>
### POST /occurrence/

#### Description
Create or Update an Occurrence


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Body**|**data**  <br>*required*|[Occurrence](#occurrence)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[Occurrence](#occurrence)|


#### Tags

* occurrence


#### Example HTTP request

##### Request path
```
/occurrence/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_by" : 0,
  "created_on" : "1970-01-01T00:00:00Z",
  "team" : 0,
  "central" : 0
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_by" : 0,
  "created_on" : "1970-01-01T00:00:00Z",
  "team" : 0,
  "central" : 0
}
```


<a name="occurrences_list"></a>
### GET /occurrences/

#### Description
List all Occurrences


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Occurrence](#occurrence) > array|


#### Tags

* occurrences


#### Example HTTP request

##### Request path
```
/occurrences/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_by" : 0,
  "created_on" : "1970-01-01T00:00:00Z",
  "team" : 0,
  "central" : 0
} ]
```


<a name="occurrences_create"></a>
### POST /occurrences/{occurrence_id}/

#### Description
List the details of an Occurrence


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**occurrence_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[OccurrenceDetail](#occurrencedetail)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[OccurrenceDetail](#occurrencedetail)|


#### Tags

* occurrences


#### Example HTTP request

##### Request path
```
/occurrences/string/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_on" : "1970-01-01T00:00:00Z",
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "team" : {
    "id" : 0,
    "technicians" : [ {
      "id" : "string",
      "user" : {
        "id" : 0,
        "username" : "string",
        "first_name" : "string",
        "last_name" : "string",
        "email" : "email@example.com"
      },
      "active" : true,
      "team_leader" : true
    } ],
    "central" : {
      "id" : 0,
      "designation" : "string",
      "address" : "string",
      "area_of_action" : "string",
      "contact" : 0,
      "is_administrative" : true
    },
    "active" : true
  },
  "victims" : [ {
    "id" : 0,
    "name" : "string",
    "birthdate" : "1970-01-01",
    "age" : 0,
    "gender" : "string",
    "identity_number" : "string",
    "address" : "string",
    "circumstances" : "string",
    "disease_history" : "string",
    "allergies" : "string",
    "last_meal" : "string",
    "last_meal_time" : "1970-01-01T00:00:00Z",
    "usual_medication" : "string",
    "risk_situation" : "string",
    "medical_followup" : true,
    "hospital_checkin_date" : "1970-01-01T00:00:00Z",
    "episode_number" : 0,
    "comments" : "string",
    "type_of_emergency" : "string",
    "type_of_transport" : 0,
    "non_transport_reason" : 0,
    "occurrence" : 0,
    "hospital" : 0
  } ],
  "states" : [ {
    "id" : 0,
    "state" : {
      "id" : 0,
      "state" : "string"
    },
    "longitude" : "string",
    "latitude" : "string",
    "date_time" : "1970-01-01T00:00:00Z"
  } ]
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_on" : "1970-01-01T00:00:00Z",
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "team" : {
    "id" : 0,
    "technicians" : [ {
      "id" : "string",
      "user" : {
        "id" : 0,
        "username" : "string",
        "first_name" : "string",
        "last_name" : "string",
        "email" : "email@example.com"
      },
      "active" : true,
      "team_leader" : true
    } ],
    "central" : {
      "id" : 0,
      "designation" : "string",
      "address" : "string",
      "area_of_action" : "string",
      "contact" : 0,
      "is_administrative" : true
    },
    "active" : true
  },
  "victims" : [ {
    "id" : 0,
    "name" : "string",
    "birthdate" : "1970-01-01",
    "age" : 0,
    "gender" : "string",
    "identity_number" : "string",
    "address" : "string",
    "circumstances" : "string",
    "disease_history" : "string",
    "allergies" : "string",
    "last_meal" : "string",
    "last_meal_time" : "1970-01-01T00:00:00Z",
    "usual_medication" : "string",
    "risk_situation" : "string",
    "medical_followup" : true,
    "hospital_checkin_date" : "1970-01-01T00:00:00Z",
    "episode_number" : 0,
    "comments" : "string",
    "type_of_emergency" : "string",
    "type_of_transport" : 0,
    "non_transport_reason" : 0,
    "occurrence" : 0,
    "hospital" : 0
  } ],
  "states" : [ {
    "id" : 0,
    "state" : {
      "id" : 0,
      "state" : "string"
    },
    "longitude" : "string",
    "latitude" : "string",
    "date_time" : "1970-01-01T00:00:00Z"
  } ]
}
```


<a name="occurrences_read"></a>
### GET /occurrences/{occurrence_id}/

#### Description
List the details of an Occurrence


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**occurrence_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[OccurrenceDetail](#occurrencedetail)|


#### Tags

* occurrences


#### Example HTTP request

##### Request path
```
/occurrences/string/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
{
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_on" : "1970-01-01T00:00:00Z",
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "team" : {
    "id" : 0,
    "technicians" : [ {
      "id" : "string",
      "user" : {
        "id" : 0,
        "username" : "string",
        "first_name" : "string",
        "last_name" : "string",
        "email" : "email@example.com"
      },
      "active" : true,
      "team_leader" : true
    } ],
    "central" : {
      "id" : 0,
      "designation" : "string",
      "address" : "string",
      "area_of_action" : "string",
      "contact" : 0,
      "is_administrative" : true
    },
    "active" : true
  },
  "victims" : [ {
    "id" : 0,
    "name" : "string",
    "birthdate" : "1970-01-01",
    "age" : 0,
    "gender" : "string",
    "identity_number" : "string",
    "address" : "string",
    "circumstances" : "string",
    "disease_history" : "string",
    "allergies" : "string",
    "last_meal" : "string",
    "last_meal_time" : "1970-01-01T00:00:00Z",
    "usual_medication" : "string",
    "risk_situation" : "string",
    "medical_followup" : true,
    "hospital_checkin_date" : "1970-01-01T00:00:00Z",
    "episode_number" : 0,
    "comments" : "string",
    "type_of_emergency" : "string",
    "type_of_transport" : 0,
    "non_transport_reason" : 0,
    "occurrence" : 0,
    "hospital" : 0
  } ],
  "states" : [ {
    "id" : 0,
    "state" : {
      "id" : 0,
      "state" : "string"
    },
    "longitude" : "string",
    "latitude" : "string",
    "date_time" : "1970-01-01T00:00:00Z"
  } ]
}
```


<a name="occurrences_states_create"></a>
### POST /occurrences/{occurrence_id}/states/

#### Description
List all States of an Occurrence


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**occurrence_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[OccurrenceState](#occurrencestate)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[OccurrenceState](#occurrencestate)|


#### Tags

* occurrences


#### Example HTTP request

##### Request path
```
/occurrences/string/states/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "state" : {
    "id" : 0,
    "state" : "string"
  },
  "longitude" : "string",
  "latitude" : "string",
  "date_time" : "1970-01-01T00:00:00Z"
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "state" : {
    "id" : 0,
    "state" : "string"
  },
  "longitude" : "string",
  "latitude" : "string",
  "date_time" : "1970-01-01T00:00:00Z"
}
```


<a name="occurrences_states_list"></a>
### GET /occurrences/{occurrence_id}/states/

#### Description
List all States of an Occurrence


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**occurrence_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [OccurrenceState](#occurrencestate) > array|


#### Tags

* occurrences


#### Example HTTP request

##### Request path
```
/occurrences/string/states/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "state" : {
    "id" : 0,
    "state" : "string"
  },
  "longitude" : "string",
  "latitude" : "string",
  "date_time" : "1970-01-01T00:00:00Z"
} ]
```


<a name="occurrences_victims_create"></a>
### POST /occurrences/{occurrence_id}/victims/

#### Description
List all victims of an Occurrence


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**occurrence_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|< [Victim](#victim) > array|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|< [Victim](#victim) > array|


#### Tags

* occurrences


#### Example HTTP request

##### Request path
```
/occurrences/string/victims/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
[ {
  "id" : 0,
  "name" : "string",
  "birthdate" : "1970-01-01",
  "age" : 0,
  "gender" : "string",
  "identity_number" : "string",
  "address" : "string",
  "circumstances" : "string",
  "disease_history" : "string",
  "allergies" : "string",
  "last_meal" : "string",
  "last_meal_time" : "1970-01-01T00:00:00Z",
  "usual_medication" : "string",
  "risk_situation" : "string",
  "medical_followup" : true,
  "hospital_checkin_date" : "1970-01-01T00:00:00Z",
  "episode_number" : 0,
  "comments" : "string",
  "type_of_emergency" : "string",
  "type_of_transport" : 0,
  "non_transport_reason" : 0,
  "occurrence" : 0,
  "hospital" : 0
} ]
```


#### Example HTTP response

##### Response 201
```json
[ {
  "id" : 0,
  "name" : "string",
  "birthdate" : "1970-01-01",
  "age" : 0,
  "gender" : "string",
  "identity_number" : "string",
  "address" : "string",
  "circumstances" : "string",
  "disease_history" : "string",
  "allergies" : "string",
  "last_meal" : "string",
  "last_meal_time" : "1970-01-01T00:00:00Z",
  "usual_medication" : "string",
  "risk_situation" : "string",
  "medical_followup" : true,
  "hospital_checkin_date" : "1970-01-01T00:00:00Z",
  "episode_number" : 0,
  "comments" : "string",
  "type_of_emergency" : "string",
  "type_of_transport" : 0,
  "non_transport_reason" : 0,
  "occurrence" : 0,
  "hospital" : 0
} ]
```


<a name="occurrences_victims_list"></a>
### GET /occurrences/{occurrence_id}/victims/

#### Description
List all victims of an Occurrence


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**occurrence_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Victim](#victim) > array|


#### Tags

* occurrences


#### Example HTTP request

##### Request path
```
/occurrences/string/victims/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "name" : "string",
  "birthdate" : "1970-01-01",
  "age" : 0,
  "gender" : "string",
  "identity_number" : "string",
  "address" : "string",
  "circumstances" : "string",
  "disease_history" : "string",
  "allergies" : "string",
  "last_meal" : "string",
  "last_meal_time" : "1970-01-01T00:00:00Z",
  "usual_medication" : "string",
  "risk_situation" : "string",
  "medical_followup" : true,
  "hospital_checkin_date" : "1970-01-01T00:00:00Z",
  "episode_number" : 0,
  "comments" : "string",
  "type_of_emergency" : "string",
  "type_of_transport" : 0,
  "non_transport_reason" : 0,
  "occurrence" : 0,
  "hospital" : 0
} ]
```


<a name="pharmacy_create"></a>
### POST /pharmacy/

#### Description
Create or Update a Pharmacy


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Body**|**data**  <br>*required*|[Pharmacy](#pharmacy)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[Pharmacy](#pharmacy)|


#### Tags

* pharmacy


#### Example HTTP request

##### Request path
```
/pharmacy/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "time" : "1970-01-01T00:00:00Z",
  "pharmacy" : "string",
  "dose" : "string",
  "route" : "string",
  "adverse_effect" : "string",
  "victim" : 0
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "time" : "1970-01-01T00:00:00Z",
  "pharmacy" : "string",
  "dose" : "string",
  "route" : "string",
  "adverse_effect" : "string",
  "victim" : 0
}
```


<a name="teams_create"></a>
### POST /teams/

#### Description
List all Teams


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Body**|**data**  <br>*required*|[Team](#team)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[Team](#team)|


#### Tags

* teams


#### Example HTTP request

##### Request path
```
/teams/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "technicians" : [ {
    "id" : "string",
    "user" : {
      "id" : 0,
      "username" : "string",
      "first_name" : "string",
      "last_name" : "string",
      "email" : "email@example.com"
    },
    "active" : true,
    "team_leader" : true
  } ],
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "active" : true
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "technicians" : [ {
    "id" : "string",
    "user" : {
      "id" : 0,
      "username" : "string",
      "first_name" : "string",
      "last_name" : "string",
      "email" : "email@example.com"
    },
    "active" : true,
    "team_leader" : true
  } ],
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "active" : true
}
```


<a name="teams_list"></a>
### GET /teams/

#### Description
List all Teams


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Team](#team) > array|


#### Tags

* teams


#### Example HTTP request

##### Request path
```
/teams/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "technicians" : [ {
    "id" : "string",
    "user" : {
      "id" : 0,
      "username" : "string",
      "first_name" : "string",
      "last_name" : "string",
      "email" : "email@example.com"
    },
    "active" : true,
    "team_leader" : true
  } ],
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "active" : true
} ]
```


<a name="teams_read"></a>
### GET /teams/{team_id}/

#### Description
List the details of a Team


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**team_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[Team](#team)|


#### Tags

* teams


#### Example HTTP request

##### Request path
```
/teams/string/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
{
  "id" : 0,
  "technicians" : [ {
    "id" : "string",
    "user" : {
      "id" : 0,
      "username" : "string",
      "first_name" : "string",
      "last_name" : "string",
      "email" : "email@example.com"
    },
    "active" : true,
    "team_leader" : true
  } ],
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "active" : true
}
```


<a name="teams_update"></a>
### PUT /teams/{team_id}/

#### Description
List the details of a Team


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**team_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[Team](#team)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[Team](#team)|


#### Tags

* teams


#### Example HTTP request

##### Request path
```
/teams/string/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "technicians" : [ {
    "id" : "string",
    "user" : {
      "id" : 0,
      "username" : "string",
      "first_name" : "string",
      "last_name" : "string",
      "email" : "email@example.com"
    },
    "active" : true,
    "team_leader" : true
  } ],
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "active" : true
}
```


#### Example HTTP response

##### Response 200
```json
{
  "id" : 0,
  "technicians" : [ {
    "id" : "string",
    "user" : {
      "id" : 0,
      "username" : "string",
      "first_name" : "string",
      "last_name" : "string",
      "email" : "email@example.com"
    },
    "active" : true,
    "team_leader" : true
  } ],
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "active" : true
}
```


<a name="teams_occurrences_create"></a>
### POST /teams/{team_id}/occurrences/

#### Description
List all Occurrences for a specific Team


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**team_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[Occurrence](#occurrence)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[Occurrence](#occurrence)|


#### Tags

* teams


#### Example HTTP request

##### Request path
```
/teams/string/occurrences/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_by" : 0,
  "created_on" : "1970-01-01T00:00:00Z",
  "team" : 0,
  "central" : 0
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_by" : 0,
  "created_on" : "1970-01-01T00:00:00Z",
  "team" : 0,
  "central" : 0
}
```


<a name="teams_occurrences_list"></a>
### GET /teams/{team_id}/occurrences/

#### Description
List all Occurrences for a specific Team


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**team_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Occurrence](#occurrence) > array|


#### Tags

* teams


#### Example HTTP request

##### Request path
```
/teams/string/occurrences/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_by" : 0,
  "created_on" : "1970-01-01T00:00:00Z",
  "team" : 0,
  "central" : 0
} ]
```


<a name="technician_by_token_list"></a>
### GET /technician/by_token/

#### Description
List the details of a Technician


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[TechnicianDetail](#techniciandetail)|


#### Tags

* technician


#### Example HTTP request

##### Request path
```
/technician/by_token/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
{
  "id" : "string",
  "user" : {
    "id" : 0,
    "username" : "string",
    "first_name" : "string",
    "last_name" : "string",
    "email" : "email@example.com"
  },
  "active" : true,
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  }
}
```


<a name="technician_occurrence_list"></a>
### GET /technician/{technician_id}/occurrence/

#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**technician_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[OccurrenceAllDetails](#occurrencealldetails)|


#### Tags

* technician


#### Example HTTP request

##### Request path
```
/technician/string/occurrence/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
{
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_on" : "1970-01-01T00:00:00Z",
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "team" : {
    "id" : 0,
    "technicians" : [ {
      "id" : "string",
      "user" : {
        "id" : 0,
        "username" : "string",
        "first_name" : "string",
        "last_name" : "string",
        "email" : "email@example.com"
      },
      "active" : true,
      "team_leader" : true
    } ],
    "central" : {
      "id" : 0,
      "designation" : "string",
      "address" : "string",
      "area_of_action" : "string",
      "contact" : 0,
      "is_administrative" : true
    },
    "active" : true
  },
  "victims" : [ {
    "id" : 0,
    "name" : "string",
    "birthdate" : "1970-01-01",
    "age" : 0,
    "gender" : "string",
    "identity_number" : "string",
    "address" : "string",
    "circumstances" : "string",
    "disease_history" : "string",
    "allergies" : "string",
    "last_meal" : "string",
    "last_meal_time" : "1970-01-01T00:00:00Z",
    "usual_medication" : "string",
    "risk_situation" : "string",
    "medical_followup" : true,
    "hospital_checkin_date" : "1970-01-01T00:00:00Z",
    "episode_number" : 0,
    "comments" : "string",
    "type_of_emergency" : "string",
    "type_of_transport" : "string",
    "non_transport_reason" : "string",
    "occurrence" : {
      "id" : 0,
      "occurrence_number" : 0
    },
    "evaluations" : [ {
      "id" : 0,
      "hours" : "1970-01-01T00:00:00Z",
      "avds" : "string",
      "ventilation" : 0,
      "spo2" : 0,
      "o2" : 0,
      "etco2" : 0,
      "pulse" : 0,
      "ecg" : true,
      "skin" : "string",
      "temperature" : "string",
      "systolic_blood_pressure" : 0,
      "diastolic_blood_pressure" : 0,
      "pupils" : "string",
      "pain" : 0,
      "glycemia" : 0,
      "news" : 0,
      "victim" : 0,
      "glasgow_scale" : {
        "eyes" : 0,
        "verbal" : 0,
        "motor" : 0,
        "total" : 0
      }
    } ],
    "symptom" : {
      "comments" : "string",
      "traumas" : [ {
        "id" : 0,
        "body_part" : "string",
        "type_of_injury" : "string",
        "closed" : true,
        "burn_degree" : "string"
      } ],
      "victim" : 0,
      "total_burn_area" : "string"
    },
    "procedure_rcp" : {
      "witnessed" : true,
      "SBV_DAE" : "1970-01-01T00:00:00Z",
      "SIV_SAV" : "1970-01-01T00:00:00Z",
      "first_rhythm" : "string",
      "nr_shocks" : 0,
      "recovery" : "1970-01-01T00:00:00Z",
      "downtime" : "1970-01-01T00:00:00Z",
      "mechanical_compressions" : true,
      "not_performed" : true,
      "victim" : 0
    },
    "procedure_ventilation" : {
      "clearance" : true,
      "oropharyngeal" : true,
      "laryngeal_tube" : true,
      "endotracheal" : true,
      "laryngeal_mask" : true,
      "mechanical_ventilation" : true,
      "cpap" : true,
      "victim" : 0
    },
    "procedure_protocol" : {
      "immobilization" : true,
      "TEPH" : true,
      "SIV" : true,
      "VV_AVC" : true,
      "VV_coronary" : true,
      "VV_sepsis" : true,
      "VV_trauma" : true,
      "VV_PCR" : true,
      "victim" : 0
    },
    "procedure_circulation" : {
      "temperature_monitoring" : true,
      "compression" : true,
      "tourniquet" : true,
      "pelvic_belt" : true,
      "venous_access" : true,
      "patch" : true,
      "ecg" : true,
      "victim" : 0
    },
    "procedure_scale" : {
      "cincinatti" : 0,
      "PROACS" : 0,
      "RTS" : 0,
      "MGAP" : 0,
      "RACE" : 0,
      "victim" : 0
    },
    "pharmacies" : [ {
      "id" : 0,
      "time" : "1970-01-01T00:00:00Z",
      "pharmacy" : "string",
      "dose" : "string",
      "route" : "string",
      "adverse_effect" : "string",
      "victim" : 0
    } ],
    "hospital" : {
      "id" : 0,
      "name" : "string",
      "address" : "string",
      "capacity" : 0,
      "current_capacity" : 0,
      "contact" : 0,
      "image_url" : "string"
    }
  } ],
  "states" : [ {
    "id" : 0,
    "state" : {
      "id" : 0,
      "state" : "string"
    },
    "longitude" : "string",
    "latitude" : "string",
    "date_time" : "1970-01-01T00:00:00Z"
  } ]
}
```


<a name="technician_occurrence_update"></a>
### PUT /technician/{technician_id}/occurrence/

#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**technician_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[OccurrenceAllDetails](#occurrencealldetails)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[OccurrenceAllDetails](#occurrencealldetails)|


#### Tags

* technician


#### Example HTTP request

##### Request path
```
/technician/string/occurrence/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_on" : "1970-01-01T00:00:00Z",
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "team" : {
    "id" : 0,
    "technicians" : [ {
      "id" : "string",
      "user" : {
        "id" : 0,
        "username" : "string",
        "first_name" : "string",
        "last_name" : "string",
        "email" : "email@example.com"
      },
      "active" : true,
      "team_leader" : true
    } ],
    "central" : {
      "id" : 0,
      "designation" : "string",
      "address" : "string",
      "area_of_action" : "string",
      "contact" : 0,
      "is_administrative" : true
    },
    "active" : true
  },
  "victims" : [ {
    "id" : 0,
    "name" : "string",
    "birthdate" : "1970-01-01",
    "age" : 0,
    "gender" : "string",
    "identity_number" : "string",
    "address" : "string",
    "circumstances" : "string",
    "disease_history" : "string",
    "allergies" : "string",
    "last_meal" : "string",
    "last_meal_time" : "1970-01-01T00:00:00Z",
    "usual_medication" : "string",
    "risk_situation" : "string",
    "medical_followup" : true,
    "hospital_checkin_date" : "1970-01-01T00:00:00Z",
    "episode_number" : 0,
    "comments" : "string",
    "type_of_emergency" : "string",
    "type_of_transport" : "string",
    "non_transport_reason" : "string",
    "occurrence" : {
      "id" : 0,
      "occurrence_number" : 0
    },
    "evaluations" : [ {
      "id" : 0,
      "hours" : "1970-01-01T00:00:00Z",
      "avds" : "string",
      "ventilation" : 0,
      "spo2" : 0,
      "o2" : 0,
      "etco2" : 0,
      "pulse" : 0,
      "ecg" : true,
      "skin" : "string",
      "temperature" : "string",
      "systolic_blood_pressure" : 0,
      "diastolic_blood_pressure" : 0,
      "pupils" : "string",
      "pain" : 0,
      "glycemia" : 0,
      "news" : 0,
      "victim" : 0,
      "glasgow_scale" : {
        "eyes" : 0,
        "verbal" : 0,
        "motor" : 0,
        "total" : 0
      }
    } ],
    "symptom" : {
      "comments" : "string",
      "traumas" : [ {
        "id" : 0,
        "body_part" : "string",
        "type_of_injury" : "string",
        "closed" : true,
        "burn_degree" : "string"
      } ],
      "victim" : 0,
      "total_burn_area" : "string"
    },
    "procedure_rcp" : {
      "witnessed" : true,
      "SBV_DAE" : "1970-01-01T00:00:00Z",
      "SIV_SAV" : "1970-01-01T00:00:00Z",
      "first_rhythm" : "string",
      "nr_shocks" : 0,
      "recovery" : "1970-01-01T00:00:00Z",
      "downtime" : "1970-01-01T00:00:00Z",
      "mechanical_compressions" : true,
      "not_performed" : true,
      "victim" : 0
    },
    "procedure_ventilation" : {
      "clearance" : true,
      "oropharyngeal" : true,
      "laryngeal_tube" : true,
      "endotracheal" : true,
      "laryngeal_mask" : true,
      "mechanical_ventilation" : true,
      "cpap" : true,
      "victim" : 0
    },
    "procedure_protocol" : {
      "immobilization" : true,
      "TEPH" : true,
      "SIV" : true,
      "VV_AVC" : true,
      "VV_coronary" : true,
      "VV_sepsis" : true,
      "VV_trauma" : true,
      "VV_PCR" : true,
      "victim" : 0
    },
    "procedure_circulation" : {
      "temperature_monitoring" : true,
      "compression" : true,
      "tourniquet" : true,
      "pelvic_belt" : true,
      "venous_access" : true,
      "patch" : true,
      "ecg" : true,
      "victim" : 0
    },
    "procedure_scale" : {
      "cincinatti" : 0,
      "PROACS" : 0,
      "RTS" : 0,
      "MGAP" : 0,
      "RACE" : 0,
      "victim" : 0
    },
    "pharmacies" : [ {
      "id" : 0,
      "time" : "1970-01-01T00:00:00Z",
      "pharmacy" : "string",
      "dose" : "string",
      "route" : "string",
      "adverse_effect" : "string",
      "victim" : 0
    } ],
    "hospital" : {
      "id" : 0,
      "name" : "string",
      "address" : "string",
      "capacity" : 0,
      "current_capacity" : 0,
      "contact" : 0,
      "image_url" : "string"
    }
  } ],
  "states" : [ {
    "id" : 0,
    "state" : {
      "id" : 0,
      "state" : "string"
    },
    "longitude" : "string",
    "latitude" : "string",
    "date_time" : "1970-01-01T00:00:00Z"
  } ]
}
```


#### Example HTTP response

##### Response 200
```json
{
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_on" : "1970-01-01T00:00:00Z",
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "team" : {
    "id" : 0,
    "technicians" : [ {
      "id" : "string",
      "user" : {
        "id" : 0,
        "username" : "string",
        "first_name" : "string",
        "last_name" : "string",
        "email" : "email@example.com"
      },
      "active" : true,
      "team_leader" : true
    } ],
    "central" : {
      "id" : 0,
      "designation" : "string",
      "address" : "string",
      "area_of_action" : "string",
      "contact" : 0,
      "is_administrative" : true
    },
    "active" : true
  },
  "victims" : [ {
    "id" : 0,
    "name" : "string",
    "birthdate" : "1970-01-01",
    "age" : 0,
    "gender" : "string",
    "identity_number" : "string",
    "address" : "string",
    "circumstances" : "string",
    "disease_history" : "string",
    "allergies" : "string",
    "last_meal" : "string",
    "last_meal_time" : "1970-01-01T00:00:00Z",
    "usual_medication" : "string",
    "risk_situation" : "string",
    "medical_followup" : true,
    "hospital_checkin_date" : "1970-01-01T00:00:00Z",
    "episode_number" : 0,
    "comments" : "string",
    "type_of_emergency" : "string",
    "type_of_transport" : "string",
    "non_transport_reason" : "string",
    "occurrence" : {
      "id" : 0,
      "occurrence_number" : 0
    },
    "evaluations" : [ {
      "id" : 0,
      "hours" : "1970-01-01T00:00:00Z",
      "avds" : "string",
      "ventilation" : 0,
      "spo2" : 0,
      "o2" : 0,
      "etco2" : 0,
      "pulse" : 0,
      "ecg" : true,
      "skin" : "string",
      "temperature" : "string",
      "systolic_blood_pressure" : 0,
      "diastolic_blood_pressure" : 0,
      "pupils" : "string",
      "pain" : 0,
      "glycemia" : 0,
      "news" : 0,
      "victim" : 0,
      "glasgow_scale" : {
        "eyes" : 0,
        "verbal" : 0,
        "motor" : 0,
        "total" : 0
      }
    } ],
    "symptom" : {
      "comments" : "string",
      "traumas" : [ {
        "id" : 0,
        "body_part" : "string",
        "type_of_injury" : "string",
        "closed" : true,
        "burn_degree" : "string"
      } ],
      "victim" : 0,
      "total_burn_area" : "string"
    },
    "procedure_rcp" : {
      "witnessed" : true,
      "SBV_DAE" : "1970-01-01T00:00:00Z",
      "SIV_SAV" : "1970-01-01T00:00:00Z",
      "first_rhythm" : "string",
      "nr_shocks" : 0,
      "recovery" : "1970-01-01T00:00:00Z",
      "downtime" : "1970-01-01T00:00:00Z",
      "mechanical_compressions" : true,
      "not_performed" : true,
      "victim" : 0
    },
    "procedure_ventilation" : {
      "clearance" : true,
      "oropharyngeal" : true,
      "laryngeal_tube" : true,
      "endotracheal" : true,
      "laryngeal_mask" : true,
      "mechanical_ventilation" : true,
      "cpap" : true,
      "victim" : 0
    },
    "procedure_protocol" : {
      "immobilization" : true,
      "TEPH" : true,
      "SIV" : true,
      "VV_AVC" : true,
      "VV_coronary" : true,
      "VV_sepsis" : true,
      "VV_trauma" : true,
      "VV_PCR" : true,
      "victim" : 0
    },
    "procedure_circulation" : {
      "temperature_monitoring" : true,
      "compression" : true,
      "tourniquet" : true,
      "pelvic_belt" : true,
      "venous_access" : true,
      "patch" : true,
      "ecg" : true,
      "victim" : 0
    },
    "procedure_scale" : {
      "cincinatti" : 0,
      "PROACS" : 0,
      "RTS" : 0,
      "MGAP" : 0,
      "RACE" : 0,
      "victim" : 0
    },
    "pharmacies" : [ {
      "id" : 0,
      "time" : "1970-01-01T00:00:00Z",
      "pharmacy" : "string",
      "dose" : "string",
      "route" : "string",
      "adverse_effect" : "string",
      "victim" : 0
    } ],
    "hospital" : {
      "id" : 0,
      "name" : "string",
      "address" : "string",
      "capacity" : 0,
      "current_capacity" : 0,
      "contact" : 0,
      "image_url" : "string"
    }
  } ],
  "states" : [ {
    "id" : 0,
    "state" : {
      "id" : 0,
      "state" : "string"
    },
    "longitude" : "string",
    "latitude" : "string",
    "date_time" : "1970-01-01T00:00:00Z"
  } ]
}
```


<a name="technician_occurrences_list"></a>
### GET /technician/{technician_id}/occurrences/

#### Description
List the occurrences of a Technician


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**technician_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [OccurrenceAllDetails](#occurrencealldetails) > array|


#### Tags

* technician


#### Example HTTP request

##### Request path
```
/technician/string/occurrences/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_on" : "1970-01-01T00:00:00Z",
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "team" : {
    "id" : 0,
    "technicians" : [ {
      "id" : "string",
      "user" : {
        "id" : 0,
        "username" : "string",
        "first_name" : "string",
        "last_name" : "string",
        "email" : "email@example.com"
      },
      "active" : true,
      "team_leader" : true
    } ],
    "central" : {
      "id" : 0,
      "designation" : "string",
      "address" : "string",
      "area_of_action" : "string",
      "contact" : 0,
      "is_administrative" : true
    },
    "active" : true
  },
  "victims" : [ {
    "id" : 0,
    "name" : "string",
    "birthdate" : "1970-01-01",
    "age" : 0,
    "gender" : "string",
    "identity_number" : "string",
    "address" : "string",
    "circumstances" : "string",
    "disease_history" : "string",
    "allergies" : "string",
    "last_meal" : "string",
    "last_meal_time" : "1970-01-01T00:00:00Z",
    "usual_medication" : "string",
    "risk_situation" : "string",
    "medical_followup" : true,
    "hospital_checkin_date" : "1970-01-01T00:00:00Z",
    "episode_number" : 0,
    "comments" : "string",
    "type_of_emergency" : "string",
    "type_of_transport" : "string",
    "non_transport_reason" : "string",
    "occurrence" : {
      "id" : 0,
      "occurrence_number" : 0
    },
    "evaluations" : [ {
      "id" : 0,
      "hours" : "1970-01-01T00:00:00Z",
      "avds" : "string",
      "ventilation" : 0,
      "spo2" : 0,
      "o2" : 0,
      "etco2" : 0,
      "pulse" : 0,
      "ecg" : true,
      "skin" : "string",
      "temperature" : "string",
      "systolic_blood_pressure" : 0,
      "diastolic_blood_pressure" : 0,
      "pupils" : "string",
      "pain" : 0,
      "glycemia" : 0,
      "news" : 0,
      "victim" : 0,
      "glasgow_scale" : {
        "eyes" : 0,
        "verbal" : 0,
        "motor" : 0,
        "total" : 0
      }
    } ],
    "symptom" : {
      "comments" : "string",
      "traumas" : [ {
        "id" : 0,
        "body_part" : "string",
        "type_of_injury" : "string",
        "closed" : true,
        "burn_degree" : "string"
      } ],
      "victim" : 0,
      "total_burn_area" : "string"
    },
    "procedure_rcp" : {
      "witnessed" : true,
      "SBV_DAE" : "1970-01-01T00:00:00Z",
      "SIV_SAV" : "1970-01-01T00:00:00Z",
      "first_rhythm" : "string",
      "nr_shocks" : 0,
      "recovery" : "1970-01-01T00:00:00Z",
      "downtime" : "1970-01-01T00:00:00Z",
      "mechanical_compressions" : true,
      "not_performed" : true,
      "victim" : 0
    },
    "procedure_ventilation" : {
      "clearance" : true,
      "oropharyngeal" : true,
      "laryngeal_tube" : true,
      "endotracheal" : true,
      "laryngeal_mask" : true,
      "mechanical_ventilation" : true,
      "cpap" : true,
      "victim" : 0
    },
    "procedure_protocol" : {
      "immobilization" : true,
      "TEPH" : true,
      "SIV" : true,
      "VV_AVC" : true,
      "VV_coronary" : true,
      "VV_sepsis" : true,
      "VV_trauma" : true,
      "VV_PCR" : true,
      "victim" : 0
    },
    "procedure_circulation" : {
      "temperature_monitoring" : true,
      "compression" : true,
      "tourniquet" : true,
      "pelvic_belt" : true,
      "venous_access" : true,
      "patch" : true,
      "ecg" : true,
      "victim" : 0
    },
    "procedure_scale" : {
      "cincinatti" : 0,
      "PROACS" : 0,
      "RTS" : 0,
      "MGAP" : 0,
      "RACE" : 0,
      "victim" : 0
    },
    "pharmacies" : [ {
      "id" : 0,
      "time" : "1970-01-01T00:00:00Z",
      "pharmacy" : "string",
      "dose" : "string",
      "route" : "string",
      "adverse_effect" : "string",
      "victim" : 0
    } ],
    "hospital" : {
      "id" : 0,
      "name" : "string",
      "address" : "string",
      "capacity" : 0,
      "current_capacity" : 0,
      "contact" : 0,
      "image_url" : "string"
    }
  } ],
  "states" : [ {
    "id" : 0,
    "state" : {
      "id" : 0,
      "state" : "string"
    },
    "longitude" : "string",
    "latitude" : "string",
    "date_time" : "1970-01-01T00:00:00Z"
  } ]
} ]
```


<a name="technician_team_list"></a>
### GET /technician/{technician_id}/team/

#### Description
List the active Team of a Technician


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**technician_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[Team](#team)|


#### Tags

* technician


#### Example HTTP request

##### Request path
```
/technician/string/team/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
{
  "id" : 0,
  "technicians" : [ {
    "id" : "string",
    "user" : {
      "id" : 0,
      "username" : "string",
      "first_name" : "string",
      "last_name" : "string",
      "email" : "email@example.com"
    },
    "active" : true,
    "team_leader" : true
  } ],
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "active" : true
}
```


<a name="user_create"></a>
### POST /user/

#### Description
Create or Update a SIREPH User


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Body**|**data**  <br>*required*|[User](#user)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[User](#user)|


#### Tags

* user


#### Example HTTP request

##### Request path
```
/user/
```


##### Request body
```json
{
  "id" : 0,
  "username" : "string",
  "first_name" : "string",
  "last_name" : "string",
  "email" : "email@example.com",
  "password" : "string"
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "username" : "string",
  "first_name" : "string",
  "last_name" : "string",
  "email" : "email@example.com",
  "password" : "string"
}
```


<a name="user_by_token_list"></a>
### GET /user/by_token/

#### Description
List the details of a User


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[UserSimplified](#usersimplified)|


#### Tags

* user


#### Example HTTP request

##### Request path
```
/user/by_token/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
{
  "id" : 0,
  "username" : "string",
  "first_name" : "string",
  "last_name" : "string",
  "email" : "email@example.com"
}
```


<a name="user_read"></a>
### GET /user/{user_id}/

#### Description
List the details of a User


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**user_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [UserSimplified](#usersimplified) > array|


#### Tags

* user


#### Example HTTP request

##### Request path
```
/user/string/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "username" : "string",
  "first_name" : "string",
  "last_name" : "string",
  "email" : "email@example.com"
} ]
```


<a name="user_central_list"></a>
### GET /user/{user_id}/central/

#### Description
Lists the Central of a User


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**user_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [DispatcherDetail](#dispatcherdetail) > array|


#### Tags

* user


#### Example HTTP request

##### Request path
```
/user/string/central/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : "string",
  "username" : "string",
  "first_name" : "string",
  "last_name" : "string",
  "active" : true,
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  }
} ]
```


<a name="user_dispatcher_list"></a>
### GET /user/{user_id}/dispatcher/

#### Description
List a specific User that is a Dispatcher


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**user_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Dispatcher](#dispatcher) > array|


#### Tags

* user


#### Example HTTP request

##### Request path
```
/user/string/dispatcher/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : "string",
  "username" : "string",
  "first_name" : "string",
  "last_name" : "string",
  "active" : true,
  "central" : 0
} ]
```


<a name="user_hospital_list"></a>
### GET /user/{user_id}/hospital/

#### Description
Lists the hospital of the current user


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**user_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [HospitalStaffDetail](#hospitalstaffdetail) > array|


#### Tags

* user


#### Example HTTP request

##### Request path
```
/user/string/hospital/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : "string",
  "username" : "string",
  "first_name" : "string",
  "last_name" : "string",
  "active" : true,
  "hospital" : {
    "id" : 0,
    "name" : "string",
    "address" : "string",
    "capacity" : 0,
    "current_capacity" : 0,
    "contact" : 0,
    "image_url" : "string"
  }
} ]
```


<a name="users_list"></a>
### GET /users/

#### Description
List all Users


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [UserSimplified](#usersimplified) > array|


#### Tags

* users


#### Example HTTP request

##### Request path
```
/users/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "username" : "string",
  "first_name" : "string",
  "last_name" : "string",
  "email" : "email@example.com"
} ]
```


<a name="users_dispatchers_list"></a>
### GET /users/dispatchers/

#### Description
List all Dispatchers


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Dispatcher](#dispatcher) > array|


#### Tags

* users


#### Example HTTP request

##### Request path
```
/users/dispatchers/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : "string",
  "username" : "string",
  "first_name" : "string",
  "last_name" : "string",
  "active" : true,
  "central" : 0
} ]
```


<a name="users_employees_list"></a>
### GET /users/employees/

#### Description
List all Hospital Staff Users


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [HospitalStaff](#hospitalstaff) > array|


#### Tags

* users


#### Example HTTP request

##### Request path
```
/users/employees/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : "string",
  "username" : "string",
  "first_name" : "string",
  "last_name" : "string",
  "active" : true,
  "hospital" : 0
} ]
```


<a name="users_teams_create"></a>
### POST /users/{user_id}/teams/

#### Description
List the teams of a User


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Path**|**user_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[Team](#team)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[Team](#team)|


#### Tags

* users


#### Example HTTP request

##### Request path
```
/users/string/teams/
```


##### Request body
```json
{
  "id" : 0,
  "technicians" : [ {
    "id" : "string",
    "user" : {
      "id" : 0,
      "username" : "string",
      "first_name" : "string",
      "last_name" : "string",
      "email" : "email@example.com"
    },
    "active" : true,
    "team_leader" : true
  } ],
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "active" : true
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "technicians" : [ {
    "id" : "string",
    "user" : {
      "id" : 0,
      "username" : "string",
      "first_name" : "string",
      "last_name" : "string",
      "email" : "email@example.com"
    },
    "active" : true,
    "team_leader" : true
  } ],
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "active" : true
}
```


<a name="users_teams_list"></a>
### GET /users/{user_id}/teams/

#### Description
List the teams of a User


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Path**|**user_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[Team](#team)|


#### Tags

* users


#### Example HTTP request

##### Request path
```
/users/string/teams/
```


#### Example HTTP response

##### Response 200
```json
{
  "id" : 0,
  "technicians" : [ {
    "id" : "string",
    "user" : {
      "id" : 0,
      "username" : "string",
      "first_name" : "string",
      "last_name" : "string",
      "email" : "email@example.com"
    },
    "active" : true,
    "team_leader" : true
  } ],
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "active" : true
}
```


<a name="victim_create"></a>
### POST /victim/

#### Description
Create or Update a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Body**|**data**  <br>*required*|[Victim](#victim)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[Victim](#victim)|


#### Tags

* victim


#### Example HTTP request

##### Request path
```
/victim/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "name" : "string",
  "birthdate" : "1970-01-01",
  "age" : 0,
  "gender" : "string",
  "identity_number" : "string",
  "address" : "string",
  "circumstances" : "string",
  "disease_history" : "string",
  "allergies" : "string",
  "last_meal" : "string",
  "last_meal_time" : "1970-01-01T00:00:00Z",
  "usual_medication" : "string",
  "risk_situation" : "string",
  "medical_followup" : true,
  "hospital_checkin_date" : "1970-01-01T00:00:00Z",
  "episode_number" : 0,
  "comments" : "string",
  "type_of_emergency" : "string",
  "type_of_transport" : 0,
  "non_transport_reason" : 0,
  "occurrence" : 0,
  "hospital" : 0
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "name" : "string",
  "birthdate" : "1970-01-01",
  "age" : 0,
  "gender" : "string",
  "identity_number" : "string",
  "address" : "string",
  "circumstances" : "string",
  "disease_history" : "string",
  "allergies" : "string",
  "last_meal" : "string",
  "last_meal_time" : "1970-01-01T00:00:00Z",
  "usual_medication" : "string",
  "risk_situation" : "string",
  "medical_followup" : true,
  "hospital_checkin_date" : "1970-01-01T00:00:00Z",
  "episode_number" : 0,
  "comments" : "string",
  "type_of_emergency" : "string",
  "type_of_transport" : 0,
  "non_transport_reason" : 0,
  "occurrence" : 0,
  "hospital" : 0
}
```


<a name="victim_occurrences_list"></a>
### GET /victim/{user_id}/occurrences

#### Description
List all Occurrences of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**user_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [OccurrenceDetail](#occurrencedetail) > array|


#### Tags

* victim


#### Example HTTP request

##### Request path
```
/victim/string/occurrences
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "occurrence_number" : 0,
  "entity" : "string",
  "mean_of_assistance" : "string",
  "motive" : "string",
  "number_of_victims" : 0,
  "local" : "string",
  "gps_coordinates" : "string",
  "parish" : "string",
  "municipality" : "string",
  "active" : true,
  "alert_mode" : true,
  "created_on" : "1970-01-01T00:00:00Z",
  "central" : {
    "id" : 0,
    "designation" : "string",
    "address" : "string",
    "area_of_action" : "string",
    "contact" : 0,
    "is_administrative" : true
  },
  "team" : {
    "id" : 0,
    "technicians" : [ {
      "id" : "string",
      "user" : {
        "id" : 0,
        "username" : "string",
        "first_name" : "string",
        "last_name" : "string",
        "email" : "email@example.com"
      },
      "active" : true,
      "team_leader" : true
    } ],
    "central" : {
      "id" : 0,
      "designation" : "string",
      "address" : "string",
      "area_of_action" : "string",
      "contact" : 0,
      "is_administrative" : true
    },
    "active" : true
  },
  "victims" : [ {
    "id" : 0,
    "name" : "string",
    "birthdate" : "1970-01-01",
    "age" : 0,
    "gender" : "string",
    "identity_number" : "string",
    "address" : "string",
    "circumstances" : "string",
    "disease_history" : "string",
    "allergies" : "string",
    "last_meal" : "string",
    "last_meal_time" : "1970-01-01T00:00:00Z",
    "usual_medication" : "string",
    "risk_situation" : "string",
    "medical_followup" : true,
    "hospital_checkin_date" : "1970-01-01T00:00:00Z",
    "episode_number" : 0,
    "comments" : "string",
    "type_of_emergency" : "string",
    "type_of_transport" : 0,
    "non_transport_reason" : 0,
    "occurrence" : 0,
    "hospital" : 0
  } ],
  "states" : [ {
    "id" : 0,
    "state" : {
      "id" : 0,
      "state" : "string"
    },
    "longitude" : "string",
    "latitude" : "string",
    "date_time" : "1970-01-01T00:00:00Z"
  } ]
} ]
```


<a name="victims_list"></a>
### GET /victims/

#### Description
List all Victims


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Victim](#victim) > array|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "name" : "string",
  "birthdate" : "1970-01-01",
  "age" : 0,
  "gender" : "string",
  "identity_number" : "string",
  "address" : "string",
  "circumstances" : "string",
  "disease_history" : "string",
  "allergies" : "string",
  "last_meal" : "string",
  "last_meal_time" : "1970-01-01T00:00:00Z",
  "usual_medication" : "string",
  "risk_situation" : "string",
  "medical_followup" : true,
  "hospital_checkin_date" : "1970-01-01T00:00:00Z",
  "episode_number" : 0,
  "comments" : "string",
  "type_of_emergency" : "string",
  "type_of_transport" : 0,
  "non_transport_reason" : 0,
  "occurrence" : 0,
  "hospital" : 0
} ]
```


<a name="victims_read"></a>
### GET /victims/{victim_id}/

#### Description
List the details of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[VictimDetails](#victimdetails)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
{
  "id" : 0,
  "name" : "string",
  "birthdate" : "1970-01-01",
  "age" : 0,
  "gender" : "string",
  "identity_number" : "string",
  "address" : "string",
  "circumstances" : "string",
  "disease_history" : "string",
  "allergies" : "string",
  "last_meal" : "string",
  "last_meal_time" : "1970-01-01T00:00:00Z",
  "usual_medication" : "string",
  "risk_situation" : "string",
  "medical_followup" : true,
  "hospital_checkin_date" : "1970-01-01T00:00:00Z",
  "episode_number" : 0,
  "comments" : "string",
  "type_of_emergency" : "string",
  "type_of_transport" : "string",
  "non_transport_reason" : "string",
  "occurrence" : {
    "id" : 0,
    "occurrence_number" : 0
  },
  "evaluations" : [ {
    "id" : 0,
    "hours" : "1970-01-01T00:00:00Z",
    "avds" : "string",
    "ventilation" : 0,
    "spo2" : 0,
    "o2" : 0,
    "etco2" : 0,
    "pulse" : 0,
    "ecg" : true,
    "skin" : "string",
    "temperature" : "string",
    "systolic_blood_pressure" : 0,
    "diastolic_blood_pressure" : 0,
    "pupils" : "string",
    "pain" : 0,
    "glycemia" : 0,
    "news" : 0,
    "victim" : 0,
    "glasgow_scale" : {
      "eyes" : 0,
      "verbal" : 0,
      "motor" : 0,
      "total" : 0
    }
  } ],
  "symptom" : {
    "comments" : "string",
    "traumas" : [ {
      "id" : 0,
      "body_part" : "string",
      "type_of_injury" : "string",
      "closed" : true,
      "burn_degree" : "string"
    } ],
    "victim" : 0,
    "total_burn_area" : "string"
  },
  "procedure_rcp" : {
    "witnessed" : true,
    "SBV_DAE" : "1970-01-01T00:00:00Z",
    "SIV_SAV" : "1970-01-01T00:00:00Z",
    "first_rhythm" : "string",
    "nr_shocks" : 0,
    "recovery" : "1970-01-01T00:00:00Z",
    "downtime" : "1970-01-01T00:00:00Z",
    "mechanical_compressions" : true,
    "not_performed" : true,
    "victim" : 0
  },
  "procedure_ventilation" : {
    "clearance" : true,
    "oropharyngeal" : true,
    "laryngeal_tube" : true,
    "endotracheal" : true,
    "laryngeal_mask" : true,
    "mechanical_ventilation" : true,
    "cpap" : true,
    "victim" : 0
  },
  "procedure_protocol" : {
    "immobilization" : true,
    "TEPH" : true,
    "SIV" : true,
    "VV_AVC" : true,
    "VV_coronary" : true,
    "VV_sepsis" : true,
    "VV_trauma" : true,
    "VV_PCR" : true,
    "victim" : 0
  },
  "procedure_circulation" : {
    "temperature_monitoring" : true,
    "compression" : true,
    "tourniquet" : true,
    "pelvic_belt" : true,
    "venous_access" : true,
    "patch" : true,
    "ecg" : true,
    "victim" : 0
  },
  "procedure_scale" : {
    "cincinatti" : 0,
    "PROACS" : 0,
    "RTS" : 0,
    "MGAP" : 0,
    "RACE" : 0,
    "victim" : 0
  },
  "pharmacies" : [ {
    "id" : 0,
    "time" : "1970-01-01T00:00:00Z",
    "pharmacy" : "string",
    "dose" : "string",
    "route" : "string",
    "adverse_effect" : "string",
    "victim" : 0
  } ],
  "hospital" : 0
}
```


<a name="victims_update"></a>
### PUT /victims/{victim_id}/

#### Description
List the details of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[VictimDetails](#victimdetails)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[VictimDetails](#victimdetails)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "name" : "string",
  "birthdate" : "1970-01-01",
  "age" : 0,
  "gender" : "string",
  "identity_number" : "string",
  "address" : "string",
  "circumstances" : "string",
  "disease_history" : "string",
  "allergies" : "string",
  "last_meal" : "string",
  "last_meal_time" : "1970-01-01T00:00:00Z",
  "usual_medication" : "string",
  "risk_situation" : "string",
  "medical_followup" : true,
  "hospital_checkin_date" : "1970-01-01T00:00:00Z",
  "episode_number" : 0,
  "comments" : "string",
  "type_of_emergency" : "string",
  "type_of_transport" : "string",
  "non_transport_reason" : "string",
  "occurrence" : {
    "id" : 0,
    "occurrence_number" : 0
  },
  "evaluations" : [ {
    "id" : 0,
    "hours" : "1970-01-01T00:00:00Z",
    "avds" : "string",
    "ventilation" : 0,
    "spo2" : 0,
    "o2" : 0,
    "etco2" : 0,
    "pulse" : 0,
    "ecg" : true,
    "skin" : "string",
    "temperature" : "string",
    "systolic_blood_pressure" : 0,
    "diastolic_blood_pressure" : 0,
    "pupils" : "string",
    "pain" : 0,
    "glycemia" : 0,
    "news" : 0,
    "victim" : 0,
    "glasgow_scale" : {
      "eyes" : 0,
      "verbal" : 0,
      "motor" : 0,
      "total" : 0
    }
  } ],
  "symptom" : {
    "comments" : "string",
    "traumas" : [ {
      "id" : 0,
      "body_part" : "string",
      "type_of_injury" : "string",
      "closed" : true,
      "burn_degree" : "string"
    } ],
    "victim" : 0,
    "total_burn_area" : "string"
  },
  "procedure_rcp" : {
    "witnessed" : true,
    "SBV_DAE" : "1970-01-01T00:00:00Z",
    "SIV_SAV" : "1970-01-01T00:00:00Z",
    "first_rhythm" : "string",
    "nr_shocks" : 0,
    "recovery" : "1970-01-01T00:00:00Z",
    "downtime" : "1970-01-01T00:00:00Z",
    "mechanical_compressions" : true,
    "not_performed" : true,
    "victim" : 0
  },
  "procedure_ventilation" : {
    "clearance" : true,
    "oropharyngeal" : true,
    "laryngeal_tube" : true,
    "endotracheal" : true,
    "laryngeal_mask" : true,
    "mechanical_ventilation" : true,
    "cpap" : true,
    "victim" : 0
  },
  "procedure_protocol" : {
    "immobilization" : true,
    "TEPH" : true,
    "SIV" : true,
    "VV_AVC" : true,
    "VV_coronary" : true,
    "VV_sepsis" : true,
    "VV_trauma" : true,
    "VV_PCR" : true,
    "victim" : 0
  },
  "procedure_circulation" : {
    "temperature_monitoring" : true,
    "compression" : true,
    "tourniquet" : true,
    "pelvic_belt" : true,
    "venous_access" : true,
    "patch" : true,
    "ecg" : true,
    "victim" : 0
  },
  "procedure_scale" : {
    "cincinatti" : 0,
    "PROACS" : 0,
    "RTS" : 0,
    "MGAP" : 0,
    "RACE" : 0,
    "victim" : 0
  },
  "pharmacies" : [ {
    "id" : 0,
    "time" : "1970-01-01T00:00:00Z",
    "pharmacy" : "string",
    "dose" : "string",
    "route" : "string",
    "adverse_effect" : "string",
    "victim" : 0
  } ],
  "hospital" : 0
}
```


#### Example HTTP response

##### Response 200
```json
{
  "id" : 0,
  "name" : "string",
  "birthdate" : "1970-01-01",
  "age" : 0,
  "gender" : "string",
  "identity_number" : "string",
  "address" : "string",
  "circumstances" : "string",
  "disease_history" : "string",
  "allergies" : "string",
  "last_meal" : "string",
  "last_meal_time" : "1970-01-01T00:00:00Z",
  "usual_medication" : "string",
  "risk_situation" : "string",
  "medical_followup" : true,
  "hospital_checkin_date" : "1970-01-01T00:00:00Z",
  "episode_number" : 0,
  "comments" : "string",
  "type_of_emergency" : "string",
  "type_of_transport" : "string",
  "non_transport_reason" : "string",
  "occurrence" : {
    "id" : 0,
    "occurrence_number" : 0
  },
  "evaluations" : [ {
    "id" : 0,
    "hours" : "1970-01-01T00:00:00Z",
    "avds" : "string",
    "ventilation" : 0,
    "spo2" : 0,
    "o2" : 0,
    "etco2" : 0,
    "pulse" : 0,
    "ecg" : true,
    "skin" : "string",
    "temperature" : "string",
    "systolic_blood_pressure" : 0,
    "diastolic_blood_pressure" : 0,
    "pupils" : "string",
    "pain" : 0,
    "glycemia" : 0,
    "news" : 0,
    "victim" : 0,
    "glasgow_scale" : {
      "eyes" : 0,
      "verbal" : 0,
      "motor" : 0,
      "total" : 0
    }
  } ],
  "symptom" : {
    "comments" : "string",
    "traumas" : [ {
      "id" : 0,
      "body_part" : "string",
      "type_of_injury" : "string",
      "closed" : true,
      "burn_degree" : "string"
    } ],
    "victim" : 0,
    "total_burn_area" : "string"
  },
  "procedure_rcp" : {
    "witnessed" : true,
    "SBV_DAE" : "1970-01-01T00:00:00Z",
    "SIV_SAV" : "1970-01-01T00:00:00Z",
    "first_rhythm" : "string",
    "nr_shocks" : 0,
    "recovery" : "1970-01-01T00:00:00Z",
    "downtime" : "1970-01-01T00:00:00Z",
    "mechanical_compressions" : true,
    "not_performed" : true,
    "victim" : 0
  },
  "procedure_ventilation" : {
    "clearance" : true,
    "oropharyngeal" : true,
    "laryngeal_tube" : true,
    "endotracheal" : true,
    "laryngeal_mask" : true,
    "mechanical_ventilation" : true,
    "cpap" : true,
    "victim" : 0
  },
  "procedure_protocol" : {
    "immobilization" : true,
    "TEPH" : true,
    "SIV" : true,
    "VV_AVC" : true,
    "VV_coronary" : true,
    "VV_sepsis" : true,
    "VV_trauma" : true,
    "VV_PCR" : true,
    "victim" : 0
  },
  "procedure_circulation" : {
    "temperature_monitoring" : true,
    "compression" : true,
    "tourniquet" : true,
    "pelvic_belt" : true,
    "venous_access" : true,
    "patch" : true,
    "ecg" : true,
    "victim" : 0
  },
  "procedure_scale" : {
    "cincinatti" : 0,
    "PROACS" : 0,
    "RTS" : 0,
    "MGAP" : 0,
    "RACE" : 0,
    "victim" : 0
  },
  "pharmacies" : [ {
    "id" : 0,
    "time" : "1970-01-01T00:00:00Z",
    "pharmacy" : "string",
    "dose" : "string",
    "route" : "string",
    "adverse_effect" : "string",
    "victim" : 0
  } ],
  "hospital" : 0
}
```


<a name="victims_evaluations_create"></a>
### POST /victims/{victim_id}/evaluations/

#### Description
List the evaluations of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[EvaluationDetail](#evaluationdetail)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[EvaluationDetail](#evaluationdetail)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/evaluations/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "hours" : "1970-01-01T00:00:00Z",
  "avds" : "string",
  "ventilation" : 0,
  "spo2" : 0,
  "o2" : 0,
  "etco2" : 0,
  "pulse" : 0,
  "ecg" : true,
  "skin" : "string",
  "temperature" : "string",
  "systolic_blood_pressure" : 0,
  "diastolic_blood_pressure" : 0,
  "pupils" : "string",
  "pain" : 0,
  "glycemia" : 0,
  "news" : 0,
  "victim" : {
    "id" : 0
  },
  "glasgow_scale" : {
    "eyes" : 0,
    "verbal" : 0,
    "motor" : 0,
    "total" : 0
  }
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "hours" : "1970-01-01T00:00:00Z",
  "avds" : "string",
  "ventilation" : 0,
  "spo2" : 0,
  "o2" : 0,
  "etco2" : 0,
  "pulse" : 0,
  "ecg" : true,
  "skin" : "string",
  "temperature" : "string",
  "systolic_blood_pressure" : 0,
  "diastolic_blood_pressure" : 0,
  "pupils" : "string",
  "pain" : 0,
  "glycemia" : 0,
  "news" : 0,
  "victim" : {
    "id" : 0
  },
  "glasgow_scale" : {
    "eyes" : 0,
    "verbal" : 0,
    "motor" : 0,
    "total" : 0
  }
}
```


<a name="victims_evaluations_list"></a>
### GET /victims/{victim_id}/evaluations/

#### Description
List the evaluations of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Evaluation](#evaluation) > array|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/evaluations/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "hours" : "1970-01-01T00:00:00Z",
  "avds" : "string",
  "ventilation" : 0,
  "spo2" : 0,
  "o2" : 0,
  "etco2" : 0,
  "pulse" : 0,
  "ecg" : true,
  "skin" : "string",
  "temperature" : "string",
  "systolic_blood_pressure" : 0,
  "diastolic_blood_pressure" : 0,
  "pupils" : "string",
  "pain" : 0,
  "glycemia" : 0,
  "news" : 0,
  "victim" : 0,
  "glasgow_scale" : {
    "eyes" : 0,
    "verbal" : 0,
    "motor" : 0,
    "total" : 0
  }
} ]
```


<a name="victims_evaluations_read"></a>
### GET /victims/{victim_id}/evaluations/{evaluation_id}/

#### Description
List the details of an evaluation of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**evaluation_id**  <br>*required*|string|
|**Path**|**victim_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Evaluation](#evaluation) > array|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/evaluations/string/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "hours" : "1970-01-01T00:00:00Z",
  "avds" : "string",
  "ventilation" : 0,
  "spo2" : 0,
  "o2" : 0,
  "etco2" : 0,
  "pulse" : 0,
  "ecg" : true,
  "skin" : "string",
  "temperature" : "string",
  "systolic_blood_pressure" : 0,
  "diastolic_blood_pressure" : 0,
  "pupils" : "string",
  "pain" : 0,
  "glycemia" : 0,
  "news" : 0,
  "victim" : 0,
  "glasgow_scale" : {
    "eyes" : 0,
    "verbal" : 0,
    "motor" : 0,
    "total" : 0
  }
} ]
```


<a name="victims_pharmacies_create"></a>
### POST /victims/{victim_id}/pharmacies/

#### Description
List the pharmacies of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[PharmacyDetail](#pharmacydetail)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[PharmacyDetail](#pharmacydetail)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/pharmacies/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "time" : "1970-01-01T00:00:00Z",
  "pharmacy" : "string",
  "dose" : "string",
  "route" : "string",
  "adverse_effect" : "string",
  "victim" : {
    "id" : 0
  }
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "time" : "1970-01-01T00:00:00Z",
  "pharmacy" : "string",
  "dose" : "string",
  "route" : "string",
  "adverse_effect" : "string",
  "victim" : {
    "id" : 0
  }
}
```


<a name="victims_pharmacies_list"></a>
### GET /victims/{victim_id}/pharmacies/

#### Description
List the pharmacies of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Pharmacy](#pharmacy) > array|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/pharmacies/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "time" : "1970-01-01T00:00:00Z",
  "pharmacy" : "string",
  "dose" : "string",
  "route" : "string",
  "adverse_effect" : "string",
  "victim" : 0
} ]
```


<a name="victims_pharmacies_read"></a>
### GET /victims/{victim_id}/pharmacies/{pharmacy_id}/

#### Description
List the details of a pharmacies of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**pharmacy_id**  <br>*required*|string|
|**Path**|**victim_id**  <br>*required*|string|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|< [Pharmacy](#pharmacy) > array|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/pharmacies/string/
```


##### Request header
```json
Authorization:"string"
```


#### Example HTTP response

##### Response 200
```json
[ {
  "id" : 0,
  "time" : "1970-01-01T00:00:00Z",
  "pharmacy" : "string",
  "dose" : "string",
  "route" : "string",
  "adverse_effect" : "string",
  "victim" : 0
} ]
```


<a name="victims_procedure_circulation_create"></a>
### POST /victims/{victim_id}/procedure_circulation/

#### Description
List the Circulation Procedures of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[ProcedureCirculation](#procedurecirculation)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[ProcedureCirculation](#procedurecirculation)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/procedure_circulation/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "temperature_monitoring" : true,
  "compression" : true,
  "tourniquet" : true,
  "pelvic_belt" : true,
  "venous_access" : true,
  "patch" : true,
  "ecg" : true,
  "victim" : 0
}
```


#### Example HTTP response

##### Response 201
```json
{
  "temperature_monitoring" : true,
  "compression" : true,
  "tourniquet" : true,
  "pelvic_belt" : true,
  "venous_access" : true,
  "patch" : true,
  "ecg" : true,
  "victim" : 0
}
```


<a name="victims_procedure_circulation_update"></a>
### PUT /victims/{victim_id}/procedure_circulation/

#### Description
List the Circulation Procedures of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[ProcedureCirculation](#procedurecirculation)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[ProcedureCirculation](#procedurecirculation)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/procedure_circulation/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "temperature_monitoring" : true,
  "compression" : true,
  "tourniquet" : true,
  "pelvic_belt" : true,
  "venous_access" : true,
  "patch" : true,
  "ecg" : true,
  "victim" : 0
}
```


#### Example HTTP response

##### Response 200
```json
{
  "temperature_monitoring" : true,
  "compression" : true,
  "tourniquet" : true,
  "pelvic_belt" : true,
  "venous_access" : true,
  "patch" : true,
  "ecg" : true,
  "victim" : 0
}
```


<a name="victims_procedure_protocol_create"></a>
### POST /victims/{victim_id}/procedure_protocol/

#### Description
List the Protocol Procedures of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[ProcedureProtocol](#procedureprotocol)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[ProcedureProtocol](#procedureprotocol)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/procedure_protocol/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "immobilization" : true,
  "TEPH" : true,
  "SIV" : true,
  "VV_AVC" : true,
  "VV_coronary" : true,
  "VV_sepsis" : true,
  "VV_trauma" : true,
  "VV_PCR" : true,
  "victim" : 0
}
```


#### Example HTTP response

##### Response 201
```json
{
  "immobilization" : true,
  "TEPH" : true,
  "SIV" : true,
  "VV_AVC" : true,
  "VV_coronary" : true,
  "VV_sepsis" : true,
  "VV_trauma" : true,
  "VV_PCR" : true,
  "victim" : 0
}
```


<a name="victims_procedure_protocol_update"></a>
### PUT /victims/{victim_id}/procedure_protocol/

#### Description
List the Protocol Procedures of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[ProcedureProtocol](#procedureprotocol)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[ProcedureProtocol](#procedureprotocol)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/procedure_protocol/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "immobilization" : true,
  "TEPH" : true,
  "SIV" : true,
  "VV_AVC" : true,
  "VV_coronary" : true,
  "VV_sepsis" : true,
  "VV_trauma" : true,
  "VV_PCR" : true,
  "victim" : 0
}
```


#### Example HTTP response

##### Response 200
```json
{
  "immobilization" : true,
  "TEPH" : true,
  "SIV" : true,
  "VV_AVC" : true,
  "VV_coronary" : true,
  "VV_sepsis" : true,
  "VV_trauma" : true,
  "VV_PCR" : true,
  "victim" : 0
}
```


<a name="victims_procedure_rcp_create"></a>
### POST /victims/{victim_id}/procedure_rcp/

#### Description
List the RCP Procedures of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[ProcedureRCP](#procedurercp)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[ProcedureRCP](#procedurercp)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/procedure_rcp/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "witnessed" : true,
  "SBV_DAE" : "1970-01-01T00:00:00Z",
  "SIV_SAV" : "1970-01-01T00:00:00Z",
  "first_rhythm" : "string",
  "nr_shocks" : 0,
  "recovery" : "1970-01-01T00:00:00Z",
  "downtime" : "1970-01-01T00:00:00Z",
  "mechanical_compressions" : true,
  "not_performed" : true,
  "victim" : 0
}
```


#### Example HTTP response

##### Response 201
```json
{
  "witnessed" : true,
  "SBV_DAE" : "1970-01-01T00:00:00Z",
  "SIV_SAV" : "1970-01-01T00:00:00Z",
  "first_rhythm" : "string",
  "nr_shocks" : 0,
  "recovery" : "1970-01-01T00:00:00Z",
  "downtime" : "1970-01-01T00:00:00Z",
  "mechanical_compressions" : true,
  "not_performed" : true,
  "victim" : 0
}
```


<a name="victims_procedure_rcp_update"></a>
### PUT /victims/{victim_id}/procedure_rcp/

#### Description
List the RCP Procedures of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[ProcedureRCP](#procedurercp)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[ProcedureRCP](#procedurercp)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/procedure_rcp/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "witnessed" : true,
  "SBV_DAE" : "1970-01-01T00:00:00Z",
  "SIV_SAV" : "1970-01-01T00:00:00Z",
  "first_rhythm" : "string",
  "nr_shocks" : 0,
  "recovery" : "1970-01-01T00:00:00Z",
  "downtime" : "1970-01-01T00:00:00Z",
  "mechanical_compressions" : true,
  "not_performed" : true,
  "victim" : 0
}
```


#### Example HTTP response

##### Response 200
```json
{
  "witnessed" : true,
  "SBV_DAE" : "1970-01-01T00:00:00Z",
  "SIV_SAV" : "1970-01-01T00:00:00Z",
  "first_rhythm" : "string",
  "nr_shocks" : 0,
  "recovery" : "1970-01-01T00:00:00Z",
  "downtime" : "1970-01-01T00:00:00Z",
  "mechanical_compressions" : true,
  "not_performed" : true,
  "victim" : 0
}
```


<a name="victims_procedure_scale_create"></a>
### POST /victims/{victim_id}/procedure_scale/

#### Description
List the Scale Procedures of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[ProcedureScale](#procedurescale)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[ProcedureScale](#procedurescale)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/procedure_scale/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "cincinatti" : 0,
  "PROACS" : 0,
  "RTS" : 0,
  "MGAP" : 0,
  "RACE" : 0,
  "victim" : 0
}
```


#### Example HTTP response

##### Response 201
```json
{
  "cincinatti" : 0,
  "PROACS" : 0,
  "RTS" : 0,
  "MGAP" : 0,
  "RACE" : 0,
  "victim" : 0
}
```


<a name="victims_procedure_scale_update"></a>
### PUT /victims/{victim_id}/procedure_scale/

#### Description
List the Scale Procedures of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[ProcedureScale](#procedurescale)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[ProcedureScale](#procedurescale)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/procedure_scale/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "cincinatti" : 0,
  "PROACS" : 0,
  "RTS" : 0,
  "MGAP" : 0,
  "RACE" : 0,
  "victim" : 0
}
```


#### Example HTTP response

##### Response 200
```json
{
  "cincinatti" : 0,
  "PROACS" : 0,
  "RTS" : 0,
  "MGAP" : 0,
  "RACE" : 0,
  "victim" : 0
}
```


<a name="victims_procedure_ventilation_create"></a>
### POST /victims/{victim_id}/procedure_ventilation/

#### Description
List the Ventilation Procedures of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[ProcedureVentilation](#procedureventilation)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[ProcedureVentilation](#procedureventilation)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/procedure_ventilation/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "clearance" : true,
  "oropharyngeal" : true,
  "laryngeal_tube" : true,
  "endotracheal" : true,
  "laryngeal_mask" : true,
  "mechanical_ventilation" : true,
  "cpap" : true,
  "victim" : 0
}
```


#### Example HTTP response

##### Response 201
```json
{
  "clearance" : true,
  "oropharyngeal" : true,
  "laryngeal_tube" : true,
  "endotracheal" : true,
  "laryngeal_mask" : true,
  "mechanical_ventilation" : true,
  "cpap" : true,
  "victim" : 0
}
```


<a name="victims_procedure_ventilation_update"></a>
### PUT /victims/{victim_id}/procedure_ventilation/

#### Description
List the Ventilation Procedures of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[ProcedureVentilation](#procedureventilation)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[ProcedureVentilation](#procedureventilation)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/procedure_ventilation/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "clearance" : true,
  "oropharyngeal" : true,
  "laryngeal_tube" : true,
  "endotracheal" : true,
  "laryngeal_mask" : true,
  "mechanical_ventilation" : true,
  "cpap" : true,
  "victim" : 0
}
```


#### Example HTTP response

##### Response 200
```json
{
  "clearance" : true,
  "oropharyngeal" : true,
  "laryngeal_tube" : true,
  "endotracheal" : true,
  "laryngeal_mask" : true,
  "mechanical_ventilation" : true,
  "cpap" : true,
  "victim" : 0
}
```


<a name="victims_symptom_create"></a>
### POST /victims/{victim_id}/symptom/

#### Description
List the Symptons of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[SymptomDetails](#symptomdetails)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[SymptomDetails](#symptomdetails)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/symptom/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "comments" : "string",
  "traumas" : [ {
    "id" : 0,
    "body_part" : "string",
    "type_of_injury" : "string",
    "closed" : true,
    "burn_degree" : "string"
  } ],
  "victim" : 0,
  "total_burn_area" : "string"
}
```


#### Example HTTP response

##### Response 201
```json
{
  "comments" : "string",
  "traumas" : [ {
    "id" : 0,
    "body_part" : "string",
    "type_of_injury" : "string",
    "closed" : true,
    "burn_degree" : "string"
  } ],
  "victim" : 0,
  "total_burn_area" : "string"
}
```


<a name="victims_symptom_update"></a>
### PUT /victims/{victim_id}/symptom/

#### Description
List the Symptons of a Victim


#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[SymptomDetails](#symptomdetails)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**200**|[SymptomDetails](#symptomdetails)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/symptom/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "comments" : "string",
  "traumas" : [ {
    "id" : 0,
    "body_part" : "string",
    "type_of_injury" : "string",
    "closed" : true,
    "burn_degree" : "string"
  } ],
  "victim" : 0,
  "total_burn_area" : "string"
}
```


#### Example HTTP response

##### Response 200
```json
{
  "comments" : "string",
  "traumas" : [ {
    "id" : 0,
    "body_part" : "string",
    "type_of_injury" : "string",
    "closed" : true,
    "burn_degree" : "string"
  } ],
  "victim" : 0,
  "total_burn_area" : "string"
}
```


<a name="victims_symptom_traumas_create"></a>
### POST /victims/{victim_id}/symptom/traumas/

#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[TraumaSerializaer](#traumaserializaer)|


#### Responses

|HTTP Code|Schema|
|---|---|
|**201**|[TraumaDetailsSerializaer](#traumadetailsserializaer)|


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/symptom/traumas/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "body_part" : "string",
  "type_of_injury" : "string",
  "closed" : true,
  "burn_degree" : "string"
}
```


#### Example HTTP response

##### Response 201
```json
{
  "id" : 0,
  "body_part" : "string",
  "type_of_injury" : "string",
  "closed" : true,
  "burn_degree" : "string",
  "symptom" : {
    "comments" : "string",
    "victim" : 0,
    "total_burn_area" : "string"
  }
}
```


<a name="victims_transport_update"></a>
### PUT /victims/{victim_id}/transport/

#### Parameters

|Type|Name|Schema|
|---|---|---|
|**Header**|**Authorization**  <br>*optional*|string|
|**Path**|**victim_id**  <br>*required*|string|
|**Body**|**data**  <br>*required*|[VictimTransport](#victimtransport)|


#### Responses

| HTTP Code | Schema                              |
|-----------|-------------------------------------|
| **200**   | [VictimTransport](#victimtransport) |


#### Tags

* victims


#### Example HTTP request

##### Request path
```
/victims/string/transport/
```


##### Request header
```json
Authorization:"string"
```


##### Request body
```json
{
  "id" : 0,
  "medical_followup" : true,
  "episode_number" : 0,
  "type_of_transport" : 0,
  "non_transport_reason" : 0,
  "hospital" : 0
}
```


#### Example HTTP response

##### Response 200
```json
{
  "id" : 0,
  "medical_followup" : true,
  "episode_number" : 0,
  "type_of_transport" : 0,
  "non_transport_reason" : 0,
  "hospital" : 0
}
```




<a name="definitions"></a>
## Definitions

<a name="central"></a>
### Central

| Name                                    | Description                                         | Schema  |
|-----------------------------------------|-----------------------------------------------------|---------|
| **address**  <br>*required*             | **Length** : `1 - 50`  <br>**Example** : `"string"` | string  |
| **area_of_action**  <br>*required*      | **Length** : `1 - 50`  <br>**Example** : `"string"` | string  |
| **contact**  <br>*required*             | **Example** : `0`                                   | integer |
| **designation**  <br>*required*         | **Length** : `1 - 50`  <br>**Example** : `"string"` | string  |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0`                                   | integer |
| **is_administrative**  <br>*required*   | **Example** : `true`                                | boolean |


<a name="dispatcher"></a>
### Dispatcher

| Name                                            | Description              | Schema  |
|-------------------------------------------------|--------------------------|---------|
| **active**  <br>*optional*                      | **Example** : `true`     | boolean |
| **central**  <br>*required*                     | **Example** : `0`        | integer |
| **first_name**  <br>*optional*  <br>*read-only* | **Example** : `"string"` | string  |
| **id**  <br>*optional*  <br>*read-only*         | **Example** : `"string"` | string  |
| **last_name**  <br>*optional*  <br>*read-only*  | **Example** : `"string"` | string  |
| **username**  <br>*optional*  <br>*read-only*   | **Example** : `"string"` | string  |


<a name="dispatcherdetail"></a>
### DispatcherDetail

| Name                                            | Description                           | Schema              |
|-------------------------------------------------|---------------------------------------|---------------------|
| **active**  <br>*optional*                      | **Example** : `true`                  | boolean             |
| **central**  <br>*optional*                     | **Example** : `"[central](#central)"` | [Central](#central) |
| **first_name**  <br>*optional*  <br>*read-only* | **Example** : `"string"`              | string              |
| **id**  <br>*optional*  <br>*read-only*         | **Example** : `"string"`              | string              |
| **last_name**  <br>*optional*  <br>*read-only*  | **Example** : `"string"`              | string              |
| **username**  <br>*optional*  <br>*read-only*   | **Example** : `"string"`              | string              |


<a name="evaluation"></a>
### Evaluation

| Name                                         | Description                                             | Schema                        |
|----------------------------------------------|---------------------------------------------------------|-------------------------------|
| **avds**  <br>*optional*                     | **Maximal length** : `1`  <br>**Example** : `"string"`  | string                        |
| **diastolic_blood_pressure**  <br>*optional* | **Example** : `0`                                       | integer                       |
| **ecg**  <br>*optional*                      | **Example** : `true`                                    | boolean                       |
| **etco2**  <br>*optional*                    | **Example** : `0`                                       | integer                       |
| **glasgow_scale**  <br>*required*            | **Example** : `"[glasgowscale](#glasgowscale)"`         | [GlasgowScale](#glasgowscale) |
| **glycemia**  <br>*optional*                 | **Example** : `0`                                       | integer                       |
| **hours**  <br>*required*                    | **Example** : `"1970-01-01T00:00:00Z"`                  | string (date-time)            |
| **id**  <br>*optional*  <br>*read-only*      | **Example** : `0`                                       | integer                       |
| **news**  <br>*optional*                     | **Example** : `0`                                       | integer                       |
| **o2**  <br>*optional*                       | **Example** : `0`                                       | integer                       |
| **pain**  <br>*optional*                     | **Maximum value** : `10`  <br>**Example** : `0`         | integer                       |
| **pulse**  <br>*optional*                    | **Example** : `0`                                       | integer                       |
| **pupils**  <br>*optional*                   | **Maximal length** : `50`  <br>**Example** : `"string"` | string                        |
| **skin**  <br>*optional*                     | **Maximal length** : `50`  <br>**Example** : `"string"` | string                        |
| **spo2**  <br>*optional*                     | **Example** : `0`                                       | integer                       |
| **systolic_blood_pressure**  <br>*optional*  | **Example** : `0`                                       | integer                       |
| **temperature**  <br>*optional*              | **Example** : `"string"`                                | string (decimal)              |
| **ventilation**  <br>*optional*              | **Example** : `0`                                       | integer                       |
| **victim**  <br>*required*                   | **Example** : `0`                                       | integer                       |


<a name="evaluationdetail"></a>
### EvaluationDetail

| Name                                         | Description                                             | Schema                        |
|----------------------------------------------|---------------------------------------------------------|-------------------------------|
| **avds**  <br>*optional*                     | **Maximal length** : `1`  <br>**Example** : `"string"`  | string                        |
| **diastolic_blood_pressure**  <br>*optional* | **Example** : `0`                                       | integer                       |
| **ecg**  <br>*optional*                      | **Example** : `true`                                    | boolean                       |
| **etco2**  <br>*optional*                    | **Example** : `0`                                       | integer                       |
| **glasgow_scale**  <br>*required*            | **Example** : `"[glasgowscale](#glasgowscale)"`         | [GlasgowScale](#glasgowscale) |
| **glycemia**  <br>*optional*                 | **Example** : `0`                                       | integer                       |
| **hours**  <br>*required*                    | **Example** : `"1970-01-01T00:00:00Z"`                  | string (date-time)            |
| **id**  <br>*optional*  <br>*read-only*      | **Example** : `0`                                       | integer                       |
| **news**  <br>*optional*                     | **Example** : `0`                                       | integer                       |
| **o2**  <br>*optional*                       | **Example** : `0`                                       | integer                       |
| **pain**  <br>*optional*                     | **Maximum value** : `10`  <br>**Example** : `0`         | integer                       |
| **pulse**  <br>*optional*                    | **Example** : `0`                                       | integer                       |
| **pupils**  <br>*optional*                   | **Maximal length** : `50`  <br>**Example** : `"string"` | string                        |
| **skin**  <br>*optional*                     | **Maximal length** : `50`  <br>**Example** : `"string"` | string                        |
| **spo2**  <br>*optional*                     | **Example** : `0`                                       | integer                       |
| **systolic_blood_pressure**  <br>*optional*  | **Example** : `0`                                       | integer                       |
| **temperature**  <br>*optional*              | **Example** : `"string"`                                | string (decimal)              |
| **ventilation**  <br>*optional*              | **Example** : `0`                                       | integer                       |
| **victim**  <br>*optional*                   | **Example** : `"[victimid](#victimid)"`                 | [VictimId](#victimid)         |


<a name="glasgowscale"></a>
### GlasgowScale

| Name                       | Description       | Schema  |
|----------------------------|-------------------|---------|
| **eyes**  <br>*optional*   | **Example** : `0` | integer |
| **motor**  <br>*optional*  | **Example** : `0` | integer |
| **total**  <br>*optional*  | **Example** : `0` | integer |
| **verbal**  <br>*optional* | **Example** : `0` | integer |


<a name="hospital"></a>
### Hospital

| Name                                    | Description                                              | Schema  |
|-----------------------------------------|----------------------------------------------------------|---------|
| **address**  <br>*required*             | **Length** : `1 - 50`  <br>**Example** : `"string"`      | string  |
| **capacity**  <br>*required*            | **Example** : `0`                                        | integer |
| **contact**  <br>*required*             | **Example** : `0`                                        | integer |
| **current_capacity**  <br>*required*    | **Example** : `0`                                        | integer |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0`                                        | integer |
| **image_url**  <br>*optional*           | **Maximal length** : `250`  <br>**Example** : `"string"` | string  |
| **name**  <br>*required*                | **Length** : `1 - 50`  <br>**Example** : `"string"`      | string  |


<a name="hospitalstaff"></a>
### HospitalStaff

| Name                                            | Description              | Schema  |
|-------------------------------------------------|--------------------------|---------|
| **active**  <br>*optional*                      | **Example** : `true`     | boolean |
| **first_name**  <br>*optional*  <br>*read-only* | **Example** : `"string"` | string  |
| **hospital**  <br>*required*                    | **Example** : `0`        | integer |
| **id**  <br>*optional*  <br>*read-only*         | **Example** : `"string"` | string  |
| **last_name**  <br>*optional*  <br>*read-only*  | **Example** : `"string"` | string  |
| **username**  <br>*optional*  <br>*read-only*   | **Example** : `"string"` | string  |


<a name="hospitalstaffdetail"></a>
### HospitalStaffDetail

| Name                                            | Description                             | Schema                |
|-------------------------------------------------|-----------------------------------------|-----------------------|
| **active**  <br>*optional*                      | **Example** : `true`                    | boolean               |
| **first_name**  <br>*optional*  <br>*read-only* | **Example** : `"string"`                | string                |
| **hospital**  <br>*optional*                    | **Example** : `"[hospital](#hospital)"` | [Hospital](#hospital) |
| **id**  <br>*optional*  <br>*read-only*         | **Example** : `"string"`                | string                |
| **last_name**  <br>*optional*  <br>*read-only*  | **Example** : `"string"`                | string                |
| **username**  <br>*optional*  <br>*read-only*   | **Example** : `"string"`                | string                |


<a name="news"></a>
### News

| Name                                    | Description                                              | Schema  |
|-----------------------------------------|----------------------------------------------------------|---------|
| **description**  <br>*optional*         | **Maximal length** : `500`  <br>**Example** : `"string"` | string  |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0`                                        | integer |
| **image_url**  <br>*optional*           | **Maximal length** : `500`  <br>**Example** : `"string"` | string  |
| **title**  <br>*optional*               | **Maximal length** : `500`  <br>**Example** : `"string"` | string  |


<a name="occurrence"></a>
### Occurrence

| Name                                    | Description                                              | Schema             |
|-----------------------------------------|----------------------------------------------------------|--------------------|
| **active**  <br>*optional*              | **Example** : `true`                                     | boolean            |
| **alert_mode**  <br>*optional*          | **Example** : `true`                                     | boolean            |
| **central**  <br>*optional*             | **Example** : `0`                                        | integer            |
| **created_by**  <br>*optional*          | **Example** : `0`                                        | integer            |
| **created_on**  <br>*optional*          | **Example** : `"1970-01-01T00:00:00Z"`                   | string (date-time) |
| **entity**  <br>*optional*              | **Maximal length** : `50`  <br>**Example** : `"string"`  | string             |
| **gps_coordinates**  <br>*optional*     | **Maximal length** : `100`  <br>**Example** : `"string"` | string             |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0`                                        | integer            |
| **local**  <br>*required*               | **Length** : `1 - 100`  <br>**Example** : `"string"`     | string             |
| **mean_of_assistance**  <br>*optional*  | **Maximal length** : `50`  <br>**Example** : `"string"`  | string             |
| **motive**  <br>*required*              | **Length** : `1 - 50`  <br>**Example** : `"string"`      | string             |
| **municipality**  <br>*optional*        | **Maximal length** : `50`  <br>**Example** : `"string"`  | string             |
| **number_of_victims**  <br>*required*   | **Example** : `0`                                        | integer            |
| **occurrence_number**  <br>*required*   | **Example** : `0`                                        | integer            |
| **parish**  <br>*optional*              | **Maximal length** : `50`  <br>**Example** : `"string"`  | string             |
| **team**  <br>*optional*                | **Example** : `0`                                        | integer            |


<a name="occurrencealldetails"></a>
### OccurrenceAllDetails

| Name                                         | Description                                                 | Schema                                          |
|----------------------------------------------|-------------------------------------------------------------|-------------------------------------------------|
| **active**  <br>*optional*                   | **Example** : `true`                                        | boolean                                         |
| **alert_mode**  <br>*optional*               | **Example** : `true`                                        | boolean                                         |
| **central**  <br>*optional*                  | **Example** : `"[central](#central)"`                       | [Central](#central)                             |
| **created_on**  <br>*optional*               | **Example** : `"1970-01-01T00:00:00Z"`                      | string (date-time)                              |
| **entity**  <br>*optional*                   | **Maximal length** : `50`  <br>**Example** : `"string"`     | string                                          |
| **gps_coordinates**  <br>*optional*          | **Maximal length** : `100`  <br>**Example** : `"string"`    | string                                          |
| **id**  <br>*optional*  <br>*read-only*      | **Example** : `0`                                           | integer                                         |
| **local**  <br>*required*                    | **Length** : `1 - 100`  <br>**Example** : `"string"`        | string                                          |
| **mean_of_assistance**  <br>*optional*       | **Maximal length** : `50`  <br>**Example** : `"string"`     | string                                          |
| **motive**  <br>*required*                   | **Length** : `1 - 50`  <br>**Example** : `"string"`         | string                                          |
| **municipality**  <br>*optional*             | **Maximal length** : `50`  <br>**Example** : `"string"`     | string                                          |
| **number_of_victims**  <br>*required*        | **Example** : `0`                                           | integer                                         |
| **occurrence_number**  <br>*required*        | **Example** : `0`                                           | integer                                         |
| **parish**  <br>*optional*                   | **Maximal length** : `50`  <br>**Example** : `"string"`     | string                                          |
| **states**  <br>*optional*  <br>*read-only*  | **Example** : `[ "[occurrencestate](#occurrencestate)" ]`   | < [OccurrenceState](#occurrencestate) > array   |
| **team**  <br>*optional*                     | **Example** : `"[team](#team)"`                             | [Team](#team)                                   |
| **victims**  <br>*optional*  <br>*read-only* | **Example** : `[ "[victimalldetails](#victimalldetails)" ]` | < [VictimAllDetails](#victimalldetails) > array |


<a name="occurrencedetail"></a>
### OccurrenceDetail

| Name                                         | Description                                               | Schema                                        |
|----------------------------------------------|-----------------------------------------------------------|-----------------------------------------------|
| **active**  <br>*optional*                   | **Example** : `true`                                      | boolean                                       |
| **alert_mode**  <br>*optional*               | **Example** : `true`                                      | boolean                                       |
| **central**  <br>*optional*                  | **Example** : `"[central](#central)"`                     | [Central](#central)                           |
| **created_on**  <br>*optional*               | **Example** : `"1970-01-01T00:00:00Z"`                    | string (date-time)                            |
| **entity**  <br>*optional*                   | **Maximal length** : `50`  <br>**Example** : `"string"`   | string                                        |
| **gps_coordinates**  <br>*optional*          | **Maximal length** : `100`  <br>**Example** : `"string"`  | string                                        |
| **id**  <br>*optional*  <br>*read-only*      | **Example** : `0`                                         | integer                                       |
| **local**  <br>*required*                    | **Length** : `1 - 100`  <br>**Example** : `"string"`      | string                                        |
| **mean_of_assistance**  <br>*optional*       | **Maximal length** : `50`  <br>**Example** : `"string"`   | string                                        |
| **motive**  <br>*required*                   | **Length** : `1 - 50`  <br>**Example** : `"string"`       | string                                        |
| **municipality**  <br>*optional*             | **Maximal length** : `50`  <br>**Example** : `"string"`   | string                                        |
| **number_of_victims**  <br>*required*        | **Example** : `0`                                         | integer                                       |
| **occurrence_number**  <br>*required*        | **Example** : `0`                                         | integer                                       |
| **parish**  <br>*optional*                   | **Maximal length** : `50`  <br>**Example** : `"string"`   | string                                        |
| **states**  <br>*optional*  <br>*read-only*  | **Example** : `[ "[occurrencestate](#occurrencestate)" ]` | < [OccurrenceState](#occurrencestate) > array |
| **team**  <br>*optional*                     | **Example** : `"[team](#team)"`                           | [Team](#team)                                 |
| **victims**  <br>*optional*  <br>*read-only* | **Example** : `[ "[victim](#victim)" ]`                   | < [Victim](#victim) > array                   |


<a name="occurrencesimplified"></a>
### OccurrenceSimplified

| Name                                    | Description       | Schema  |
|-----------------------------------------|-------------------|---------|
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0` | integer |
| **occurrence_number**  <br>*required*   | **Example** : `0` | integer |


<a name="occurrencestate"></a>
### OccurrenceState

| Name                                    | Description                            | Schema             |
|-----------------------------------------|----------------------------------------|--------------------|
| **date_time**  <br>*required*           | **Example** : `"1970-01-01T00:00:00Z"` | string (date-time) |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0`                      | integer            |
| **latitude**  <br>*required*            | **Example** : `"string"`               | string (decimal)   |
| **longitude**  <br>*required*           | **Example** : `"string"`               | string (decimal)   |
| **state**  <br>*optional*               | **Example** : `"[state](#state)"`      | [State](#state)    |


<a name="pharmacy"></a>
### Pharmacy

| Name                                    | Description                                             | Schema             |
|-----------------------------------------|---------------------------------------------------------|--------------------|
| **adverse_effect**  <br>*optional*      | **Maximal length** : `50`  <br>**Example** : `"string"` | string             |
| **dose**  <br>*optional*                | **Maximal length** : `50`  <br>**Example** : `"string"` | string             |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0`                                       | integer            |
| **pharmacy**  <br>*required*            | **Length** : `1 - 50`  <br>**Example** : `"string"`     | string             |
| **route**  <br>*optional*               | **Maximal length** : `50`  <br>**Example** : `"string"` | string             |
| **time**  <br>*optional*                | **Example** : `"1970-01-01T00:00:00Z"`                  | string (date-time) |
| **victim**  <br>*required*              | **Example** : `0`                                       | integer            |


<a name="pharmacydetail"></a>
### PharmacyDetail

| Name                                    | Description                                             | Schema                |
|-----------------------------------------|---------------------------------------------------------|-----------------------|
| **adverse_effect**  <br>*optional*      | **Maximal length** : `50`  <br>**Example** : `"string"` | string                |
| **dose**  <br>*optional*                | **Maximal length** : `50`  <br>**Example** : `"string"` | string                |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0`                                       | integer               |
| **pharmacy**  <br>*required*            | **Length** : `1 - 50`  <br>**Example** : `"string"`     | string                |
| **route**  <br>*optional*               | **Maximal length** : `50`  <br>**Example** : `"string"` | string                |
| **time**  <br>*optional*                | **Example** : `"1970-01-01T00:00:00Z"`                  | string (date-time)    |
| **victim**  <br>*optional*              | **Example** : `"[victimid](#victimid)"`                 | [VictimId](#victimid) |


<a name="procedurecirculation"></a>
### ProcedureCirculation

| Name                                       | Description          | Schema  |
|--------------------------------------------|----------------------|---------|
| **compression**  <br>*required*            | **Example** : `true` | boolean |
| **ecg**  <br>*required*                    | **Example** : `true` | boolean |
| **patch**  <br>*required*                  | **Example** : `true` | boolean |
| **pelvic_belt**  <br>*required*            | **Example** : `true` | boolean |
| **temperature_monitoring**  <br>*required* | **Example** : `true` | boolean |
| **tourniquet**  <br>*required*             | **Example** : `true` | boolean |
| **venous_access**  <br>*required*          | **Example** : `true` | boolean |
| **victim**  <br>*required*                 | **Example** : `0`    | integer |


<a name="procedureprotocol"></a>
### ProcedureProtocol

| Name                               | Description          | Schema  |
|------------------------------------|----------------------|---------|
| **SIV**  <br>*optional*            | **Example** : `true` | boolean |
| **TEPH**  <br>*optional*           | **Example** : `true` | boolean |
| **VV_AVC**  <br>*optional*         | **Example** : `true` | boolean |
| **VV_PCR**  <br>*optional*         | **Example** : `true` | boolean |
| **VV_coronary**  <br>*optional*    | **Example** : `true` | boolean |
| **VV_sepsis**  <br>*optional*      | **Example** : `true` | boolean |
| **VV_trauma**  <br>*optional*      | **Example** : `true` | boolean |
| **immobilization**  <br>*optional* | **Example** : `true` | boolean |
| **victim**  <br>*required*         | **Example** : `0`    | integer |


<a name="procedurercp"></a>
### ProcedureRCP

| Name                                        | Description                                             | Schema             |
|---------------------------------------------|---------------------------------------------------------|--------------------|
| **SBV_DAE**  <br>*optional*                 | **Example** : `"1970-01-01T00:00:00Z"`                  | string (date-time) |
| **SIV_SAV**  <br>*optional*                 | **Example** : `"1970-01-01T00:00:00Z"`                  | string (date-time) |
| **downtime**  <br>*optional*                | **Example** : `"1970-01-01T00:00:00Z"`                  | string (date-time) |
| **first_rhythm**  <br>*optional*            | **Maximal length** : `25`  <br>**Example** : `"string"` | string             |
| **mechanical_compressions**  <br>*optional* | **Example** : `true`                                    | boolean            |
| **not_performed**  <br>*optional*           | **Example** : `true`                                    | boolean            |
| **nr_shocks**  <br>*optional*               | **Example** : `0`                                       | integer            |
| **recovery**  <br>*optional*                | **Example** : `"1970-01-01T00:00:00Z"`                  | string (date-time) |
| **victim**  <br>*required*                  | **Example** : `0`                                       | integer            |
| **witnessed**  <br>*optional*               | **Example** : `true`                                    | boolean            |


<a name="procedurescale"></a>
### ProcedureScale

| Name                           | Description       | Schema  |
|--------------------------------|-------------------|---------|
| **MGAP**  <br>*optional*       | **Example** : `0` | integer |
| **PROACS**  <br>*optional*     | **Example** : `0` | integer |
| **RACE**  <br>*optional*       | **Example** : `0` | integer |
| **RTS**  <br>*optional*        | **Example** : `0` | integer |
| **cincinatti**  <br>*optional* | **Example** : `0` | integer |
| **victim**  <br>*required*     | **Example** : `0` | integer |


<a name="procedureventilation"></a>
### ProcedureVentilation

| Name                                       | Description          | Schema  |
|--------------------------------------------|----------------------|---------|
| **clearance**  <br>*optional*              | **Example** : `true` | boolean |
| **cpap**  <br>*optional*                   | **Example** : `true` | boolean |
| **endotracheal**  <br>*optional*           | **Example** : `true` | boolean |
| **laryngeal_mask**  <br>*optional*         | **Example** : `true` | boolean |
| **laryngeal_tube**  <br>*optional*         | **Example** : `true` | boolean |
| **mechanical_ventilation**  <br>*optional* | **Example** : `true` | boolean |
| **oropharyngeal**  <br>*optional*          | **Example** : `true` | boolean |
| **victim**  <br>*required*                 | **Example** : `0`    | integer |


<a name="state"></a>
### State

| Name                                    | Description                                         | Schema  |
|-----------------------------------------|-----------------------------------------------------|---------|
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0`                                   | integer |
| **state**  <br>*required*               | **Length** : `1 - 25`  <br>**Example** : `"string"` | string  |


<a name="symptom"></a>
### Symptom

| Name                                | Description                                              | Schema           |
|-------------------------------------|----------------------------------------------------------|------------------|
| **comments**  <br>*optional*        | **Maximal length** : `400`  <br>**Example** : `"string"` | string           |
| **total_burn_area**  <br>*optional* | **Example** : `"string"`                                 | string (decimal) |
| **victim**  <br>*required*          | **Example** : `0`                                        | integer          |


<a name="symptomdetails"></a>
### SymptomDetails

| Name                                         | Description                                                   | Schema                                            |
|----------------------------------------------|---------------------------------------------------------------|---------------------------------------------------|
| **comments**  <br>*optional*                 | **Maximal length** : `400`  <br>**Example** : `"string"`      | string                                            |
| **total_burn_area**  <br>*optional*          | **Example** : `"string"`                                      | string (decimal)                                  |
| **traumas**  <br>*optional*  <br>*read-only* | **Example** : `[ "[traumaserializaer](#traumaserializaer)" ]` | < [TraumaSerializaer](#traumaserializaer) > array |
| **victim**  <br>*required*                   | **Example** : `0`                                             | integer                                           |


<a name="team"></a>
### Team

| Name                                    | Description                                             | Schema                                      |
|-----------------------------------------|---------------------------------------------------------|---------------------------------------------|
| **active**  <br>*optional*              | **Example** : `true`                                    | boolean                                     |
| **central**  <br>*optional*             | **Example** : `"[central](#central)"`                   | [Central](#central)                         |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0`                                       | integer                                     |
| **technicians**  <br>*required*         | **Example** : `[ "[teamtechnician](#teamtechnician)" ]` | < [TeamTechnician](#teamtechnician) > array |


<a name="teamtechnician"></a>
### TeamTechnician

| Name                                    | Description                                         | Schema                            |
|-----------------------------------------|-----------------------------------------------------|-----------------------------------|
| **active**  <br>*optional*              | **Example** : `true`                                | boolean                           |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `"string"`                            | string                            |
| **team_leader**  <br>*optional*         | **Example** : `true`                                | boolean                           |
| **user**  <br>*optional*                | **Example** : `"[usersimplified](#usersimplified)"` | [UserSimplified](#usersimplified) |


<a name="technician"></a>
### Technician

| Name                                    | Description                                         | Schema                            |
|-----------------------------------------|-----------------------------------------------------|-----------------------------------|
| **active**  <br>*optional*              | **Example** : `true`                                | boolean                           |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `"string"`                            | string                            |
| **user**  <br>*required*                | **Example** : `"[usersimplified](#usersimplified)"` | [UserSimplified](#usersimplified) |


<a name="techniciandetail"></a>
### TechnicianDetail

| Name                                    | Description                                         | Schema                            |
|-----------------------------------------|-----------------------------------------------------|-----------------------------------|
| **active**  <br>*optional*              | **Example** : `true`                                | boolean                           |
| **central**  <br>*required*             | **Example** : `"[central](#central)"`               | [Central](#central)               |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `"string"`                            | string                            |
| **user**  <br>*required*                | **Example** : `"[usersimplified](#usersimplified)"` | [UserSimplified](#usersimplified) |


<a name="traumadetailsserializaer"></a>
### TraumaDetailsSerializaer

| Name                                    | Description                                             | Schema              |
|-----------------------------------------|---------------------------------------------------------|---------------------|
| **body_part**  <br>*optional*           | **Maximal length** : `20`  <br>**Example** : `"string"` | string              |
| **burn_degree**  <br>*optional*         | **Maximal length** : `2`  <br>**Example** : `"string"`  | string              |
| **closed**  <br>*optional*              | **Example** : `true`                                    | boolean             |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0`                                       | integer             |
| **symptom**  <br>*optional*             | **Example** : `"[symptom](#symptom)"`                   | [Symptom](#symptom) |
| **type_of_injury**  <br>*optional*      | **Maximal length** : `1`  <br>**Example** : `"string"`  | string              |


<a name="traumaserializaer"></a>
### TraumaSerializaer

| Name                                    | Description                                             | Schema  |
|-----------------------------------------|---------------------------------------------------------|---------|
| **body_part**  <br>*optional*           | **Maximal length** : `20`  <br>**Example** : `"string"` | string  |
| **burn_degree**  <br>*optional*         | **Maximal length** : `2`  <br>**Example** : `"string"`  | string  |
| **closed**  <br>*optional*              | **Example** : `true`                                    | boolean |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0`                                       | integer |
| **type_of_injury**  <br>*optional*      | **Maximal length** : `1`  <br>**Example** : `"string"`  | string  |


<a name="user"></a>
### User

| Name                                    | Description                                                                                                                                                          | Schema         |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| **email**  <br>*optional*               | **Maximal length** : `254`  <br>**Example** : `"email@example.com"`                                                                                                  | string (email) |
| **first_name**  <br>*optional*          | **Maximal length** : `150`  <br>**Example** : `"string"`                                                                                                             | string         |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0`                                                                                                                                                    | integer        |
| **last_name**  <br>*optional*           | **Maximal length** : `150`  <br>**Example** : `"string"`                                                                                                             | string         |
| **password**  <br>*required*            | **Length** : `1 - 128`  <br>**Example** : `"string"`                                                                                                                 | string         |
| **username**  <br>*required*            | Obrigatório. 150 carateres ou menos. Apenas letras, dígitos @/./+/-/_.  <br>**Length** : `1 - 150`  <br>**Pattern** : `"^[\\w.@+-]+$"`  <br>**Example** : `"string"` | string         |


<a name="usersimplified"></a>
### UserSimplified

| Name                                    | Description                                                                                                                                                          | Schema         |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| **email**  <br>*optional*               | **Maximal length** : `254`  <br>**Example** : `"email@example.com"`                                                                                                  | string (email) |
| **first_name**  <br>*optional*          | **Maximal length** : `150`  <br>**Example** : `"string"`                                                                                                             | string         |
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0`                                                                                                                                                    | integer        |
| **last_name**  <br>*optional*           | **Maximal length** : `150`  <br>**Example** : `"string"`                                                                                                             | string         |
| **username**  <br>*required*            | Obrigatório. 150 carateres ou menos. Apenas letras, dígitos @/./+/-/_.  <br>**Length** : `1 - 150`  <br>**Pattern** : `"^[\\w.@+-]+$"`  <br>**Example** : `"string"` | string         |


<a name="victim"></a>
### Victim

| Name                                      | Description                                              | Schema             |
|-------------------------------------------|----------------------------------------------------------|--------------------|
| **address**  <br>*optional*               | **Maximal length** : `100`  <br>**Example** : `"string"` | string             |
| **age**  <br>*optional*                   | **Example** : `0`                                        | integer            |
| **allergies**  <br>*optional*             | **Maximal length** : `100`  <br>**Example** : `"string"` | string             |
| **birthdate**  <br>*optional*             | **Example** : `"1970-01-01"`                             | string (date)      |
| **circumstances**  <br>*optional*         | **Maximal length** : `100`  <br>**Example** : `"string"` | string             |
| **comments**  <br>*optional*              | **Maximal length** : `400`  <br>**Example** : `"string"` | string             |
| **disease_history**  <br>*optional*       | **Maximal length** : `200`  <br>**Example** : `"string"` | string             |
| **episode_number**  <br>*optional*        | **Example** : `0`                                        | integer            |
| **gender**  <br>*optional*                | **Maximal length** : `25`  <br>**Example** : `"string"`  | string             |
| **hospital**  <br>*optional*              | **Example** : `0`                                        | integer            |
| **hospital_checkin_date**  <br>*optional* | **Example** : `"1970-01-01T00:00:00Z"`                   | string (date-time) |
| **id**  <br>*optional*  <br>*read-only*   | **Example** : `0`                                        | integer            |
| **identity_number**  <br>*optional*       | **Maximal length** : `30`  <br>**Example** : `"string"`  | string             |
| **last_meal**  <br>*optional*             | **Maximal length** : `50`  <br>**Example** : `"string"`  | string             |
| **last_meal_time**  <br>*optional*        | **Example** : `"1970-01-01T00:00:00Z"`                   | string (date-time) |
| **medical_followup**  <br>*optional*      | **Example** : `true`                                     | boolean            |
| **name**  <br>*optional*                  | **Maximal length** : `50`  <br>**Example** : `"string"`  | string             |
| **non_transport_reason**  <br>*optional*  | **Example** : `0`                                        | integer            |
| **occurrence**  <br>*optional*            | **Example** : `0`                                        | integer            |
| **risk_situation**  <br>*optional*        | **Maximal length** : `50`  <br>**Example** : `"string"`  | string             |
| **type_of_emergency**  <br>*optional*     | **Maximal length** : `100`  <br>**Example** : `"string"` | string             |
| **type_of_transport**  <br>*optional*     | **Example** : `0`                                        | integer            |
| **usual_medication**  <br>*optional*      | **Maximal length** : `100`  <br>**Example** : `"string"` | string             |


<a name="victimalldetails"></a>
### VictimAllDetails

| Name                                                      | Description                                                     | Schema                                        |
|-----------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| **address**  <br>*optional*                               | **Maximal length** : `100`  <br>**Example** : `"string"`        | string                                        |
| **age**  <br>*optional*                                   | **Example** : `0`                                               | integer                                       |
| **allergies**  <br>*optional*                             | **Maximal length** : `100`  <br>**Example** : `"string"`        | string                                        |
| **birthdate**  <br>*optional*                             | **Example** : `"1970-01-01"`                                    | string (date)                                 |
| **circumstances**  <br>*optional*                         | **Maximal length** : `100`  <br>**Example** : `"string"`        | string                                        |
| **comments**  <br>*optional*                              | **Maximal length** : `400`  <br>**Example** : `"string"`        | string                                        |
| **disease_history**  <br>*optional*                       | **Maximal length** : `200`  <br>**Example** : `"string"`        | string                                        |
| **episode_number**  <br>*optional*                        | **Example** : `0`                                               | integer                                       |
| **evaluations**  <br>*optional*  <br>*read-only*          | **Example** : `[ "[evaluation](#evaluation)" ]`                 | < [Evaluation](#evaluation) > array           |
| **gender**  <br>*optional*                                | **Maximal length** : `25`  <br>**Example** : `"string"`         | string                                        |
| **hospital**  <br>*optional*                              | **Example** : `"[hospital](#hospital)"`                         | [Hospital](#hospital)                         |
| **hospital_checkin_date**  <br>*optional*                 | **Example** : `"1970-01-01T00:00:00Z"`                          | string (date-time)                            |
| **id**  <br>*optional*  <br>*read-only*                   | **Example** : `0`                                               | integer                                       |
| **identity_number**  <br>*optional*                       | **Maximal length** : `30`  <br>**Example** : `"string"`         | string                                        |
| **last_meal**  <br>*optional*                             | **Maximal length** : `50`  <br>**Example** : `"string"`         | string                                        |
| **last_meal_time**  <br>*optional*                        | **Example** : `"1970-01-01T00:00:00Z"`                          | string (date-time)                            |
| **medical_followup**  <br>*optional*                      | **Example** : `true`                                            | boolean                                       |
| **name**  <br>*optional*                                  | **Maximal length** : `50`  <br>**Example** : `"string"`         | string                                        |
| **non_transport_reason**  <br>*optional*  <br>*read-only* | **Example** : `"string"`                                        | string                                        |
| **occurrence**  <br>*optional*                            | **Example** : `"[occurrencesimplified](#occurrencesimplified)"` | [OccurrenceSimplified](#occurrencesimplified) |
| **pharmacies**  <br>*optional*  <br>*read-only*           | **Example** : `[ "[pharmacy](#pharmacy)" ]`                     | < [Pharmacy](#pharmacy) > array               |
| **procedure_circulation**  <br>*optional*                 | **Example** : `"[procedurecirculation](#procedurecirculation)"` | [ProcedureCirculation](#procedurecirculation) |
| **procedure_protocol**  <br>*optional*                    | **Example** : `"[procedureprotocol](#procedureprotocol)"`       | [ProcedureProtocol](#procedureprotocol)       |
| **procedure_rcp**  <br>*optional*                         | **Example** : `"[procedurercp](#procedurercp)"`                 | [ProcedureRCP](#procedurercp)                 |
| **procedure_scale**  <br>*optional*                       | **Example** : `"[procedurescale](#procedurescale)"`             | [ProcedureScale](#procedurescale)             |
| **procedure_ventilation**  <br>*optional*                 | **Example** : `"[procedureventilation](#procedureventilation)"` | [ProcedureVentilation](#procedureventilation) |
| **risk_situation**  <br>*optional*                        | **Maximal length** : `50`  <br>**Example** : `"string"`         | string                                        |
| **symptom**  <br>*optional*                               | **Example** : `"[symptomdetails](#symptomdetails)"`             | [SymptomDetails](#symptomdetails)             |
| **type_of_emergency**  <br>*optional*                     | **Maximal length** : `100`  <br>**Example** : `"string"`        | string                                        |
| **type_of_transport**  <br>*optional*  <br>*read-only*    | **Example** : `"string"`                                        | string                                        |
| **usual_medication**  <br>*optional*                      | **Maximal length** : `100`  <br>**Example** : `"string"`        | string                                        |


<a name="victimdetails"></a>
### VictimDetails

| Name                                                      | Description                                                     | Schema                                        |
|-----------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------|
| **address**  <br>*optional*                               | **Maximal length** : `100`  <br>**Example** : `"string"`        | string                                        |
| **age**  <br>*optional*                                   | **Example** : `0`                                               | integer                                       |
| **allergies**  <br>*optional*                             | **Maximal length** : `100`  <br>**Example** : `"string"`        | string                                        |
| **birthdate**  <br>*optional*                             | **Example** : `"1970-01-01"`                                    | string (date)                                 |
| **circumstances**  <br>*optional*                         | **Maximal length** : `100`  <br>**Example** : `"string"`        | string                                        |
| **comments**  <br>*optional*                              | **Maximal length** : `400`  <br>**Example** : `"string"`        | string                                        |
| **disease_history**  <br>*optional*                       | **Maximal length** : `200`  <br>**Example** : `"string"`        | string                                        |
| **episode_number**  <br>*optional*                        | **Example** : `0`                                               | integer                                       |
| **evaluations**  <br>*optional*  <br>*read-only*          | **Example** : `[ "[evaluation](#evaluation)" ]`                 | < [Evaluation](#evaluation) > array           |
| **gender**  <br>*optional*                                | **Maximal length** : `25`  <br>**Example** : `"string"`         | string                                        |
| **hospital**  <br>*optional*                              | **Example** : `0`                                               | integer                                       |
| **hospital_checkin_date**  <br>*optional*                 | **Example** : `"1970-01-01T00:00:00Z"`                          | string (date-time)                            |
| **id**  <br>*optional*  <br>*read-only*                   | **Example** : `0`                                               | integer                                       |
| **identity_number**  <br>*optional*                       | **Maximal length** : `30`  <br>**Example** : `"string"`         | string                                        |
| **last_meal**  <br>*optional*                             | **Maximal length** : `50`  <br>**Example** : `"string"`         | string                                        |
| **last_meal_time**  <br>*optional*                        | **Example** : `"1970-01-01T00:00:00Z"`                          | string (date-time)                            |
| **medical_followup**  <br>*optional*                      | **Example** : `true`                                            | boolean                                       |
| **name**  <br>*optional*                                  | **Maximal length** : `50`  <br>**Example** : `"string"`         | string                                        |
| **non_transport_reason**  <br>*optional*  <br>*read-only* | **Example** : `"string"`                                        | string                                        |
| **occurrence**  <br>*optional*                            | **Example** : `"[occurrencesimplified](#occurrencesimplified)"` | [OccurrenceSimplified](#occurrencesimplified) |
| **pharmacies**  <br>*optional*  <br>*read-only*           | **Example** : `[ "[pharmacy](#pharmacy)" ]`                     | < [Pharmacy](#pharmacy) > array               |
| **procedure_circulation**  <br>*optional*                 | **Example** : `"[procedurecirculation](#procedurecirculation)"` | [ProcedureCirculation](#procedurecirculation) |
| **procedure_protocol**  <br>*optional*                    | **Example** : `"[procedureprotocol](#procedureprotocol)"`       | [ProcedureProtocol](#procedureprotocol)       |
| **procedure_rcp**  <br>*optional*                         | **Example** : `"[procedurercp](#procedurercp)"`                 | [ProcedureRCP](#procedurercp)                 |
| **procedure_scale**  <br>*optional*                       | **Example** : `"[procedurescale](#procedurescale)"`             | [ProcedureScale](#procedurescale)             |
| **procedure_ventilation**  <br>*optional*                 | **Example** : `"[procedureventilation](#procedureventilation)"` | [ProcedureVentilation](#procedureventilation) |
| **risk_situation**  <br>*optional*                        | **Maximal length** : `50`  <br>**Example** : `"string"`         | string                                        |
| **symptom**  <br>*optional*                               | **Example** : `"[symptomdetails](#symptomdetails)"`             | [SymptomDetails](#symptomdetails)             |
| **type_of_emergency**  <br>*optional*                     | **Maximal length** : `100`  <br>**Example** : `"string"`        | string                                        |
| **type_of_transport**  <br>*optional*  <br>*read-only*    | **Example** : `"string"`                                        | string                                        |
| **usual_medication**  <br>*optional*                      | **Maximal length** : `100`  <br>**Example** : `"string"`        | string                                        |


<a name="victimid"></a>
### VictimId

| Name                                    | Description       | Schema  |
|-----------------------------------------|-------------------|---------|
| **id**  <br>*optional*  <br>*read-only* | **Example** : `0` | integer |


<a name="victimtransport"></a>
### VictimTransport

| Name                                     | Description          | Schema  |
|------------------------------------------|----------------------|---------|
| **episode_number**  <br>*optional*       | **Example** : `0`    | integer |
| **hospital**  <br>*required*             | **Example** : `0`    | integer |
| **id**  <br>*optional*  <br>*read-only*  | **Example** : `0`    | integer |
| **medical_followup**  <br>*optional*     | **Example** : `true` | boolean |
| **non_transport_reason**  <br>*required* | **Example** : `0`    | integer |
| **type_of_transport**  <br>*required*    | **Example** : `0`    | integer |




<a name="securityscheme"></a>
## Security

<a name="basic"></a>
### Basic
*Type* : basic



