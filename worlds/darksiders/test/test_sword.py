from ..Locations import ARMAGEDDON_LOCATIONS
from .bases import DSTestBase

class TestStartSwordRemoved(DSTestBase):
    options = {
        "sword": "remove",
        "weapons": "start_with_sword",
        "armageddon":5
        }

    def test_armageddon_blade_precollected(self) -> None:
        armageddon_blade = self.get_items_by_name("Armageddon Blade")

        with self.subTest("Test that there are no Armageddon Blade in the pool"):
            self.assertEqual(len(armageddon_blade), 0)

        with self.subTest("Test that no Armageddon Blade is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater"))

        with self.subTest("Test that the Armageddon Blade has been precollected"):
            item = self.world.create_item("Armageddon Blade")
            self.assertTrue(item in self.multiworld.precollected_items[1])

    def test_armageddon_shards_absent(self) -> None:
        armageddon_shards = self.get_items_by_name("Armageddon Blade Shard")

        with self.subTest("Test that there are no Armageddon Blade Shards in the pool"):
            self.assertEqual(len(armageddon_shards), 0)

        with self.subTest("Test that no Armageddon Blade Shards are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Armageddon Blade Shard"))

    def test_chaoseater_absent(self) -> None:
        chaoseater = self.get_items_by_name("Chaoseater")

        with self.subTest("Test that there are no Chaoseater in the pool"):
            self.assertEqual(len(chaoseater), 0)

        with self.subTest("Test that no Chaoseater is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater"))

    def test_chaoseater_lvl_absent(self) -> None:
        chaoseater_lvl = self.get_items_by_name("Chaoseater Level Up")

        with self.subTest("Test that there are no Chaoseater Level Up in the pool"):
            self.assertEqual(len(chaoseater_lvl), 0)

        with self.subTest("Test that no Chaoseater Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater Level Up"))

    def test_progressive_sword_absent(self) -> None:
        progressive_sword = self.get_items_by_name("Progressive Sword")

        with self.subTest("Test that there are no Progressive Sword in the pool"):
            self.assertEqual(len(progressive_sword), 0)

        with self.subTest("Test that no Progressive Sword are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Sword"))

class TestSwordRemoved(DSTestBase):
    options = {
        "sword": "remove",
        "weapons": "start_with_scythe",
        "armageddon":5
        }

    def test_armageddon_blade_shuffled(self) -> None:
        armageddon_blade = self.get_items_by_name("Armageddon Blade")

        with self.subTest("Test that there is exactly 1 Armageddon Blade in the pool"):
            self.assertEqual(len(armageddon_blade), 1)

        with self.subTest("Test that no Armageddon Blade is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Armageddon Blade"))

    def test_armageddon_shards_absent(self) -> None:
        armageddon_shards = self.get_items_by_name("Armageddon Blade Shard")

        with self.subTest("Test that there are no Armageddon Blade Shards in the pool"):
            self.assertEqual(len(armageddon_shards), 0)

        with self.subTest("Test that no Armageddon Blade Shards are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Armageddon Blade Shard"))

    def test_chaoseater_absent(self) -> None:
        chaoseater = self.get_items_by_name("Chaoseater")

        with self.subTest("Test that there are no Chaoseater in the pool"):
            self.assertEqual(len(chaoseater), 0)

        with self.subTest("Test that no Chaoseater is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater"))

    def test_chaoseater_lvl_absent(self) -> None:
        chaoseater_lvl = self.get_items_by_name("Chaoseater Level Up")

        with self.subTest("Test that there are no Chaoseater Level Up in the pool"):
            self.assertEqual(len(chaoseater_lvl), 0)

        with self.subTest("Test that no Chaoseater Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater Level Up"))

    def test_progressive_sword_absent(self) -> None:
        progressive_sword = self.get_items_by_name("Progressive Sword")

        with self.subTest("Test that there are no Progressive Sword in the pool"):
            self.assertEqual(len(progressive_sword), 0)

        with self.subTest("Test that no Progressive Sword are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Sword"))

