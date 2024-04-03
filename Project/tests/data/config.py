

import os
import json

settings = None

def load_settings(es_prueba=False):
    global settings
    archivo_config = "settings.json" if not es_prueba else "settings_prod_smoke_test.json"

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), archivo_config.strip('"'))) as f:
        settings = json.load(f)

load_settings()
