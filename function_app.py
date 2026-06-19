import azure.functions as func
from azure.functions import AsgiMiddleware

from main import fastapi_app

app = func.FunctionApp()

asgi_middleware = AsgiMiddleware(fastapi_app)

@app.function_name(name="fastapi")
@app.route(
    route="{*route}",
    auth_level=func.AuthLevel.ANONYMOUS,
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
)
async def fastapi_handler(req: func.HttpRequest, context: func.Context):
    return await asgi_middleware.handle_async(req, context)
