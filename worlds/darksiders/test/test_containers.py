from .bases import DSTestBase

class TestArtifactRemoved(DSTestBase):
    options = {
        "containers": 6
        }

    def test_containers(self) -> None:
        self.start_with_item("Empty Vessel", total_count = 6)