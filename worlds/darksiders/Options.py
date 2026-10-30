from __future__ import annotations
from dataclasses import dataclass

from Options import Choice, Range, Toggle, OptionGroup, PerGameCommonOptions

class DifficultyLevel(Choice):
    """Difficulty level for Darksiders Warmastered Edition."""

    display_name = "Difficulty Level"
    option_easy = 0
    option_normal = 1
    option_apocalyptic = 2

    default = option_normal

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

    default = option_hard

class ShuffleArmor(Choice):
    """
    Determines how to obtain the Abyssal Armor and how it is shuffled into the item pool.
    Remove : The Abyssal Armor and all its pieces are removed from the item pool. Their location are added to the pool.
    Vanilla : The Abyssal Armor is automatically obtained after collecting all 10 Pieces. The Abyssal Armor Pieces remain at their vanilla locations.
    Own (Pieces) : The Abyssal Armor Pieces are shuffled into their own world. Their location are added to the pool.
    Own (Armor) : The Abyssal Armor is shuffled into its own world. The Abyssal Armor Pieces are removed from the item pool. Their location are added to the pool.
    Armorsanity (Pieces) : The Abyssal Armor Pieces are shuffled anywhere in the multiworld. Their location are added to the pool.
    Armorsanity (Armor) : The Abyssal Armor is shuffled anywhere in the multiworld. The Abyssal Armor Pieces are removed from the item pool. Their location are added to the pool.
    """

    display_name = "Abyssal Armor"
    option_remove = 0
    option_vanilla = 1
    option_own_pieces = 2
    option_own_armor = 3
    option_armorsanity_pieces = 4
    option_armorsanity_armor = 5

    default = option_armorsanity_pieces

class ShuffleArmorPieces(Range):
    """
    Determines how many Abyssal Armor Pieces are required to unlock the Abyssal Armor.
    This option is ignored unless the Abyssal Armor option is set to "Own (Pieces)" or "Armorsanity (Pieces)"
    """

    display_name = "Abyssal Armor Pieces"
    range_start = 1
    range_end = 10

    default = 10

class ShuffleArtifacts(Choice):
    """
    Determines how the Artifacts are shuffled into the item pool.
    Remove : The Artifacts are removed from the item pool. Their location are added to the pool.
    Vanilla : The Artifacts remain at their vanilla locations.
    Own : The Artifacts are shuffled into their own world. Their location are added to the pool.
    Artisanity : The Artifacts are shuffled anywhere in the multiworld. Their location are added to the pool.
    """

    display_name = "Artifacts"
    option_remove = 0
    option_vanilla = 1
    option_own = 2
    option_artisanity = 3

    default = option_own

class ShuffleSoldierArtifacts(Range):
    """
    Determines how many Soldier Artifacts are required to unlock Vulgrim's reward.
    This option is ignored unless the Artifacts option is set to Own or Artisanity.
    """

    display_name = "Soldier Artifacts"
    range_start = 1
    range_end = 20

    default = 20

class ShuffleChampionArtifacts(Range):
    """
    Determines how many Champion Artifacts are required to unlock Vulgrim's reward.
    This option is ignored unless the Artifacts option is set to Own or Artisanity.
    """

    display_name = "Champion Artifacts"
    range_start = 1
    range_end = 6

    default = 6

class Containers(Range):
    """Determines the number of Containers available in the game. Containers hold consumables."""

    display_name = "Containers"
    range_start = 0
    range_end = 8

    default = 8

