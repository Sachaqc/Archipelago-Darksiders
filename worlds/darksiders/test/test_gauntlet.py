from .bases import DSTestBase

class TestGauntletStart(DSTestBase):
    options = {
        "weapons": "start_with_gauntlet"
        }

    def test_gauntlet_start_with(self) -> None:
        tremor_gauntlet = self.get_items_by_name("Tremor Gauntlet")

        with self.subTest("Test that there are no Tremor Gauntlet in the pool"):
            self.assertEqual(len(tremor_gauntlet), 0)

        with self.subTest("Test that no Tremor Gauntlet is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Tremor Gauntlet"))

        with self.subTest("Test that the Tremor Gauntlet has been precollected"):
            item = self.world.create_item("Tremor Gauntlet")
            self.assertTrue(item in self.multiworld.precollected_items[1])

    def test_gauntlet_lvl_shuffled(self) -> None:
        gauntlet_lvl = self.get_items_by_name("Gauntlet Level Up")

        with self.subTest("Test that there are exactly 3 Gauntlet Level Up in the pool"):
            self.assertEqual(len(gauntlet_lvl), 3)

        with self.subTest("Test that no Gauntlet Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Tremor Gauntlet Level Up"))

class TestGauntlet(DSTestBase):
    options = {
        "weapons": "start_with_sword"
        }

    def test_tremor_gauntlet_shuffled(self) -> None:
        tremor_gauntlet = self.get_items_by_name("Tremor Gauntlet")

        with self.subTest("Test that there is exactly 1 Tremor Gauntlet in the pool"):
            self.assertEqual(len(tremor_gauntlet), 1)

        with self.subTest("Test that no Tremor Gauntlet is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Tremor Gauntlet"))

    def test_gauntlet_lvl_shuffled(self) -> None:
        gauntlet_lvl = self.get_items_by_name("Gauntlet Level Up")

        with self.subTest("Test that there are exactly 3 Gauntlet Level Up in the pool"):
            self.assertEqual(len(gauntlet_lvl), 3)

        with self.subTest("Test that no Gauntlet Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Tremor Gauntlet Level Up"))