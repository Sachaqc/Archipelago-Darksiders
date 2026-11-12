from ..Locations import SCYTHE_LOCATIONS
from .bases import DSTestBase

class TestStartScytheRemoved(DSTestBase):
    options = {
        "scythe": "remove",
        "weapons": "start_with_scythe"
        }

    def test_hellraiser_start_with(self) -> None:
        hellraiser = self.get_items_by_name("Hellraiser")

        with self.subTest("Test that there are no Hellraiser in the pool"):
            self.assertEqual(len(hellraiser), 0)

        with self.subTest("Test that no Hellraiser is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Hellraiser"))

        with self.subTest("Test that the Hellraiser has been precollected"):
            item = self.world.create_item("Hellraiser")
            self.assertTrue(item in self.multiworld.precollected_items[1])

    def test_harvester_absent(self) -> None:
        harvester = self.get_items_by_name("Harvester")

        with self.subTest("Test that there are no Harvester in the pool"):
            self.assertEqual(len(harvester), 0)

        with self.subTest("Test that no Harvester is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Harvester"))

        with self.subTest("Test that the Harvester has not been precollected"):
            item = self.world.create_item("Harvester")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_progressive_absent(self) -> None:
        progressive_scythes = self.get_items_by_name("Progressive Scythe")

        with self.subTest("Test that there are no Progressive Scythe in the pool"):
            self.assertEqual(len(progressive_scythes), 0)

        with self.subTest("Test that no Progressive Scythe is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Scythe"))

        with self.subTest("Test that no Progressive Scythe has been precollected"):
            item = self.world.create_item("Progressive Scythe")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_scythe_lvl_shuffled(self) -> None:
        scythe_lvl = self.get_items_by_name("Scythe Level Up")

        with self.subTest("Test that there are exactly 3 Scythe Level Up in the pool"):
            self.assertEqual(len(scythe_lvl), 3)

        with self.subTest("Test that no Scythe Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Scythe Level Up"))

class TestScytheRemoved(DSTestBase):
    options = {
        "scythe": "remove",
        "weapons": "start_with_sword"
        }

    def test_hellraiser_absent(self) -> None:
        hellraiser = self.get_items_by_name("Hellraiser")

        with self.subTest("Test that there are no Hellraiser in the pool"):
            self.assertEqual(len(hellraiser), 0)

        with self.subTest("Test that no Hellraiser is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Hellraiser"))

        with self.subTest("Test that the Hellraiser has not been precollected"):
            item = self.world.create_item("Hellraiser")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_harvester_absent(self) -> None:
        harvester = self.get_items_by_name("Harvester")

        with self.subTest("Test that there are no Harvester in the pool"):
            self.assertEqual(len(harvester), 0)

        with self.subTest("Test that no Harvester is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Harvester"))

        with self.subTest("Test that the Harvester has not been precollected"):
            item = self.world.create_item("Harvester")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_progressive_absent(self) -> None:
        progressive_scythes = self.get_items_by_name("Progressive Scythe")

        with self.subTest("Test that there are no Progressive Scythe in the pool"):
            self.assertEqual(len(progressive_scythes), 0)

        with self.subTest("Test that no Progressive Scythe is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Scythe"))

        with self.subTest("Test that no Progressive Scythe has been precollected"):
            item = self.world.create_item("Progressive Scythe")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_scythe_lvl_absent(self) -> None:
        scythe_lvl = self.get_items_by_name("Scythe Level Up")

        with self.subTest("Test that there are no Scythe Level Up in the pool"):
            self.assertEqual(len(scythe_lvl), 0)

        with self.subTest("Test that no Scythe Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Scythe Level Up"))

