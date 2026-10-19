from __future__ import annotations

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .Options import option_groups, option_presets

class DSWeb(WebWorld):
    
    game = "Darksiders"

    theme = "stone"
    
    rich_text_options_doc = True

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Darksiders in Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Sachaqc"],
    )

    #game_info_languages = ["en"]
    tutorials = [setup_en]

    option_groups = option_groups
    option_presets = option_presets