class ShuffleMapHoardseeker(Choice):
    """
    Determines where the Map and Hoardseeker for each dungeon get shuffled.
    Remove : The Map and Hoardseeker are removed from the item pool. Their location are added to the pool.
    Vanilla : The Map and Hoardseeker remain at their vanilla locations.
    Start With : The Map and Hoardseeker are available from the start. Their location are added to the pool.
    Region : The Map and Hoardseeker are shuffled into their relevant region (Ashlands, Black Throne, Hollows, Iron Canopy and Twilight Cathedral). Their location are added to the pool.
    Own : The Map and Hoardseeker are shuffled into their own world. Their location are added to the pool.
    Anywhere : The Map and Hoardseeker are shuffled anywhere in the multiworld. Their location are added to the pool.
    """

    display_name = "Map and Hoardseeker"
    option_remove = 0
    option_vanilla = 1
    option_start_with = 2
    option_region = 3
    option_own = 4
    option_anywhere = 5

    default = option_start_with

class ShuffleHearts(Choice):
    """
    Determines where the Hearts of the Chosen get shuffled.
    Remove : The Hearts of the Chosen are removed from the item pool. Their location are added to the pool. The Samael rewards are removed from the locations. The Black Throne is reachable after defeating the Phantom General.
    Vanilla : The Hearts of the Chosen remain at their vanilla locations.
    Own : The Hearts of the Chosen are shuffled into their own world. Their location are added to the pool.
    Heartsanity : The Hearts of the Chosen are shuffled anywhere in the multiworld. Their location are added to the pool.
    """

    display_name = "Hearts of the Chosen"
    option_remove = 0
    option_vanilla = 1
    option_own = 2
    option_heartsanity = 3

    default = option_vanilla

class BlackThroneAccess(Range):
    """
    Determines how many Hearts of the Chosen are required to unlock access to the Black Throne.
    This option is ignored unless the Hearts of the Chosen option is set to Own or Heartsanity.
    """

    display_name = "Hearts of the Chosen required to access The Black Throne"
    range_start = 1
    range_end = 4

    default = 4

class ShuffleKeys(Choice):
    """
    Determines where the Beholder Keys get shuffled.
    Remove : The Beholder Keys are removed from the item pool. Their location are added to the pool. All Beholder Doors are automatically unlocked.
    Vanilla : The Beholder Keys remain at their vanilla locations.
    Region : The Beholder Keys are shuffled into their relevant region (2 in Black Throne, 1 in Broken Stairs, 3 in Hollows, 2 in Iron Canopy and 2 in Twilight Cathedral). Their location are added to the pool.
    Own : The Beholder Keys are shuffled into their own world. Their location are added to the pool.
    Keysanity : The Beholder Keys are shuffled anywhere in the multiworld. Their location are added to the pool.
    """

    display_name = "Beholder Keys"
    option_remove = 0
    option_vanilla = 1
    option_region = 2
    option_own = 3
    option_keysanity = 4

    default = option_region

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
    option_half = 1
    option_max = 2

    default = option_max

class ShuffleWeapons(Choice):
    """
    Determines your starting weapon. The others are shuffled in the item pool. Their location are added to the pool.
    """

    display_name = "Weapons"
    option_start_with_sword = 1
    option_start_with_scythe = 2
    option_start_with_gauntlet = 3

    default = option_start_with_sword

class ShuffleSword(Choice):
    """
    Determines the Sword primary weapon available in the game and its behaviour.
    Remove : The Chaoseater is removed from the item pool. If Weapons option is "Start with Sword", the Armageddon blade is unlocked from the start and all Armageddon Blade Shards are removed from the item pool and their location are added to the pool.
    Vanilla : Chaoseater is part of the item pool unless Weapons option is "Start with Sword". The Armageddon Blade needs 7 shards before it can be reforged. All the Shards are at their vanilla location.
    Shards : Randomizes the number of shards required to reforge the Armageddon Blade. Their location are added to the pool. Chaoseater is part of the item pool unless Weapons option is "Start with Sword".
    Progressive : The first Progressive Sword unlocked will always be Chaoseater. The second unlock will be Armageddon Blade. The location of the Armageddon Blade Shards are added to the pool. If Weapons option is "Start with Sword", this option makes the player start with Chaoseater and adds only one Progressive Sword to the item pool.
    """

    display_name = "Sword"
    option_remove = 0
    option_vanilla = 1
    option_shards = 2
    option_progressive = 3

    default = option_vanilla

