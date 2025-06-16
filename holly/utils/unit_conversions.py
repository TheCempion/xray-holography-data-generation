"""Unit conversions to match other repositories or general functionality.

Convert units for values used in the configuration files or generally in this repository, so in case the units
that are used in this repository are changed, the conversions only need to be done here.

"""

# standard libraries

# third party libraries

# local libraries


__all__ = [
    "convert_z01",
    "convert_z02",
]


def convert_z01(z01: float) -> float:
    """Transforms the value for z01 to the globally used unit (in [nm]).

    Args:
        z01 (float): Distance z01 (in [cm]).

    Returns:
        float: Distance transformed into correct unit (in [nm]).
    """
    return round(z01, 7) * 1e7


def convert_z02(z02: float) -> float:
    """Transforms the value for z02 to the globally used unit (in [nm]).

    Args:
        z02 (float): Distance z02 (in [m]).

    Returns:
        float: Distance transformed into correct unit (in [nm]).
    """
    return round(z02, 9) * 1e9
