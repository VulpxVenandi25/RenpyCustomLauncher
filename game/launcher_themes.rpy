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
    
    register_theme("dmike", _("DMike Theme"),
        text="#d9d3d2",
        idle="#a88064",
        hover="#bc644c",
        disable="#7a6665",
        reverse_idle="#604740",
        reverse_hover="#854944",
        reverse_text="#d9d3d2",
        scrollbar_idle="#4c4a46",
        scrollbar_hover="#a7542f",
        pattern="images/pattern.png",
        background="theme/theme_background_dark.jpg",
        projects_window=Color("#190505b0"),
        info_window="#1f2a29",
        error_color="#77100a",
        info_color="#c3a77d",
        interaction_color="#be946f",
        question_color="#c3a474",
        input_color="#bc644c",
        window=Color("#190505b0"),
    )
    
    register_theme("bandit", _("Bandit Theme"),
        text="#cbd5e1",
        idle="#38bdf8",
        hover="#f97316",
        disable="#475569",
        reverse_idle="#0284c7",
        reverse_hover="#ea580c",
        reverse_text="#ffffff",
        scrollbar_idle="#334155",
        scrollbar_hover="#f97316",
        pattern="images/pattern.png",
        background="chekoanim",
        projects_window=Color("#0f172a72"),
        info_window="#0f172ae8",
        error_color="#ef4444",
        info_color="#cbd5e1",
        interaction_color="#fb923c",
        question_color="#fb923c",
        input_color="#f97316",
        window=Color("#0f172a72"),
    )


init -3:
    image chekoanim:
        "images/transition/cheko_000.png"
        pause 0.1
        "images/transition/cheko_001.png"
        pause 0.1
        "images/transition/cheko_002.png"
        pause 0.1
        "images/transition/cheko_003.png"
        pause 0.1
        "images/transition/cheko_004.png"
        pause 0.1
        "images/transition/cheko_005.png"
        pause 0.1
        "images/transition/cheko_006.png"
        pause 0.1
        "images/transition/cheko_007.png"
        pause 0.1
        "images/transition/cheko_008.png"
        pause 0.1
        "images/transition/cheko_009.png"
        pause 0.1
        "images/transition/cheko_010.png"
        pause 0.1
        "images/transition/cheko_011.png"
        pause 0.1
        "images/transition/cheko_012.png"
        pause 0.1
        "images/transition/cheko_013.png"
        pause 0.1
        "images/transition/cheko_014.png"
        pause 0.1
        "images/transition/cheko_015.png"
        pause 0.1
        "images/transition/cheko_016.png"
        pause 0.1
        "images/transition/cheko_017.png"
        pause 0.1
        "images/transition/cheko_018.png"
        pause 0.1
        "images/transition/cheko_019.png"
        pause 0.1
        "images/transition/cheko_020.png"
        pause 0.1
        repeat