class TestStartSwordVanilla(DSTestBase):
    options = {
        "sword": "vanilla",
        "weapons": "start_with_sword",
        "armageddon":5
        }

    def test_armageddon_blade_vanilla(self) -> None:
        armageddon_blade = self.get_items_by_name("Armageddon Blade")

        with self.subTest("Test that there are no Armageddon Blade in the pool"):
            self.assertEqual(len(armageddon_blade), 0)

        with self.subTest("Test that the Armageddon Blade is placed at its vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in ARMAGEDDON_LOCATIONS and Location.item and Location.item.name == "Armageddon Blade"))
    
        with self.subTest("Test that no Armageddon Blade is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in ARMAGEDDON_LOCATIONS and Location.item and Location.item.name == "Armageddon Blade"))
    
        with self.subTest("Test that there is exactly 1 Armageddon Blade vanilla location"):
            BLADE_LOCATIONS = {location: item for location, item in ARMAGEDDON_LOCATIONS.items() if item == "Armageddon Blade"}
            self.assertEqual(len(BLADE_LOCATIONS), 1)

        with self.subTest("Test that the Armageddon Blade has not been precollected"):
            item = self.world.create_item("Armageddon Blade")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_armageddon_shards_vanilla(self) -> None:
        armageddon_shards = self.get_items_by_name("Armageddon Blade Shard")

        with self.subTest("Test that there are no Armageddon Blade Shards in the pool"):
            self.assertEqual(len(armageddon_shards), 0)

        with self.subTest("Test that the Armageddon Blade Shards are placed at their vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in ARMAGEDDON_LOCATIONS and Location.item and Location.item.name == "Armageddon Blade Shard"))
    
        with self.subTest("Test that no Armageddon Blade Shard is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in ARMAGEDDON_LOCATIONS and Location.item and Location.item.name == "Armageddon Blade Shard"))
    
        with self.subTest("Test that there are exactly 7 Armageddon Blade Shards vanilla location"):
            BLADE_LOCATIONS = {location: item for location, item in ARMAGEDDON_LOCATIONS.items() if item == "Armageddon Blade Shard"}
            self.assertEqual(len(BLADE_LOCATIONS), 7)

    def test_chaoseater_vanilla(self) -> None:
        chaoseaters = self.get_items_by_name("Chaoseater")

        with self.subTest("Test that there is no Chaoseater in the pool"):
            self.assertEqual(len(chaoseaters), 0)

        with self.subTest("Test that the Chaoseater has been precollected"):
            item = self.world.create_item("Chaoseater")
            self.assertTrue(item in self.multiworld.precollected_items[1])
    
        with self.subTest("Test that no Chaoseater is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater"))

    def test_chaoseater_lvl_shuffled(self) -> None:
        chaoseater_lvl = self.get_items_by_name("Chaoseater Level Up")

        with self.subTest("Test that there are exactly 3 Chaoseater Level Up in the pool"):
            self.assertEqual(len(chaoseater_lvl), 3)

        with self.subTest("Test that no Chaoseater Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater Level Up"))

    def test_progressive_sword_vanilla(self) -> None:
        progressive_swords = self.get_items_by_name("Progressive Sword")

        with self.subTest("Test that there are no Progressive Sword in the pool"):
            self.assertEqual(len(progressive_swords), 0)
    
        with self.subTest("Test that no Progressive Sword is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Sword"))

        with self.subTest("Test that no Progressive Sword has been precollected"):
            item = self.world.create_item("Progressive Sword")
            self.assertFalse(item in self.multiworld.precollected_items[1])

class TestSwordVanilla(DSTestBase):
    options = {
        "sword": "vanilla",
        "weapons": "start_with_scythe",
        "armageddon":5
        }

    def test_armageddon_blade_vanilla(self) -> None:
        armageddon_blade = self.get_items_by_name("Armageddon Blade")

        with self.subTest("Test that there are no Armageddon Blade in the pool"):
            self.assertEqual(len(armageddon_blade), 0)

        with self.subTest("Test that the Armageddon Blade is placed at its vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in ARMAGEDDON_LOCATIONS and Location.item and Location.item.name == "Armageddon Blade"))
    
        with self.subTest("Test that no Armageddon Blade is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in ARMAGEDDON_LOCATIONS and Location.item and Location.item.name == "Armageddon Blade"))
    
        with self.subTest("Test that there is exactly 1 Armageddon Blade vanilla location"):
            BLADE_LOCATIONS = {location: item for location, item in ARMAGEDDON_LOCATIONS.items() if item == "Armageddon Blade"}
            self.assertEqual(len(BLADE_LOCATIONS), 1)

        with self.subTest("Test that the Armageddon Blade has not been precollected"):
            item = self.world.create_item("Armageddon Blade")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_armageddon_shards_vanilla(self) -> None:
        armageddon_shards = self.get_items_by_name("Armageddon Blade Shard")

        with self.subTest("Test that there are no Armageddon Blade Shards in the pool"):
            self.assertEqual(len(armageddon_shards), 0)

        with self.subTest("Test that the Armageddon Blade Shards are placed at their vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in ARMAGEDDON_LOCATIONS and Location.item and Location.item.name == "Armageddon Blade Shard"))
    
        with self.subTest("Test that no Armageddon Blade Shard is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in ARMAGEDDON_LOCATIONS and Location.item and Location.item.name == "Armageddon Blade Shard"))
    
        with self.subTest("Test that there are exactly 7 Armageddon Blade Shards vanilla location"):
            BLADE_LOCATIONS = {location: item for location, item in ARMAGEDDON_LOCATIONS.items() if item == "Armageddon Blade Shard"}
            self.assertEqual(len(BLADE_LOCATIONS), 7)

    def test_chaoseater_vanilla(self) -> None:
        chaoseaters = self.get_items_by_name("Chaoseater")

        with self.subTest("Test that there is exactly 1 Chaoseater in the pool"):
            self.assertEqual(len(chaoseaters), 1)

        with self.subTest("Test that the Chaoseater has not been precollected"):
            item = self.world.create_item("Chaoseater")
            self.assertFalse(item in self.multiworld.precollected_items[1])
    
        with self.subTest("Test that no Chaoseater is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater"))

    def test_chaoseater_lvl_shuffled(self) -> None:
        chaoseater_lvl = self.get_items_by_name("Chaoseater Level Up")

        with self.subTest("Test that there are exactly 3 Chaoseater Level Up in the pool"):
            self.assertEqual(len(chaoseater_lvl), 3)

        with self.subTest("Test that no Chaoseater Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater Level Up"))

    def test_progressive_sword_vanilla(self) -> None:
        progressive_swords = self.get_items_by_name("Progressive Sword")

        with self.subTest("Test that there are no Progressive Sword in the pool"):
            self.assertEqual(len(progressive_swords), 0)
    
        with self.subTest("Test that no Progressive Sword is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Sword"))

        with self.subTest("Test that no Progressive Sword has been precollected"):
            item = self.world.create_item("Progressive Sword")
            self.assertFalse(item in self.multiworld.precollected_items[1])

class TestStartSwordShards(DSTestBase):
    options = {
        "sword": "shards",
        "weapons": "start_with_sword",
        "armageddon":5
        }

    def test_armageddon_blade_vanilla(self) -> None:
        armageddon_blade = self.get_items_by_name("Armageddon Blade")

        with self.subTest("Test that there are no Armageddon Blade in the pool"):
            self.assertEqual(len(armageddon_blade), 0)

        with self.subTest("Test that the Armageddon Blade is placed at its vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in ARMAGEDDON_LOCATIONS and Location.item and Location.item.name == "Armageddon Blade"))
    
        with self.subTest("Test that no Armageddon Blade is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in ARMAGEDDON_LOCATIONS and Location.item and Location.item.name == "Armageddon Blade"))
    
        with self.subTest("Test that there is exactly 1 Armageddon Blade vanilla location"):
            BLADE_LOCATIONS = {location: item for location, item in ARMAGEDDON_LOCATIONS.items() if item == "Armageddon Blade"}
            self.assertEqual(len(BLADE_LOCATIONS), 1)

        with self.subTest("Test that the Armageddon Blade has not been precollected"):
            item = self.world.create_item("Armageddon Blade")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_armageddon_shards_shuffled(self) -> None:
        armageddon_shards = self.get_items_by_name("Armageddon Blade Shard")

        with self.subTest("Test that the number of Armageddon Blade Shard in the pool is exactly as the Options expect"):
            self.assertEqual(len(armageddon_shards), 5)

    def test_chaoseater_vanilla(self) -> None:
        chaoseaters = self.get_items_by_name("Chaoseater")

        with self.subTest("Test that there is no Chaoseater in the pool"):
            self.assertEqual(len(chaoseaters), 0)

        with self.subTest("Test that the Chaoseater has been precollected"):
            item = self.world.create_item("Chaoseater")
            self.assertTrue(item in self.multiworld.precollected_items[1])
    
        with self.subTest("Test that no Chaoseater is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater"))

    def test_chaoseater_lvl_shuffled(self) -> None:
        chaoseater_lvl = self.get_items_by_name("Chaoseater Level Up")

        with self.subTest("Test that there are exactly 3 Chaoseater Level Up in the pool"):
            self.assertEqual(len(chaoseater_lvl), 3)

        with self.subTest("Test that no Chaoseater Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater Level Up"))

    def test_progressive_sword_vanilla(self) -> None:
        progressive_swords = self.get_items_by_name("Progressive Sword")

        with self.subTest("Test that there are no Progressive Sword in the pool"):
            self.assertEqual(len(progressive_swords), 0)
    
        with self.subTest("Test that no Progressive Sword is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Sword"))

        with self.subTest("Test that no Progressive Sword has been precollected"):
            item = self.world.create_item("Progressive Sword")
            self.assertFalse(item in self.multiworld.precollected_items[1])

class TestSwordShards(DSTestBase):
    options = {
        "sword": "shards",
        "weapons": "start_with_scythe",
        "armageddon":5
        }

    def test_armageddon_blade_vanilla(self) -> None:
        armageddon_blade = self.get_items_by_name("Armageddon Blade")

        with self.subTest("Test that there are no Armageddon Blade in the pool"):
            self.assertEqual(len(armageddon_blade), 0)

        with self.subTest("Test that the Armageddon Blade is placed at its vanilla location"):
            self.assertTrue(all(Location for Location in self.multiworld.get_locations() if Location.name in ARMAGEDDON_LOCATIONS and Location.item and Location.item.name == "Armageddon Blade"))
    
        with self.subTest("Test that no Armageddon Blade is placed outside its vanilla location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.name not in ARMAGEDDON_LOCATIONS and Location.item and Location.item.name == "Armageddon Blade"))
    
        with self.subTest("Test that there is exactly 1 Armageddon Blade vanilla location"):
            BLADE_LOCATIONS = {location: item for location, item in ARMAGEDDON_LOCATIONS.items() if item == "Armageddon Blade"}
            self.assertEqual(len(BLADE_LOCATIONS), 1)

        with self.subTest("Test that the Armageddon Blade has not been precollected"):
            item = self.world.create_item("Armageddon Blade")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_armageddon_shards_shuffled(self) -> None:
        armageddon_shards = self.get_items_by_name("Armageddon Blade Shard")

        with self.subTest("Test that the number of Armageddon Blade Shard in the pool is exactly as the Options expect"):
            self.assertEqual(len(armageddon_shards), 5)

    def test_chaoseater_shuffled(self) -> None:
        chaoseaters = self.get_items_by_name("Chaoseater")

        with self.subTest("Test that there is exactly 1 Chaoseater in the pool"):
            self.assertEqual(len(chaoseaters), 1)

        with self.subTest("Test that the Chaoseater has not been precollected"):
            item = self.world.create_item("Chaoseater")
            self.assertFalse(item in self.multiworld.precollected_items[1])

    def test_chaoseater_lvl_shuffled(self) -> None:
        chaoseater_lvl = self.get_items_by_name("Chaoseater Level Up")

        with self.subTest("Test that there are exactly 3 Chaoseater Level Up in the pool"):
            self.assertEqual(len(chaoseater_lvl), 3)

        with self.subTest("Test that no Chaoseater Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater Level Up"))

    def test_progressive_sword_vanilla(self) -> None:
        progressive_swords = self.get_items_by_name("Progressive Sword")

        with self.subTest("Test that there are no Progressive Sword in the pool"):
            self.assertEqual(len(progressive_swords), 0)
    
        with self.subTest("Test that no Progressive Sword is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Progressive Sword"))

        with self.subTest("Test that no Progressive Sword has been precollected"):
            item = self.world.create_item("Progressive Sword")
            self.assertFalse(item in self.multiworld.precollected_items[1])

