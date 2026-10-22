import json

from .bases import DSTestBase

from ..Utils import data_path, json_read

class TestReadJson(DSTestBase):
    
    def test_json_read(self) -> None:

        json_read(data_path('Crossroads.json'))
