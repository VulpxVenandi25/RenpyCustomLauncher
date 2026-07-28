init -10 python:

    THEMES = {}
    THEME_NAMES = {}
    THEME_ORDER = []

    def register_theme(id, name, **kwargs):
        if id in THEMES:
            raise Exception("Theme '{}' already exists. Choose a unique ID.".format(id))
        kwargs["name"] = name
        THEMES[id] = kwargs
        THEME_NAMES[id] = name
        THEME_ORDER.append(id)

    def get_theme_value(th, key, default=None):
        if th is None:
            return default
        return th.get(key, default)

    register_theme("default", _("Default"),
        text="#545454",
        idle="#42637b",
        hover="#d86b45",
        disable="#808080",
        reverse_idle="#78a5c5",
        reverse_hover="#d86b45",
        reverse_text="#ffffff",
        scrollbar_idle="#dfdfdf",
        scrollbar_hover="#d86b45",
        pattern="images/pattern.png",
    )

    register_theme("dark", _("Dark theme"),
        text="#ababab",
        idle="#709cbe",
        hover="#d86b45",
        disable="#7f7f7f",
        reverse_idle="#78a5c5",
        reverse_hover="#d86b45",
        reverse_text="#0a0a0a",
        scrollbar_idle="#282828",
        scrollbar_hover="#d86b45",
        pattern="images/pattern.png",
        info_window="#101010",
        error_color="#d15353",
        info_color="#ababab",
        input_color="#d86b45",
    )

init -9 python:
    import json, os
    themes_dir = os.path.join(config.gamedir, "themes")
    if os.path.isdir(themes_dir):
        for fn in sorted(os.listdir(themes_dir)):
            if fn.endswith(".json"):
                try:
                    with open(os.path.join(themes_dir, fn), "r") as f:
                        data = json.load(f)
                    clean = {k: v for k, v in data.get("properties", {}).items() if v != ""}
                    register_theme(data["id"], data["name"], **clean)
                except Exception:
                    pass