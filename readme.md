# Challenge Houm

## Instalación

### Requerimientos

Python 3.10
Pip 2.22

### Instalación de packetes

```
pip install -r requirements.txt
```

### Ejecución de programa

En el directorio raiz de la aplicación

Para ejecución con settings de desarrollo. Esto es, logs en  consola y en archivo en carpeta logs. La carpeta logs está configurada para correr en el directorio raiz de la aplicación. Por lo tanto debemos crear ese directorio. En el caso de windows y linux el comando es

```
mkdir logs
```
Luego debemos crear la estructura de la base de datos. Esto creará una base db.sqlite3

```
python.exe  manage.py migrate --run-syncdb
```
Luego podemos iniciar la aplicación

```
python manage.py runserver
```

Abrir en un browser la url http://127.0.0.1:8000/docs/ donde está la interfaz OpenAPI.

Para ejecución con settings de testing. Esto es, logs en archivo en carpeta logs

```
python manage.py  runserver --settings=houmchallenge.settings_options.settings_testing
```

Nota: El archivos de settings por defecto usa el archivo ubicado en settings_options/settings_dev

### Pylint

Ejecución de analizador de código. En la carpeta raiz de la aplicación:

```
pylint geohoum
```

### Tests automatizados

En la carpeta raiz de la aplicación:

```
python manage.py test geohoum
```

### Analisis de cobertura de test automatizados

En la carpeta raiz de la aplicación:

```
coverage run --source="." manage.py test geohoum
```

y después:

```
coverage report
```

## Supuestos

1. Cada nuevo registro de posición que se envia desde el cliente posee un identificador de houmer y un identificador de propiedad.
2. Cada houmer posee un id unico
3. Cada propiedad posee un id unico


## Arquitecura

1. Se uso el framework Django y el paquete DRF. 
2. El esquema de la API se encuentra en el directorio static y el rendering se configuró para obtener el archivo de un recurso estático. Esto para agregar mas detalles que la configuración dinámica no pudo llenar.
3. Para el calculo de la distancia del trayecto se uso la biblioteca geopy.


## Ejecución de la API

Consiste en una api de 3 llamadas mas una de documentacion:

### 1. Envio de coordenadas

Consiste en una llamada HTTP POST con los siguientes datos:
    * Id Houmer: un identificados unico para cada houmer. (numero entre 1 y 10000)
    * Id Propiedad: es un numero que identifica a cada propiedad visitadas. (numero entre 1 y 100000)
    * Fecha y hora de comienzo de visita
    * Fecha y hora de termino de visita. 
    * Longitud: numero decimal entre -90 y 90
    * Latitud: numero decimal entre -180 y 180

Ejemplo de llamada:

```
curl -X 'POST' \
  'http://127.0.0.1:8000/geohoum/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'X-CSRFToken: N34w2AEnqzr208SwLI30XWKJstdDUJqhfF7OREp0Nskc4xGbjGZ2U4nb4LLGjRIu' \
  -d '{
  "id_houmer": 10,
  "id_property": 2300,
  "start_date": "2022-08-25T20:28:23.087Z",
  "end_date": "2022-08-25T21:28:23.087Z",
  "latitude": -78,
  "longitude": -22
}'
```

### 2. Obtención de coordenadas visitadas y tiempo en cada una (en minutos)

Consiste en una llamada HTTP GET con los siguientes datos:
    * Id Houmer: un identificados unico para cada houmer. (numero entre 1 y 10000)
    * Fecha de comienzo de visita (año/mes/dia)


Ejemplo de llamada:

```
curl -X 'GET' \
  'http://127.0.0.1:8000/geohoum/visits/3/2022/8/25' \
  -H 'accept: application/json' \
  -H 'X-CSRFToken: N34w2AEnqzr208SwLI30XWKJstdDUJqhfF7OREp0Nskc4xGbjGZ2U4nb4LLGjRIu'
```

Ejemplo de salida:

```
[
  {
    "id_houmer": 3,
    "id_property": 2,
    "time": 1380
  }
]
```

### 3. Obtención de recorridos entre visitas con exceso de velocidad

Consiste en una llamada HTTP GET con los siguientes datos:
    * Id Houmer: un identificados unico para cada houmer. (numero entre 1 y 10000)
    * Fecha de comienzo de visita (año/mes/dia)
    * Velocidad maxima permitida (km/h)

Ejemplo de llamada:

```
curl -X 'GET' \
  'http://127.0.0.1:8000/geohoum/speed/25/10/2022/8/25' \
  -H 'accept: application/json' \
  -H 'X-CSRFToken: N34w2AEnqzr208SwLI30XWKJstdDUJqhfF7OREp0Nskc4xGbjGZ2U4nb4LLGjRIu'
```

Ejemplo de salida:

```
[
  {
    "id_houmer": 213,
    "id_property_start": 2300,
    "id_property_end": 2500,
    "start_travel_date": "2022-08-25T11:00:00Z",
    "end_travel_date": "2022-08-25T12:00:00Z",
    "speed": 229
  }
]
```

### 4. Documentación

La documentación OpenAPI se encuentra en la url:

```
http://127.0.0.1:8000/docs/
```








