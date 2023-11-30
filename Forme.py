from abc import abstractmethod
import matplotlib.colors as mcolors
from matplotlib.patches import Patch

class Forme:
    """Superclasse abstraite qui sauvegarde une couleur et impose une méthode 'get' qui retourne un Patch."""

    def __init__(self, color: str = "black", edgecolor: str = None):
        assert color in mcolors.CSS4_COLORS
        if edgecolor is not None:
            assert edgecolor in mcolors.CSS4_COLORS
        self._color = color
        self._edgecolor = edgecolor

    @abstractmethod
    def get(self, x: float, y: float, h: int) -> Patch:
        pass
