from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

from .Utils import data_path, json_read

if TYPE_CHECKING:
    from .World import DSWorld

def create_and_connect_regions(world: DSWorld) -> None:

    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: DSWorld) -> None:

    #anvil_ford = Region("Anvil's Ford", world.player, world.multiworld)
    #anvil_ford_access_tunnel = Region("Anvil's Ford Access Tunnel", world.player, world.multiworld)
    #anvil_ford_challenge_area = Region("Anvil's Ford Challenge Area", world.player, world.multiworld)
    #ashlands_1 = Region("The Ashlands 1", world.player, world.multiworld)
    #ashlands_2 = Region("The Ashlands 2", world.player, world.multiworld)
    #ashlands_access_tunnel_1 = Region("The Ashlands Access Tunnel 1", world.player, world.multiworld)
    #ashlands_access_tunnel_2 = Region("The Ashlands Access Tunnel 2", world.player, world.multiworld)
    black_throne_1 = Region("Black Throne 1", world.player, world.multiworld)
    black_throne_boss_room = Region("Black Throne Boss Room", world.player, world.multiworld)
    #broken_stair = Region("The Broken Stair", world.player, world.multiworld)
    #choking_grounds = Region("The Choking Grounds", world.player, world.multiworld)
    #crossroads = Region("The Crossroads", world.player, world.multiworld)
    #drowned_pass = Region("Drowned Pass", world.player, world.multiworld)
    #drowned_pass_access_tunnel = Region("Drowned Pass Access Tunnel", world.player, world.multiworld)
    #dry_road = Region("The Dry Road", world.player, world.multiworld)
    #dry_road_access_tunnel_1 = Region("The Dry Road Access Tunnel 1", world.player, world.multiworld)
    #dry_road_access_tunnel_2 = Region("The Dry Road Access Tunnel 2", world.player, world.multiworld)
    eden = Region("Eden", world.player, world.multiworld)
    hollows_1 = Region("The Hollows 1", world.player, world.multiworld) #Before gas pipes
    hollows_2 = Region("The Hollows 2", world.player, world.multiworld) #Before First Beholder Key
    hollows_3 = Region("The Hollows 3", world.player, world.multiworld) #Before Second Beholder Key
    hollows_4 = Region("The Hollows 4", world.player, world.multiworld) #After Second Beholder Key and Gauntlet
    hollows_5 = Region("The Hollows 5", world.player, world.multiworld) #Branching from Hollows Entrance, after Block of Ice
    hollows_6 = Region("The Hollows 6", world.player, world.multiworld) #Passed Gas Pipes again
    hollows_7 = Region("The Hollows 7", world.player, world.multiworld) #Passed Geysers
    hollows_8 = Region("The Hollows 8", world.player, world.multiworld) #Passed yet another Gas Pipe Puzzle
    hollows_9 = Region("The Hollows 9", world.player, world.multiworld) #Branching from Train Cars Room, Passed Third Beholder Key
    hollows_10 = Region("The Hollows 10", world.player, world.multiworld) #Passed Block of Ice filling room with water
    hollows_boss_room = Region("The Hollows Boss Room", world.player, world.multiworld)
    hollows_access_tunnel = Region("The Hollows Access Tunnel", world.player, world.multiworld)
    iron_canopy_1 = Region("Iron Canopy 1", world.player, world.multiworld)
    leviathan_drift = Region("Leviathan's Drift", world.player, world.multiworld)
    #library = Region("The Library", world.player, world.multiworld)
    #menu = Region("Menu", world.player, world.multiworld)
    #scalding_gallow = Region("Scalding Gallow", world.player, world.multiworld)
    #seraphim_hotel = Region("Seraphim Hotel", world.player, world.multiworld)
    silitha_loom = Region("Silitha's Loom", world.player, world.multiworld)
    #serpent_holes = Region("Serpent Holes", world.player, world.multiworld)
    #sh_to_anvil_ford = Region("Serpent Hole to Anvil's Ford", world.player, world.multiworld)
    #sh_to_dry_road = Region("Serpent Hole to Dry Road", world.player, world.multiworld)
    #sh_to_twilight_cathedral = Region("Serpent Hole to Twilight Cathedral", world.player, world.multiworld)
    tree_of_knowledge = Region("Tree of Knowledge", world.player, world.multiworld)
    #twilight_cathedral_exterior = Region("Twilight Cathedral Exterior", world.player, world.multiworld)
    #twilight_cathedral_1 = Region("Twilight Cathedral 1", world.player, world.multiworld) #Before first beholder key
    #twilight_cathedral_2 = Region("Twilight Cathedral 2", world.player, world.multiworld) #After first beholder key
    #twilight_cathedral_3 = Region("Twilight Cathedral 3", world.player, world.multiworld) #After Crossblade
    #twilight_cathedral_boss_room = Region("Twilight Cathedral Boss Room", world.player, world.multiworld)
    #vulgrim_shop = Region("Vulgrim's Shop", world.player, world.multiworld)

    regions = [
        #anvil_ford,
        #anvil_ford_access_tunnel,
        #anvil_ford_challenge_area,
        #ashlands_1,
        #ashlands_2,
        #ashlands_access_tunnel_1,
        #ashlands_access_tunnel_2,
        black_throne_1,
        black_throne_boss_room,
        #broken_stair,
        #choking_grounds,
        #crossroads,
        #drowned_pass,
        #drowned_pass_access_tunnel,
        #dry_road,
        #dry_road_access_tunnel_1,
        #dry_road_access_tunnel_2,
        eden,
        hollows_1,
        hollows_2,
        hollows_3,
        hollows_4,
        hollows_5,
        hollows_6,
        hollows_7,
        hollows_8,
        hollows_9,
        hollows_10,
        hollows_boss_room,
        hollows_access_tunnel,
        iron_canopy_1,
        leviathan_drift,
        #library,
        #menu,
        #scalding_gallow,
        #seraphim_hotel,
        silitha_loom,
        #serpent_holes,
        #sh_to_anvil_ford,
        #sh_to_dry_road,
        #sh_to_twilight_cathedral,
        tree_of_knowledge,
        #twilight_cathedral_exterior,
        #twilight_cathedral_1,
        #twilight_cathedral_2,
        #twilight_cathedral_3,
        #twilight_cathedral_boss_room,
        #vulgrim_shop,
    ]

    world.multiworld.regions += regions

    create_region_from_json(world, "Anvil ford.json")
    create_region_from_json(world, "Ashlands.json")
    create_region_from_json(world, "Crossroads.json")
    create_region_from_json(world, "Choking Grounds.json")
    create_region_from_json(world, "Drowned Pass.json")
    create_region_from_json(world, "Dry Road.json")
    create_region_from_json(world, "Library.json")
    create_region_from_json(world, "Menu.json")
    create_region_from_json(world, "Scalding Gallow.json")
    create_region_from_json(world, "Serpent Holes.json")
    create_region_from_json(world, "Twilight Cathedral.json")