class TestStartScytheVanilla(DSTestBase):
    options = {
        "scythe": "vanilla",
        "weapons": "start_with_scythe"
        }

    def test_hellraiser_vanilla(self) -> None:
        hellraiser = self.get_items_by_name("Hellraiser")

        with self.subTest("Test that there are no Hellraiser in the pool"):
            self.assertEqual(len(hellraiser), 0)

        with self.subTest("Test that the Hellraiser is placed at its vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in SCYTHE_LOCATIONS and Location.item and Location.item.name == "Hellraiser"))
    
        with self.subTest("Test that no Hellraiser is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in SCYTHE_LOCATIONS and Location.item and Location.item.name == "Hellraiser"))

        with self.subTest("Test that the Hellraiser has not been precollected"):
            item = self.world.create_item("Hellraiser")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_harvester_vanilla(self) -> None:
        harvester = self.get_items_by_name("Harvester")

        with self.subTest("Test that there are no Harvester in the pool"):
            self.assertEqual(len(harvester), 0)

        with self.subTest("Test that the Harvester is placed at its vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in SCYTHE_LOCATIONS and Location.item and Location.item.name == "Harvester"))
    
        with self.subTest("Test that no Harvester is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in SCYTHE_LOCATIONS and Location.item and Location.item.name == "Harvester"))

        with self.subTest("Test that the Harvester has not been precollected"):
            item = self.world.create_item("Harvester")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_progressive_absent(self) -> None:
        progressive_scythes = self.get_items_by_name("Progressive Scythe")

        with self.subTest("Test that there are no Progressive Scythe in the pool"):
            self.assertEqual(len(progressive_scythes), 0)

        with self.subTest("Test that no Progressive Scythe is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Scythe"))

        with self.subTest("Test that no Progressive Scythe has been precollected"):
            item = self.world.create_item("Progressive Scythe")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_scythe_lvl_shuffled(self) -> None:
        scythe_lvl = self.get_items_by_name("Scythe Level Up")

        with self.subTest("Test that there are exactly 3 Scythe Level Up in the pool"):
            self.assertEqual(len(scythe_lvl), 3)

        with self.subTest("Test that no Scythe Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Scythe Level Up"))

class TestScytheVanilla(DSTestBase):
    options = {
        "scythe": "vanilla",
        "weapons": "start_with_sword"
        }

    def test_hellraiser_vanilla(self) -> None:
        hellraiser = self.get_items_by_name("Hellraiser")

        with self.subTest("Test that there are no Hellraiser in the pool"):
            self.assertEqual(len(hellraiser), 0)

        with self.subTest("Test that the Hellraiser is placed at its vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in SCYTHE_LOCATIONS and Location.item and Location.item.name == "Hellraiser"))
    
        with self.subTest("Test that no Hellraiser is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in SCYTHE_LOCATIONS and Location.item and Location.item.name == "Hellraiser"))

        with self.subTest("Test that the Hellraiser has not been precollected"):
            item = self.world.create_item("Hellraiser")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_harvester_vanilla(self) -> None:
        harvester = self.get_items_by_name("Harvester")

        with self.subTest("Test that there are no Harvester in the pool"):
            self.assertEqual(len(harvester), 0)

        with self.subTest("Test that the Harvester is placed at its vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in SCYTHE_LOCATIONS and Location.item and Location.item.name == "Harvester"))
    
        with self.subTest("Test that no Harvester is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in SCYTHE_LOCATIONS and Location.item and Location.item.name == "Harvester"))

        with self.subTest("Test that the Harvester has not been precollected"):
            item = self.world.create_item("Harvester")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_progressive_absent(self) -> None:
        progressive_scythes = self.get_items_by_name("Progressive Scythe")

        with self.subTest("Test that there are no Progressive Scythe in the pool"):
            self.assertEqual(len(progressive_scythes), 0)

        with self.subTest("Test that no Progressive Scythe is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Scythe"))

        with self.subTest("Test that no Progressive Scythe has been precollected"):
            item = self.world.create_item("Progressive Scythe")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_scythe_lvl_shuffled(self) -> None:
        scythe_lvl = self.get_items_by_name("Scythe Level Up")

        with self.subTest("Test that there are exactly 3 Scythe Level Up in the pool"):
            self.assertEqual(len(scythe_lvl), 3)

        with self.subTest("Test that no Scythe Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Scythe Level Up"))

class TestStartScytheHellraiser(DSTestBase):
    options = {
        "scythe": "hellraiser",
        "weapons": "start_with_scythe"
        }

    def test_hellraiser_start_with(self) -> None:
        hellraiser = self.get_items_by_name("Hellraiser")

        with self.subTest("Test that there are no Hellraiser in the pool"):
            self.assertEqual(len(hellraiser), 0)

        with self.subTest("Test that no Hellraiser is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Hellraiser"))

        with self.subTest("Test that the Hellraiser has been precollected"):
            item = self.world.create_item("Hellraiser")
            self.assertTrue(item in self.multiworld.precollected_items[1])

    def test_harvester_absent(self) -> None:
        harvester = self.get_items_by_name("Harvester")

        with self.subTest("Test that there are no Harvester in the pool"):
            self.assertEqual(len(harvester), 0)

        with self.subTest("Test that no Harvester is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Harvester"))

        with self.subTest("Test that the Harvester has not been precollected"):
            item = self.world.create_item("Harvester")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_progressive_absent(self) -> None:
        progressive_scythes = self.get_items_by_name("Progressive Scythe")

        with self.subTest("Test that there are no Progressive Scythe in the pool"):
            self.assertEqual(len(progressive_scythes), 0)

        with self.subTest("Test that no Progressive Scythe is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Scythe"))

        with self.subTest("Test that no Progressive Scythe has been precollected"):
            item = self.world.create_item("Progressive Scythe")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_scythe_lvl_shuffled(self) -> None:
        scythe_lvl = self.get_items_by_name("Scythe Level Up")

        with self.subTest("Test that there are exactly 3 Scythe Level Up in the pool"):
            self.assertEqual(len(scythe_lvl), 3)

        with self.subTest("Test that no Scythe Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Scythe Level Up"))

