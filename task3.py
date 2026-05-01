from pathlib import Path
import sys
from colorama import Fore, Style, init

init(autoreset=True)


def print_directory_structure(path: Path, indent: str = ""):
    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(indent + Fore.BLUE + f"📂 {item.name}")
            print_directory_structure(item, indent + "   ")
        else:
            print(indent + Fore.GREEN + f"📜 {item.name}")


def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python task3.py <directory_path>")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(Fore.RED + "Error: path does not exist.")
        return

    if not directory_path.is_dir():
        print(Fore.RED + "Error: path is not a directory.")
        return

    print(Fore.YELLOW + f"📦 {directory_path.name}")
    print_directory_structure(directory_path)


if __name__ == "__main__":
    main()