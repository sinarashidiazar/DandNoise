import os
import importlib
import inspect
from filters.base import FilterBase

def load_plugins():

    filters = []

    for file in os.listdir("filters"):

        if file.endswith(".py") and file not in ["__init__.py","base.py"]:

            module_name = f"filters.{file[:-3]}"
            module = importlib.import_module(module_name)

            for name,obj in inspect.getmembers(module):

                if inspect.isclass(obj) and issubclass(obj,FilterBase) and obj!=FilterBase:

                    filters.append(obj())

    return filters
