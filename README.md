# Ren'Py Launcher Personalizado

Launcher modificado de **Ren'Py 8.5.3 SDK** con sistema de temas múltiples extensible, Theme Manager integrado, organización mejorada de proyectos y efectos visuales opcionales.

## Características

- **Sistema de temas múltiples** con registro extensible (`register_theme`)
- **Temas de serie**: Default (claro) y Dark (oscuro), definidos en `launcher_themes.rpy`
- **Temas personalizados en JSON**: se cargan automáticamente desde `game/themes/*.json` al iniciar
- **Theme Manager**: crear, editar y eliminar temas personalizados desde Preferencias > Theme
- **Theme Editor**: edición por propiedades (colores, fondos, patrones, sombras) con vista previa visual, importación de imágenes y reset individual
- **Skin legacy** mediante variables `custom_*` de `game/skin.rpy` para compatibilidad hacia atrás
- **Text outlines** como efecto visual opcional (Preferencias > Theme)
- **Organización por carpetas** de proyectos con soporte colapsable (carpetas persistentes)
- **Gestión completa de proyectos**: crear, editar, lint, compilar, distribuir
- **Soporte multiplataforma**: Windows, macOS, Linux, Android, iOS, Web
- **Editor integrado** con detección de VS Code, VSCodium, Atom, y editores de sistema
- **Tipografías Roboto** (Regular y Light) para la interfaz del launcher

## Temas incluidos

| Tema        | ID       | Definición              | Descripción                          |
| ----------- | -------- | ----------------------- | ------------------------------------ |
| Default     | `default`| `launcher_themes.rpy`   | Tema claro con patrones por defecto   |
| Dark        | `dark`   | `launcher_themes.rpy`   | Tema oscuro con ventanas de color     |
| Ruber Theme | `ruber`  | `themes/ruber.json`     | Tema cálido con fondo propio          |

## Cómo agregar un tema nuevo

### Opción A — Archivo JSON (recomendado)

Crea un archivo `.json` dentro de `game/themes/` con la siguiente estructura:

```json
{
  "id": "mi_tema",
  "name": "Mi Tema",
  "properties": {
    "text": "#545454",
    "idle": "#42637b",
    "hover": "#d86b45",
    "disable": "#808080",
    "reverse_idle": "#78a5c5",
    "reverse_hover": "#d86b45",
    "reverse_text": "#ffffff",
    "scrollbar_idle": "#dfdfdf",
    "scrollbar_hover": "#d86b45",
    "pattern": "images/pattern.png",
    "background": "images/themes/mi_tema/fondo.png",
    "projects_window": "#000000b0",
    "info_window": "#f9f9f9c0",
    "error_color": "#d15353",
    "info_color": "#545454",
    "interaction_color": "#d19753",
    "question_color": "#d19753",
    "input_color": "#d86b45",
    "outline_shadow": "#000000",
    "window": "#000000b0"
  }
}
```

Las imágenes del fondo/patrón se colocan en `game/images/themes/mi_tema/`. El tema aparecerá automáticamente en Preferencias > Theme.

### Opción B — Registro en código

Usa `register_theme(id, name, **kwargs)` dentro de un bloque `init -10 python` (ver `launcher_themes.rpy`):

```python
init -10 python:
    register_theme("id_unico", "Nombre del Tema",
        text="#545454",
        idle="#42637b",
        hover="#d86b45",
        background="images/themes/mi_tema/fondo.jpg",  # opcional
        projects_window=Color("#000000b0"),
        ...
    )
```

El tema aparecerá automáticamente en **Preferencias > Theme**. El editor guarda los cambios como archivos JSON en `game/themes/`.

## Estructura del proyecto

| Carpeta/Archivo                     | Descripción                                             |
| ----------------------------------- | ------------------------------------------------------- |
| `game/`                             | Código fuente del launcher en Ren'Py                    |
| `game/launcher_themes.rpy`          | Registro de temas y carga de JSON (`register_theme`)    |
| `game/theme_editor.rpy`             | Theme Manager y Theme Editor (crear, editar, eliminar)  |
| `game/skin.rpy`                     | Tema legacy mediante variables custom_*                 |
| `game/style.rpy`                    | Sistema de estilos, resolución de temas y text outlines |
| `game/front_page.rpy`               | Pantalla principal y selección de proyectos             |
| `game/project.rpy`                  | Gestión de proyectos y organización por carpetas        |
| `game/interface.rpy`                | Diálogos y UI comunes                                   |
| `game/editor.rpy`                   | Detección y configuración del editor                    |
| `game/preferences.rpy`              | Preferencias (temas, opciones, efectos visuales, lint)  |
| `game/distribute.rpy`               | Sistema de builds y distribuciones                      |
| `game/themes/`                      | Temas personalizados en JSON (ej. `ruber.json`)         |
| `game/images/themes/<tema>/`        | Imágenes de fondo de cada tema                         |
| `game/fonts/`                       | Tipografías Roboto (`Roboto-Light`, `Roboto-Regular`)   |
| `game/theme_data.rpy`               | Datos de temas de los proyectos (GUI)                   |
| `.vscode/settings.json`             | Configuración del editor (ocultar `.rpyc`/`cache`, resaltado de sintaxis Ren'Py) |
| `game/tl/spanish/preferences.rpy`   | Traducción al español de las preferencias                |

## Requisitos

- [Ren'Py SDK 8.5.3](https://www.renpy.org/)

## Desarrollo

Este launcher se ejecuta como un proyecto de Ren'Py. Para modificarlo:

1. Abre la carpeta `launcher/` desde el launcher principal de Ren'Py
2. Edita los archivos `.rpy` en `game/`
3. Los cambios se reflejan al reiniciar el launcher
4. Para probar temas nuevos, usa **Preferencias > Theme > Manage Custom Themes**

## Licencia

Parte de Ren'Py (c) 2004-2026 Tom Rothamel — licensed under MIT.
Modificaciones personalizadas bajo la misma licencia.