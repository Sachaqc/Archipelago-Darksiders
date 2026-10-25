from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, HasAny, Rule

if TYPE_CHECKING:
    from .World import DSWorld

CAN_BEAT_ABADDON = Has("Armageddon Blade Shard", count = 7) & HasAll("Mask of Shadows", "Ruin", "Shadowflight")
CAN_BREAK_CHAINED_CUBES = HasAny("Armageddon Blade", "Progressive Chaoseater", "Progressive Gauntlet", "Progressive Scythe")
CAN_CLIMB_DEMONIC_GROWTH = True
CAN_DETONATE_BOMBS = HasAny("Crossblade", "Mercy")
CAN_DOUBLE_JUMP = True
CAN_DRAG_OBJECTS = True
CAN_GRAB_BOMBS = True
CAN_HIT_CRYSTAL_BLADES = HasAny("Crossblade", "Mercy")
CAN_HURT_GOREMAW = HasAny("Crossblade", "Mercy")
CAN_LEDGE_GRAB = True
CAN_SLOW_TIME_FROM_AFAR = HasAll("Crossblade", "Chronomancer")
CAN_SWIM = True
CAN_TYROLEAN_TRAVERSE = True
HAS_ABYSSAL_CHAIN = Has("Abyssal Chain")
HAS_BLOCK_COUNTER = Has("Block Counter")
HAS_CHAOS_FORM = Has("Chaos Form")
HAS_CHRONOMANCER = Has("Chronomancer")
HAS_CROSSBLADE = Has("Crossblade")
HAS_EARTHCALLER = Has("Earthcaller")
HAS_GAUNTLET = Has("Progressive Gauntlet")
HAS_MASK = Has("Mask of Shadows")
HAS_RUIN = Has("Ruin")
HAS_SERPENT_HOLES = Has("Serpent Holes")
HAS_SHADOWFLIGHT = Has("Shadowflight")
HAS_SOUL_BRIDGE = Has("Soul Bridge")
HAS_VOIDWALKER = Has("Voidwalker")

