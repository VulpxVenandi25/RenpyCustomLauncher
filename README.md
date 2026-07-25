# Ren'Py Launcher Personalizado

Launcher modificado de **Ren'Py 8.5.3 SDK** con interfaz oscura, animaciones personalizadas y organización mejorada de proyectos.

## Características

- **Tema oscuro personalizado** con paleta de colores azul eléctrico / naranja
- **Fondo animado** con bucle de sprites (21 frames) en la pantalla principal
- **Organización por carpetas** de proyectos con soporte colapsable
- **Gestión completa de proyectos**: crear, editar, lint, compilar, distribuir
- **Soporte multiplataforma**: Windows, macOS, Linux, Android, iOS, Web
- **Editor integrado** con detección automática de VS Code
- **Sistema de skins** intercambiable (default / dark / custom)

## Estructura del proyecto

| Carpeta/Archivo           | Descripción                                      |
| ------------------------- | ------------------------------------------------ |
| `game/`                   | Código fuente del launcher en Ren'Py             |
| `game/front_page.rpy`     | Pantalla principal y selección de proyectos      |
| `game/project.rpy`        | Gestión de proyectos y organización por carpetas |
| `game/skin.rpy`           | Tema personalizado con fondo animado             |
| `game/skin.txt`           | Definición del skin oscuro                       |
| `game/style.rpy`          | Sistema de estilos (default, dark, custom)       |
| `game/interface.rpy`      | Diálogos y UI comunes                            |
| `game/editor.rpy`         | Detección y configuración del editor             |
| `game/distribute.rpy`     | Sistema de builds y distribuciones               |
| `game/images/transition/` | Sprites del fondo animado (chekoanim)            |
| `game/fonts/`             | Tipografías Roboto                               |
| `game/gui7/`              | Generación de GUI para nuevos proyectos          |
| `game/theme/`             | Assets visuales del tema                         |

## Requisitos

- [Ren'Py SDK 8.5.3](https://www.renpy.org/)

## Desarrollo

Este launcher se ejecuta como un proyecto de Ren'Py. Para modificarlo:

1. Abre la carpeta `launcher/` desde el launcher principal de Ren'Py
2. Edita los archivos `.rpy` en `game/`
3. Los cambios se reflejan al reiniciar el launcher

## Licencia

Parte de Ren'Py (c) 2004-2026 Tom Rothamel — licensed under MIT.
Modificaciones personalizadas bajo la misma licencia.
