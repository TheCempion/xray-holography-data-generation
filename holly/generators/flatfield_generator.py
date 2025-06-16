# standard libraries
from typing import Callable
from abc import ABC

# third party libraries

# local libraries
import holly.datasets as module_data
import holly.utils.random as random
from holly.experiment.flatfield import FlatField
from holly.parse_config import ConfigParser
import holly.experiment as experiment


__all__ = [
    "BaseFlatFieldGenerator",
    "FlatFieldGenerator",
    "DummyFlatFieldGenerator",
]


class BaseFlatFieldGenerator(ABC):
    def __init__(self, config: ConfigParser, constructor: Callable[[], FlatField]):
        """Base class for flatfield generators.

        Args:
            config (ConfigParser): Configuration file containing
            constructor (Callable[[], FlatField]): _description_
        """
        self.config = config
        self.constructor = constructor
        self.size = experiment.GLOBAL_EXP_SETUP.detector_size

    def generate(self) -> FlatField:
        return self.create_flatfield()

    def create_flatfield(self) -> FlatField:
        return self.constructor()


class DummyFlatFieldGenerator(BaseFlatFieldGenerator):
    def __init__(self, config: ConfigParser) -> None:
        self.dataset = None
        super().__init__(config, constructor=lambda: None)


class FlatFieldGenerator(BaseFlatFieldGenerator):
    def __init__(self, config: ConfigParser) -> None:
        super().__init__(config, constructor=self._get_constructor(config))

    def _get_constructor(self, config: ConfigParser) -> Callable[[], FlatField]:
        if config.get("flatfield_dataset", None) is None:
            self.dataset = None
            return lambda: None  # always return None

        self.dataset = config.init_obj("flatfield_dataset", module_data)
        if len(self.dataset) == 0:
            raise ValueError("Flatfield dataset is empty.")

        def dataset_constructor() -> FlatField:
            idx = random.get_random_idx(self.dataset)
            flatfields = self.dataset[idx]
            return FlatField(flatfields)

        return dataset_constructor
