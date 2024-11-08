from utils import context
from datetime import datetime

def log(message):
  context["logs"].append({
    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    'message': message
  })
