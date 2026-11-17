from test.bases import WorldTestBase

from BaseClasses import Item, List, Location
from ..World import DSWorld

class DSTestBase(WorldTestBase):
    
    game = "Darksiders"
    world: DSWorld

    def _item_count_in_pool(self, item_list: List[Item], item_name: str, count: int) -> None:
        with self.subTest(f"Test that there are exactly {count} {item_name} in the pool"):
            self.assertEqual(len(item_list), count)

    def _item_not_in_pool(self, item_list: List[Item], item_name: str) -> None:
        with self.subTest(f"Test that there are no {item_name} in the pool"):
            self.assertEqual(len(item_list), 0)

    def _item_placed_count(self, item_name: str, count: int) -> None:
        with self.subTest(f"Test that there are exactly {count} {item_name} placed in the world"):
            self.assertEqual(len([Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == item_name]), count)

    def _item_placed_nowhere(self, item_name: str) -> None:
        with self.subTest(f"Test that no {item_name} is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == item_name))

    def _item_precollected(self, item_name: str) -> None:
        with self.subTest(f"Test that the {item_name} has been precollected"):
            item = self.world.create_item(item_name)
            self.assertTrue(item in self.multiworld.precollected_items[1])

    def _item_not_precollected(self, item_name: str) -> None:
        with self.subTest(f"Test that the {item_name} has been precollected"):
            item = self.world.create_item(item_name)
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def _item_in_region(self, item_name: str, region_locations: List[Location], count: int) -> None:
        with self.subTest(f"Test that exactly {count} {item_name} is placed in the specified region"):
            self.assertEqual(len([Location for Location in region_locations if Location.item and Location.item.name == item_name]), count)

    def _item_not_outside_vanilla(self, item_name: str, vanilla_locations: dict) -> None:
        with self.subTest(f"Test that no {item_name} is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in vanilla_locations and Location.item and Location.item.name == item_name))

    def _local_item(self, item_name: str) -> None:
        with self.subTest(f"Test that all {item_name} are part of the local item pool"):
            self.assertIn(item_name, self.multiworld.worlds[1].options.local_items)

    def _not_local_item(self, item_name: str) -> None:
        with self.subTest(f"Test that none {item_name} are part of the local item pool"):
            self.assertNotIn(item_name, self.multiworld.worlds[1].options.local_items)

    def _location_not_in_pool(self, item_name: str, vanilla_locations: dict) -> None:
        with self.subTest(f"Test that there are no {item_name} location in the pool"):
            for location in vanilla_locations :
                self.assertNotIn(location, self.multiworld.worlds[1].get_locations())

    def absent_item(self, item_name: str) -> None:
        item_list = self.get_items_by_name(item_name)

        self._item_not_in_pool(item_list, item_name)
        self._item_placed_nowhere(item_name)
        self._item_not_precollected(item_name)

    def shuffled_item(self, item_name: str, count: int = 1) -> None:
        item_list = self.get_items_by_name(item_name)

        self._item_count_in_pool(item_list, item_name, count)
        self._item_placed_nowhere(item_name)
        self._not_local_item(item_name)

    def shuffled_item_local(self, item_name: str, count: int = 1) -> None:
        item_list = self.get_items_by_name(item_name)

        self._item_count_in_pool(item_list, item_name, count)
        self._item_placed_nowhere(item_name)
        self._local_item(item_name)

    def shuffled_item_regions(self, item_name: str, regions: list[list[Location]], counts: list[int]) -> None:
        item_list = self.get_items_by_name(item_name)

        self._item_not_in_pool(item_list, item_name)
        for region, count in zip(regions, counts):
            self._item_in_region(item_name, region, count)
        self._item_placed_count(item_name, sum(counts))

    def start_with_item(self, item_name: str, start_count: int = 1, total_count: int = 1) -> None:
        item_list = self.get_items_by_name(item_name)

        if total_count > start_count:
            self._item_count_in_pool(item_list, item_name, total_count - start_count)
        else:
            self._item_not_in_pool(item_list, item_name)
        self._item_placed_nowhere(item_name)
        self._item_precollected(item_name)

    def vanilla_item(self, item_name: str, vanilla_locations: dict) -> None:
        item_list = self.get_items_by_name(item_name)

        self._item_not_in_pool(item_list, item_name)
        self._item_not_outside_vanilla(item_name, vanilla_locations)
        self._item_not_precollected(item_name)
        self._location_not_in_pool(item_name, vanilla_locations)