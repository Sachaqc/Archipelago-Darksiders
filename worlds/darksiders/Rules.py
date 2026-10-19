from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, HasAny, Rule

if TYPE_CHECKING:
    from .World import DSWorld

CAN_BEAT_ABADDON = Has("Armageddon Blade Shards", count = 7) & HasAll("Mask of Shadows", "Ruin", "Shadowflight")
CAN_BREAK_CHAINED_CUBES = HasAny("Armageddon Blade", "Progressive Chaoseater", "Progressive Gauntlet", "Progressive Scythe")
CAN_HURT_GOREMAW = HasAny("Crossblade", "Mercy")
CAN_SLOW_TIME_FROM_AFAR = HasAll("Crossblade", "Chronomancer")
HAS_ABYSSAL_CHAIN = Has("Abyssal Chain")
HAS_CHAOS_FORM = Has("Chaos Form")
HAS_CHRONOMANCER = Has("Chronomancer")
HAS_CROSSBLADE = Has("Crossblade")
HAS_EARTHCALLER = Has("Earthcaller")
HAS_GAUNTLET = Has("Progressive Gauntlet")
HAS_MASK = Has("Mask of Shadows")
HAS_RUIN = Has("Ruin")
HAS_SHADOWFLIGHT = Has("Shadowflight")
HAS_SOUL_BRIDGE = Has("Soul Bridge")
HAS_VOIDWALKER = Has("Voidwalker")

