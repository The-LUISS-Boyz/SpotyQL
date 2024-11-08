from fastapi import APIRouter
from fastapi.responses import HTMLResponse, Response
import os
from jinja2 import Template
from utils import configuration, context

router = APIRouter()

@router.get("/{path}", response_class=HTMLResponse)
async def get_page(path: str):
  file_path = os.path.join(configuration.frontend_path, path)
  try:
    with open(file_path, "r") as file:
      content = file.read()
      template = Template(content)
      rendered_content = template.render(**context)
      
    if path.endswith(".css"):
      return Response(content=rendered_content, media_type="text/css")
    return rendered_content
  except FileNotFoundError:
    return HTMLResponse(content="Page not found.", status_code=404)