# standard libraries
from abc import ABC

# third party libraries
import torch
import torchvision
import matplotlib.pyplot as plt

# local libraries


__all__ = [
    "Shape",
]


class Shape(ABC):
    """Abstract class for all shapes."""

    def __init__(self, shape: torch.Tensor) -> None:
        self.shape = shape
        self.shape = torch.nan_to_num(shape)
        self._standardize()

    def plot(self) -> None:
        plt.imshow(self.shape)
        plt.show()

    def rotate(self, angle: int) -> None:
        """Rotates the shape by a given angle.

        Args:
            angle (int): Angle in degrees by which the shape is rotated.
        """
        rotated = torchvision.transforms.functional.rotate(
            self.shape[None, None, :, :], angle, expand=True
        )[0, 0, :, :]
        rotated[rotated <= 0.025] = 0
        self.shape = rotated

    def _standardize(self) -> None:
        """Standardize shape to have values in [0,1]"""
        self.shape /= self.shape.max()
