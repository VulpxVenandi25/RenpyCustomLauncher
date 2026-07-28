init python:
    import json, os, shutil, re

    def custom_themes_dir():
        return os.path.join(config.gamedir, "themes")

    def theme_file_path(theme_id):
        return os.path.join(custom_themes_dir(), theme_id + ".json")

    def theme_images_dir(theme_id):
        return os.path.join(config.gamedir, "images", "themes", theme_id)

    def list_custom_theme_ids():
        d = custom_themes_dir()
        if not os.path.isdir(d):
            return []
        return sorted(fn[:-5] for fn in os.listdir(d) if fn.endswith(".json"))

    def save_custom_theme(theme_id, name, properties):
        d = custom_themes_dir()
        if not os.path.isdir(d):
            os.makedirs(d)
        clean = {k: v for k, v in properties.items() if v != ""}
        with open(theme_file_path(theme_id), "w") as f:
            json.dump({"id": theme_id, "name": name, "properties": clean}, f, indent=2, ensure_ascii=False)

    def delete_custom_theme_files(theme_id):
        fp = theme_file_path(theme_id)
        if os.path.exists(fp):
            os.remove(fp)
        img_dir = theme_images_dir(theme_id)
        if os.path.isdir(img_dir):
            shutil.rmtree(img_dir)

    def generate_theme_id(name):
        tid = re.sub(r'[^a-z0-9_]', '_', name.lower().strip())
        tid = re.sub(r'_+', '_', tid).strip('_')
        if not tid:
            tid = "custom_theme"
        base = tid
        counter = 1
        while tid in THEMES:
            tid = f"{base}_{counter}"
            counter += 1
        return tid

    def import_image_to_theme(theme_id, source_path):
        if not os.path.isfile(source_path):
            return None
        dst_dir = theme_images_dir(theme_id)
        if not os.path.isdir(dst_dir):
            os.makedirs(dst_dir)
        filename = os.path.basename(source_path)
        dst = os.path.join(dst_dir, filename)
        shutil.copy2(source_path, dst)
        return os.path.join("images", "themes", theme_id, filename)

    CUSTOM_THEME_DEFAULTS = {
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
        "background": "images/background.png",
        "projects_window": "",
        "info_window": "#f9f9f9c0",
        "error_color": "#d15353",
        "info_color": "#545454",
        "interaction_color": "#d19753",
        "question_color": "#d19753",
        "input_color": "#d86b45",
        "outline_shadow": "#000000",
        "window": "",
    }

    THEME_PROPERTY_GROUPS = [
        (_("Text Colors"), [
            ("text", _("Text Color")),
            ("info_color", _("Info Text")),
            ("error_color", _("Error Text")),
            ("interaction_color", _("Interaction Title")),
            ("question_color", _("Question Title")),
            ("input_color", _("Input Text")),
            ("reverse_text", _("Selected Text")),
        ]),
        (_("Button Colors"), [
            ("idle", _("Button Idle")),
            ("hover", _("Button Hover")),
            ("disable", _("Button Disabled")),
            ("reverse_idle", _("Selected Background")),
            ("reverse_hover", _("Selected Hover")),
        ]),
        (_("Scrollbar"), [
            ("scrollbar_idle", _("Scrollbar Color")),
            ("scrollbar_hover", _("Scrollbar Hover")),
        ]),
        (_("Backgrounds"), [
            ("background", _("Main Background")),
            ("pattern", _("Pattern Image")),
            ("info_window", _("Info Window BG")),
            ("projects_window", _("Projects BG")),
            ("window", _("Window BG")),
        ]),
        (_("Effects"), [
            ("outline_shadow", _("Outline Shadow")),
        ]),
    ]

    current_editing_theme = None
    current_editing_name = ""

    _edit_property_key = None
    _edit_property_label = None
    _delete_theme_id = None
    _import_image_key = None

    def get_custom_theme_value(key):
        if persistent.custom_theme_values and key in persistent.custom_theme_values:
            return persistent.custom_theme_values[key]
        return CUSTOM_THEME_DEFAULTS.get(key, "")

    def set_custom_theme_value(key, value):
        if not persistent.custom_theme_values:
            persistent.custom_theme_values = {}
        persistent.custom_theme_values[key] = value

    def is_hex_color(value):
        return isinstance(value, str) and value.startswith("#") and len(value) in (4, 5, 7, 9)

    class EditThemeProperty(Action):
        def __init__(self, key, label):
            self.key = key
            self.label = label

        def __call__(self):
            store._edit_property_key = self.key
            store._edit_property_label = self.label
            renpy.jump("edit_property_prompt")

    class ResetThemeProperty(Action):
        def __init__(self, key):
            self.key = key

        def __call__(self):
            if persistent.custom_theme_values and self.key in persistent.custom_theme_values:
                del persistent.custom_theme_values[self.key]
            renpy.restart_interaction()

    class DeleteThemeAction(Action):
        def __init__(self, theme_id):
            self.theme_id = theme_id

        def __call__(self):
            store._delete_theme_id = self.theme_id
            renpy.jump("delete_theme_confirm")

    class CreateNewTheme(Action):
        def __call__(self):
            renpy.jump("create_theme_prompt")

    class EditThemeAction(Action):
        def __init__(self, theme_id):
            self.theme_id = theme_id

        def __call__(self):
            fp = theme_file_path(self.theme_id)
            if not os.path.exists(fp):
                store.current_editing_theme = None
                renpy.restart_interaction()
                return
            with open(fp, "r") as f:
                data = json.load(f)
            persistent.custom_theme_values = dict(data.get("properties", {}))
            store.current_editing_theme = self.theme_id
            store.current_editing_name = data.get("name", self.theme_id)
            renpy.jump("theme_editor")

    class ImportThemeImage(Action):
        def __init__(self, key):
            self.key = key

        def __call__(self):
            store._import_image_key = self.key
            renpy.jump("import_image_prompt")

    class SaveThemeAction(Action):
        def __call__(self):
            tid = store.current_editing_theme
            name = store.current_editing_name
            if tid and persistent.custom_theme_values:
                save_custom_theme(tid, name, dict(persistent.custom_theme_values))
            persistent.theme = tid
            renpy.session["launcher_start_label"] = "preferences"
            renpy.utter_restart()