class Armageddon(Range):
    """
    Determines the number of Armageddon Shards needed to reforge the Armageddon Blade.
    This option is ignored unless Sword option is "Shards". 
    """

    display_name = "Armageddon Shards"
    range_start = 1
    range_end = 7

    default = 7

class ShuffleScythe(Choice):
    """
    Determines the Scythe secondary weapon available in the game and its behaviour.
    Remove : The Hellraiser and Harvester are removed from the item pool. Their location are added to the pool. If Weapons option is "Start with Scythe", this option is ignored.
    Vanilla : The Hellraiser and Harvester can be bought from Vulgrim. If Weapons option is "Start with Scythe", this option is ignored.
    Hellraiser : Only the Hellraiser is added to the item pool. The Harvester is unavailable. Their location are added to the pool. If Weapons option is "Start with Scythe", this option makes the player start with Hellraiser.
    Harvester : The Hellraiser is unavailable. Only the Harvester is added to the item pool. Their location are added to the pool. If Weapons option is "Start with Scythe", this option makes the player start with Harvester.
    Progressive : The first Progressive Scythe unlocked will always be Hellraiser. The second unlock will be Harvester. Their location are added to the pool. If Weapons option is "Start with Scythe", this option makes the player start with Hellraiser and adds only one Progressive Scythe to the item pool.
    """

    display_name = "Scythe"
    option_remove = 0
    option_vanilla = 1
    option_hellraiser = 2
    option_harvester = 3
    option_progressive = 4

    default = option_progressive

class ShuffleMoves(Choice):
    """
    Determines the Combos and Combat Moves available in the game and how they are shuffled.
    Remove : War is left with it's starting moves for each weapon. The location of all the moves are added to the pool.
    Vanilla : The Combos and Combat Moves can be bought from Vulgrim.
    Own : The Combos and Combat Moves are shuffled into their own world. Their location are added to the pool.
    Combosanity : The Combos and Combat Moves are shuffled anywhere in the multiworld. Their location are added to the pool.
    """

    display_name = "Combos and Combat Moves"
    option_remove = 0
    option_vanilla = 1
    option_combosanity = 2

    default = option_combosanity

class WrathCores(Range):
    """Determines the number of Wrath Cores available in the game. Each Wrath Core boosts War's maximum Wrath."""

    display_name = "Wrath Cores"
    range_start = 0
    range_end = 2

    default = 2

class WrathShards(Choice):
    """
    Determines the number of Wrath Shards available in the game. Four Wrath Shards form a Wrath Core.
    None: No wrath shards will be available in the game. All chest containing wrath shards will contain a shuffled item.
    Less: A reduced number of wrath shards will be available, but there will always be a multiple of 4 in order to form complete wrath cores. All chest containing wrath shards will contain a shuffled item.
    Max: Enough wrath shards will be available in order for War to reach his maximum wrath, even beyond the normal limit if fewer Wrath Cores are available.
    """

    display_name = "Wrath Shards"
    option_none = 0
    option_half = 1
    option_max = 2

    default = option_max