class TestScytheHellraiser(DSTestBase):
    options = {
        "scythe": "hellraiser",
        "weapons": "start_with_sword"
        }

    def test_hellraiser_shuffled(self) -> None:
        hellraiser = self.get_items_by_name("Hellraiser")

        with self.subTest("Test that there is exactly 1 Hellraiser in the pool"):
            self.assertEqual(len(hellraiser), 1)

        with self.subTest("Test that no Hellraiser is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Hellraiser"))

        with self.subTest("Test that the Hellraiser has not been precollected"):
            item = self.world.create_item("Hellraiser")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_harvester_absent(self) -> None:
        harvester = self.get_items_by_name("Harvester")

        with self.subTest("Test that there are no Harvester in the pool"):
            self.assertEqual(len(harvester), 0)

        with self.subTest("Test that no Harvester is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Harvester"))

        with self.subTest("Test that the Harvester has not been precollected"):
            item = self.world.create_item("Harvester")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_progressive_absent(self) -> None:
        progressive_scythes = self.get_items_by_name("Progressive Scythe")

        with self.subTest("Test that there are no Progressive Scythe in the pool"):
            self.assertEqual(len(progressive_scythes), 0)

        with self.subTest("Test that no Progressive Scythe is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Scythe"))

        with self.subTest("Test that no Progressive Scythe has been precollected"):
            item = self.world.create_item("Progressive Scythe")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_scythe_lvl_shuffled(self) -> None:
        scythe_lvl = self.get_items_by_name("Scythe Level Up")

        with self.subTest("Test that there are exactly 3 Scythe Level Up in the pool"):
            self.assertEqual(len(scythe_lvl), 3)

        with self.subTest("Test that no Scythe Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Scythe Level Up"))

class TestStartScytheHarvester(DSTestBase):
    options = {
        "scythe": "harvester",
        "weapons": "start_with_scythe"
        }

    def test_hellraiser_absent(self) -> None:
        hellraiser = self.get_items_by_name("Hellraiser")

        with self.subTest("Test that there are no Hellraiser in the pool"):
            self.assertEqual(len(hellraiser), 0)

        with self.subTest("Test that no Hellraiser is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Hellraiser"))

        with self.subTest("Test that the Hellraiser has not been precollected"):
            item = self.world.create_item("Hellraiser")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_harvester_start_with(self) -> None:
        harvester = self.get_items_by_name("Harvester")

        with self.subTest("Test that there are no Harvester in the pool"):
            self.assertEqual(len(harvester), 0)

        with self.subTest("Test that no Harvester is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Harvester"))

        with self.subTest("Test that the Harvester has been precollected"):
            item = self.world.create_item("Harvester")
            self.assertTrue(item in self.multiworld.precollected_items[1])

    def test_progressive_absent(self) -> None:
        progressive_scythes = self.get_items_by_name("Progressive Scythe")

        with self.subTest("Test that there are no Progressive Scythe in the pool"):
            self.assertEqual(len(progressive_scythes), 0)

        with self.subTest("Test that no Progressive Scythe is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Scythe"))

        with self.subTest("Test that no Progressive Scythe has been precollected"):
            item = self.world.create_item("Progressive Scythe")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_scythe_lvl_shuffled(self) -> None:
        scythe_lvl = self.get_items_by_name("Scythe Level Up")

        with self.subTest("Test that there are exactly 3 Scythe Level Up in the pool"):
            self.assertEqual(len(scythe_lvl), 3)

        with self.subTest("Test that no Scythe Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Scythe Level Up"))

