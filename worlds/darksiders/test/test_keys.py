from ..Locations import KEYS_LOCATIONS, get_location_list_from_json
from .bases import DSTestBase

class TestKeysRemoved(DSTestBase):
    options = {
        "keys": "remove"
        }

    def test_key_absent(self) -> None:
        self.absent_item("Beholder Key")

class TestKeysVanilla(DSTestBase):
    options = {
        "keys": "vanilla"
        }

    def test_key_vanilla(self) -> None:
        self.vanilla_item("Beholder Key", KEYS_LOCATIONS)

class TestKeysRegion(DSTestBase):
    options = {
        "keys": "region"
        }

    def test_key_region(self) -> None:
        BLACK_THRONE_LOCATIONS = get_location_list_from_json(self.world, "Black Throne.json")
        BROKEN_STAIRS_LOCATIONS = get_location_list_from_json(self.world, "Broken Stairs.json")
        HOLLOWS_LOCATIONS = get_location_list_from_json(self.world, "Hollows.json")
        IRON_CANOPY_LOCATIONS = get_location_list_from_json(self.world, "Iron Canopy.json")
        TWILIGHT_CATHEDRAL_LOCATIONS = get_location_list_from_json(self.world, "Twilight Cathedral.json")

        regions = [BLACK_THRONE_LOCATIONS, BROKEN_STAIRS_LOCATIONS, HOLLOWS_LOCATIONS, IRON_CANOPY_LOCATIONS, TWILIGHT_CATHEDRAL_LOCATIONS]
        counts = [2, 1, 3, 2, 2]

        self.shuffled_item_regions("Beholder Key", regions, counts)

class TestKeysSanity(DSTestBase):
    options = {
        "keys": "keysanity"
        }

    def test_key_anywhere(self) -> None:
        self.shuffled_item("Beholder Key", count = 10)