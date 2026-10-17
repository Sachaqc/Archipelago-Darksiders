from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .World import DSWorld

def create_and_connect_regions(world: DSWorld) -> None:

    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: DSWorld) -> None:

    anvil_ford = Region("Anvil's Ford", world.player, world.multiworld)
    ashlands = Region("The Ashlands", world.player, world.multiworld)
    black_throne = Region("Black Throne", world.player, world.multiworld)
    broken_stair = Region("The Broken Stair", world.player, world.multiworld)
    choking_grounds = Region("The Choking Grounds", world.player, world.multiworld)
    crossroads = Region("The Crossroads", world.player, world.multiworld)
    destroyed_city = Region("The Destroyed City", world.player, world.multiworld)
    drowned_pass = Region("Drowned Pass", world.player, world.multiworld)
    dry_road = Region("The Dry Road", world.player, world.multiworld)
    earth = Region("Earth", world.player, world.multiworld)
    eden = Region("Eden", world.player, world.multiworld)
    heaven = Region("Heaven", world.player, world.multiworld)
    hell = Region("Hell", world.player, world.multiworld)
    hollows = Region("The Hollows", world.player, world.multiworld)
    iron_canopy = Region("Iron Canopy", world.player, world.multiworld)
    leviathan_drift = Region("Leviathan's Drift", world.player, world.multiworld)
    scalding_gallow = Region("Scalding Gallow", world.player, world.multiworld)
    seraphim_hotel = Region("Seraphim Hotel", world.player, world.multiworld)
    shadow_realm = Region("Shadow Realm", world.player, world.multiworld)
    silitha_loom = Region("Silitha's Loom", world.player, world.multiworld)
    soul_bridge = Region("Soul Bridge", world.player, world.multiworld)
    three_kingdoms = Region("Three Kingdoms", world.player, world.multiworld)
    tree_of_knowledge = Region("Tree of Knowledge", world.player, world.multiworld)
    twilight_cathedral_exterior = Region("Twilight Cathedral Exterior", world.player, world.multiworld)
    twilight_cathedral_1 = Region("Twilight Cathedral 1", world.player, world.multiworld) #Before first beholder key
    twilight_cathedral_2 = Region("Twilight Cathedral 2", world.player, world.multiworld) #After first beholder key
    twilight_cathedral_3 = Region("Twilight Cathedral 3", world.player, world.multiworld) #After Crossblade
    well_of_souls = Region("Well of Souls", world.player, world.multiworld)

    regions = [
        anvil_ford,
        ashlands,
        black_throne,
        broken_stair,
        choking_grounds,
        crossroads,
        destroyed_city,
        drowned_pass,
        dry_road,
        earth,
        eden,
        heaven,
        hell,
        hollows,
        iron_canopy,
        leviathan_drift,
        scalding_gallow,
        seraphim_hotel,
        shadow_realm,
        silitha_loom,
        soul_bridge,
        three_kingdoms,
        tree_of_knowledge,
        twilight_cathedral_exterior,
        twilight_cathedral_1,
        twilight_cathedral_2,
        twilight_cathedral_3,
        well_of_souls
    ]

    world.multiworld.regions += regions

