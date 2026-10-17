from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, HasAny, Rule

if TYPE_CHECKING:
    from .World import DSWorld

CAN_BEAT_ABADDON = HasAll("Armageddon Blade", "Mask of Shadows", "Ruin", "Shadowflight")
CAN_BREAK_CHAINED_CUBES = HasAny("Chaoseater", "Armageddon Blade")
CAN_BREAK_ICE = Has("Tremor Gauntlet")
CAN_GLIDE = Has("Shadowflight")
CAN_MOVE_STONE_COLOSSUS = Has("Earthcaller")
HAS_BEHOLDER_KEY = Has("Beholder Key")
HAS_CROSSBLADE = Has("Crossblade")

def set_all_rules(world: DSWorld) -> None:
    
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: DSWorld) -> None:

    crossroads_to_scalding_gallow = world.get_entrance("The Crossroads to Scalding Gallow")
    world.set_rule(crossroads_to_scalding_gallow, CAN_MOVE_STONE_COLOSSUS)

    scalding_gallow_to_choking_grounds = world.get_entrance("Scalding Gallow to The Choking Grounds")
    world.set_rule(scalding_gallow_to_choking_grounds, CAN_GLIDE)

    twilight_cathedral_1_to_twilight_cathedral_2 = world.get_entrance("Twilight Cathedral 1 to Twilight Cathedral 2")
    world.set_rule(twilight_cathedral_1_to_twilight_cathedral_2, HAS_CROSSBLADE)

    twilight_cathedral_2_to_twilight_cathedral_3 = world.get_entrance("Twilight Cathedral 2 to Twilight Cathedral 3")
    world.set_rule(twilight_cathedral_2_to_twilight_cathedral_3, HAS_CROSSBLADE)


def set_all_location_rules(world: DSWorld) -> None:

    twilight_cathedral_champion_artifact_south_wing = world.get_location("Twilight Cathedral Champion Artifact South Wing")
    world.set_rule(twilight_cathedral_champion_artifact_south_wing, CAN_GLIDE)

    twilight_cathedral_soldier_artifact_south_wing = world.get_location("Twilight Cathedral Soldier Artifact South Wing")
    world.set_rule(twilight_cathedral_soldier_artifact_south_wing, CAN_GLIDE)

    twilight_cathedral_chained_cube = world.get_location("Twilight Cathedral Crossblade Chained Cube")
    world.set_rule(twilight_cathedral_chained_cube, CAN_BREAK_CHAINED_CUBES)

    twilight_cathedral_beholder_key_chest_south_wing = world.get_location("Twilight Cathedral Beholder Key Chest South Wing")
    world.set_rule(twilight_cathedral_beholder_key_chest_south_wing, HAS_CROSSBLADE)

    twilight_cathedral_currency_chest_exterior_blocked_by_ice = world.get_location("Twilight Cathedral Currency Chest Exterior Blocked by Ice")
    world.set_rule(twilight_cathedral_currency_chest_exterior_blocked_by_ice, CAN_BREAK_ICE)

    twilight_cathedral_life_chest_north_of_three_statues = world.get_location("Twilight Cathedral Life Chest North of Three Statues")
    world.set_rule(twilight_cathedral_life_chest_north_of_three_statues, CAN_GLIDE)

    twilight_cathedral_soldier_artifact_bridge_room = world.get_location("Twilight Cathedral Soldier Artifact Bridge Room")
    world.set_rule(twilight_cathedral_soldier_artifact_bridge_room, CAN_GLIDE)

    twilight_cathedral_soldier_artifact_south_wing = world.get_location("Twilight Cathedral Soldier Artifact South Wing")
    world.set_rule(twilight_cathedral_soldier_artifact_south_wing, CAN_GLIDE)


def set_completion_condition(world: DSWorld) -> None:

    world.set_completion_rule(Has("Victory"))

#TODO class DSWorld(CachedRuleBuilderWorld): ...