def set_all_rules(world: DSWorld) -> None:

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: DSWorld) -> None:

    anvil_ford_to_anvil_ford_challenge_area = world.get_entrance("Anvil's Ford to Anvil's Ford Challenge Area")
    world.set_rule(anvil_ford_to_anvil_ford_challenge_area, HAS_CHAOS_FORM | HAS_GAUNTLET)

    anvil_ford_challenge_area_to_hollows_access_tunnel = world.get_entrance("Anvil's Ford Challenge Area to Hollows Access Tunnel")
    world.set_rule(anvil_ford_challenge_area_to_hollows_access_tunnel, HAS_CROSSBLADE)
    anvil_ford_access_tunnel_to_sh = world.get_entrance("Anvil's Ford Access Tunnel to Serpent Holes")
    world.set_rule(anvil_ford_access_tunnel_to_sh, HAS_SERPENT_HOLES)

    ashlands_1_to_ashlands_2 = world.get_entrance("Ashlands 1 to Ashlands 2")
    world.set_rule(ashlands_1_to_ashlands_2, CAN_SLOW_TIME_FROM_AFAR)
 
    ashlands_access_tunnel_1_to_2 = world.get_entrance("Ashlands Access Tunnel 1 to 2")
    world.set_rule(ashlands_access_tunnel_1_to_2, HAS_CROSSBLADE)
    ashlands_access_tunnel_to_sh = world.get_entrance("Ashlands Access Tunnel to Serpent Holes")
    world.set_rule(ashlands_access_tunnel_to_sh, HAS_SERPENT_HOLES)
 
    broken_stairs_1_to_2 = world.get_entrance("Broken Stair 1 to 2")
    world.set_rule(broken_stairs_1_to_2, HAS_SHADOWFLIGHT)
    broken_stairs_to_sh = world.get_entrance("Broken Stair to Serpent Holes")
    world.set_rule(broken_stairs_to_sh, HAS_SERPENT_HOLES)
 
    broken_stairs_2_to_twilight_cathedral = world.get_entrance("Broken Stair 2 to Twilight Cathedral")
    world.set_rule(broken_stairs_2_to_twilight_cathedral, Has("Beholder Key", count = 1))

    choking_grounds_to_broken_stairs_access_tunnel = world.get_entrance("Choking Grounds to Broken Stair")
    world.set_rule(choking_grounds_to_broken_stairs_access_tunnel, HAS_EARTHCALLER)
    choking_grounds_to_sh = world.get_entrance("Choking Grounds to Serpent Holes")
    world.set_rule(choking_grounds_to_sh, HAS_SERPENT_HOLES)

    choking_grounds_access_tunnel_1_to_2 = world.get_entrance("Choking Grounds Access Tunnel 1 to 2")
    world.set_rule(choking_grounds_access_tunnel_1_to_2, HAS_SHADOWFLIGHT)

    crossroads_to_library = world.get_entrance("Crossroads to Library")
    world.set_rule(crossroads_to_library, HAS_EARTHCALLER)
    crossroads_to_sh = world.get_entrance("Crossroads to Serpent Holes")
    world.set_rule(crossroads_to_sh, HAS_SERPENT_HOLES)

    drowned_pass_to_anvil_ford_access_tunnel = world.get_entrance("Drowned Pass to Anvil's Ford Access Tunnel")
    world.set_rule(drowned_pass_to_anvil_ford_access_tunnel, HAS_EARTHCALLER)

    dry_road_to_ashlands = world.get_entrance("Dry Road to Ashlands")
    world.set_rule(dry_road_to_ashlands, CAN_HURT_GOREMAW)
    dry_road_to_vulgrim = world.get_entrance("Dry Road to Serpent Holes")
    world.set_rule(dry_road_to_vulgrim, HAS_SERPENT_HOLES & HAS_SHADOWFLIGHT)
    dry_road_to_vulgrim = world.get_entrance("Dry Road to Vulgrim's Shop")
    world.set_rule(dry_road_to_vulgrim, HAS_SHADOWFLIGHT)
    dry_road_access_tunnel_1_to_2 = world.get_entrance("Dry Road Access Tunnel 1 to 2")
    world.set_rule(dry_road_access_tunnel_1_to_2, HAS_CHRONOMANCER & HAS_GAUNTLET)

    hollows_water_room_to_maintenance = world.get_entrance("Hollows Water Room to Maintenance Area")
    world.set_rule(hollows_water_room_to_maintenance, HAS_CROSSBLADE)
    hollows_1_to_hollows_5 = world.get_entrance("Hollows Clock Room to Train Wreck Area")
    world.set_rule(hollows_1_to_hollows_5, HAS_GAUNTLET & HAS_SHADOWFLIGHT)
    hollows_2_to_hollows_3 = world.get_entrance("Hollows Maintenance Area to Chained Cube Area")
    world.set_rule(hollows_2_to_hollows_3, Has("Beholder Key", count = 4))
    hollows_2_to_4 = world.get_entrance("Hollows Water Room to Machinery Room")
    world.set_rule(hollows_2_to_4, HAS_GAUNTLET)
    hollows_3_to_hollows_4 = world.get_entrance("Hollows Chained Cube Area to Hollows Machinery Room")
    world.set_rule(hollows_3_to_hollows_4, Has("Beholder Key", count = 5) & HAS_GAUNTLET)
    hollows_4_to_2 = world.get_entrance("Hollows Machinery Room to Water Room")
    world.set_rule(hollows_4_to_2, HAS_GAUNTLET & HAS_SHADOWFLIGHT)
    hollows_5_to_hollows_6 = world.get_entrance("Hollows Train Wreck Area to Locust Room")
    world.set_rule(hollows_5_to_hollows_6, HAS_CROSSBLADE)
    hollows_5_to_hollows_9 = world.get_entrance("Hollows Train Wreck Area to Griever Tunnel")
    world.set_rule(hollows_5_to_hollows_9, Has("Beholder Key", count = 6))
    hollows_7_to_8 = world.get_entrance("Hollows Flooded Room to above Flooded Room")
    world.set_rule(hollows_7_to_8, HAS_SHADOWFLIGHT)
    hollows_9_to_hollows_10 = world.get_entrance("Hollows Griever Tunnel to Flooded Canyon")
    world.set_rule(hollows_9_to_hollows_10, HAS_GAUNTLET)

    leviathan_drift_to_eden = world.get_entrance("Leviathan's Drift to Eden")
    world.set_rule(leviathan_drift_to_eden, HAS_RUIN & HAS_MASK & HAS_SHADOWFLIGHT)

    scalding_gallow_to_black_throne_1 = world.get_entrance("Scalding Gallow to Black Throne")
    world.set_rule(scalding_gallow_to_black_throne_1, Has("Heart of the Chosen", count = 4))
    scalding_gallow_to_choking_grounds = world.get_entrance("Scalding Gallow to Choking Grounds")
    world.set_rule(scalding_gallow_to_choking_grounds, HAS_SHADOWFLIGHT)
    scalding_gallow_to_drowned_pass = world.get_entrance("Scalding Gallow to Drowned Pass")
    world.set_rule(scalding_gallow_to_drowned_pass, HAS_CROSSBLADE)
    scalding_gallow_to_dry_road_access_tunnel_1 = world.get_entrance("Scalding Gallow to Dry Road")
    world.set_rule(scalding_gallow_to_dry_road_access_tunnel_1, HAS_GAUNTLET)
    scalding_gallow_to_iron_canopy = world.get_entrance("Scalding Gallow to Iron Canopy")
    world.set_rule(scalding_gallow_to_iron_canopy, HAS_SOUL_BRIDGE)
    scalding_gallow_to_sh = world.get_entrance("Scalding Gallow to Serpent Holes")
    world.set_rule(scalding_gallow_to_sh, HAS_SERPENT_HOLES)

    twilight_cathedral_exterior_1_to_2 = world.get_entrance("Twilight Cathedral Exterior 1 to 2")
    world.set_rule(twilight_cathedral_exterior_1_to_2, HAS_ABYSSAL_CHAIN)
    twilight_cathedral_to_sh = world.get_entrance("Twilight Cathedral to Serpent Holes")
    world.set_rule(twilight_cathedral_to_sh, HAS_SERPENT_HOLES)
    twilight_cathedral_SW_to_conscript = world.get_entrance("Twilight Cathedral Entrance to Twilight Cathedral Conscript Room")
    world.set_rule(twilight_cathedral_SW_to_conscript, Has("Beholder Key", count = 2))
    twilight_cathedral_entrance_to_NW = world.get_entrance("Twilight Cathedral Entrance to North Wing")
    world.set_rule(twilight_cathedral_entrance_to_NW, Has("Crystal Blade"))
    twilight_cathedral_NW_to_abyssal = world.get_entrance("Twilight Cathedral North Wing to Abyssal Chest Area")
    world.set_rule(twilight_cathedral_NW_to_abyssal, CAN_HURT_GOREMAW & HAS_SHADOWFLIGHT)
    twilight_cathedral_NW_to_abyssal = world.get_entrance("Twilight Cathedral Entrance to Basement")
    world.set_rule(twilight_cathedral_NW_to_abyssal, CAN_HURT_GOREMAW)
    twilight_cathedral_chained_cube_area_to_three_statues = world.get_entrance("Twilight Cathedral Chained Cube Area to Three Statues")
    world.set_rule(twilight_cathedral_chained_cube_area_to_three_statues, HAS_CROSSBLADE)
    twilight_cathedral_three_statues_to_west = world.get_entrance("Twilight Cathedral Three Statues to West Path")
    world.set_rule(twilight_cathedral_three_statues_to_west, HAS_CROSSBLADE)
    twilight_cathedral_three_statues_to_north = world.get_entrance("Twilight Cathedral Three Statues to North Path")
    world.set_rule(twilight_cathedral_three_statues_to_north, HAS_SHADOWFLIGHT & HAS_CROSSBLADE)
    twilight_cathedral_three_statues_to_east = world.get_entrance("Twilight Cathedral Three Statues to East Path")
    world.set_rule(twilight_cathedral_three_statues_to_east, HasAll("West Crystal Blade", "North Crystal Blade"))
    twilight_cathedral_three_statues_to_south = world.get_entrance("Twilight Cathedral Three Statues to South Path")
    world.set_rule(twilight_cathedral_three_statues_to_south, HAS_CROSSBLADE & Has("Beholder Key", count = 3))
    twilight_cathedral_three_statues_to_north_wing = world.get_entrance("Twilight Cathedral Three Statues to North Wing")
    world.set_rule(twilight_cathedral_three_statues_to_north_wing, HasAll("West Crystal Blade", "North Crystal Blade", "South Crystal Blade"))
    twilight_cathedral_north_wing_to_boss_room = world.get_entrance("Twilight Cathedral North Wing to Boss Room")
    world.set_rule(twilight_cathedral_north_wing_to_boss_room, HasAll("West Crystal Blade", "North Crystal Blade", "South Crystal Blade"))


