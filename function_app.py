import azure.functions as func
from azure.functions import AsgiMiddleware

from main import fastapi_app

app = func.FunctionApp()

@app.function_name(name="fastapi")
@app.route(
    route="{*route}",
    auth_level=func.AuthLevel.ANONYMOUS
)
async def fastapi_handler(req: func.HttpRequest, context: func.Context):
    return await AsgiMiddleware(fastapi_app).handle_async(req, context)
