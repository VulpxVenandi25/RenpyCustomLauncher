# Ren'Py Launcher Personalizado

Launcher modificado de **Ren'Py 8.5.3 SDK** con sistema de temas múltiples, fondos animados, organización mejorada de proyectos y más.

## Características

- **Sistema de temas múltiples** con registro extensible (`register_theme`)
- **Temas incluidos**: Default (claro), Dark (oscuro), DMike (cálido/sobrio), Ruber (tierra/mutable), Bandit (azul/naranja con animación)
- **Skin legacy** desde `skin.rpy` / `skin.txt` con compatibilidad hacia atrás
- **Fondo animado** con bucle de sprites (21 frames) en la pantalla principal
- **Organización por carpetas** de proyectos con soporte colapsable
- **Gestión completa de proyectos**: crear, editar, lint, compilar, distribuir
- **Soporte multiplataforma**: Windows, macOS, Linux, Android, iOS, Web
- **Editor integrado** con detección automática de VS Code
- **Text outlines** como efecto visual opcional (Preferencias > Theme)

## Estructura del proyecto

| Carpeta/Archivo            | Descripción                                      |
| -------------------------- | ------------------------------------------------ |
| `game/`                    | Código fuente del launcher en Ren'Py             |
| `game/launcher_themes.rpy` | Registro de temas múltiples (`register_theme`)   |
| `game/skin.rpy`            | Tema custom legacy con fondo animado (chekoanim) |
| `game/skin.txt`            | Definición del skin legacy                       |
| `game/style.rpy`           | Sistema de estilos y resolución de temas         |
| `game/front_page.rpy`      | Pantalla principal y selección de proyectos      |
| `game/project.rpy`         | Gestión de proyectos y organización por carpetas |
| `game/interface.rpy`       | Diálogos y UI comunes                            |
| `game/editor.rpy`          | Detección y configuración del editor             |
| `game/distribute.rpy`      | Sistema de builds y distribuciones               |
| `game/preferences.rpy`     | Preferencias (temas, opciones, efectos visuales) |
| `game/themes/`             | Temas personalizados (bandit, dmike, ruber)      |
| `game/images/transition/`  | Sprites del fondo animado (chekoanim)            |
| `game/fonts/`              | Tipografías Roboto                               |
| `game/gui7/`               | Generación de GUI para nuevos proyectos          |

## Cómo agregar un tema nuevo

Crea un archivo `.rpy` dentro de `game/themes/` con:

```python
init -10 python:
    register_theme("id_unico", "Nombre del Tema",
        text="#color",
        idle="#color",
        hover="#color",
        disable="#color",
        reverse_idle="#color",
        reverse_hover="#color",
        reverse_text="#color",
        scrollbar_idle="#color",
        scrollbar_hover="#color",
        pattern="images/pattern.png",
        background="images/themes/mi_tema/fondo.jpg",  # opcional
        projects_window=Color("#color"),
        info_window="#color",
        error_color="#color",
        info_color="#color",
        interaction_color="#color",
        question_color="#color",
        input_color="#color",
        outline_shadow="#color",
        window=Color("#color"),
    )
```

El tema aparecerá automáticamente en Preferencias > Theme.

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