def connect_regions(world: DSWorld) -> None:

    #anvil_ford = world.get_region("Anvil's Ford")
    #anvil_ford_access_tunnel = world.get_region("Anvil's Ford Access Tunnel")
    #anvil_ford_challenge_area = world.get_region("Anvil's Ford Challenge Area")
    #ashlands_1 = world.get_region("The Ashlands 1")
    #ashlands_2 = world.get_region("The Ashlands 2")
    #ashlands_access_tunnel_1 = world.get_region("The Ashlands Access Tunnel 1")
    #ashlands_access_tunnel_2 = world.get_region("The Ashlands Access Tunnel 2")
    black_throne_1 = world.get_region("Black Throne 1")
    black_throne_boss_room = world.get_region("Black Throne Boss Room")
    #broken_stair = world.get_region("The Broken Stair")
    #choking_grounds = world.get_region("The Choking Grounds")
    #crossroads = world.get_region("The Crossroads")
    #drowned_pass = world.get_region("Drowned Pass")
    #drowned_pass_access_tunnel = world.get_region("Drowned Pass Access Tunnel")
    #dry_road = world.get_region("The Dry Road")
    #dry_road_access_tunnel_1 = world.get_region("The Dry Road Access Tunnel 1")
    #dry_road_access_tunnel_2 = world.get_region("The Dry Road Access Tunnel 2")
    eden = world.get_region("Eden")
    hollows_1 = world.get_region("The Hollows 1")
    hollows_2 = world.get_region("The Hollows 2")
    hollows_3 = world.get_region("The Hollows 3")
    hollows_4 = world.get_region("The Hollows 4")
    hollows_5 = world.get_region("The Hollows 5")
    hollows_6 = world.get_region("The Hollows 6")
    hollows_7 = world.get_region("The Hollows 7")
    hollows_8 = world.get_region("The Hollows 8")
    hollows_9 = world.get_region("The Hollows 9")
    hollows_10 = world.get_region("The Hollows 10")
    hollows_boss_room = world.get_region("The Hollows Boss Room")
    hollows_access_tunnel = world.get_region("The Hollows Access Tunnel")
    iron_canopy_1 = world.get_region("Iron Canopy 1")
    leviathan_drift = world.get_region("Leviathan's Drift")
    #library = world.get_region("The Library")
    #menu = world.get_region("Menu")
    #scalding_gallow = world.get_region("Scalding Gallow")
    #seraphim_hotel = world.get_region("Seraphim Hotel")
    silitha_loom = world.get_region("Silitha's Loom")
    #serpent_holes = world.get_region("Serpent Holes")
    #sh_to_anvil_ford = world.get_region("Serpent Hole to Anvil's Ford")
    #sh_to_dry_road = world.get_region("Serpent Hole to Dry Road")
    #sh_to_twilight_cathedral = world.get_region("Serpent Hole to Twilight Cathedral")
    tree_of_knowledge = world.get_region("Tree of Knowledge")
    #twilight_cathedral_exterior = world.get_region("Twilight Cathedral Exterior")
    #twilight_cathedral_1 = world.get_region("Twilight Cathedral 1")
    #twilight_cathedral_2 = world.get_region("Twilight Cathedral 2")
    #twilight_cathedral_3 = world.get_region("Twilight Cathedral 3")
    #twilight_cathedral_boss_room = world.get_region("Twilight Cathedral Boss Room")
    #vulgrim_shop = world.get_region("Vulgrim's Shop")

    #anvil_ford_to_anvil_ford_challenge_area = Entrance(world.player, "Anvil's Ford to Anvil's Ford Challenge Area", parent = anvil_ford)
    #anvil_ford.exits.append(anvil_ford_to_anvil_ford_challenge_area)
    #anvil_ford_to_anvil_ford_challenge_area.connect(anvil_ford_challenge_area)

    #anvil_ford_access_tunnel_to_anvil_ford = Entrance(world.player, "Anvil's Ford Access Tunnel to Anvil's Ford", parent = anvil_ford_access_tunnel)
    #anvil_ford_access_tunnel.exits.append(anvil_ford_access_tunnel_to_anvil_ford)
    #anvil_ford_access_tunnel_to_anvil_ford.connect(anvil_ford)

    #anvil_ford_access_tunnel_to_serpent_holes = Entrance(world.player, "Anvil's Ford Access Tunnel to Serpent Holes", parent = anvil_ford_access_tunnel)
    #anvil_ford_access_tunnel.exits.append(anvil_ford_access_tunnel_to_serpent_holes)
    #anvil_ford_access_tunnel_to_serpent_holes.connect(serpent_holes)

    #anvil_ford_access_tunnel_to_vulgrim_shop = Entrance(world.player, "Anvil's Ford Access Tunnel to Vulgrim's Shop", parent = anvil_ford_access_tunnel)
    #anvil_ford_access_tunnel.exits.append(anvil_ford_access_tunnel_to_vulgrim_shop)
    #anvil_ford_access_tunnel_to_vulgrim_shop.connect(vulgrim_shop)

    #anvil_ford_challenge_area_to_hollows_access_tunnel = Entrance(world.player, "Anvil's Ford Challenge Area to The Hollows Access Tunnel", parent = anvil_ford_challenge_area)
    #anvil_ford_challenge_area.exits.append(anvil_ford_challenge_area_to_hollows_access_tunnel)
    #anvil_ford_challenge_area_to_hollows_access_tunnel.connect(hollows_access_tunnel)

    create_entrances_from_json(world, "Anvil Ford.json")

    #ashlands_1_to_ashlands_2 = Entrance(world.player, "The Ashlands 1 to The Ashlands 2", parent = ashlands_1)
    #ashlands_1.exits.append(ashlands_1_to_ashlands_2)
    #ashlands_1_to_ashlands_2.connect(ashlands_2)

    #ashlands_1_to_leviathan_drift = Entrance(world.player, "The Ashlands to Leviathan's Drift", parent = ashlands_1)
    #ashlands_1.exits.append(ashlands_1_to_leviathan_drift)
    #ashlands_1_to_leviathan_drift.connect(leviathan_drift)

    #ashlands_access_tunnel_1_to_ashlands_access_tunnel_2 = Entrance(world.player, "The Ashlands Access Tunnel 1 to The Ashlands Access Tunnel 2", parent = ashlands_access_tunnel_1)
    #ashlands_access_tunnel_1.exits.append(ashlands_access_tunnel_1_to_ashlands_access_tunnel_2)
    #ashlands_access_tunnel_1_to_ashlands_access_tunnel_2.connect(ashlands_access_tunnel_2)

    #ashlands_access_tunnel_2_to_ashlands_1 = Entrance(world.player, "The Ashlands Access Tunnel 2 to The Ashlands 1", parent = ashlands_access_tunnel_2)
    #ashlands_access_tunnel_2.exits.append(ashlands_access_tunnel_2_to_ashlands_1)
    #ashlands_access_tunnel_2_to_ashlands_1.connect(ashlands_1)

    #ashlands_access_tunnel_2_to_serpent_holes = Entrance(world.player, "The Ashlands Access Tunnel 2 to Serpent Holes", parent = ashlands_access_tunnel_2)
    #ashlands_access_tunnel_2.exits.append(ashlands_access_tunnel_2_to_serpent_holes)
    #ashlands_access_tunnel_2_to_serpent_holes.connect(serpent_holes)

    #ashlands_access_tunnel_2_to_vulgrim_shop = Entrance(world.player, "The Ashlands Access Tunnel 2 to Vulgrim's Shop", parent = ashlands_access_tunnel_2)
    #ashlands_access_tunnel_2.exits.append(ashlands_access_tunnel_2_to_vulgrim_shop)
    #ashlands_access_tunnel_2_to_vulgrim_shop.connect(vulgrim_shop)

    create_entrances_from_json(world, "Ashlands.json")

    black_throne_1_to_black_throne_boss_room = Entrance(world.player, "Black Throne 1 to Black Throne Boss Room", parent = black_throne_1)
    black_throne_1.exits.append(black_throne_1_to_black_throne_boss_room)
    black_throne_1_to_black_throne_boss_room.connect(black_throne_boss_room)

    #broken_stair_to_twilight_cathedral_1 = Entrance(world.player, "The Broken Stair to Twilight Cathedral 1", parent = broken_stair)
    #broken_stair.exits.append(broken_stair_to_twilight_cathedral_1)
    #broken_stair_to_twilight_cathedral_1.connect(twilight_cathedral_1)

    #broken_stair_to_serpent_holes = Entrance(world.player, "The Broken Stair to Serpent Holes", parent = broken_stair)
    #broken_stair.exits.append(broken_stair_to_serpent_holes)
    #broken_stair_to_serpent_holes.connect(serpent_holes)

    #broken_stair_to_vulgrim_shop = Entrance(world.player, "The Broken Stair to Vulgrim's Shop", parent = broken_stair)
    #broken_stair.exits.append(broken_stair_to_vulgrim_shop)
    #broken_stair_to_vulgrim_shop.connect(vulgrim_shop)

    #choking_grounds_to_broken_stair = Entrance(world.player, "The Choking Grounds to The Broken Stair", parent = choking_grounds)
    #choking_grounds.exits.append(choking_grounds_to_broken_stair)
    #choking_grounds_to_broken_stair.connect(broken_stair)

    #choking_grounds_to_serpent_holes = Entrance(world.player, "The Choking Grounds to Serpent Holes", parent = choking_grounds)
    #choking_grounds.exits.append(choking_grounds_to_serpent_holes)
    #choking_grounds_to_serpent_holes.connect(serpent_holes)

    #choking_grounds_to_vulgrim_shop = Entrance(world.player, "The Choking Grounds to Vulgrim's Shop", parent = choking_grounds)
    #choking_grounds.exits.append(choking_grounds_to_vulgrim_shop)
    #choking_grounds_to_vulgrim_shop.connect(vulgrim_shop)

    create_entrances_from_json(world, "Choking grounds.json")

    #crossroads_to_library = Entrance(world.player, "The Crossroads to The Library", parent = crossroads)
    #crossroads.exits.append(crossroads_to_library)
    #crossroads_to_library.connect(library)

    create_entrances_from_json(world, "Crossroads.json")

    #crossroads_to_scalding_gallow = Entrance(world.player, "The Crossroads to Scalding Gallow", parent = crossroads)
    #crossroads.exits.append(crossroads_to_scalding_gallow)
    #crossroads_to_scalding_gallow.connect(scalding_gallow)

    #crossroads_to_serpent_holes = Entrance(world.player, "The Crossroads to Serpent Holes", parent = crossroads)
    #crossroads.exits.append(crossroads_to_serpent_holes)
    #crossroads_to_serpent_holes.connect(serpent_holes)

    #crossroads_to_vulgrim_shop = Entrance(world.player, "The Crossroads to Vulgrim's Shop", parent = crossroads)
    #crossroads.exits.append(crossroads_to_vulgrim_shop)
    #crossroads_to_vulgrim_shop.connect(vulgrim_shop)

    #drowned_pass_to_anvil_ford_access_tunnel = Entrance(world.player, "Drowned Pass to Anvil's Ford Access Tunnel", parent = drowned_pass)
    #drowned_pass.exits.append(drowned_pass_to_anvil_ford_access_tunnel)
    #drowned_pass_to_anvil_ford_access_tunnel.connect(anvil_ford_access_tunnel)

    #drowned_pass_access_tunnel_to_drowned_pass = Entrance(world.player, "Drowned Pass Access Tunnel to Drowned Pass", parent = drowned_pass_access_tunnel)
    #drowned_pass_access_tunnel.exits.append(drowned_pass_access_tunnel_to_drowned_pass)
    #drowned_pass_access_tunnel_to_drowned_pass.connect(drowned_pass)

    #drowned_pass_access_tunnel_to_serpent_holes = Entrance(world.player, "Drowned Pass Access Tunnel to Serpent Holes", parent = drowned_pass_access_tunnel)
    #drowned_pass_access_tunnel.exits.append(drowned_pass_access_tunnel_to_serpent_holes)
    #drowned_pass_access_tunnel_to_serpent_holes.connect(serpent_holes)

    #drowned_pass_access_tunnel_to_vulgrim_shop = Entrance(world.player, "Drowned Pass Access Tunnel to Vulgrim's Shop", parent = drowned_pass_access_tunnel)
    #drowned_pass_access_tunnel.exits.append(drowned_pass_access_tunnel_to_vulgrim_shop)
    #drowned_pass_access_tunnel_to_vulgrim_shop.connect(vulgrim_shop)

    create_entrances_from_json(world, "Drowned Pass.json")

    #dry_road_to_ashlands_access_tunnel_1 = Entrance(world.player, "Dry Road to Ashlands Access Tunnel 1", parent = dry_road)
    #dry_road.exits.append(dry_road_to_ashlands_access_tunnel_1)
    #dry_road_to_ashlands_access_tunnel_1.connect(ashlands_access_tunnel_1)

    #dry_road_to_serpent_holes = Entrance(world.player, "Dry Road to Serpent Holes", parent = dry_road)
    #dry_road.exits.append(dry_road_to_serpent_holes)
    #dry_road_to_serpent_holes.connect(serpent_holes)

    #dry_road_to_vulgrim_shop = Entrance(world.player, "Dry Road to Vulgrim's Shop", parent = dry_road)
    #dry_road.exits.append(dry_road_to_vulgrim_shop)
    #dry_road_to_vulgrim_shop.connect(vulgrim_shop)

    #dry_road_access_tunnel_1_to_dry_road_access_tunnel_2 = Entrance(world.player, "Dry Road Access Tunnel 1 to Dry Road Access Tunnel 2", parent = dry_road_access_tunnel_1)
    #dry_road_access_tunnel_1.exits.append(dry_road_access_tunnel_1_to_dry_road_access_tunnel_2)
    #dry_road_access_tunnel_1_to_dry_road_access_tunnel_2.connect(dry_road_access_tunnel_2)

    #dry_road_access_tunnel_2_to_dry_road = Entrance(world.player, "Dry Road Access Tunnel 2 to Dry Road", parent = dry_road_access_tunnel_2)
    #dry_road_access_tunnel_2.exits.append(dry_road_access_tunnel_2_to_dry_road)
    #dry_road_access_tunnel_2_to_dry_road.connect(dry_road_access_tunnel_2)

    create_entrances_from_json(world, "Dry Road.json")

    eden_to_tree_of_knowledge = Entrance(world.player, "Eden to Three of Knowledge", parent = eden)
    eden.exits.append(eden_to_tree_of_knowledge)
    eden_to_tree_of_knowledge.connect(tree_of_knowledge)

    hollows_1_to_hollows_2 = Entrance(world.player, "The Hollows 1 to The Hollows 2", parent = hollows_1)
    hollows_1.exits.append(hollows_1_to_hollows_2)
    hollows_1_to_hollows_2.connect(hollows_2)

    hollows_1_to_hollows_5 = Entrance(world.player, "The Hollows 1 to The Hollows 5", parent = hollows_1)
    hollows_1.exits.append(hollows_1_to_hollows_5)
    hollows_1_to_hollows_5.connect(hollows_5)

    hollows_2_to_hollows_3 = Entrance(world.player, "The Hollows 2 to The Hollows 3", parent = hollows_2)
    hollows_2.exits.append(hollows_2_to_hollows_3)
    hollows_2_to_hollows_3.connect(hollows_3)

    hollows_3_to_hollows_4 = Entrance(world.player, "The Hollows 3 to The Hollows 4", parent = hollows_3)
    hollows_3.exits.append(hollows_3_to_hollows_4)
    hollows_3_to_hollows_4.connect(hollows_4)

    hollows_4_to_hollows_1 = Entrance(world.player, "The Hollows 4 to The Hollows 1", parent = hollows_4)
    hollows_4.exits.append(hollows_4_to_hollows_1)
    hollows_4_to_hollows_1.connect(hollows_1)

    hollows_5_to_hollows_6 = Entrance(world.player, "The Hollows 5 to The Hollows 6", parent = hollows_5)
    hollows_5.exits.append(hollows_5_to_hollows_6)
    hollows_5_to_hollows_6.connect(hollows_6)

    hollows_5_to_hollows_9 = Entrance(world.player, "The Hollows 5 to The Hollows 9", parent = hollows_5)
    hollows_5.exits.append(hollows_5_to_hollows_9)
    hollows_5_to_hollows_9.connect(hollows_9)

    hollows_6_to_hollows_7 = Entrance(world.player, "The Hollows 6 to The Hollows 7", parent = hollows_6)
    hollows_6.exits.append(hollows_6_to_hollows_7)
    hollows_6_to_hollows_7.connect(hollows_7)

    hollows_7_to_hollows_8 = Entrance(world.player, "The Hollows 7 to The Hollows 8", parent = hollows_7)
    hollows_7.exits.append(hollows_7_to_hollows_8)
    hollows_7_to_hollows_8.connect(hollows_8)

    hollows_9_to_hollows_10 = Entrance(world.player, "The Hollows 9 to The Hollows 10", parent = hollows_9)
    hollows_9.exits.append(hollows_9_to_hollows_10)
    hollows_9_to_hollows_10.connect(hollows_10)

    hollows_10_to_hollows_boss_room = Entrance(world.player, "The Hollows 10 to The Hollows Boss Room", parent = hollows_10)
    hollows_10.exits.append(hollows_10_to_hollows_boss_room)
    hollows_10_to_hollows_boss_room.connect(hollows_boss_room)

    iron_canopy_1_to_silitha_loom = Entrance(world.player, "Iron Canopy 1 to Silitha's Loom", parent = iron_canopy_1)
    iron_canopy_1.exits.append(iron_canopy_1_to_silitha_loom)
    iron_canopy_1_to_silitha_loom.connect(silitha_loom)

    hollows_access_tunnel_to_hollows_1 = Entrance(world.player, "The Hollows Access Tunnel to The Hollows 1", parent = hollows_access_tunnel)
    hollows_access_tunnel.exits.append(hollows_access_tunnel_to_hollows_1)
    hollows_access_tunnel_to_hollows_1.connect(hollows_1)

    leviathan_drift_to_eden = Entrance(world.player, "Leviathan's Drift to Eden", parent = leviathan_drift)
    leviathan_drift.exits.append(leviathan_drift_to_eden)
    leviathan_drift_to_eden.connect(eden)

    #library_to_scalding_gallow = Entrance(world.player, "The Crossroads to Scalding Gallow", parent = library)
    #library.exits.append(library_to_scalding_gallow)
    #library_to_scalding_gallow.connect(scalding_gallow)
    
    create_entrances_from_json(world, "Library.json")

    #menu_to_crossroads = Entrance(world.player, "Menu to The Crossroads", parent = menu)
    #menu.exits.append(menu_to_crossroads)
    #menu_to_crossroads.connect(crossroads)
    
    create_entrances_from_json(world, "Menu.json")

    #scalding_gallow_to_black_throne_1 = Entrance(world.player, "Scalding Gallow to Black Throne 1", parent = scalding_gallow)
    #scalding_gallow.exits.append(scalding_gallow_to_black_throne_1)
    #scalding_gallow_to_black_throne_1.connect(black_throne_1)

    #scalding_gallow_to_choking_grounds = Entrance(world.player, "Scalding Gallow to The Choking Grounds", parent = scalding_gallow)
    #scalding_gallow.exits.append(scalding_gallow_to_choking_grounds)
    #scalding_gallow_to_choking_grounds.connect(choking_grounds)

    #scalding_gallow_to_drowned_pass_access_tunnel = Entrance(world.player, "Scalding Gallow to Drowned Pass Access Tunnel", parent = scalding_gallow)
    #scalding_gallow.exits.append(scalding_gallow_to_drowned_pass_access_tunnel)
    #scalding_gallow_to_drowned_pass_access_tunnel.connect(drowned_pass_access_tunnel)

    #scalding_gallow_to_dry_road_access_tunnel_1 = Entrance(world.player, "Scalding Gallow to Dry Road Access Tunnel 1", parent = scalding_gallow)
    #scalding_gallow.exits.append(scalding_gallow_to_dry_road_access_tunnel_1)
    #scalding_gallow_to_dry_road_access_tunnel_1.connect(dry_road_access_tunnel_1)

    #scalding_gallow_to_iron_canopy_1 = Entrance(world.player, "Scalding Gallow to Iron Canopy 1", parent = scalding_gallow)
    #scalding_gallow.exits.append(scalding_gallow_to_iron_canopy_1)
    #scalding_gallow_to_iron_canopy_1.connect(iron_canopy_1)

    #scalding_gallow_to_serpent_holes = Entrance(world.player, "Scalding Gallow to Serpent Holes", parent = scalding_gallow)
    #scalding_gallow.exits.append(scalding_gallow_to_serpent_holes)
    #scalding_gallow_to_serpent_holes.connect(serpent_holes)

    #scalding_gallow_to_vulgrim_shop = Entrance(world.player, "Scalding Gallow to Vulgrim's Shop", parent = scalding_gallow)
    #scalding_gallow.exits.append(scalding_gallow_to_vulgrim_shop)
    #scalding_gallow_to_vulgrim_shop.connect(vulgrim_shop)
    
    create_entrances_from_json(world, "Scalding Gallow.json")

    #seraphim_hotel_to_crossroads = Entrance(world.player, "Seraphim Hotel to The Crossroads", parent = seraphim_hotel)
    #seraphim_hotel.exits.append(seraphim_hotel_to_crossroads)
    #seraphim_hotel_to_crossroads.connect(crossroads)

    #serpent_holes_to_ashlands_access_tunnel_1 = Entrance(world.player, "Serpent Holes to The Ashlands Access Tunnel 1", parent = serpent_holes)
    #serpent_holes.exits.append(serpent_holes_to_ashlands_access_tunnel_1)
    #serpent_holes_to_ashlands_access_tunnel_1.connect(ashlands_access_tunnel_1)

    #serpent_holes_to_broken_stairs = Entrance(world.player, "Serpent Holes to The Broken Stair", parent = serpent_holes)
    #serpent_holes.exits.append(serpent_holes_to_broken_stairs)
    #serpent_holes_to_broken_stairs.connect(broken_stair)

    #serpent_holes_to_choking_grounds = Entrance(world.player, "Serpent Holes to The Choking Grounds", parent = serpent_holes)
    #serpent_holes.exits.append(serpent_holes_to_choking_grounds)
    #serpent_holes_to_choking_grounds.connect(choking_grounds)

    #serpent_holes_to_crossroads = Entrance(world.player, "Serpent Holes to The Crossroads", parent = serpent_holes)
    #serpent_holes.exits.append(serpent_holes_to_crossroads)
    #serpent_holes_to_crossroads.connect(crossroads)

    #serpent_holes_to_drowned_pass = Entrance(world.player, "Serpent Holes to Drowned Pass", parent = serpent_holes)
    #serpent_holes.exits.append(serpent_holes_to_drowned_pass)
    #serpent_holes_to_drowned_pass.connect(drowned_pass)

    #serpent_holes_to_scalding_gallows = Entrance(world.player, "Serpent Holes to Scalding Gallow", parent = serpent_holes)
    #serpent_holes.exits.append(serpent_holes_to_scalding_gallows)
    #serpent_holes_to_scalding_gallows.connect(scalding_gallow)

    #serpent_holes_to_sh_to_anvil_ford = Entrance(world.player, "Serpent Holes to The Serpent Holes to Anvil's Ford", parent = serpent_holes)
    #serpent_holes.exits.append(serpent_holes_to_sh_to_anvil_ford)
    #serpent_holes_to_sh_to_anvil_ford.connect(sh_to_anvil_ford)

    #serpent_holes_to_sh_to_dry_road = Entrance(world.player, "Serpent Holes to The Serpent Holes to Dry Road", parent = serpent_holes)
    #serpent_holes.exits.append(serpent_holes_to_sh_to_dry_road)
    #serpent_holes_to_sh_to_dry_road.connect(sh_to_dry_road)

    #serpent_holes_to_sh_to_twilight_cathedral = Entrance(world.player, "Serpent Holes to The Serpent Holes to Twilight Cathedral", parent = serpent_holes)
    #serpent_holes.exits.append(serpent_holes_to_sh_to_twilight_cathedral)
    #serpent_holes_to_sh_to_twilight_cathedral.connect(sh_to_twilight_cathedral)

    #sh_to_anvil_ford_to_anvil_ford_access_tunnel = Entrance(world.player, "Serpent Holes to Anvil's Ford to Anvil's Ford Access Tunnel", parent = sh_to_anvil_ford)
    #sh_to_anvil_ford.exits.append(sh_to_anvil_ford_to_anvil_ford_access_tunnel)
    #sh_to_anvil_ford_to_anvil_ford_access_tunnel.connect(anvil_ford_access_tunnel)

    #sh_to_dry_road_to_dry_road = Entrance(world.player, "Serpent Holes to Dry Road to Dry Road", parent = sh_to_dry_road)
    #sh_to_dry_road.exits.append(sh_to_dry_road_to_dry_road)
    #sh_to_dry_road_to_dry_road.connect(dry_road)

    #sh_to_twilight_cathedral_to_twilight_cathedral_exterior = Entrance(world.player, "Serpent Holes to Twilight Cathedral to Twilight Cathedral Exterior", parent = sh_to_twilight_cathedral)
    #sh_to_twilight_cathedral.exits.append(sh_to_twilight_cathedral_to_twilight_cathedral_exterior)
    #sh_to_twilight_cathedral_to_twilight_cathedral_exterior.connect(twilight_cathedral_exterior)
    
    create_entrances_from_json(world, "Serpent Holes.json")

    #twilight_cathedral_exterior_to_serpent_hole = Entrance(world.player, "Twilight Cathedral Exterior to Serpent Hole", parent = twilight_cathedral_exterior)
    #twilight_cathedral_exterior.exits.append(twilight_cathedral_exterior_to_serpent_hole)
    #twilight_cathedral_exterior_to_serpent_hole.connect(serpent_holes)

    #twilight_cathedral_exterior_to_twilight_cathedral_1 = Entrance(world.player, "Twilight Cathedral Exterior to Twilight Cathedral 1", parent = twilight_cathedral_exterior)
    #twilight_cathedral_exterior.exits.append(twilight_cathedral_exterior_to_twilight_cathedral_1)
    #twilight_cathedral_exterior_to_twilight_cathedral_1.connect(twilight_cathedral_1)

    #twilight_cathedral_exterior_to_vulgrim_shop = Entrance(world.player, "Twilight Cathedral Exterior to Vulgrim's Shop", parent = twilight_cathedral_exterior)
    #twilight_cathedral_exterior.exits.append(twilight_cathedral_exterior_to_vulgrim_shop)
    #twilight_cathedral_exterior_to_vulgrim_shop.connect(vulgrim_shop)

    #twilight_cathedral_1_to_twilight_cathedral_2 = Entrance(world.player, "Twilight Cathedral 1 to Twilight Cathedral 2", parent = twilight_cathedral_1)
    #twilight_cathedral_1.exits.append(twilight_cathedral_1_to_twilight_cathedral_2)
    #twilight_cathedral_1_to_twilight_cathedral_2.connect(twilight_cathedral_2)

    #twilight_cathedral_2_to_twilight_cathedral_3 = Entrance(world.player, "Twilight Cathedral 2 to Twilight Cathedral 3", parent = twilight_cathedral_2)
    #twilight_cathedral_2.exits.append(twilight_cathedral_2_to_twilight_cathedral_3)
    #twilight_cathedral_2_to_twilight_cathedral_3.connect(twilight_cathedral_3)

    #twilight_cathedral_3_to_twilight_cathedral_boss_room = Entrance(world.player, "Twilight Cathedral 3 to Twilight Cathedral Exterior", parent = twilight_cathedral_3)
    #twilight_cathedral_3.exits.append(twilight_cathedral_3_to_twilight_cathedral_boss_room)
    #twilight_cathedral_3_to_twilight_cathedral_boss_room.connect(twilight_cathedral_boss_room)

    create_entrances_from_json(world, "Twilight Cathedral.json")

def create_entrances_from_json(world: DSWorld, filename) -> None:

    region_json = json_read(data_path(filename))

    for region in region_json:
        if 'entrances' in region:
            this_region = world.get_region(region.get("name"))
            for entrance_name, entrance_data in region.get("entrances").items():
                new_entrance = Entrance(world.player, entrance_name, this_region)
                this_region.exits.append(new_entrance)
                new_target = world.get_region(entrance_data.get("vanilla target"))
                new_entrance.connect(new_target)

def create_region_from_json(world: DSWorld, filename) -> None:

    region_json = json_read(data_path(filename))

    for region in region_json:
        new_region = Region(region["name"], world.player, world.multiworld)
        world.multiworld.regions += [new_region]