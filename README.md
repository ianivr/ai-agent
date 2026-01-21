# AI Agent

Un agente de IA conversacional potenciado por Google Gemini que puede ejecutar funciones para manipular archivos, leer contenido y ejecutar código Python.

## 📋 Descripción General

Este proyecto implementa un agente de IA que utiliza el modelo **Gemini 2.5 Flash** de Google para interactuar de forma conversacional. El agente es capaz de invocar automáticamente funciones para realizar tareas específicas como:

- Leer el contenido de archivos
- Obtener información sobre archivos en directorios
- Ejecutar scripts de Python
- Escribir y guardar archivos

El agente utiliza el patrón de **function calling** para determinar automáticamente qué acciones tomar basándose en las indicaciones del usuario.

## ✨ Características

- **Interacción con Gemini API**: Integración con Google Generative AI
- **Function Calling**: Ejecución automática de funciones disponibles
- **Gestión de Archivos**: Lectura, escritura y análisis de archivos
- **Ejecución de Código**: Capacidad de ejecutar scripts Python
- **Modo Verbose**: Opción para ver métricas de tokens y detalles de procesamiento
- **Soporte Multiconversación**: Mantiene el contexto de conversación

## 🚀 Instalación

### Requisitos Previos
- Python >= 3.12
- Clave API de Google Gemini

### Pasos

1. **Clonar el repositorio**
```bash
git clone <repository-url>
cd ai-agent
```

2. **Instalar dependencias**
```bash
pip install -r pyproject.toml
```

O usando `pip`:
```bash
pip install google-genai==1.12.1 python-dotenv==1.1.0
```

3. **Configurar variables de entorno**

Crea un archivo `.env` en la raíz del proyecto:
```
GEMINI_API_KEY=tu_clave_api_aqui
```

## 💻 Uso

### Uso Básico

```bash
python main.py "Tu pregunta aquí"
```

Ejemplo:
```bash
python main.py "¿Cuál es el contenido del archivo calculator/main.py?"
```

### Modo Verbose

Para ver información detallada sobre el procesamiento:

```bash
python main.py "Tu pregunta aquí" --verbose
```

### Ejemplos de Uso

```bash
# Leer un archivo
python main.py "Lee el contenido de calculator/main.py"

# Obtener información de archivos
python main.py "¿Qué archivos hay en el directorio calculator?"

# Ejecutar código Python
python main.py "Ejecuta el archivo calculator/tests.py"

# Escribir un archivo
python main.py "Escribe 'Hola Mundo' en un archivo llamado saludo.txt"
```

## 📁 Estructura del Proyecto

```
ai-agent/
├── main.py                 # Punto de entrada principal
├── config.py               # Configuración del proyecto
├── prompts.py              # Prompts del sistema
├── call_function.py        # Lógica de invocación de funciones
├── pyproject.toml          # Definición de dependencias
├── README.md               # Este archivo
├── functions/              # Funciones disponibles para el agente
│   ├── get_file_content.py    # Leer contenido de archivos
│   ├── get_files_info.py      # Obtener info de directorios
│   ├── run_python_file.py     # Ejecutar scripts Python
│   └── write_file.py          # Escribir archivos
├── calculator/             # Ejemplo de directorio de trabajo
│   ├── main.py
│   ├── tests.py
│   ├── lorem.txt
│   └── pkg/
│       ├── calculator.py
│       ├── render.py
│       └── morelorem.txt
└── tests/                  # Pruebas unitarias
```

## 🔧 Funciones Disponibles

El agente tiene acceso a las siguientes funciones:

### 1. `get_file_content(file_path: str)`
Lee el contenido de un archivo.

### 2. `get_files_info(directory_path: str)`
Obtiene información sobre archivos en un directorio.

### 3. `run_python_file(file_path: str)`
Ejecuta un script Python.

### 4. `write_file(file_path: str, content: str)`
Escribe contenido en un archivo.

## 🧪 Pruebas

El proyecto incluye pruebas unitarias para las funciones:

```bash
python test_get_file_content.py
python test_get_files_info.py
python test_run_python_file.py
python test_write_file.py
```

## ⚙️ Configuración

### Variables de Entorno

- `GEMINI_API_KEY`: Tu clave API de Google Gemini (requerida)

### Configuración del Proyecto (config.py)

- `MAX_CHARS`: Máximo de caracteres a procesar (por defecto: 10000)
- `WORKING_DIR`: Directorio de trabajo (por defecto: "./calculator")

## 📚 API de Google Gemini

Este proyecto utiliza:
- **Modelo**: `gemini-2.5-flash`
- **Librería**: `google-genai` v1.12.1
- **Documentación**: [Google Generative AI Documentation](https://ai.google.dev/)

## 🆘 Solución de Problemas

### Error: "GEMINI_API_KEY is not set"
Asegúrate de que el archivo `.env` existe y contiene tu clave API de Gemini.

### Error: "No usage metadata found"
Este error generalmente indica un problema con la respuesta de la API. Verifica tu conexión a internet y clave API.

### El agente no ejecuta funciones
Verifica que:
- Las funciones en `functions/` están correctamente importadas
- La configuración del modelo en `main.py` es correcta
- El prompt del sistema contiene las instrucciones adecuadas

## 📝 Notas

- El agente mantiene el contexto de conversación durante múltiples pasos
- Usa el modo `--verbose` para depuración y monitoreo de tokens
- El directorio de trabajo por defecto es `./calculator`
