import subprocess
import sys
import webbrowser as wb

def run_command(command):
    """Ejecuta un comando en el sistema."""
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al ejecutar el comando {command}: {e}", file=sys.stderr)
        sys.exit(1)

# Ejemplo de cómo ejecutar un comando Django antes de iniciar la aplicación principal
# run_command(["py", "manage.py", "migrate"])  # Ejecuta las migraciones
# run_command(["py", "manage.py", "collectstatic", "--noinput"])  # Recopila archivos estáticos

# Aquí puedes añadir más comandos según necesites

# Finalmente, inicia la aplicación principal
# Por ejemplo, si tu archivo principal es `main.py`, reemplaza 'my_application' por 'main'
wb.open('http://localhost:8000/')
run_command(["py", "manage.py", "runserver"])
