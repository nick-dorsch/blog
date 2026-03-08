import altair as alt


THEME_NAME = "lex_warm"

WARM_BG = "#292524"
WARM_SURFACE = "#3f342a"
WARM_BORDER = "#665340"
WARM_TEXT = "#f4e9d7"
WARM_TEXT_MUTED = "#d5c2a6"
WARM_GOLD = "#c78d3b"
WARM_GOLD_SOFT = "#ddb06d"


def _lex_theme() -> dict:
    return {
        "config": {
            "background": WARM_BG,
            "view": {
                "fill": WARM_BG,
                "stroke": WARM_BORDER,
            },
            "title": {
                "color": WARM_TEXT,
                "font": "Merriweather",
                "fontSize": 18,
                "fontWeight": 600,
                "subtitleColor": WARM_TEXT_MUTED,
                "anchor": "start",
            },
            "axis": {
                "domainColor": WARM_BORDER,
                "gridColor": WARM_BORDER,
                "tickColor": WARM_BORDER,
                "labelColor": WARM_TEXT_MUTED,
                "titleColor": WARM_TEXT,
                "labelFont": "Merriweather",
                "titleFont": "Merriweather",
            },
            "legend": {
                "titleColor": WARM_TEXT,
                "labelColor": WARM_TEXT_MUTED,
                "labelFont": "Merriweather",
                "titleFont": "Merriweather",
                "orient": "top-right",
                "symbolType": "circle",
            },
            "header": {
                "labelColor": WARM_TEXT_MUTED,
                "titleColor": WARM_TEXT,
                "labelFont": "Merriweather",
                "titleFont": "Merriweather",
            },
            "mark": {
                "color": WARM_GOLD,
            },
            "line": {
                "color": WARM_GOLD,
            },
            "bar": {
                "color": WARM_GOLD,
            },
            "point": {
                "color": WARM_GOLD_SOFT,
            },
            "area": {
                "color": WARM_GOLD,
                "opacity": 0.35,
            },
            "text": {
                "color": WARM_TEXT,
                "font": "Merriweather",
            },
            "range": {
                "category": [
                    WARM_GOLD,
                    WARM_GOLD_SOFT,
                    "#a2743e",
                    "#8c6740",
                    "#c9a472",
                    "#7b6149",
                    "#b79e81",
                    "#d5c2a6",
                ]
            },
        }
    }


def apply_lex_altair_theme() -> None:
    if THEME_NAME not in alt.themes.names():
        alt.themes.register(THEME_NAME, _lex_theme)
    alt.themes.enable(THEME_NAME)
