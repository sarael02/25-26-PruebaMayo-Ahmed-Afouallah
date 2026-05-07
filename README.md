# Inventory Manager API

Una API REST construida con **FastAPI** para gestionar un inventario de productos, utilizando **SQLite** como base de datos. Este proyecto está diseñado con una arquitectura modular que separa las rutas, los modelos y la lógica de base de datos.

## Prueba local

```cmd
uvicorn app.main:app --reload
firefox localhost:8000/docs
```

## Personalizar

Modificar la aplicación para añadir una nueva ruta que muestre la versión de la aplicación junto con su nombre y apellidos.

Los más directo es añadir el siguiente código en `main.py`:

```python
app.include_router(tasks.router)

# Código que se añade
@app.get("/status")
def version():
    return {"status": "Apellidos, Nombre - v.xx"}
```

## Dockerizar

## Estructura del Proyecto

```out
inventory_manager/
│
├── app/
│   ├── main.py              # Punto de entrada de la aplicación FastAPI
│   ├── database.py          # Configuración de la base de datos y conexión
│   ├── models.py            # Definición de los modelos de datos
│   └── routers/
│       └── items.py         # Endpoints relacionados con los ítems del inventario
├── requirements.txt         # Dependencias del proyecto
├── Dockerfile               # Imagen de contenedor para despliegue
└── README.md                # Documentación general
```

## Modelos de Datos

```python
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    quantity: int

    class Config:
        from_attributes = True
```

## Endpoints Disponibles

| Método | Ruta              | Descripción                             | Parámetros            | Cuerpo (`Body`)     |
|--------|-------------------|-----------------------------------------|-----------------------|---------------------|
| GET    | `/items/`         | Lista todos los ítems del inventario    | -                     | -                   |
| GET    | `/items/{item_id}`| Devuelve un ítem por su ID              | `item_id: int`        | -                   |
| POST   | `/items/`         | Crea un nuevo ítem                      | -                     | `ItemCreate`        |
| PUT    | `/items/{item_id}`| Actualiza un ítem existente             | `item_id: int`        | `ItemCreate`        |
| DELETE | `/items/{item_id}`| Elimina un ítem                         | `item_id: int`        | -                   |

## Documentación

Disponible automáticamente en:

- `/docs` (Swagger UI)
- `/redoc` (ReDoc)

## Ejemplo de uso con `curl`

```bash
curl -X POST http://127.0.0.1:8000/items/ \
-H "Content-Type: application/json" \
-d '{"name": "Teclado", "description": "Mecánico", "price": 45.99, "quantity": 10}'
```

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/items/' \
  -H 'accept: application/json'
```
