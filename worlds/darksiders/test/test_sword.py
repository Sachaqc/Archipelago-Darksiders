from ..Locations import ARMAGEDDON_LOCATIONS
from .bases import DSTestBase

class TestStartSwordRemoved(DSTestBase):
    options = {
        "sword": "remove",
        "weapons": "start_with_sword",
        "armageddon":5
        }

    def test_armageddon_blade_precollected(self) -> None:
        self.start_with_item("Armageddon Blade")

    def test_armageddon_shards_absent(self) -> None:
        self.absent_item("Armageddon Blade Shard")

    def test_chaoseater_absent(self) -> None:
        self.absent_item("Chaoseater")

    def test_chaoseater_lvl_absent(self) -> None:
        self.absent_item("Chaoseater Level Up")

    def test_progressive_sword_absent(self) -> None:
        self.absent_item("Progressive Sword")

class TestSwordRemoved(DSTestBase):
    options = {
        "sword": "remove",
        "weapons": "start_with_scythe",
        "armageddon":5
        }

    def test_armageddon_blade_shuffled(self) -> None:
        self.shuffled_item("Armageddon Blade")

    def test_armageddon_shards_absent(self) -> None:
        self.absent_item("Armageddon Blade Shard")

    def test_chaoseater_absent(self) -> None:
        self.absent_item("Chaoseater")

    def test_chaoseater_lvl_absent(self) -> None:
        self.absent_item("Chaoseater Level Up")

    def test_progressive_sword_absent(self) -> None:
        self.absent_item("Progressive Sword")

class TestStartSwordVanilla(DSTestBase):
    options = {
        "sword": "vanilla",
        "weapons": "start_with_sword",
        "armageddon":5
        }

    def test_armageddon_blade_vanilla(self) -> None:
        self.vanilla_item("Armageddon Blade", ARMAGEDDON_LOCATIONS)

    def test_armageddon_shards_vanilla(self) -> None:
        self.vanilla_item("Armageddon Blade Shard", ARMAGEDDON_LOCATIONS, count = 7)

    def test_chaoseater_vanilla(self) -> None:
        self.start_with_item("Chaoseater")

    def test_chaoseater_lvl_shuffled(self) -> None:
        self.shuffled_item("Chaoseater Level Up", count = 3)

    def test_progressive_sword_vanilla(self) -> None:
        self.absent_item("Progressive Sword")

class TestSwordVanilla(DSTestBase):
    options = {
        "sword": "vanilla",
        "weapons": "start_with_scythe",
        "armageddon":5
        }

    def test_armageddon_blade_vanilla(self) -> None:
        self.vanilla_item("Armageddon Blade", ARMAGEDDON_LOCATIONS)

    def test_armageddon_shards_vanilla(self) -> None:
        self.vanilla_item("Armageddon Blade Shard", ARMAGEDDON_LOCATIONS, count = 7)

    def test_chaoseater_shuffled(self) -> None:
        self.shuffled_item("Chaoseater")

    def test_chaoseater_lvl_shuffled(self) -> None:
        self.shuffled_item("Chaoseater Level Up", count = 3) 

    def test_progressive_sword_absent(self) -> None:
        self.absent_item("Progressive Sword")

class TestStartSwordShards(DSTestBase):
    options = {
        "sword": "shards",
        "weapons": "start_with_sword",
        "armageddon":5
        }

    def test_armageddon_blade_vanilla(self) -> None:
        self.vanilla_item("Armageddon Blade", ARMAGEDDON_LOCATIONS)

    def test_armageddon_shards_shuffled(self) -> None:
        self.shuffled_item("Armageddon Blade Shard", count = 5)

    def test_chaoseater_start_with(self) -> None:
        self.start_with_item("Chaoseater")

    def test_chaoseater_lvl_shuffled(self) -> None:
        self.shuffled_item("Chaoseater Level Up", count = 3) 

    def test_progressive_sword_absent(self) -> None:
        self.absent_item("Progressive Sword")

class TestSwordShards(DSTestBase):
    options = {
        "sword": "shards",
        "weapons": "start_with_scythe",
        "armageddon":5
        }

    def test_armageddon_blade_vanilla(self) -> None:
        self.vanilla_item("Armageddon Blade", ARMAGEDDON_LOCATIONS)

    def test_armageddon_shards_shuffled(self) -> None:
        self.shuffled_item("Armageddon Blade Shard", count = 5)

    def test_chaoseater_shuffled(self) -> None:
        self.shuffled_item("Chaoseater")

    def test_chaoseater_lvl_shuffled(self) -> None:
        self.shuffled_item("Chaoseater Level Up", count = 3) 

    def test_progressive_sword_absent(self) -> None:
        self.absent_item("Progressive Sword")

class TestStartSwordProgressive(DSTestBase):
    options = {
        "sword": "progressive",
        "weapons": "start_with_sword",
        "armageddon":5
        }

    def test_armageddon_blade_absent(self) -> None:
        self.absent_item("Armageddon Blade")

    def test_armageddon_shards_absent(self) -> None:
        self.absent_item("Armageddon Blade Shard")

    def test_chaoseater_absent(self) -> None:
        self.absent_item("Chaoseater")

    def test_chaoseater_lvl_shuffled(self) -> None:
        self.shuffled_item("Chaoseater Level Up", count = 3) 

    def test_progressive_sword_shuffled(self) -> None:
        self.shuffled_item("Progressive Sword", count = 1)

class TestSwordProgressive(DSTestBase):
    options = {
        "sword": "progressive",
        "weapons": "start_with_scythe",
        "armageddon":5
        }

    def test_armageddon_blade_absent(self) -> None:
        self.absent_item("Armageddon Blade")

    def test_armageddon_shards_absent(self) -> None:
        self.absent_item("Armageddon Blade Shard")

    def test_chaoseater_absent(self) -> None:
        self.absent_item("Chaoseater")

    def test_chaoseater_lvl_shuffled(self) -> None:
        self.shuffled_item("Chaoseater Level Up", count = 3) 

    def test_progressive_sword_shuffled(self) -> None:
        self.shuffled_item("Progressive Sword", count = 2)