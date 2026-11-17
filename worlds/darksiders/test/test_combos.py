from ..Locations import MOVES_LOCATIONS
from .bases import DSTestBase

class TestComboRemoved(DSTestBase):
    options = {
        "moves": "remove"
        }

    def test_sword_combos_absent(self) -> None:
        self.absent_item("180 Orbit Slash")
        self.absent_item("Demon Edge")
        self.absent_item("Devil's Cross")
        self.absent_item("Flipsaw")
        self.absent_item("Harpoon Tackle")
        self.absent_item("Meteor Strike")
        self.absent_item("Power Strike")
        self.absent_item("Sword Uppercut")
        self.absent_item("Whirl Wind Combo")

    def test_scythe_combos_absent(self) -> None:
        self.absent_item("Air Reaper Blade")
        self.absent_item("Death's Rage")
        self.absent_item("Hell Razor")
        self.absent_item("Reaper Blade")
        self.absent_item("Reaper's Revenge")

    def test_gauntlet_combos_absent(self) -> None:
        self.absent_item("Air Tremor Smash")
        self.absent_item("Earthbreaker")
        self.absent_item("Meteor Launch")
        self.absent_item("Tremor Punch")
        self.absent_item("Tremor Smash")

class TestComboVanilla(DSTestBase):
    options = {
        "moves": "vanilla"
        }

    def test_sword_combos_vanilla(self) -> None:
        self.vanilla_item("180 Orbit Slash", MOVES_LOCATIONS)
        self.vanilla_item("Demon Edge",MOVES_LOCATIONS)
        self.vanilla_item("Devil's Cross", MOVES_LOCATIONS)#War starts with this move's level 1 unlocked by default
        self.vanilla_item("Flipsaw", MOVES_LOCATIONS)
        self.vanilla_item("Harpoon Tackle", MOVES_LOCATIONS)
        self.vanilla_item("Meteor Strike", MOVES_LOCATIONS)
        self.vanilla_item("Power Strike", MOVES_LOCATIONS)
        self.vanilla_item("Sword Uppercut", MOVES_LOCATIONS)#War starts with this move's level 1 unlocked by default
        self.vanilla_item("Whirl Wind Combo", MOVES_LOCATIONS)

    def test_scythe_combos_vanilla(self) -> None:
        self.vanilla_item("Air Reaper Blade", MOVES_LOCATIONS)
        self.vanilla_item("Death's Rage", MOVES_LOCATIONS)
        self.vanilla_item("Hell Razor", MOVES_LOCATIONS)
        self.vanilla_item("Reaper Blade", MOVES_LOCATIONS)
        self.vanilla_item("Reaper's Revenge", MOVES_LOCATIONS)

    def test_gauntlet_combos_vanilla(self) -> None:
        self.vanilla_item("Air Tremor Smash", MOVES_LOCATIONS)
        self.vanilla_item("Earthbreaker", MOVES_LOCATIONS)
        self.vanilla_item("Meteor Launch", MOVES_LOCATIONS)
        self.vanilla_item("Tremor Punch", MOVES_LOCATIONS)
        self.vanilla_item("Tremor Smash", MOVES_LOCATIONS)#War starts with this move's level 1 unlocked by default

class TestComboAnywhere(DSTestBase):
    options = {
        "moves": "combosanity"
        }

    def test_sword_combos_shuffled(self) -> None:
        self.shuffled_item("180 Orbit Slash", count = 1)
        self.shuffled_item("Demon Edge", count = 3)
        self.shuffled_item("Devil's Cross", count = 2)#War starts with this move's level 1 unlocked by default
        self.shuffled_item("Flipsaw", count = 3)
        self.shuffled_item("Harpoon Tackle", count = 3)
        self.shuffled_item("Meteor Strike", count = 1)
        self.shuffled_item("Power Strike", count = 3)
        self.shuffled_item("Sword Uppercut", count = 2)#War starts with this move's level 1 unlocked by default
        self.shuffled_item("Whirl Wind Combo", count = 1)

    def test_scythe_combos_shuffled(self) -> None:
        self.shuffled_item("Air Reaper Blade", count = 3)
        self.shuffled_item("Death's Rage", count = 1)
        self.shuffled_item("Hell Razor", count = 3)
        self.shuffled_item("Reaper Blade", count = 2)
        self.shuffled_item("Reaper's Revenge", count = 1)

    def test_gauntlet_combos_shuffled(self) -> None:
        self.shuffled_item("Air Tremor Smash", count = 3)
        self.shuffled_item("Earthbreaker", count = 1)
        self.shuffled_item("Meteor Launch", count = 1)
        self.shuffled_item("Tremor Punch", count = 3)
        self.shuffled_item("Tremor Smash", count = 2)#War starts with this move's level 1 unlocked by default