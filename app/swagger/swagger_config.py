# Cấu hình tài liệu API 
from fastapi.openapi.utils import get_openapi

def custom_openapi(app):
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title= "CommercePython",
        version= "1.0.0",
        description= "Api for CommercePython",
        routes = app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema