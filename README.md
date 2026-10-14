# 🚀 Automated Python Health Checker & CI/CD Pipeline

Este repositorio contiene un sistema automatizado de monitorización de infraestructura (*Health Checker*) desarrollado en Python, empaquetado con Docker y desplegado mediante flujos de Integración Continua (CI) en GitHub Actions.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10 (Lógica de comprobación de endpoints y manejo de errores)
* **Integración Continua (CI):** GitHub Actions (Validación automática de código en cada commit)
* **Contenedorización:** Docker (Dockerfile multi-stage/slim optimizado)
* **Orquestación:** Docker Compose (Definición declarativa del servicio)

---

## 📋 Características Técnicas

1. **Scripting Automático (`health_check.py`):** Realiza peticiones HTTP a endpoints críticos y valida el estado operativo, registrando respuestas y excepciones.
2. **Pipeline Declarativo (`.github/workflows/ci.yml`):** Ejecuta tests automáticos en entornos aislados Ubuntu runner en cada `push` a la rama `main`.
3. **Entorno Aislado (`Dockerfile` & `docker-compose.yml`):** Permite ejecutar el monitor en cualquier servidor o nube sin dependencias locales previa instalación de Docker.

---

## 💻 Ejemplo de Ejecución Local

Para levantar el entorno de monitorización en local utilizando Docker Compose:

```bash
# Clonar el repositorio
git clone [https://github.com/johannbiz-wq/DevOps-Python-Automation.git](https://github.com/johannbiz-wq/DevOps-Python-Automation.git)

# Acceder al directorio
cd DevOps-Python-Automation

# Levantar el contenedor
docker compose up --build
