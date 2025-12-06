#!/bin/bash

# Colores para la terminal
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}=== Iniciando Acortador de URL ===${NC}"

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 no está instalado. Por favor instálalo e inténtalo de nuevo."
    exit 1
fi

# Crear entorno virtual si no existe
if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv venv

    echo "Instalando dependencias..."
    source venv/bin/activate
    pip install -r requirements.txt
else
    source venv/bin/activate
fi

# Inicializar base de datos si no existe
if [ ! -f "database.db" ]; then
    echo "Inicializando base de datos..."
    python database.py
fi

# Abrir navegador (intentar diferentes comandos según el SO)
echo "Abriendo navegador..."
if which xdg-open > /dev/null; then
  xdg-open http://127.0.0.1:5000 &
elif which open > /dev/null; then
  open http://127.0.0.1:5000 &
fi

# Iniciar la aplicación
echo -e "${GREEN}La aplicación está corriendo. Presiona CTRL+C para detenerla.${NC}"
python app.py