def set_all_rules(world: DSWorld) -> None:
    
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: DSWorld) -> None:

    anvil_ford_to_anvil_ford_challenge_area = world.get_entrance("Anvil's Ford to Anvil's Ford Challenge Area")
    world.set_rule(anvil_ford_to_anvil_ford_challenge_area, HAS_CHAOS_FORM)

    anvil_ford_challenge_area_to_hollows_access_tunnel = world.get_entrance("Anvil's Ford Challenge Area to The Hollows Access Tunnel")
    world.set_rule(anvil_ford_challenge_area_to_hollows_access_tunnel, HAS_CROSSBLADE)

    ashlands_1_to_ashlands_2 = world.get_entrance("The Ashlands 1 to The Ashlands 2")
    world.set_rule(ashlands_1_to_ashlands_2, CAN_SLOW_TIME_FROM_AFAR)

    ashlands_access_tunnel_1_to_ashlands_access_tunnel_2 = world.get_entrance("The Ashlands Access Tunnel 1 to The Ashlands Access Tunnel 2")
    world.set_rule(ashlands_access_tunnel_1_to_ashlands_access_tunnel_2, HAS_CROSSBLADE)

    crossroads_to_library = world.get_entrance("The Crossroads to The Library")
    world.set_rule(crossroads_to_library, HAS_EARTHCALLER)

    dry_road_to_ashlands_access_tunnel = world.get_entrance("Dry Road to Ashlands Access Tunnel 1")
    world.set_rule(dry_road_to_ashlands_access_tunnel, CAN_HURT_GOREMAW)

    dry_road_access_tunnel_1_to_dry_road_access_tunnel_2 = world.get_entrance("Dry Road Access Tunnel 1 to Dry Road Access Tunnel 2")
    world.set_rule(dry_road_access_tunnel_1_to_dry_road_access_tunnel_2, HAS_GAUNTLET & HAS_CHRONOMANCER)

    hollows_1_to_hollows_5 = world.get_entrance("The Hollows 1 to The Hollows 5")
    world.set_rule(hollows_1_to_hollows_5, HAS_GAUNTLET)

    hollows_2_to_hollows_3 = world.get_entrance("The Hollows 2 to The Hollows 3")
    world.set_rule(hollows_2_to_hollows_3, Has("Beholder Key", count = 2))

    hollows_3_to_hollows_4 = world.get_entrance("The Hollows 3 to The Hollows 4")
    world.set_rule(hollows_3_to_hollows_4, Has("Beholder Key", count = 3) & HAS_GAUNTLET)

    hollows_5_to_hollows_6 = world.get_entrance("The Hollows 5 to The Hollows 6")
    world.set_rule(hollows_5_to_hollows_6, HAS_CROSSBLADE)

    hollows_5_to_hollows_9 = world.get_entrance("The Hollows 5 to The Hollows 9")
    world.set_rule(hollows_5_to_hollows_9, Has("Beholder Key", count = 4))

    hollows_6_to_hollows_7 = world.get_entrance("The Hollows 6 to The Hollows 7")
    world.set_rule(hollows_6_to_hollows_7, HAS_SHADOWFLIGHT)

    hollows_7_to_hollows_8 = world.get_entrance("The Hollows 7 to The Hollows 8")
    world.set_rule(hollows_7_to_hollows_8, HAS_CROSSBLADE & HAS_GAUNTLET)

    hollows_9_to_hollows_10 = world.get_entrance("The Hollows 9 to The Hollows 10")
    world.set_rule(hollows_9_to_hollows_10, HAS_GAUNTLET)

    crossroads_to_scalding_gallow = world.get_entrance("The Crossroads to Scalding Gallow")
    world.set_rule(crossroads_to_scalding_gallow, HAS_EARTHCALLER)

    drowned_pass_to_anvil_ford_access_tunnel = world.get_entrance("Drowned Pass to Anvil's Ford Access Tunnel")
    world.set_rule(drowned_pass_to_anvil_ford_access_tunnel, HAS_EARTHCALLER)

    hollows_1_to_hollows_2 = world.get_entrance("The Hollows 1 to The Hollows 2")
    world.set_rule(hollows_1_to_hollows_2, HAS_CROSSBLADE)

    leviathan_drift_to_eden = world.get_entrance("Leviathan's Drift to Eden")
    world.set_rule(leviathan_drift_to_eden, HAS_RUIN & HAS_MASK & HAS_SHADOWFLIGHT)

    scalding_gallow_to_black_throne_1 = world.get_entrance("Scalding Gallow to Black Throne 1")
    world.set_rule(scalding_gallow_to_black_throne_1, Has("Heart of the Chosen", count = 4))

    scalding_gallow_to_choking_grounds = world.get_entrance("Scalding Gallow to The Choking Grounds")
    world.set_rule(scalding_gallow_to_choking_grounds, HAS_SHADOWFLIGHT)

    scalding_gallow_to_iron_canopy = world.get_entrance("Scalding Gallow to Iron Canopy 1")
    world.set_rule(scalding_gallow_to_iron_canopy, HAS_SOUL_BRIDGE)

    scalding_gallow_to_dry_road_access_tunnel_1 = world.get_entrance("Scalding Gallow to Dry Road Access Tunnel 1")
    world.set_rule(scalding_gallow_to_dry_road_access_tunnel_1, HAS_GAUNTLET)

    twilight_cathedral_1_to_twilight_cathedral_2 = world.get_entrance("Twilight Cathedral 1 to Twilight Cathedral 2")
    world.set_rule(twilight_cathedral_1_to_twilight_cathedral_2, Has("Beholder Key", count = 1))

    twilight_cathedral_2_to_twilight_cathedral_3 = world.get_entrance("Twilight Cathedral 2 to Twilight Cathedral 3")
    world.set_rule(twilight_cathedral_2_to_twilight_cathedral_3, HAS_CROSSBLADE)


