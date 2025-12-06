# Acortador de URL con Tracking

Esta es una aplicación simple de acortador de URLs construida con Python y Flask. Permite acortar enlaces largos y rastrear cuántas veces han sido visitados.

## Requisitos

- Python 3.x instalado en tu sistema.

## Instalación y Configuración

Sigue estos pasos para poner en marcha la aplicación en tu ordenador:

1.  **Clonar o descargar este repositorio** en tu máquina.

2.  **Crear un entorno virtual (Opcional pero recomendado):**
    Abre tu terminal en la carpeta del proyecto y ejecuta:
    ```bash
    python3 -m venv venv
    ```
    Activa el entorno virtual:
    - En Windows: `venv\Scripts\activate`
    - En macOS/Linux: `source venv/bin/activate`

3.  **Instalar las dependencias:**
    Ejecuta el siguiente comando para instalar Flask y las librerías necesarias:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicializar la base de datos:**
    Antes de arrancar la app por primera vez, necesitas crear la base de datos. Ejecuta:
    ```bash
    python database.py
    ```
    Esto creará un archivo `database.db` y configurará las tablas.

## Ejecutar la Aplicación

Para iniciar el servidor, ejecuta:

```bash
python app.py
```

Verás un mensaje indicando que el servidor está corriendo (normalmente en `http://127.0.0.1:5000`).

## Uso

1.  Abre tu navegador web y ve a `http://127.0.0.1:5000`.
2.  **Acortar URL:** Introduce la URL que quieres acortar en el formulario. Opcionalmente, escribe un nombre personalizado.
3.  **Compartir:** Copia la URL acortada que aparece y compártela.
4.  **Ver Estadísticas:** Haz clic en "Estadísticas" en el menú superior (o ve a `http://127.0.0.1:5000/stats`) para ver cuántos clicks han recibido tus enlaces.
