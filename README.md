# Demo de GitHub Actions Workflows Reutilizables

Este repositorio contiene una demostración de cómo utilizar GitHub Actions workflows reutilizables para construir y desplegar una aplicación web simple en Kubernetes.

## 🌟 La Aplicación

Es una aplicación web simple en Python/Flask que:
- Muestra un mensaje "Hello from [hostname]!"
- Escucha en el puerto 80
- Incluye una característica especial de build que puede hacer el proceso más intensivo en CPU (útil para demostraciones)

### 🔧 Construcción Local

Para construir la aplicación localmente:

```bash
# Build normal (rápido)
docker build -t mi-app .

# Build con cálculos pesados (lento)
docker build --build-arg HEAVY_BUILD=true -t mi-app .
```

Para ejecutar localmente:
```bash
docker run -p 80:80 mi-app
```

## 🚀 CI/CD Pipeline

El pipeline de CI/CD utiliza workflows reutilizables desde el repositorio `Pelado-Nerdworks/workflows-compartidos`:

### Build Workflow
- Ubicación: `.github/workflows/build-docker.yaml`
- Función: Construye y publica la imagen Docker
- Inputs requeridos:
  - `image-name`: Nombre de la imagen
  - `dockerfile-path`: Ruta al Dockerfile

### Deploy Workflow
- Ubicación: `.github/workflows/deploy-k8s.yaml`
- Función: Despliega la aplicación en Kubernetes
- Inputs requeridos:
  - `app-name`: Nombre de la aplicación
  - `namespace`: Namespace de Kubernetes
  - `image-tag`: Tag de la imagen a desplegar

## 🔐 Secretos Necesarios

Para que el pipeline funcione correctamente, necesitas configurar los siguientes secretos en tu repositorio de GitHub:

### Para el Build
- `DOCKER_USERNAME`: Usuario de Docker Hub
- `DOCKER_TOKEN`: Token de acceso a Docker Hub

### Para el Deploy
- `KUBECONFIG`: Archivo de configuración de Kubernetes en base64
  ```bash
  # Para generar el KUBECONFIG en base64:
  cat ~/.kube/config | base64
  ```

## 📝 Estructura del Repositorio

```
.
├── .github/
│   └── workflows/
│       └── build-deploy.yaml
├── app.py              # Aplicación Flask
├── Dockerfile          # Definición del contenedor
├── requirements.txt    # Dependencias de Python
└── README.md          # Este archivo
```

## 🔄 Flujo de Trabajo

1. Al hacer push a la rama `main`:
   - Se dispara el workflow de build
   - Se construye la imagen Docker
   - Se publica en Docker Hub
   - Se obtiene el tag de la imagen

2. Una vez completado el build:
   - Se dispara el workflow de deploy
   - Se despliega la nueva versión en Kubernetes
   - La aplicación se actualiza en el cluster

## 🤝 Contribuciones

Este es un proyecto de demostración para mostrar el uso de workflows reutilizables. ¡Las contribuciones son bienvenidas! 