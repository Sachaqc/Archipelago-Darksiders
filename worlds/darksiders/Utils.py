from __future__ import annotations

import json, os

def data_path(*args):
    return os.path.join(os.path.dirname(__file__), 'data', *args)

def json_read(filepath):

    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)