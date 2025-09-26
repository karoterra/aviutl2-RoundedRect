# /// script
# requires-python = ">=3.13"
# ///

from pathlib import Path
import subprocess


def main():
    dist_dir = Path("publish")
    dist_dir.mkdir(exist_ok=True)

    dist_path = dist_dir / "aviutl2-RoundedRect.zip"

    subprocess.run(["7z", "a", dist_path, "README.md", "LICENSE", ".\\build\\角丸四角形KR.obj2"], check=True)


if __name__ == "__main__":
    main()