@dataclass
class DSOptions(PerGameCommonOptions):
    difficulty_level: DifficultyLevel
    logic_rules: LogicRules
    armor: ShuffleArmor
    armor_pieces: ShuffleArmorPieces
    artifacts: ShuffleArtifacts
    soldier_artifacts: ShuffleSoldierArtifacts
    champion_artifacts: ShuffleChampionArtifacts
    containers: Containers
    dungeon_items: ShuffleMapHoardseeker
    hearts: ShuffleHearts
    black_throne: BlackThroneAccess
    keys: ShuffleKeys
    lifestones: Lifestones
    lifestones_shards: LifestonesShards
    weapons: ShuffleWeapons
    sword: ShuffleSword
    scythe: ShuffleScythe
    moves: ShuffleMoves
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
        "Weapons and Combat Options", [
            ShuffleWeapons,
            ShuffleSword,
            ShuffleScythe,
            ShuffleMoves
        ],
    ),
    OptionGroup(
        "Item & Location Options", [
            ShuffleArmor,
            ShuffleArmorPieces,
            ShuffleArtifacts,
            ShuffleSoldierArtifacts,
            ShuffleChampionArtifacts,
            Containers,
            ShuffleMapHoardseeker,
            ShuffleHearts,
            BlackThroneAccess,
            ShuffleKeys,
            Lifestones,
            LifestonesShards,
            WrathCores,
            WrathShards
        ],
    ),
]
option_presets = {
    "default": {
        "difficulty_level": DifficultyLevel.default,
        "logic_rules": LogicRules.default,
        "armor": ShuffleArmor.default,
        "armor_pieces": ShuffleArmorPieces.default,
        "artifacts": ShuffleArtifacts.default,
        "soldier_artifacts": ShuffleSoldierArtifacts.default,
        "champion_artifacts": ShuffleChampionArtifacts.default,
        "containers": Containers.default,
        "dungeon_items": ShuffleMapHoardseeker.default,
        "hearts": ShuffleHearts.default,
        "black_throne": BlackThroneAccess.default,
        "keys": ShuffleKeys.default,
        "lifestones": Lifestones.default,
        "lifestones_shards": LifestonesShards.default,
        "weapons": ShuffleWeapons.default,
        "sword": ShuffleSword.default,
        "armageddon": Armageddon.default,
        "scythe": ShuffleScythe.default,
        "moves": ShuffleMoves.default,
        "wrath_cores": WrathCores.default,
        "wrath_shards": WrathShards.default
    },
    "Easy": {
        "difficulty_level": DifficultyLevel.option_easy,
        "logic_rules": LogicRules.option_casual,
        "armor": ShuffleArmor.option_own_armor,
        "armor_pieces": 10,
        "artifacts": ShuffleArtifacts.option_remove,
        "soldier_artifacts": 20,
        "champion_artifacts": 6,
        "containers": 8,
        "dungeon_items": ShuffleMapHoardseeker.option_start_with,
        "hearts": ShuffleHearts.option_vanilla,
        "black_throne": 1,
        "keys": ShuffleKeys.option_vanilla,
        "lifestones": 9,
        "lifestones_shards": LifestonesShards.option_none,
        "weapons": ShuffleWeapons.option_start_with_sword,
        "sword": ShuffleSword.option_remove,
        "armageddon": 7,
        "scythe": ShuffleScythe.option_harvester,
        "moves": ShuffleMoves.option_vanilla,
        "wrath_cores": 8,
        "wrath_shards": WrathShards.option_none
    },
    "Yes": {
        "difficulty_level": DifficultyLevel.option_apocalyptic,
        "logic_rules": LogicRules.option_glitched,
        "armor": ShuffleArmor.option_armorsanity_pieces,
        "armor_pieces": 10,
        "artifacts": ShuffleArtifacts.option_artisanity,
        "soldier_artifacts": 20,
        "champion_artifacts": 6,
        "containers": 8,
        "dungeon_items": ShuffleMapHoardseeker.option_anywhere,
        "hearts": ShuffleHearts.option_heartsanity,
        "black_throne": 4,
        "keys": ShuffleKeys.option_keysanity,
        "lifestones": 0,
        "lifestones_shards": LifestonesShards.option_none,
        "weapons": ShuffleWeapons.option_start_with_scythe,
        "sword": ShuffleSword.option_shards,
        "armageddon": 7,
        "scythe": ShuffleScythe.option_hellraiser,
        "moves": ShuffleMoves.option_combosanity,
        "wrath_cores": 0,
        "wrath_shards": WrathShards.option_none
    }
}