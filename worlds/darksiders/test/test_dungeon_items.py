from ..Locations import DUNGEON_ITEMS_LOCATIONS, get_location_list_from_json
from .bases import DSTestBase

class TestDungeonItemsRemoved(DSTestBase):
    options = {
        "dungeon_items": "remove"
        }

    def test_hoardseeker_absent(self) -> None:
        self.absent_item("Hoardseeker")

    def test_map_absent(self) -> None:
        self.absent_item("Map")

class TestDungeonItemsVanilla(DSTestBase):
    options = {
        "dungeon_items": "vanilla"
        }

    def test_hoardseeker_vanilla(self) -> None:
        self.vanilla_item("Hoardseeker", DUNGEON_ITEMS_LOCATIONS)

    def test_map_vanilla(self) -> None:
        self.vanilla_item("Map", DUNGEON_ITEMS_LOCATIONS)

class TestDungeonItemsStart(DSTestBase):
    options = {
        "dungeon_items": "start_with"
        }

    def test_hoardseeker_start(self) -> None:
        self.start_with_item("Hoardseeker", start_count = 4, total_count = 4)

    def test_map_start(self) -> None:
        self.start_with_item("Map", start_count = 4, total_count = 4)

class TestDungeonItemsRegion(DSTestBase):
    options = {
        "dungeon_items": "region"
        }

    def test_hoardseeker_region(self) -> None:
        BLACK_THRONE_LOCATIONS = get_location_list_from_json(self.world, "Black Throne.json")
        HOLLOWS_LOCATIONS = get_location_list_from_json(self.world, "Hollows.json")
        IRON_CANOPY_LOCATIONS = get_location_list_from_json(self.world, "Iron Canopy.json")
        TWILIGHT_CATHEDRAL_LOCATIONS = get_location_list_from_json(self.world, "Twilight Cathedral.json")

        regions = [BLACK_THRONE_LOCATIONS, HOLLOWS_LOCATIONS, IRON_CANOPY_LOCATIONS, TWILIGHT_CATHEDRAL_LOCATIONS]
        counts = [1, 1, 1, 1]
        
        self.shuffled_item_regions("Hoardseeker", regions, counts)

    def test_map_region(self) -> None:
        BLACK_THRONE_LOCATIONS = get_location_list_from_json(self.world, "Black Throne.json")
        HOLLOWS_LOCATIONS = get_location_list_from_json(self.world, "Hollows.json")
        IRON_CANOPY_LOCATIONS = get_location_list_from_json(self.world, "Iron Canopy.json")
        TWILIGHT_CATHEDRAL_LOCATIONS = get_location_list_from_json(self.world, "Twilight Cathedral.json")

        regions = [BLACK_THRONE_LOCATIONS, HOLLOWS_LOCATIONS, IRON_CANOPY_LOCATIONS, TWILIGHT_CATHEDRAL_LOCATIONS]
        counts = [1, 1, 1, 1]
        
        self.shuffled_item_regions("Map", regions, counts)

class TestDungeonItemsSanity(DSTestBase):
    options = {
        "dungeon_items": "anywhere"
        }

    def test_hoardseeker_anywhere(self) -> None:
        self.shuffled_item("Hoardseeker", count = 4)

    def test_map_anywhere(self) -> None:
        self.shuffled_item("Map", count = 4)