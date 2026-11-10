from .bases import DSTestBase

class TestArtifactRemoved(DSTestBase):
    options = {
        "containers": 6
        }

    def test_containers(self) -> None:
        containers = self.get_items_by_name("Empty Vessel")
    
        with self.subTest("Test that there are the exact number of containers in the itempool"):
            containers = self.get_items_by_name("Empty Vessel")
            self.assertEqual(len(containers), 5)