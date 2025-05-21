# FastAPI MongoDB Base Template

A production-ready boilerplate for building FastAPI applications with MongoDB integration. This template uses [fastapi-mongo-base](https://pypi.org/project/fastapi-mongo-base) package which provides pre-built CRUD operations and uses Beanie as the MongoDB ODM (Object Document Mapper).

## 🚀 Quick Start

1. Clone and setup:
```bash
git clone https://github.com/mahdikiani/FastAPIMongoLaunchpad.git
cd fastapi-mongo-base-template
cp sample.env .env
```

2. Start the application:
```bash
docker-compose up --build
```

Your API docs will be available at `http://localhost:8000/api/v1/docs`

## ✨ Features

- **Ready-to-use CRUD Operations**: Pre-built endpoints for Create, Read, Update, and Delete operations
- **MongoDB Integration**: Uses Beanie ODM for MongoDB operations
- **FastAPI Framework**: Modern, fast API development with automatic OpenAPI documentation
- **Docker Support**: Containerized development and deployment
- **Modular Architecture**: Easy to extend and maintain
- **Environment Configuration**: Flexible configuration management

## 📁 Project Structure

```
app/
├── apps/                    # Your application modules go here
│   └── your_app/           # Example: books, users, products, etc.
│       ├── __init__.py     # Module initialization
│       ├── models.py       # MongoDB models (Beanie documents)
│       ├── schemas.py      # Pydantic schemas for request/response
│       ├── routes.py       # API endpoints
│       └── services.py     # Business logic
├── server/                 # Server configuration
└── main.py                # Application entry point
```

## Getting Started

Let's create a simple "Books" module as an example:

1. Create the module directory and files:
```bash
mkdir -p app/apps/books
touch app/apps/books/{__init__.py,models.py,schemas.py,routes.py,services.py}
```

2. Define your schemas (`schemas.py`):
```python
from fastapi_mongo_base.schemas import BaseEntitySchema

class BookSchema(BaseEntitySchema):
    title: str
    author: str
    publish_year: int
    isbn: str | None = None
```

3. Create your model (`models.py`):
```python
from fastapi_mongo_base.models import BaseEntity
from .schemas import BookSchema

class Book(BookSchema, BaseEntity):
    """Book model that inherits from both BookSchema and BaseEntity"""
    pass
```

4. Set up routes (`routes.py`):
```python
from fastapi_mongo_base.routes import AbstractBaseRouter
from . import models, schemas

class BookRouter(AbstractBaseRouter):
    def __init__(self):
        super().__init__(model=models.Book, schema=schemas.BookSchema)

router = BookRouter().router
```

5. Add business logic (`services.py`):
```python
from . import models

# Add custom business logic here
# The basic CRUD operations are already provided by AbstractBaseRouter
```

6. Register your router in `server/server.py`:
```python
from fastapi_mongo_base.core import app_factory
from apps.books import router as book_router
from . import config

app = app_factory.create_app(settings=config.Settings())
app.include_router(book_router, prefix=f"{config.Settings.base_path}/books")
```

## 📚 Available Endpoints

After setting up your module, you'll automatically have these endpoints:

- `GET /api/v1/books` - List all books
- `POST /api/v1/books` - Create a new book
- `GET /api/v1/books/{id}` - Get a specific book
- `PATCH /api/v1/books/{id}` - Update a book
- `DELETE /api/v1/books/{id}` - Delete a book

## 🔧 Configuration

1. Environment Variables:
   - Copy `sample.env` to `.env`
   - Update the values in `.env` with your configuration

2. MongoDB Connection:
   - The template uses MongoDB running in Docker
   - Connection settings are configured in `sample.env`

## 📖 API Documentation

Once your application is running, you can access:
- Swagger UI: `http://localhost:8000/api/v1/docs`
- ReDoc: `http://localhost:8000/api/v1/redoc`

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