screen theme_manager:

    $ custom_ids = list_custom_theme_ids()

    frame:
        style_group "l"
        style "l_root"

        window:

            has vbox

            label _("Theme Manager") text_outlines TEXT_OUTLINES

            add SPACER

            text _("Custom Themes:") outlines TEXT_OUTLINES

            if custom_ids:
                viewport:
                    mousewheel True
                    scrollbars "vertical"
                    ymaximum 300

                    has vbox

                    for tid in custom_ids:
                        $ tname = THEME_NAMES.get(tid, tid)

                        hbox:
                            xfill True
                            spacing 10

                            text tname:
                                style "l_text"
                                yalign 0.5
                                xminimum 300

                            textbutton _("Edit"):
                                text_outlines TEXT_OUTLINES
                                action EditThemeAction(tid)
                                style "l_small_button"

                            textbutton _("Delete"):
                                text_outlines TEXT_OUTLINES
                                action DeleteThemeAction(tid)
                                style "l_small_button"

                        add SEPARATOR

            else:
                add HALF_SPACER
                text _("No custom themes yet.") outlines TEXT_OUTLINES

            add SPACER
            add SEPARATOR2

            textbutton _("+ Create New Theme"):
                text_outlines TEXT_OUTLINES
                action CreateNewTheme()
                style "l_list"

    textbutton _("Return"):
        text_outlines TEXT_OUTLINES
        action Jump("preferences")
        style "l_left_button"


