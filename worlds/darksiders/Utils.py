from __future__ import annotations

import orjson, pkgutil

def json_read(file_name: str):
    data: bytes | None = pkgutil.get_data(__name__, "data/" + file_name)
    assert data is not None, "Expected data to be bytes, got None"
    return orjson.loads(data)