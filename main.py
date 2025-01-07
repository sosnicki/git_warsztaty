import argparse

import sys

from image import Image


def main():
    # Parser argumentów wiersza poleceń
    parser = argparse.ArgumentParser(description="Przetwarzanie obrazów za pomocą Pillow.")
    parser.add_argument("input", help="Ścieżka do pliku wejściowego (obraz).")
    parser.add_argument("--filter", choices=["blur", "sharpen", "invert"],
                        help="Zastosuj wybrany filtr.")
    parser.add_argument("--filter-output", help="Ścieżka do pliku wyjściowego po filtrze.")
    parser.add_argument("--sharpness", action="store_true",
                        help="Oblicz ostrość obrazu.")
    parser.add_argument("--histogram", help="Zapisz histogram obrazu.")
    args = parser.parse_args()

    # Wczytanie obrazu lub obrazów
    try:
        image = Image(args.input)
    except Exception as e:
        print(f"Błąd podczas wczytywania obrazu: {e}")
        return 1

    # Obliczenie ostrości
    if args.sharpness:
        print(f"Ostrość obrazu: {image.sharpness:.2f}")

    # Wyświetlenie histogramu
    if args.histogram:
        image.histogram(args.histogram)

    # Zastosowanie filtru
    if args.filter:
        if args.filter == "blur":
            image.blur()
        elif args.filter == "sharpen":
            image.sharpen()
        elif args.filter == "invert":
            image.invert()
        else:
            print(f"Nieznany filtr: {args.filter}")
            return 2

        print(f"Zastosowano filtr: {args.filter}")

        # Zapis obrazu
        try:
            image.save(args.filter_output)
            print(f"Zapisano wynikowy obraz do: {args.filter_output}")
        except Exception as e:
            print(f"Błąd podczas zapisywania obrazu: {e}")


if __name__ == "__main__":
    sys.exit(main())