from pathlib import Path

from PIL import Image as PILImage


class Image:
    image: PILImage
    width: int
    height: int

    def __init__(self, path: str | Path):
        if path:
            self.load(path)

    def load(self, path: str | Path):
        self.image = PILImage.open(path)
        self.width, self.height = self.image.size

    @property
    def sharpness(self) -> float:
        # TODO: Funkcja zwraca ocenę ostrości obrazu w postci liczby rzeczywistej
        ...

    def histogram(self, path: str | Path):
        # TODO: Funkcja tworzy histogram i zapisuje go w ścieżce path
        ...

    def blur(self):
        # TODO: Funkcja rozmywa obraz metodą np. Gaussa i podmienia zmienną self.image
        ...

    def sharpen(self):
        # TODO: Funkcja wyostrza obraz i podmienia zmienną self.image
        ...

    def invert(self):
        # TODO: Funkcja odwraca kolory i podmienia zmienną self.image
        ...

    def save(self, path: str | Path):
        # TODO: Funkcja zapisuje obraz z self.image pod ścieżką path
        # jakość formatu JPEG i poziom kompresji PNG powinien być w konfiguracji
        ...


