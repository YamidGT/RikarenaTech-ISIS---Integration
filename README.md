# RikarenaTech

Proyecto: RikarenaTech — plataforma agrícola (backend Django + frontend React/Vite).

Este repositorio contiene una API REST en Django (backend) y una aplicación frontend en React (Vite + TypeScript) para gestionar usuarios, productos agrícolas, cultivos y alertas geolocalizadas.

---

**Resumen rápido**
- Backend: Django 5.2 + Django REST Framework + django-allauth (Google OAuth) + djangorestframework-simplejwt
- Frontend: React + Vite + TypeScript
- Base de datos por defecto: SQLite (desarrollo). Soporta S3/Cloudflare R2 para archivos.

---

**Estructura principal**
- `Project/backend/` — código Django (aplicaciones: `posts`, `users`, `crops`, `alerts`, `AuthenticationProject`, etc.)
- `Project/frontend/` — aplicación React (Vite + TypeScript)
- `Workshop-2/` — material complementario / mockups

---

## Requisitos previos
- Python 3.8+ (se recomienda 3.10+)
- Node.js 18+ y `npm` o `pnpm`
- pip

En Windows PowerShell (ejemplos):

```powershell
# Crear y activar entorno virtual (backend)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Instalar dependencias backend
pip install -r Project\backend\requirements.txt

# Instalar dependencias frontend
cd Project\frontend
npm install
# o usando pnpm: pnpm install
```

---

## Configuración de entorno
- Copia `Project/backend/.env.example` a `Project/backend/.env` y ajusta las variables (SECRET_KEY, DEBUG, FRONTEND_URL, BACKEND_URL, credenciales de S3/R2, DB si usas Postgres, etc.).

Variables más importantes:
- `SECRET_KEY` — clave Django
- `DEBUG` — True/False
- `FRONTEND_URL` / `BACKEND_URL`
- `DATABASE_*` — si usas Postgres en producción
- `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_STORAGE_BUCKET_NAME` — para S3/R2
- `GOOGLE_OAUTH2_CLIENT_ID` / `GOOGLE_OAUTH2_CLIENT_SECRET` — para login con Google (allauth)

---

## Ejecutar la aplicación (desarrollo)

Backend (desde `Project/backend` y con el venv activado):

```powershell
cd Project\backend
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Frontend (desde `Project/frontend`):

```powershell
cd Project\frontend
npm run dev
```

Accede al frontend en la URL que indique Vite (por defecto `http://localhost:5173`) y al backend en `http://localhost:8000`.

---

## Endpoints relevantes
- `GET /api/auth/token/` — Devuelve `refresh` y `access` JWT para el `request.user` autenticado (requiere cookie de sesión tras login con allauth). Se usa `rest_framework_simplejwt`.
- `api/auth/` — rutas de `AuthenticationProject` que incluyen `auth/` (allauth) y OAuth con Google.
- `api/users/` — endpoints de usuarios y perfiles.
- `api/posts/` — endpoints de productos/mercado.
- `api/crops/` — endpoints de cultivos.
- `api/alerts/` — endpoints de alertas (solo moderadores para crear/publicar).

Autenticación API: usar encabezado `Authorization: Bearer <access_token>` para endpoints que requieran JWT.

---

## Notas sobre autenticación social (Google)
- El sistema usa `django-allauth` para login social con Google. Si el usuario inicia sesión vía Google se crea/actualiza su `Profile.picture_url` con la URL de la imagen que provee Google.
- Tras el flujo OAuth, el proyecto dispone de una vista `get_jwt_token` que devuelve tokens JWT para el usuario autenticado.

Redirecciones y `next`:
- El adaptador social personalizado puede establecer `next` tras el login. Asegúrate de que la URL configurada concuerde con `/api/auth/token/` si tu frontend espera esa ruta.

---

## Almacenamiento de imágenes
- En desarrollo las imágenes se pueden servir desde disco. Para producción configure S3 o Cloudflare R2 con las variables indicadas en `.env`.

---

## Tests y calidad de código
- El proyecto incluye herramientas de linters (`flake8`, `black`, `isort`) y tests unitarios en las apps (`tests.py`).
- Ejecuta linters/formatters según tu flujo local: `black .`, `isort .`, `flake8`.

---

## Arquitectura (resumen)
- Capa Dominio: modelos y reglas de negocio en `users`, `posts`, `crops`, `alerts`.
- Capa Aplicación: servicios/serializers y manejadores de eventos en las apps.
- Capa Interfaz: vistas REST en cada app (`views.py`, `urls.py`) y frontend React.
- Capa Infraestructura: repositorios, almacenamiento en S3/R2, configuración DB.

---

## Desarrollo y contribuciones
- Para contribuir, crear ramas con prefijo `feature/` o `fix/` y abrir PR contra `main`.
- Ejecuta `python manage.py test` desde `Project/backend` para correr tests.

---

Si quieres, puedo:
- generar un `README` más corto orientado a despliegue en producción (Docker / Gunicorn + nginx),
- añadir ejemplos de .env para producción o
- crear un `docs/` con OpenAPI extraído de `drf-yasg`.

---

Licencia: (añade la licencia que prefieras)
