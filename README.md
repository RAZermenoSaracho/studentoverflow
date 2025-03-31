# StudentOverflow

StudentOverflow es una aplicación web de preguntas y respuestas inspirada en StackOverflow. Permite a los usuarios registrarse, iniciar sesión, publicar preguntas, responder, votar, editar su perfil y ver rankings basados en reputación.

---

## 🚀 Requisitos

- Python 3.9+
- PostgreSQL
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

4. **Configura la base de datos PostgreSQL**:

- Crea una base de datos llamada `studentoverflow`:

```sql
CREATE DATABASE studentoverflow;
```

- Asegúrate de que `app.py` o el archivo de configuración apunte a tu URI de conexión, por ejemplo:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://usuario:contraseña@localhost/studentoverflow"
```

5. **Inicializa las tablas**:

```bash
python app.py
```

Esto creará todas las tablas si aún no existen.

---

## 📂 Estructura del proyecto

```
studentoverflow/
├── app.py
├── backend/
│   ├── models/
│   ├── routes/
│   ├── templates/
│   ├── static/
│   └── ...
├── requirements.txt
└── README.md
```

---

## 🧪 Funcionalidades

- Registro e inicio de sesión con validaciones
- Perfil de usuario editable con foto de perfil
- Publicación de preguntas y respuestas
- Votación positiva y negativa en respuestas
- Ranking de usuarios por reputación
- Búsqueda por preguntas y respuestas
- Diseño responsive para dispositivos móviles

---

## 🧼 Notas

- Las imágenes se almacenan en `static/uploads/`
- Para que las imágenes de perfil se carguen correctamente, asegúrate de que la carpeta `uploads/` exista y contenga el archivo `default_pp.jpg`.

---

## 💬 Licencia

Este proyecto es de uso educativo.