class TestStartSwordProgressive(DSTestBase):
    options = {
        "sword": "progressive",
        "weapons": "start_with_sword",
        "armageddon":5
        }

    def test_armageddon_blade_absent(self) -> None:
        armageddon_blade = self.get_items_by_name("Armageddon Blade")

        with self.subTest("Test that there are no Armageddon Blade in the pool"):
            self.assertEqual(len(armageddon_blade), 0)

        with self.subTest("Test that no Armageddon Blade is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Armageddon Blade"))

    def test_armageddon_shards_absent(self) -> None:
        armageddon_shards = self.get_items_by_name("Armageddon Blade Shard")

        with self.subTest("Test that there are no Armageddon Blade Shards in the pool"):
            self.assertEqual(len(armageddon_shards), 0)

        with self.subTest("Test that no Armageddon Blade Shards are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Armageddon Blade Shard"))

    def test_chaoseater_absent(self) -> None:
        chaoseater = self.get_items_by_name("Chaoseater")

        with self.subTest("Test that there are no Chaoseater in the pool"):
            self.assertEqual(len(chaoseater), 0)

        with self.subTest("Test that no Chaoseater is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater"))

    def test_chaoseater_lvl_shuffled(self) -> None:
        chaoseater_lvl = self.get_items_by_name("Chaoseater Level Up")

        with self.subTest("Test that there are exactly 3 Chaoseater Level Up in the pool"):
            self.assertEqual(len(chaoseater_lvl), 3)

        with self.subTest("Test that no Chaoseater Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater Level Up"))

    def test_progressive_sword_shuffled(self) -> None:
        progressive_sword = self.get_items_by_name("Progressive Sword")

        with self.subTest("Test that the number of Progressive Sword in the pool is exactly as the Options expect"):
            self.assertEqual(len(progressive_sword), 1)

