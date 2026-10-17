from __future__ import annotations
from dataclasses import dataclass

from Options import Choice, Range, Toggle, OptionGroup, PerGameCommonOptions

class DifficultyLevel(Choice):
    """Difficulty level for Darksiders Warmastered Edition."""

    display_name = "Difficulty Level"
    option_easy = 0
    option_normal = 1
    option_apocalyptic = 2

    default = 1

class LogicRules(Choice):
    """
    Set the logic rules for Darksiders Warmastered Edition. This option determines the requirements for accessing certain areas and obtaining specific items in the game.
    Casual: The logic is basically the same as any guide or walkthrough, with no additional requirements or restrictions.
    Hard: The logic is more challenging, requiring the player to obtain certain items in a way the devs did not intend, but no glitches are to be performed.
    Glitched: The logic allows for the use of glitches and unintended mechanics to access areas and obtain items. If a speedrunner can do it, so can you.
    """

    display_name = "Logic Rules"
    option_casual = 0
    option_hard = 1
    option_glitched = 2

    default = 1

class Abyssanity(Toggle):
    """Shuffles the Abyssal Armor Pieces into the item pool and adds their locations to the world."""

    display_name = "Abyssanity"

class Artisanity(Toggle):
    """Shuffles the Artifacts into the item pool and adds their locations to the world."""

    display_name = "Artisanity"

class Enhansanity(Choice):
    """Shuffles the Enhancements into the item pool and adds their locations to the world."""

    display_name = "Enhansanity"
    option_none = 0
    option_basic = 1
    option_legendary = 2
    option_all = 3

    default = 1

class Lifestones(Range):
    """Determines the number of Lifestones available in the game. Each lifestone boosts War maximum health."""

    display_name = "Lifestones"
    range_start = 0
    range_end = 9

    default = 5

class LifestonesShards(Choice):
    """
    Determines the number of Lifestones Shards available in the game. Four Lifestone Shards form a Lifestone.
    None: No lifestone shards will be available in the game. All chest containing lifestone shards will contain a shuffled item.
    Less: A reduced number of lifestone shards will be available, but there will always be a multiple of 4 in order to form complete lifestones. All chest containing lifestone shards will contain a shuffled item.
    Max: Enough lifestone shards will be available in order for War to reach his maximum health, even beyond the normal limit if fewer Lifestones are available.
    """

    display_name = "Lifestones Shards"
    option_none = 0
    #option_less = 1
    option_max = 2

    default = 1

class WrathCores(Range):
    """Determines the number of Wrath Cores available in the game. Each Wrath Core boosts War's maximum Wrath."""

    display_name = "Wrath Cores"
    range_start = 0
    range_end = 2

    default = 3

class WrathShards(Choice):
    """
    Determines the number of Wrath Shards available in the game. Four Wrath Shards form a Wrath Core.
    None: No wrath shards will be available in the game. All chest containing wrath shards will contain a shuffled item.
    Less: A reduced number of wrath shards will be available, but there will always be a multiple of 4 in order to form complete wrath cores. All chest containing wrath shards will contain a shuffled item.
    Max: Enough wrath shards will be available in order for War to reach his maximum wrath, even beyond the normal limit if fewer Wrath Cores are available.
    """

    display_name = "Wrath Shards"
    option_none = 0
    #option_less = 1
    option_max = 2

    default = 1

@dataclass
class DSOptions(PerGameCommonOptions):
    difficulty_level: DifficultyLevel
    abyssanity: Abyssanity
    artisanity: Artisanity
    enhansanity: Enhansanity
    lifestones: Lifestones
    lifestones_shards: LifestonesShards
    wrath_cores: WrathCores
    wrath_shards: WrathShards
option_groups = [
    OptionGroup(
        "Gameplay Options", [
            DifficultyLevel, 
            LogicRules
        ],
    ),
    OptionGroup(
        "Item & Location Options", [
            Abyssanity,
            Artisanity,
            Enhansanity,
            Lifestones,
            LifestonesShards,
            WrathCores,
            WrathShards
        ],
    ),
]
option_presets = {
    "default": {
        "difficulty_level": 1,
        "abyssanity": True,
        "artisanity": True,
        "enhansanity": True,
        "lifestones": 5,
        "lifestones_shards": 2,
        "wrath_cores": 3,
        "wrath_shards": 2
    },
    "Easy": {
        "difficulty_level": 0,
        "abyssanity": False,
        "artisanity": False,
        "enhansanity": False,
        "lifestones": 9,
        "lifestones_shards": 0,
        "wrath_cores": 8,
        "wrath_shards": 0
    },
    "Yes": {
        "difficulty_level": 2,
        "abyssanity": True,
        "artisanity": True,
        "enhansanity": True,
        "lifestones": 0,
        "lifestones_shards": 1,
        "wrath_cores": 0,
        "wrath_shards": 1
    }
}