screen theme_editor:

    frame:
        style_group "l"
        style "l_root"

        window:

            has vbox

            label _("Editing: [current_editing_name]") text_outlines TEXT_OUTLINES

            viewport:
                mousewheel True
                scrollbars "vertical"

                has vbox

                for group_name, properties in THEME_PROPERTY_GROUPS:
                    add SPACER
                    add SPACER
                    frame style "l_label_small":
                        text group_name outlines TEXT_OUTLINES

                    for key, label in properties:
                        $ value = get_custom_theme_value(key)
                        $ is_default = (value == CUSTOM_THEME_DEFAULTS.get(key, ""))

                        hbox:
                            xfill True
                            spacing 10
                            yalign 0.5

                            # Nombre de la propiedad a la izquierda con ancho mínimo fijo
                            text label + ":":
                                style "l_text"
                                xminimum 220
                                yalign 0.5

                            # Controles a la derecha con estructura de celdas fijas para perfecta alineación
                            hbox:
                                spacing 8
                                yalign 0.5
                                xalign 1.0

                                # 1. Cuadro de color o espacio reservado idéntico
                                if is_hex_color(value):
                                    button:
                                        xysize (26, 26)
                                        yalign 0.5
                                        background value
                                        action EditThemeProperty(key, label)
                                else:
                                    null width 26 height 26

                                # 2. Botón con el valor (ancho fijo)
                                textbutton value:
                                    text_outlines TEXT_OUTLINES
                                    action EditThemeProperty(key, label)
                                    style "l_small_button"
                                    yalign 0.5
                                    text_size 12
                                    xminimum 140
                                    xmaximum 140

                                # 3. Botón Reset "R" o espacio reservado idéntico
                                if not is_default:
                                    textbutton _("R"):
                                        text_outlines TEXT_OUTLINES
                                        action ResetThemeProperty(key)
                                        style "l_small_button"
                                        yalign 0.5
                                        text_size 12
                                        text_color "#d86b45"
                                        xmaximum 30
                                else:
                                    null width 30 height 24

                                # 4. Botón de Imagen "Img" o espacio reservado idéntico
                                if key in ("background", "pattern"):
                                    textbutton _("Img"):
                                        text_outlines TEXT_OUTLINES
                                        action ImportThemeImage(key)
                                        style "l_small_button"
                                        yalign 0.5
                                        text_size 11
                                        xmaximum 36
                                else:
                                    null width 36 height 24

    textbutton _("Cancel"):
        text_outlines TEXT_OUTLINES
        action Jump("theme_manager")
        style "l_left_button"

    textbutton _("Save Theme"):
        text_outlines TEXT_OUTLINES
        action SaveThemeAction()
        style "l_right_button"


label theme_manager:
    call screen theme_manager
    jump theme_manager

label theme_editor:
    if not current_editing_theme:
        jump theme_manager
    call screen theme_editor
    jump theme_editor

label create_theme_prompt:
    python:
        name = interface.input(
            _("New Theme"),
            _("Enter a name for the new theme:"),
            sanitize=False,
            cancel=Jump("theme_manager"),
        )
        if name and name.strip():
            name = name.strip()
            tid = generate_theme_id(name)
            save_custom_theme(tid, name, dict(CUSTOM_THEME_DEFAULTS))
            persistent.custom_theme_values = dict(CUSTOM_THEME_DEFAULTS)
            store.current_editing_theme = tid
            store.current_editing_name = name
            renpy.jump("theme_editor")
        else:
            renpy.jump("theme_manager")

label delete_theme_confirm:
    $ tid = store._delete_theme_id
    $ name = THEME_NAMES.get(tid, tid)
    python:
        result = interface.yesno(
            _("Are you sure you want to delete '%s'?") % name,
            yes=Return(True),
            no=Jump("theme_manager"),
        )
        if result:
            delete_custom_theme_files(tid)
            if persistent.theme == tid:
                persistent.theme = None
            renpy.session["launcher_start_label"] = "preferences"
            renpy.utter_restart()
        else:
            renpy.jump("theme_manager")

label edit_property_prompt:
    python:
        key = store._edit_property_key
        lbl = store._edit_property_label
        current = get_custom_theme_value(key)
        new_value = interface.input(
            _("Edit %s") % lbl,
            _("Enter the value for %s:") % lbl,
            filename=False,
            sanitize=False,
            cancel=Jump("theme_editor"),
            default=current,
        )
        if new_value is not None and new_value != current:
            set_custom_theme_value(key, new_value)
        renpy.jump("theme_editor")

label import_image_prompt:
    python:
        key = store._import_image_key
        tid = store.current_editing_theme
        source = interface.input(
            _("Import Image"),
            _("Enter the full path to the image file:"),
            filename=False,
            sanitize=False,
            cancel=Jump("theme_editor"),
        )
        if source and os.path.isfile(source):
            result = import_image_to_theme(tid, source)
            if result:
                set_custom_theme_value(key, result)
        renpy.jump("theme_editor")