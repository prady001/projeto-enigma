import hello_world
import os
from pathlib import Path


def main():
    print("Hello world!")
    hello_world.my_function()
    script_path = Path(os.path.abspath(__file__))
    parent_path = script_path.parent
    print("Script path:", script_path)
    with open(parent_path / "assets/poetry.txt") as f:
        print(f.read())
    with open(parent_path / "assets/test_folder/test_something.txt") as f:
        print(f.read())    
if __name__ == "__main__":
    main()