def set_all_location_rules(world: DSWorld) -> None:

    anvil_ford_ulthane_defeated = world.get_location("Anvil's Ford Ulthane defeated")
    world.set_rule(anvil_ford_ulthane_defeated, HAS_CHAOS_FORM)
    anvil_ford_ulthane_outscored = world.get_location("Anvil's Ford Challenge Area Ulthane outscored")
    world.set_rule(anvil_ford_ulthane_outscored, HAS_CHAOS_FORM)
    anvil_ford_chest_ice_entrance = world.get_location("Anvil's Ford Challenge Area Chest Blocked by Ice near Entrance")
    world.set_rule(anvil_ford_chest_ice_entrance, HAS_GAUNTLET)
    anvil_ford_west_chest = world.get_location("Anvil's Ford Challenge Area West Platform Chest")
    world.set_rule(anvil_ford_west_chest, HAS_ABYSSAL_CHAIN)
    anvil_ford_chest_ice_uriel = world.get_location("Anvil's Ford Challenge Area Chest Blocked by Ice near Uriel")
    world.set_rule(anvil_ford_chest_ice_uriel, HAS_GAUNTLET)
    anvil_ford_access_tunnel_chest_ice = world.get_location("Anvil's Ford Access Tunnel Chest Blocked by Ice")
    world.set_rule(anvil_ford_access_tunnel_chest_ice, HAS_GAUNTLET)

    ashlands_chest_by_goremaw = world.get_location("Ashlands Access Tunnel Rare Chest by Goremaw")
    world.set_rule(ashlands_chest_by_goremaw, CAN_HURT_GOREMAW)
    ashlands_chest_blocked_by_ice = world.get_location("Ashlands Access Tunnel Life Blocked by Ice")
    world.set_rule(ashlands_chest_blocked_by_ice, HAS_GAUNTLET)


    broken_stairs_artifact = world.get_location("Broken Stair Artifact")
    world.set_rule(broken_stairs_artifact, HAS_SHADOWFLIGHT)
    broken_stairs_access_tunnel_artifact = world.get_location("Broken Stair Artifact Blocked by Ice")
    world.set_rule(broken_stairs_access_tunnel_artifact, HAS_GAUNTLET)

    choking_grounds_aerial_brawl = world.get_location("Choking Grounds Aerial Brawl Reward")
    world.set_rule(choking_grounds_aerial_brawl, HAS_MASK)
    choking_grounds_speed_brawl = world.get_location("Choking Grounds Speed Brawl Reward")
    world.set_rule(choking_grounds_speed_brawl, HAS_MASK)
    choking_grounds_gory_end = world.get_location("Choking Grounds The Gory End Reward")
    world.set_rule(choking_grounds_gory_end, HAS_MASK)
    choking_grounds_venomous = world.get_location("Choking Grounds Venomous Reward")
    world.set_rule(choking_grounds_venomous, HAS_MASK)
    choking_grounds_blade_shard = world.get_location("Choking Grounds North Building Armaggedon Blade Shard")
    world.set_rule(choking_grounds_blade_shard, HAS_CROSSBLADE & HAS_GAUNTLET & HAS_MASK & HAS_SHADOWFLIGHT)
    choking_grounds_iced_chest = world.get_location("Choking Grounds Top Floor of North Building Chest Blocked by Ice")
    world.set_rule(choking_grounds_iced_chest, HAS_GAUNTLET & HAS_SHADOWFLIGHT & HAS_CROSSBLADE)
    choking_grounds_chest_in_North_Building = world.get_location("Choking Grounds Top Floor of North Building Chest")
    world.set_rule(choking_grounds_chest_in_North_Building, HAS_SHADOWFLIGHT & HAS_CROSSBLADE)
    choking_grounds_rare_chest_in_North_Building = world.get_location("Choking Grounds North Building Rare Chest")
    world.set_rule(choking_grounds_rare_chest_in_North_Building, HAS_ABYSSAL_CHAIN & HAS_SHADOWFLIGHT & HAS_CROSSBLADE)
    choking_grounds_abyssal_chest = world.get_location("Choking Grounds Access Tunnel Chest behind Portals")
    world.set_rule(choking_grounds_abyssal_chest, HAS_SHADOWFLIGHT & HAS_VOIDWALKER)

    crossroads_chest_blocked_by_ice = world.get_location("Crossroads Chest Blocked by Ice")
    world.set_rule(crossroads_chest_blocked_by_ice, HAS_GAUNTLET)
    #crossroads_artifact_in_water = world.get_location("Crossroads Soldier Artifact in Subway Station")
    #world.set_rule(crossroads_artifact_in_water, CAN_SWIM)

    drowned_pass_world_of_pain = world.get_location("Drowned Pass World of Pain Reward")
    world.set_rule(drowned_pass_world_of_pain, HAS_MASK)
    drowned_pass_defender = world.get_location("Drowned Pass Defender Reward")
    world.set_rule(drowned_pass_defender, HAS_MASK)
    drowned_pass_wrath_of_war = world.get_location("Drowned Pass Wrath of War Reward")
    world.set_rule(drowned_pass_wrath_of_war, HAS_MASK)
    drowned_pass_counter_killer = world.get_location("Drowned Pass Counter Killer Reward")
    world.set_rule(drowned_pass_counter_killer, HAS_BLOCK_COUNTER & HAS_MASK)
    drowned_pass_armageddon_shard = world.get_location("Drowned Pass Armageddon Blade Shard")
    world.set_rule(drowned_pass_armageddon_shard, HAS_ABYSSAL_CHAIN & HAS_MASK)
    drowned_pass_chest_blocked_by_ice = world.get_location("Drowned Pass Chest Blocked by Ice")
    world.set_rule(drowned_pass_chest_blocked_by_ice, HAS_GAUNTLET)
    drowned_pass_access_tunnel_artifact = world.get_location("Drowned Pass Access Tunnel Artifact")
    world.set_rule(drowned_pass_access_tunnel_artifact, HAS_ABYSSAL_CHAIN & HAS_SHADOWFLIGHT)
    drowned_pass_access_tunnel_first_chest = world.get_location("Drowned Pass Access Tunnel First Chest")
    world.set_rule(drowned_pass_access_tunnel_first_chest, HAS_ABYSSAL_CHAIN & HAS_SHADOWFLIGHT & HAS_VOIDWALKER)

    dry_road_uriel_defeated = world.get_location("Dry Road Uriel defeated")
    world.set_rule(dry_road_uriel_defeated, Has("Armageddon Blade Shard"))
    dry_road_voidwalker_chest = world.get_location("Dry Road Access Tunnel above Gate Chest")
    world.set_rule(dry_road_voidwalker_chest, HAS_VOIDWALKER)

    hollows_griever_defeated = world.get_location('Griever defeated')
    world.set_rule(hollows_griever_defeated, HAS_GAUNTLET)
    hollows_griever_item_reward = world.get_location('Griever Item Reward')
    world.set_rule(hollows_griever_item_reward, HAS_GAUNTLET)
    hollows_across_flooded_room_chest = world.get_location('Hollows across the Flooded Hole Chest')
    world.set_rule(hollows_across_flooded_room_chest, HAS_GAUNTLET)
    hollows_across_flooded_room_chest = world.get_location('Hollows Machinery Room South of Platforms Artifact')
    world.set_rule(hollows_across_flooded_room_chest, HAS_SHADOWFLIGHT)
    hollows_locust_room_artifact = world.get_location('Hollows Pipe Leading North Artifact')
    world.set_rule(hollows_locust_room_artifact, Has("Stalactite fell"))
    hollows_flooded_room_chest = world.get_location('Hollows Flooded Room Chest')
    world.set_rule(hollows_flooded_room_chest, Has("Stalactite fell"))
    hollows_chest_under_goremaw = world.get_location('Hollows Chest under Goremaw')
    world.set_rule(hollows_chest_under_goremaw, CAN_HURT_GOREMAW)

    library_artifact = world.get_location("Library West Side Artifact")
    world.set_rule(library_artifact, HAS_SHADOWFLIGHT)
    library_north_chest = world.get_location("Library North Chest after Hook")
    world.set_rule(library_north_chest, HAS_ABYSSAL_CHAIN)

    scalding_gallow_trade_first_heart = world.get_location('Scalding Gallow Trade first Heart of the Chosen')
    world.set_rule(scalding_gallow_trade_first_heart, Has("Heart of the Chosen", count = 1))
    scalding_gallow_trade_second_heart = world.get_location('Scalding Gallow Trade second Heart of the Chosen')
    world.set_rule(scalding_gallow_trade_second_heart, Has("Heart of the Chosen", count = 2))
    scalding_gallow_trade_third_heart = world.get_location('Scalding Gallow Trade third Heart of the Chosen')
    world.set_rule(scalding_gallow_trade_third_heart, Has("Heart of the Chosen", count = 3))
    scalding_gallow_trade_fourth_heart = world.get_location('Scalding Gallow Trade fourth Heart of the Chosen')
    world.set_rule(scalding_gallow_trade_fourth_heart, Has("Heart of the Chosen", count = 4))
    scalding_gallow_pillar_chest = world.get_location("Scalding Gallow Bombable Pillar Chest Near Library")
    world.set_rule(scalding_gallow_pillar_chest, CAN_DETONATE_BOMBS)
    #scalding_gallow_wrath_chest = world.get_location("Scalding Gallow Wrath Chest Above Vulgrim")
    #world.set_rule(scalding_gallow_wrath_chest, CAN_CLIMB_DEMONIC_GROWTH)
    scalding_gallow_under_central_platform = world.get_location("Scalding Gallow Under Central Platform Chest")
    world.set_rule(scalding_gallow_under_central_platform, HAS_SHADOWFLIGHT) #CAN_DOUBLE_JUMP

    serpent_hole_to_anvil_ford_chest = world.get_location("Serpent Hole to Anvil\'s Ford Chest")
    world.set_rule(serpent_hole_to_anvil_ford_chest, HAS_ABYSSAL_CHAIN)
    serpent_hole_to_twilight_cathedral_chest = world.get_location("Serpent Hole to Twilight Cathedral Chest")
    world.set_rule(serpent_hole_to_twilight_cathedral_chest, HAS_SHADOWFLIGHT & HAS_MASK)
    
    twilight_cathedral_tiamat_defeated = world.get_location('Tiamat defeated')
    world.set_rule(twilight_cathedral_tiamat_defeated, HAS_CROSSBLADE)
    twilight_cathedral_tiamat_item_reward = world.get_location('Tiamat Item Reward')
    world.set_rule(twilight_cathedral_tiamat_item_reward, HAS_CROSSBLADE)
    twilight_cathedral_champion_artifact_north_wing = world.get_location("Twilight Cathedral North Wing Artifact")
    world.set_rule(twilight_cathedral_champion_artifact_north_wing, HAS_SHADOWFLIGHT)
    twilight_cathedral_chained_cube = world.get_location("Twilight Cathedral Chained Cube")
    world.set_rule(twilight_cathedral_chained_cube, CAN_BREAK_CHAINED_CUBES)
    twilight_cathedral_SW_beholder = world.get_location("Twilight Cathedral South Wing Beholder Key Chest")
    world.set_rule(twilight_cathedral_SW_beholder, HAS_CROSSBLADE)
    twilight_cathedral_chest_blocked_by_ice = world.get_location("Twilight Cathedral Exterior Chest Blocked by Ice")
    world.set_rule(twilight_cathedral_chest_blocked_by_ice, HAS_GAUNTLET)
    twilight_cathedral_hoardseeker = world.get_location("Twilight Cathedral South Wing Hoardseeker Chest")
    world.set_rule(twilight_cathedral_hoardseeker, CAN_DETONATE_BOMBS & HAS_SHADOWFLIGHT)


def set_completion_condition(world: DSWorld) -> None:

    world.set_completion_rule(Has("Victory"))

#TODO class DSWorld(CachedRuleBuilderWorld): ...