class TestSwordProgressive(DSTestBase):
    options = {
        "sword": "progressive",
        "weapons": "start_with_scythe",
        "armageddon":5
        }

    def test_armageddon_blade_absent(self) -> None:
        armageddon_blade = self.get_items_by_name("Armageddon Blade")

        with self.subTest("Test that there are no Armageddon Blade in the pool"):
            self.assertEqual(len(armageddon_blade), 0)

        with self.subTest("Test that no Armageddon Blade is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater"))

    def test_armageddon_shards_absent(self) -> None:
        armageddon_shards = self.get_items_by_name("Armageddon Blade Shard")

        with self.subTest("Test that there are no Armageddon Blade Shards in the pool"):
            self.assertEqual(len(armageddon_shards), 0)

        with self.subTest("Test that no Armageddon Blade Shards are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Armageddon Blade Shard"))

    def test_chaoseater_absent(self) -> None:
        chaoseater = self.get_items_by_name("Chaoseater")

        with self.subTest("Test that there are no Chaoseater in the pool"):
            self.assertEqual(len(chaoseater), 0)

        with self.subTest("Test that no Chaoseater is placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater"))

    def test_chaoseater_lvl_shuffled(self) -> None:
        chaoseater_lvl = self.get_items_by_name("Chaoseater Level Up")

        with self.subTest("Test that there are exactly 3 Chaoseater Level Up in the pool"):
            self.assertEqual(len(chaoseater_lvl), 3)

        with self.subTest("Test that no Chaoseater Level Up are placed at any location"):
            self.assertFalse(any(Location for Location in self.multiworld.get_locations() if Location.item and Location.item.name == "Chaoseater Level Up"))

    def test_progressive_sword_shuffled(self) -> None:
        progressive_sword = self.get_items_by_name("Progressive Sword")

        with self.subTest("Test that the number of Progressive Sword in the pool is exactly as the Options expect"):
            self.assertEqual(len(progressive_sword), 2)