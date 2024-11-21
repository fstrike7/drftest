# Django Rest Framework TEST

Proyecto desplegado en [render.com](https://drfcrud-test-aq9l.onrender.com/api/projects/)

Desarrollado con Django REST Framework, se basa en una API tipo CRUD para administrar proyectos personales. 
Tiene un único modelo Projects con los siguientes campos:
- **ID**
- **Title**: Max 200 Char. Título del proyecto.
- **Description**: Campo de texto. Descripción básica del proyecto.
- **Image**: Permite subir y alojar una imagen estatica.
- **Technologies**: Conjunto de strings que representan las técnologias usadas en cada proyecto, separados por tags usando django-taggit.

## Ejemplos:
### [GET]:
```
curl --location 'https://drfcrud-test-aq9l.onrender.com/api/projects'
```

### [POST]:

### [PATCH]:
```
curl --location --request PATCH 'https://drfcrud-test-aq9l.onrender.com/api/projects/1/' \
--header 'Content-Type: application/json' \
--data '{
    "technologies": [
        "Python", "Django", "CSS"
    ]
}'
```

### [DELETE]:
```
curl --location --request DELETE 'https://drfcrud-test-aq9l.onrender.com/api/projects/1/'
```
