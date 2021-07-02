import enum
import importlib
import os

__all__ = {"lookup_any_item_id_to_name",
           "lookup_any_location_id_to_name",
           "network_data_package",
           "Games"}

# all of the below should be moved to AutoWorld functionality
from .alttp.Items import lookup_id_to_name as alttp
from .hk.Items import lookup_id_to_name as hk
from .factorio import Technologies
from .minecraft.Items import lookup_id_to_name as mc

lookup_any_item_id_to_name = {**alttp, **hk, **Technologies.lookup_id_to_name, **mc}
assert len(alttp) + len(hk) + len(Technologies.lookup_id_to_name) + len(mc) == len(lookup_any_item_id_to_name)
lookup_any_item_name_to_id = {name: id for id, name in lookup_any_item_id_to_name.items()}
# assert len(lookup_any_item_name_to_id) == len(lookup_any_item_id_to_name) # currently broken: Single Arrow

from .alttp import Regions
from .hk import Locations
from .minecraft import Locations as Advancements

lookup_any_location_id_to_name = {**Regions.lookup_id_to_name, **Locations.lookup_id_to_name,
                                  **Technologies.lookup_id_to_name, **Advancements.lookup_id_to_name}
assert len(Regions.lookup_id_to_name) + len(Locations.lookup_id_to_name) + \
       len(Technologies.lookup_id_to_name) + len(Advancements.lookup_id_to_name) == \
       len(lookup_any_location_id_to_name)
lookup_any_location_name_to_id = {name: id for id, name in lookup_any_location_id_to_name.items()}
assert len(lookup_any_location_name_to_id) == len(lookup_any_location_id_to_name)

network_data_package = {"lookup_any_location_id_to_name": lookup_any_location_id_to_name,
                        "lookup_any_item_id_to_name": lookup_any_item_id_to_name,
                        "version": 7}


@enum.unique
class Games(str, enum.Enum):
    HK = "Hollow Knight"
    LTTP = "A Link to the Past"
    Factorio = "Factorio"
    Minecraft = "Minecraft"


# end of TODO block

# import all submodules to trigger AutoWorldRegister
for file in os.scandir(os.path.dirname(__file__)):
    if file.is_dir():
        importlib.import_module(f".{file.name}", "worlds")
