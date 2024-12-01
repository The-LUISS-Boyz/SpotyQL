"""
This script is entitled to create the virtual environment and install the dependencies.
It will also load the application inside said environment.
"""

import venv
import os, sys
import logging
import subprocess
from datetime import datetime
from typing import Literal
import traceback

logging.basicConfig(level=logging.INFO)

def compose_log_message(timestamp: datetime, sender: str, message: str, type: Literal["info", "error"]):
  return f"[{timestamp.strftime('%Y-%m-%d %H:%M:%S')}] [{sender}] [{type}]: {message}"
def format_multiline_message(message: str):
  return message.replace("\n", "\n\t") + '\n'

def create_venv(venv_path: str):
  logger = logging.getLogger("create_venv")
  
  # create folder if not exists
  if not os.path.exists(venv_path):
    os.makedirs(venv_path)
  
  # create virtual environment
  venv.create(env_dir=venv_path, with_pip=True)
  
  log_message = compose_log_message(
    datetime.now(),
    "create_venv",
    f"Virtual environment created in {venv_path}",
    "info"
  )
  logger.info(log_message)
  
def install_dependencies(venv_path: str):
  logger = logging.getLogger("install_dependencies")
  # .env/Scripts/pip.exe or .env/bin/pip3
  pip_path = os.path.join(venv_path, "Scripts", "pip.exe") if os.name == "nt" else \
             os.path.join(venv_path, "bin", "pip")
  application_path = os.path.join(os.getcwd(), "application")
  
  log_message = compose_log_message(
    datetime.now(),
    "install_dependencies",
    f"Installing dependencies using {pip_path} for application in {application_path}",
    "info"
  )
  logger.info(log_message)
  
  # execute pip install -r requirements.txt
  process = subprocess.Popen(
    [pip_path, "install", "-r", os.path.join(application_path, "requirements.txt")],
    text=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
  )
  process.wait()
  
  # format output
  stdout, stderr = process.communicate()
  stdout = format_multiline_message(stdout)
  stderr = format_multiline_message(stderr)
  
  exit_code = process.returncode
  
  if exit_code != 0:
    logger_file = open("dep_install_startup.log", "a")
    
    log_message = compose_log_message(
      datetime.now(),
      "install_dependencies",
      f"Subprocess {pip_path} failed:\n\t{stderr}",
      "error"
    )
    logger_file.write(log_message)
    logger_file.close()
    
    logger.error(log_message)
    raise Exception(f"Subprocess {pip_path} failed (check dep_install_startup.log)")
  else:
    log_message = compose_log_message(
      datetime.now(),
      "install_dependencies",
      f"Dependencies installed successfully:\n\t{stdout}",
      "info"
    )
    logger.info(log_message)

def initial_config(venv_path: str):
  logger = logging.getLogger("initial_config")
  try:
    logger.info(f"Creating virtual environment in {venv_path}")
    create_venv(venv_path)
  except Exception as e:
    logger.error(f"Error creating virtual environment: {e}")
    sys.exit(1)
  
  try:
    logger.info("Installing dependencies")
    install_dependencies(venv_path)
  except Exception as e:
    logger.error(f"Error installing dependencies: {e}")
    sys.exit(1)
def load_application(venv_path: str):
  logger = logging.getLogger("load_application")
  application_path = os.path.join(os.getcwd(), "application")
  application_script = os.path.join(application_path, "main.py")
  # .env/Scripts/python.exe or .env/bin/python3
  python_path = os.path.join(venv_path, "Scripts", "python.exe") if os.name == "nt" else \
                os.path.join(venv_path, "bin", "python")
  
  log_message = compose_log_message(
    datetime.now(),
    "load_application",
    f"Loading application in {application_script}",
    "info"
  )
  logger.info(log_message)
  
  # execute python application/main.py
  process = subprocess.run(
    [python_path, application_script],
    check=False,
    text=True
  )
  
  exit(process.returncode)

def main():
  logger = logging.getLogger("main")
  venv_path = sys.argv[1]
  
  if not os.path.exists(venv_path):
    logger.info("Virtual environment not found, creating it")
    initial_config(venv_path)
  
  logger.info("Loading application")
  load_application(venv_path)
  
if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python startup.py <venv_path>")
    print("Where <venv_path> is the desired path for the virtual environment")
    print("Example: python startup.py .env")
    sys.exit(1)
  
  main()
