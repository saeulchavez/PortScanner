# PortScanner – Verificador de puertos TCP

## 1. Descripción del proyecto

PortScanner es un proyecto desarrollado para comprobar el estado de los puertos de un equipo o servidor mediante conexiones TCP.

El proyecto implementa dos versiones de un verificador de puertos:

- **Linux:** utiliza un script Bash ejecutado dentro de un contenedor Docker basado en Ubuntu.
- **Windows:** utiliza un script PowerShell para comprobar la conectividad de los puertos.

Adicionalmente, se desarrolla un programa en Python que permite ejecutar las versiones correspondientes y comprobar múltiples puertos de manera consecutiva.

## 2. Objetivo

Desarrollar una herramienta multiplataforma que permita identificar si determinados puertos TCP aceptan conexiones, utilizando herramientas propias de Linux y Windows, además de automatizar las pruebas mediante Python.

## 3. Tecnologías utilizadas

- Ubuntu 24.04
- Docker
- Bash
- PowerShell
- Python 3
- Git y GitHub

## 4. Estructura del proyecto

```text
PortScanner/
│
├── linux/
│   ├── Dockerfile
│   └── check_port.sh
│
├── windows/
│   └── check_port.ps1
│
├── python/
│   └── port_scanner.py
│
└── README.md
```

## 5. Implementación en Linux con Docker

La versión de Linux utiliza Bash para intentar establecer una conexión TCP con el host y puerto indicados.

### Requisitos

- Docker instalado y funcionando.
- WSL con Ubuntu, o una distribución Linux.
- Acceso a una terminal.

### Construir la imagen

Desde la carpeta principal del proyecto, ejecutar:

```bash
docker build -t port-scanner-linux ./linux
```

### Ejecutar el contenedor

Comprobar un puerto en localhost:

```bash
docker run --rm port-scanner-linux 80
```

Comprobar un puerto de un servidor externo:

```bash
docker run --rm port-scanner-linux 443 google.com
```

Para comprobar un servicio que se encuentra en el equipo Windows anfitrión:

```bash
docker run --rm port-scanner-linux 8080 host.docker.internal
```

## 6. Implementación en Windows con PowerShell

La versión de Windows utiliza la clase `TcpClient` de .NET para intentar establecer una conexión TCP.

### Requisitos

- Windows 10 o superior.
- PowerShell.

### Ejecución

Desde PowerShell, ubicarse en la carpeta principal del proyecto y ejecutar:

```powershell
.\windows\check_port.ps1 -Port 443 -HostName google.com
```

Para comprobar un puerto local:

```powershell
.\windows\check_port.ps1 -Port 8080
```

## 7. Automatización mediante Python

El programa Python permite enviar múltiples puertos a los scripts correspondientes dependiendo del sistema operativo.

### Requisitos

- Python 3 instalado.
- Los archivos del proyecto disponibles localmente.
- Power