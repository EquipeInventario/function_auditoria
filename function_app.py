import azure.functions as func
from azure.functions import AsgiMiddleware

from main import fastapi_app

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="{*route}")
def main(req: func.HttpRequest, context: func.Context):
    return AsgiMiddleware(fastapi_app).handle(req, context)