class TestScytheHarvester(DSTestBase):
    options = {
        "scythe": "harvester",
        "weapons": "start_with_sword"
        }

    def test_hellraiser_absent(self) -> None:
        hellraiser = self.get_items_by_name("Hellraiser")

        with self.subTest("Test that there are no Hellraiser in the pool"):
            self.assertEqual(len(hellraiser), 0)

        with self.subTest("Test that no Hellraiser is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Hellraiser"))

        with self.subTest("Test that the Hellraiser has not been precollected"):
            item = self.world.create_item("Hellraiser")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_harvester_shuffled(self) -> None:
        harvester = self.get_items_by_name("Harvester")

        with self.subTest("Test that there is exactly 1 Harvester in the pool"):
            self.assertEqual(len(harvester), 1)

        with self.subTest("Test that no Harvester is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Harvester"))

        with self.subTest("Test that the Harvester has not been precollected"):
            item = self.world.create_item("Harvester")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_progressive_absent(self) -> None:
        progressive_scythes = self.get_items_by_name("Progressive Scythe")

        with self.subTest("Test that there are no Progressive Scythe in the pool"):
            self.assertEqual(len(progressive_scythes), 0)

        with self.subTest("Test that no Progressive Scythe is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Scythe"))

        with self.subTest("Test that no Progressive Scythe has been precollected"):
            item = self.world.create_item("Progressive Scythe")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_scythe_lvl_shuffled(self) -> None:
        scythe_lvl = self.get_items_by_name("Scythe Level Up")

        with self.subTest("Test that there are exactly 3 Scythe Level Up in the pool"):
            self.assertEqual(len(scythe_lvl), 3)

        with self.subTest("Test that no Scythe Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Scythe Level Up"))

class TestStartScytheProgressive(DSTestBase):
    options = {
        "scythe": "progressive", 
        "weapons": "start_with_scythe"
        }

    def test_hellraiser_absent(self) -> None:
        hellraiser = self.get_items_by_name("Hellraiser")

        with self.subTest("Test that there are no Hellraiser in the pool"):
            self.assertEqual(len(hellraiser), 0)

        with self.subTest("Test that no Hellraiser is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Hellraiser"))

        with self.subTest("Test that the Hellraiser has not been precollected"):
            item = self.world.create_item("Hellraiser")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_harvester_absent(self) -> None:
        harvester = self.get_items_by_name("Harvester")

        with self.subTest("Test that there are no Harvester in the pool"):
            self.assertEqual(len(harvester), 0)

        with self.subTest("Test that no Harvester is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Harvester"))

        with self.subTest("Test that the Harvester has not been precollected"):
            item = self.world.create_item("Harvester")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_progressive_start_with(self) -> None:
        progressive_scythes = self.get_items_by_name("Progressive Scythe")

        with self.subTest("Test that there is exactly 1 Progressive Scythe in the pool"):
            self.assertEqual(len(progressive_scythes), 1)

        with self.subTest("Test that no Progressive Scythe is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Scythe"))

        with self.subTest("Test that the Progressive Scythe has been precollected"):
            item = self.world.create_item("Progressive Scythe")
            self.assertTrue(item in self.multiworld.precollected_items[1])

    def test_scythe_lvl_shuffled(self) -> None:
        scythe_lvl = self.get_items_by_name("Scythe Level Up")

        with self.subTest("Test that there are exactly 3 Scythe Level Up in the pool"):
            self.assertEqual(len(scythe_lvl), 3)

        with self.subTest("Test that no Scythe Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Scythe Level Up"))

class TestScytheProgressive(DSTestBase):
    options = {
        "scythe": "progressive",
        "weapons": "start_with_sword"
        }

    def test_hellraiser_absent(self) -> None:
        hellraiser = self.get_items_by_name("Hellraiser")

        with self.subTest("Test that there are no Hellraiser in the pool"):
            self.assertEqual(len(hellraiser), 0)

        with self.subTest("Test that no Hellraiser is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Hellraiser"))

        with self.subTest("Test that the Hellraiser has not been precollected"):
            item = self.world.create_item("Hellraiser")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_harvester_absent(self) -> None:
        harvester = self.get_items_by_name("Harvester")

        with self.subTest("Test that there are no Harvester in the pool"):
            self.assertEqual(len(harvester), 0)

        with self.subTest("Test that no Harvester is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Harvester"))

        with self.subTest("Test that the Harvester has not been precollected"):
            item = self.world.create_item("Harvester")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_progressive_shuffled(self) -> None:
        progressive_scythes = self.get_items_by_name("Progressive Scythe")

        with self.subTest("Test that there are exactly 2 Progressive Scythe in the pool"):
            self.assertEqual(len(progressive_scythes), 2)

        with self.subTest("Test that no Progressive Scythe is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Scythe"))

        with self.subTest("Test that the Progressive Scythe has not been precollected"):
            item = self.world.create_item("Harvester")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_scythe_lvl_shuffled(self) -> None:
        scythe_lvl = self.get_items_by_name("Scythe Level Up")

        with self.subTest("Test that there are exactly 3 Scythe Level Up in the pool"):
            self.assertEqual(len(scythe_lvl), 3)

        with self.subTest("Test that no Scythe Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Scythe Level Up"))