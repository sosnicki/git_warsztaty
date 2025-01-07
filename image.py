from pathlib import Path

import numpy as np
from PIL import Image as PILImage
from scipy.ndimage import laplace
import config

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
        if config.SHARPNESS_TYPE == 'laplace':
            # Konwersja obrazu na skalę szarości
            image = self.image.convert("L")

            # Konwersja obrazu do tablicy numpy
            image_array = np.array(image, dtype=np.float32)

            # Obliczenie Laplacjana
            laplacian = laplace(image_array)

            # Obliczenie wariancji Laplacjana
            sharpness = laplacian.var()

            return sharpness
        elif config.SHARPNESS_TYPE == 'fft':
            # Wczytanie obrazu w skali szarości
            image = self.image.convert("L")

            # Konwersja do numpy
            image_array = np.array(image, dtype=np.float32)

            # Transformata Fouriera
            fft = np.fft.fft2(image_array)
            fft_shift = np.fft.fftshift(fft)
            magnitude_spectrum = np.abs(fft_shift)

            # Obliczenie sumy wysokich częstotliwości
            high_freq_magnitude = magnitude_spectrum[magnitude_spectrum > np.median(magnitude_spectrum)]
            sharpness = np.sum(high_freq_magnitude)

            return sharpness
        else:
            raise Exception('Invalid sharpness type')

    def histogram(self, path: str | Path):
        # TODO: Funkcja tworzy histogram i zapisuje go w ścieżce path
        # Wyświetlenie histogramu dla obrazu kolorowego
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.title("Histogram obrazu kolorowego")
        plt.plot(r_hist, color='red', label='Czerwony')
        plt.plot(g_hist, color='green', label='Zielony')
        plt.plot(b_hist, color='blue', label='Niebieski')
        plt.legend()

        # Wyświetlenie histogramu dla obrazu monochromatycznego
        plt.subplot(1, 2, 2)
        plt.title("Histogram obrazu monochromatycznego")
        plt.plot(gray_hist, color='black', label='Gray')
        plt.legend()

        # Wyświetlenie wykresów
        plt.tight_layout()
        plt.savefig(path)

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


