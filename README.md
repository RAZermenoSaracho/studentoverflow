# StudentOverflow

**StudentOverflow** es una aplicación web de preguntas y respuestas tipo StackOverflow, construida con Flask, PostgreSQL y Bootstrap. Permite a los usuarios registrarse, publicar preguntas y respuestas, votar, editar su perfil y subir imágenes.

---

## 🚀 Requisitos

- Python 3.9+
- PostgreSQL instalado y corriendo
- pip

---

## 🔧 Instalación (modo local)

1. **Clona el repositorio**:

```bash
git clone https://github.com/tu_usuario/studentoverflow.git
cd studentoverflow
```

2. **Crea un entorno virtual**:

```bash
python3 -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
```

3. **Instala las dependencias**:

```bash
pip install -r requirements.txt
```

4. **Copia el archivo de configuración**:

```bash
cp config_example.json config.json
```

Luego edita `config.json` con tus credenciales de PostgreSQL:

```json
{
    "DB_USER": "tu_usuario",
    "DB_PASSWORD": "tu_contraseña",
    "DB_HOST": "localhost",
    "DB_PORT": "5432",
    "DB_NAME": "studentoverflow",
    "SECRET_KEY": "clave_ultra_segura"
}
```

5. **Ejecuta la app**:

```bash
python app.py
```

Esto creará la base de datos y las tablas automáticamente si no existen.

---

## 📂 Estructura del proyecto

```
studentoverflow/
├── app.py
├── backend/
│   ├── forms/
│       ├── answer_form.py
│       └── question_form.py
│   ├── models/
│       ├── answer.py
│       ├── image.py
│       ├── question.py
│       ├── user.py
│       └── vote.py
│   ├── routes/
│       ├── __init__.py
│       ├── auth.py
│       └── views.py
│   ├── extensions.py
│   └── login_manager.py
├── templates/
│   ├── ask.html
│   ├── base.html
│   ├── edit_answer.html
│   ├── edit_question.html
│   ├── footer.html
│   ├── header.html
│   ├── index.html
│   ├── login.html
│   ├── profile.html
│   ├── question.html
│   └── signup.html
├── static/
│   ├── css/
│       └── styles.css
│   ├── js/
│       └── scripts.js
│   └── uploads/
│       └── default_pp.jpg
├── config/
│   ├── init_app.py
│   ├── init_db.py
│   ├── config_example.json
│   └── config.json              # (creado manualmente)
├── requirements.txt
└── README.md
```

---

## 🧪 Funcionalidades principales

- Registro e inicio de sesión con validaciones
- Subida de foto de perfil
- Edición de perfil
- Publicación de preguntas y respuestas con imágenes
- Votación positiva y negativa en respuestas
- Ranking dinámico de usuarios por reputación
- Búsqueda de preguntas y respuestas
- Vista responsive para móviles

---

## 📦 Notas

- Las imágenes de usuarios y preguntas se almacenan en `static/uploads/`
- La imagen `default_pp.jpg` se usa como avatar predeterminado

---

## 💬 Licencia

Este proyecto fue desarrollado con fines educativos.
