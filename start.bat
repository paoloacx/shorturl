@echo off
echo === Iniciando Acortador de URL ===

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python no encontrado. Por favor instala Python.
    pause
    exit /b
)

REM Crear entorno virtual si no existe
if not exist venv (
    echo Creando entorno virtual...
    python -m venv venv

    echo Instalando dependencias...
    call venv\Scripts\activate
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate
)

REM Inicializar base de datos si no existe
if not exist database.db (
    echo Inicializando base de datos...
    python database.py
)

REM Abrir navegador
echo Abriendo navegador...
start http://127.0.0.1:5000

REM Iniciar la aplicación
echo La aplicacion esta corriendo. Cierra esta ventana para detenerla.
python app.py
pause