def set_all_location_rules(world: DSWorld) -> None:

    ashlands_chest_by_goremaw = world.get_location("The Ashlands Access Tunnel Rare Chest by Goremaw")
    world.set_rule(ashlands_chest_by_goremaw, CAN_HURT_GOREMAW)

    ashlands_chest_blocked_by_ice = world.get_location("The Ashlands Access Tunnel Life Blocked by Ice")
    world.set_rule(ashlands_chest_blocked_by_ice, HAS_GAUNTLET)

    choking_grounds_chest_in_NE_Building = world.get_location("Choking Grounds Life Chest in NE Building")
    world.set_rule(choking_grounds_chest_in_NE_Building, HAS_GAUNTLET & HAS_SHADOWFLIGHT & HAS_CROSSBLADE)

    crossroads_chest_blocked_by_ice = world.get_location("Crossroads Rare Chest Blocked by Ice")
    world.set_rule(crossroads_chest_blocked_by_ice, HAS_GAUNTLET)

    drowned_pass_chest_blocked_by_ice = world.get_location("Drowned Pass Wrath Chest Blocked by Ice")
    world.set_rule(drowned_pass_chest_blocked_by_ice, HAS_GAUNTLET)

    drowned_pass_access_tunnel_champion_artifact = world.get_location("Drowned Pass Access Tunnel Champion Artifact")
    world.set_rule(drowned_pass_access_tunnel_champion_artifact, HAS_ABYSSAL_CHAIN)

    hollows_chest_under_goremaw = world.get_location('The Hollows Currency Chest under Goremaw')
    world.set_rule(hollows_chest_under_goremaw, HAS_CROSSBLADE)

    scalding_gallow_abyssal_armor_chest_near_entrance = world.get_location("Scalding Gallow Abyssal Armor Piece Near Entrance")
    world.set_rule(scalding_gallow_abyssal_armor_chest_near_entrance, HAS_CROSSBLADE)

    scalding_gallow_abyssal_armor_chest_under_central_platform = world.get_location("Scalding Gallow Abyssal Armor Piece Under Central Platform")
    world.set_rule(scalding_gallow_abyssal_armor_chest_under_central_platform, HAS_SHADOWFLIGHT)

    serpent_hole_to_anvil_ford_chest = world.get_location("Serpent Hole to Anvil\'s Ford Chest")
    world.set_rule(serpent_hole_to_anvil_ford_chest, HAS_ABYSSAL_CHAIN)

    serpent_hole_to_twilight_cathedral_chest = world.get_location("Serpent Hole to Twilight Cathedral Chest")
    world.set_rule(serpent_hole_to_twilight_cathedral_chest, HAS_SHADOWFLIGHT & HAS_MASK)
    
    twilight_cathedral_champion_artifact_north_wing = world.get_location("Twilight Cathedral Champion Artifact North Wing")
    world.set_rule(twilight_cathedral_champion_artifact_north_wing, HAS_SHADOWFLIGHT)

    twilight_cathedral_soldier_artifact_south_wing = world.get_location("Twilight Cathedral Soldier Artifact South Wing")
    world.set_rule(twilight_cathedral_soldier_artifact_south_wing, HAS_SHADOWFLIGHT)

    twilight_cathedral_chained_cube = world.get_location("Twilight Cathedral Chained Cube")
    world.set_rule(twilight_cathedral_chained_cube, CAN_BREAK_CHAINED_CUBES)

    twilight_cathedral_beholder_key_chest_south_wing = world.get_location("Twilight Cathedral Beholder Key Chest South Wing")
    world.set_rule(twilight_cathedral_beholder_key_chest_south_wing, HAS_CROSSBLADE)

    twilight_cathedral_currency_chest_exterior_blocked_by_ice = world.get_location("Twilight Cathedral Currency Chest Exterior Blocked by Ice")
    world.set_rule(twilight_cathedral_currency_chest_exterior_blocked_by_ice, HAS_GAUNTLET)

    twilight_cathedral_life_chest_north_of_three_statues = world.get_location("Twilight Cathedral Life Chest North of Three Statues")
    world.set_rule(twilight_cathedral_life_chest_north_of_three_statues, HAS_SHADOWFLIGHT)

    twilight_cathedral_soldier_artifact_bridge_room = world.get_location("Twilight Cathedral Soldier Artifact Bridge Room")
    world.set_rule(twilight_cathedral_soldier_artifact_bridge_room, HAS_SHADOWFLIGHT)

    twilight_cathedral_soldier_artifact_south_wing = world.get_location("Twilight Cathedral Soldier Artifact South Wing")
    world.set_rule(twilight_cathedral_soldier_artifact_south_wing, HAS_SHADOWFLIGHT)


def set_completion_condition(world: DSWorld) -> None:

    world.set_completion_rule(Has("Victory"))

#TODO class DSWorld(CachedRuleBuilderWorld): ...