def connect_regions(world: DSWorld) -> None:

    anvil_ford = world.get_region("Anvil's Ford")
    ashlands = world.get_region("The Ashlands")
    black_throne = world.get_region("Black Throne")
    broken_stair = world.get_region("The Broken Stair")
    choking_grounds = world.get_region("The Choking Grounds")
    crossroads = world.get_region("The Crossroads")
    destroyed_city = world.get_region("The Destroyed City")
    drowned_pass = world.get_region("Drowned Pass")
    dry_road = world.get_region("The Dry Road")
    earth = world.get_region("Earth")
    eden = world.get_region("Eden")
    heaven = world.get_region("Heaven")
    hell = world.get_region("Hell")
    hollows = world.get_region("The Hollows")
    iron_canopy = world.get_region("Iron Canopy")
    leviathan_drift = world.get_region("Leviathan's Drift")
    menu = world.get_region("Menu")
    scalding_gallow = world.get_region("Scalding Gallow")
    seraphim_hotel = world.get_region("Seraphim Hotel")
    shadow_realm = world.get_region("Shadow Realm")
    silitha_loom = world.get_region("Silitha's Loom")
    soul_bridge = world.get_region("Soul Bridge")
    broken_stair = world.get_region("The Broken Stair")
    crossroads = world.get_region("The Crossroads")
    three_kingdoms = world.get_region("Three Kingdoms")
    tree_of_knowledge = world.get_region("Tree of Knowledge")
    twilight_cathedral_exterior = world.get_region("Twilight Cathedral Exterior")
    twilight_cathedral_1 = world.get_region("Twilight Cathedral 1")
    twilight_cathedral_2 = world.get_region("Twilight Cathedral 2")
    twilight_cathedral_3 = world.get_region("Twilight Cathedral 3")
    well_of_souls = world.get_region("Well of Souls")

    broken_stair_to_twilight_cathedral_1 = Entrance(world.player, "The Broken Stair to Twilight Cathedral 1", parent=broken_stair)
    broken_stair.exits.append(broken_stair_to_twilight_cathedral_1)
    broken_stair_to_twilight_cathedral_1.connect(twilight_cathedral_1)

    choking_grounds_to_broken_stair = Entrance(world.player, "The Choking Grounds to The Broken Stair", parent=choking_grounds)
    choking_grounds.exits.append(choking_grounds_to_broken_stair)
    choking_grounds_to_broken_stair.connect(broken_stair)

    crossroads_to_scalding_gallow = Entrance(world.player, "The Crossroads to Scalding Gallow", parent=crossroads)
    crossroads.exits.append(crossroads_to_scalding_gallow)
    crossroads_to_scalding_gallow.connect(scalding_gallow)

    menu_to_crossroads = Entrance(world.player, "Menu to The Crossroads", parent=menu)
    menu.exits.append(menu_to_crossroads)
    menu_to_crossroads.connect(crossroads)

    scalding_gallow_to_choking_grounds = Entrance(world.player, "Scalding Gallow to The Choking Grounds", parent=scalding_gallow)
    scalding_gallow.exits.append(scalding_gallow_to_choking_grounds)
    scalding_gallow_to_choking_grounds.connect(choking_grounds)

    seraphim_hotel_to_crossroads = Entrance(world.player, "Seraphim Hotel to The Crossroads", parent=seraphim_hotel)
    seraphim_hotel.exits.append(seraphim_hotel_to_crossroads)
    seraphim_hotel_to_crossroads.connect(crossroads)

    twilight_cathedral_exterior_to_twilight_cathedral_1 = Entrance(world.player, "Twilight Cathedral Exterior to Twilight Cathedral 1", parent=twilight_cathedral_exterior)
    twilight_cathedral_exterior.exits.append(twilight_cathedral_exterior_to_twilight_cathedral_1)
    twilight_cathedral_exterior_to_twilight_cathedral_1.connect(twilight_cathedral_1)

    twilight_cathedral_1_to_twilight_cathedral_2 = Entrance(world.player, "Twilight Cathedral 1 to Twilight Cathedral 2", parent=twilight_cathedral_1)
    twilight_cathedral_1.exits.append(twilight_cathedral_1_to_twilight_cathedral_2)
    twilight_cathedral_1_to_twilight_cathedral_2.connect(twilight_cathedral_2)

    twilight_cathedral_2_to_twilight_cathedral_3 = Entrance(world.player, "Twilight Cathedral 2 to Twilight Cathedral 3", parent=twilight_cathedral_1)
    twilight_cathedral_2.exits.append(twilight_cathedral_2_to_twilight_cathedral_3)
    twilight_cathedral_2_to_twilight_cathedral_3.connect(twilight_cathedral_3)
