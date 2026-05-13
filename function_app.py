import azure.functions as func
from azure.functions import AsgiMiddleware

from main import fastapi_app

app = func.FunctionApp()

@app.function_name(name="fastapi")
@app.route(route="{*route}", auth_level=func.AuthLevel.ANONYMOUS)
def main(req: func.HttpRequest, context: func.Context):
    return AsgiMiddleware(fastapi_app).handle(req, context)
