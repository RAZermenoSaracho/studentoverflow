# StudentOverflow

💡 Plataforma tipo StackOverflow hecha con Flask y PostgreSQL, donde estudiantes pueden publicar preguntas académicas, recibir respuestas, votar, y usar formato Markdown.

---

## 🚀 Tecnologías

- Python 3
- Flask
- Flask-Login
- SQLAlchemy
- PostgreSQL
- Markdown
- HTML + CSS

---

## ⚙️ Instalación

### 1. Clona el repositorio

```bash
git clone https://github.com/tu-usuario/studentoverflow.git
cd studentoverflow
```

### 2. Crea y activa un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Configura tus credenciales de PostgreSQL

Crea un archivo `config/config.json` basado en el ejemplo:

```
config/
├── config.json ← este archivo lo creas tú
└── config_example.json ← ya incluido
```

Contenido de ejemplo:

```json
{
  "DB_USER": "tu_usuario",
  "DB_PASSWORD": "tu_contraseña",
  "DB_HOST": "localhost",
  "DB_PORT": 5432,
  "DB_NAME": "studentoverflow",
  "SECRET_KEY": "clave-secreta-para-sesiones"
}
```

> 🔒 Nota: `config/config.json` ya está ignorado en `.gitignore`.

---

## 🧪 Ejecución local

```bash
python app.py
```

La aplicación se ejecutará en:

```
http://localhost:5000
```

---

## 📝 Funcionalidades

- Registro e inicio de sesión con sesiones persistentes
- Crear y responder preguntas
- Votar respuestas (positivo/negativo)
- Renderizado de Markdown
- Header y footer fijos
- Interfaz limpia y responsiva

---

## 🧩 Próximas mejoras

- Vista previa de Markdown en tiempo real
- Filtros por materia o categoría
- Notificaciones y reputación de usuario

---

## 📄 Licencia

MIT License
