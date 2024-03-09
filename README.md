# API de Fecha y Contador

Esta API proporciona funcionalidades para obtener la fecha actual en diferentes formatos y contar el número de veces que se han llamado los endpoints. El desarrollo de esta API fue acelerado con la asistencia de **ChatGPT**, que sirvió como una herramienta de soporte para optimizar el tiempo de implementación y aclarar dudas durante el proceso de desarrollo, complementando así las habilidades del desarrollador.

## Funcionalidades

- **Obtener Fecha (`/date/`):**
  - Método `POST`: Devuelve la fecha actual. El formato de la respuesta depende del valor booleano `boolean_param` enviado en el cuerpo de la solicitud. Si `boolean_param` es `true`, devuelve la fecha en formato "aaaa-mm-dd hh:mm:ss". Si es `false`, en formato "aaaa-dd-mm".
  - Método `GET`: Devuelve la fecha actual en formato "aaaa-mm-dd hh:mm:ss" sin necesidad de parámetros.

- **Obtener Contador de Accesos (`/counter/`):**
  - Método `GET`: Devuelve el número de veces que se ha accedido a los endpoints `/date/` y `/counter/`.

## Tecnologías Utilizadas

- FastAPI: Para la creación de la API.
- Pydantic: Para la validación y gestión de los modelos de datos.
- Uvicorn: Como servidor ASGI para servir la API.

## Ejecución

Para ejecutar la API localmente, necesitas tener instalado `Python` y los paquetes `fastapi` y `uvicorn`. Una vez instalados, puedes ejecutar el servidor utilizando el siguiente comando:

```bash
uvicorn main:app --reload
```

El servidor estará disponible en http://127.0.0.1:8000. Puedes acceder a http://127.0.0.1:8000/docs para ver la documentación interactiva generada por FastAPI y probar los endpoints directamente desde el navegador.

