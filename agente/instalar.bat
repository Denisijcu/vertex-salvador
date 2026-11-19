@echo off
REM ============================================================================
REM  instalar.bat - Prepara el servidor de herramientas de vertex-salvador.
REM  Crea un entorno de Python propio (.venv) dentro de esta carpeta: no cambia
REM  nada del Python del sistema. Se puede ejecutar varias veces sin problema.
REM ============================================================================
setlocal
cd /d "%~dp0"

echo.
echo [1/4] Comprobando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: no encuentro Python. Instala Python 3.10 o superior desde https://www.python.org/downloads/
    echo y marca la casilla "Add python.exe to PATH" durante la instalacion. Luego vuelve a ejecutar este archivo.
    pause
    exit /b 1
)
python -c "import sys; sys.exit(0 if sys.version_info >= (3, 10) else 1)"
if errorlevel 1 (
    echo.
    echo ERROR: hace falta Python 3.10 o superior. Version encontrada:
    python --version
    pause
    exit /b 1
)
python --version

echo.
echo [2/4] Creando el entorno .venv (solo la primera vez)...
if not exist ".venv\Scripts\python.exe" (
    python -m venv .venv
    if errorlevel 1 (
        echo ERROR: no se pudo crear el entorno .venv.
        pause
        exit /b 1
    )
)

echo.
echo [3/4] Instalando el paquete mcp dentro de .venv...
".venv\Scripts\python.exe" -m pip install --quiet --upgrade pip
".venv\Scripts\python.exe" -m pip install --quiet "mcp>=1.2"
if errorlevel 1 (
    echo ERROR: no se pudo instalar mcp. Revisa la conexion a internet y vuelve a intentarlo.
    pause
    exit /b 1
)

echo.
echo [4/4] Probando el servidor...
".venv\Scripts\python.exe" probar_servidor.py
if errorlevel 1 (
    echo ERROR: la prueba del servidor fallo. Copia lo que aparece arriba y envialo al soporte.
    pause
    exit /b 1
)

".venv\Scripts\python.exe" mostrar_config.py
echo.
echo Listo. Sigue el paso 4 de GUIA_INSTALACION.md.
pause
