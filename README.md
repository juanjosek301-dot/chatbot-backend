# Chatbot backend

API backend del chatbot institucional.

## Ejecutar con Docker Compose

```powershell
docker compose up -d --build db backend
```

La ruta <http://127.0.0.1:8000/> devuelve un mensaje de bienvenida para comprobar que el backend está activo. La documentación interactiva de la API está en <http://127.0.0.1:8000/docs> y el esquema OpenAPI en <http://127.0.0.1:8000/openapi.json>.

Rutas principales:

- `GET /` (bienvenida)
- `GET /opciones`
- `GET /ai/verificar_identificacion/{identificacion}`
- `POST /ai/generate`
- `POST /ai/sugerencia`
- `GET /ai/models`
- `POST /procesar_mensaje`

Para iniciar el servidor directamente con Python se necesita configurar `DATABASE_URL` con una instancia PostgreSQL accesible. Además, ejecuta Uvicorn desde `backend/app`, porque allí están los archivos JSON de configuración:

```powershell
Set-Location .\app
python -m pip install -r ..\requirements.txt
python -m uvicorn main:app --reload --port 8000
```
