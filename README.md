# **SolecitoCrochet**

## **Descripción del Proyecto**
**SolecitoCrochet** es una tienda en línea dedicada a productos hechos a mano con técnicas de crochet. La aplicación permite a los usuarios explorar una lista de productos, agregarlos al carrito de compras y realizar pedidos. El backend está construido con **Django**, mientras que el frontend utiliza **Alpine.js** para añadir interactividad sin sacrificar la simplicidad.

---

## **Tecnologías Utilizadas**

### **Backend**
- **Framework:** Django
- **Base de Datos:** SQLite (integrada por defecto en Django)
- **APIs:** Django REST Framework (opcional para futuras expansiones)

### **Frontend**
- **Interactividad:** Alpine.js
- **Estilos:** CSS personalizados y Tailwind
- **Gestión de Plantillas:** Sistema de plantillas de Django

### **Herramientas Adicionales**
- **Desarrollo Frontend:** Alpine.js (ligero y fácil de integrar)
- **Despliegue:** Compatible con plataformas como Heroku, AWS, o DigitalOcean

---

## **Estructura del Proyecto**

```
SolecitoCrochet/
├── backend/                  # Carpeta principal del backend (Django)
│   ├── manage.py
│   ├── SolecitoCrochet/      # Configuración principal del proyecto Django
│   │   ├── settings/
│   │   │   ├── base.py       # Configuración base compartida
│   │   │   ├── development.py # Configuración para desarrollo
│   │   │   ├── production.py  # Configuración para producción
│   │   ├── urls.py           # URLs principales del proyecto
│   │   └── wsgi.py
│   ├── apps/                 # Aplicaciones backend (separadas por módulos)
│   │   ├── core/             # Aplicación principal/core
│   │   ├── products/         # Gestión de productos
│   │   ├── orders/           # Gestión de pedidos
│   │   └── users/            # Gestión de usuarios
│   ├── static/               # Archivos estáticos (CSS, JS, imágenes, etc.)
│   │   ├── css/
│   │   ├── js/
│   │   │   └── alpine.js     # Script principal de Alpine.js
│   │   └── images/
│   ├── templates/            # Plantillas HTML gestionadas por Django
│   │   ├── base.html         # Plantilla base
│   │   ├── products/
│   │   │   ├── list.html
│   │   │   └── detail.html
│   │   ├── orders/
│   │   │   ├── checkout.html
│   │   │   └── confirmation.html
│   │   └── users/
│   │       ├── login.html
│   │       └── register.html
│   ├── media/                # Archivos multimedia subidos por usuarios
│   └── requirements.txt      # Dependencias del proyecto
│
├── .env                      # Variables de entorno
├── .gitignore                # Archivos ignorados por Git
└── README.md                 # Documentación del proyecto
```

---

## **Configuración Inicial**

### **1. Clonar el Repositorio**
```bash
git clone https://github.com/tu-usuario/SolecitoCrochet.git
cd SolecitoCrochet
```

### **2. Crear y Activar un Entorno Virtual**
```bash
# Crear un entorno virtual
python3 -m venv venv

# Activar el entorno virtual
# En Linux/Mac:
source venv/bin/activate
# En Windows:
venv\Scripts\activate
```

### **3. Instalar Dependencias**
```bash
pip install -r backend/requirements.txt
```

### **4. Configurar la Base de Datos**
SQLite ya está configurado por defecto en Django. Para aplicar las migraciones iniciales:
```bash
python backend/manage.py migrate
```

### **5. Crear un Superusuario (Opcional)**
Si deseas acceder al panel de administración de Django:
```bash
python backend/manage.py createsuperuser
```

### **6. Ejecutar el Servidor de Desarrollo**
```bash
python backend/manage.py runserver
```
La aplicación estará disponible en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## **Características Principales**

### **1. Lista de Productos**
- Los productos se muestran dinámicamente usando Alpine.js.
- Se pueden cargar productos desde una API simple expuesta por Django.

### **2. Carrito de Compras**
- Los usuarios pueden agregar productos al carrito y ver el total.
- Implementado completamente con Alpine.js para manejar el estado del carrito.

### **3. Gestión de Pedidos**
- Los usuarios pueden realizar pedidos (funcionalidad básica implementada).
- Futuras expansiones incluyen integración con pasarelas de pago.

### **4. Panel de Administración**
- Acceso al panel de administración de Django para gestionar productos, pedidos y usuarios.

---

## **Cómo Contribuir**

1. **Fork del Repositorio:** Haz un fork del repositorio en GitHub.
2. **Crear una Rama:** Crea una nueva rama para tus cambios:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. **Realizar Cambios:** Implementa tus cambios y asegúrate de que todo funcione correctamente.
4. **Enviar un Pull Request:** Envía un pull request explicando tus cambios.

---

## **Pruebas y Calidad del Código**

### **Pruebas Backend**
Usa `pytest` o `unittest` para escribir pruebas unitarias y de integración para el backend.

```bash
# Ejecutar pruebas
python backend/manage.py test
```

### **Pruebas Frontend**
Asegúrate de probar manualmente la interactividad de Alpine.js en diferentes navegadores.

---

## **Despliegue**

### **Opciones de Despliegue**
- **Heroku:** Compatible con Django y SQLite (ideal para proyectos pequeños).
- **AWS/DigitalOcean:** Ideal para proyectos más grandes que requieren escalabilidad.

### **Pasos Básicos para Desplegar en Heroku**
1. Crea una cuenta en Heroku e instala la CLI.
2. Crea un archivo `Procfile` en la raíz del proyecto:
   ```
   web: python backend/manage.py runserver 0.0.0.0:$PORT
   ```
3. Despliega el proyecto:
   ```bash
   heroku create
   git push heroku main
   ```

---

## **Licencia**

Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

---

## **Contacto**

Si tienes preguntas o sugerencias, no dudes en contactarme:

- **Correo Electrónico:** wilhelmeselpro@gmail.com
- **GitHub:** [https://github.com/WilhelmPro007](https://github.com/WilhelmPro007)


