import asyncio
import os
import re
import tomllib
from concurrent.futures import ProcessPoolExecutor
from io import BytesIO
from pathlib import Path

import kcl
import requests
from kcl import UnitLength
from PIL import Image

RETRIES = 5

# Map strings to kcl units
UNIT_MAP = {
    'in': kcl.UnitLength.In,
    'mm': kcl.UnitLength.Mm,
    'ft': kcl.UnitLength.Ft,
    'm': kcl.UnitLength.M,
    'cm': kcl.UnitLength.Cm,
    'yd': kcl.UnitLength.Yd,
}


def export_step(code: str, save_path: Path, unit_length: UnitLength = kcl.UnitLength.Mm) -> bool:
    try:
        export_response = asyncio.run(
            kcl.execute_and_export(code, unit_length, kcl.FileExportFormat.Step)
        )

        stl_path = save_path.with_suffix(".step")

        with open(stl_path, "wb") as out:
            out.write(bytes(export_response[0].contents))

        return True
    except Exception as e:
        print(e)
        return False


def find_files(
        path: str | Path, valid_suffixes: list[str], name_pattern: str | None = None
) -> list[Path]:
    """
    Recursively find files in a folder by a list of provided suffixes or file naming pattern

    Args:
        path: str | Path
            Root folder to search
        valid_suffixes: Container[str]
            List of valid suffixes to find files by (e.g. ".stp", ".step")
        name_pattern: str
            Name pattern to additionally filter files by (e.g. "_component")

    Returns:
        list[Path]
    """
    path = Path(path)
    valid_suffixes = [i.lower() for i in valid_suffixes]
    return sorted(
        file for file in path.rglob("*")
        if file.suffix.lower() in valid_suffixes and
        (name_pattern is None or re.match(name_pattern, file.name))
    )


def get_units(kcl_path: Path) -> UnitLength:
    settings_path = kcl_path.parent / "project.toml"
    if not settings_path.exists():
        return kcl.UnitLength.Mm
 
    with open(settings_path, "rb") as f:
        data = tomllib.load(f)
    try:
        return UNIT_MAP[data['settings']['modeling']['base_unit']]
    except KeyError:
        return kcl.UnitLength.Mm


def snapshot(code: str, save_path: Path, unit_length: UnitLength = kcl.UnitLength.Mm) -> bool:
    try:
        snapshot_response = asyncio.run(
            kcl.execute_and_snapshot(code, unit_length, kcl.ImageFormat.Png)
        )

        image = Image.open(BytesIO(bytearray(snapshot_response)))

        im_path = save_path.with_suffix(".png")

        image.save(im_path)

        return True
    except Exception as e:
        print(e)
        return False


def process_single_kcl(kcl_path: Path) -> dict:
    print(f"Processing {kcl_path.name}")

    units = get_units(kcl_path)

    with open(kcl_path, "r") as inp:
        code = str(inp.read())

    export_status = export_step(code=code, save_path=Path(__file__).parent / "step" / kcl_path.stem, unit_length=units)
    count = 1
    while not export_status and count < RETRIES:
        export_status = export_step(code=code, save_path=Path(__file__).parent / "step" / kcl_path.stem,
                                    unit_length=units)
        count += 1

    snapshot_status = snapshot(code=code, save_path=Path(__file__).parent / "screenshots" / kcl_path.stem,
                               unit_length=units)
    count = 1
    while not snapshot_status and count < RETRIES:
        snapshot_status = snapshot(code=code, save_path=Path(__file__).parent / "screenshots" / kcl_path.stem,
                                   unit_length=units)
        count += 1

    return {"filename": kcl_path.name, "export_status": export_status, "snapshot_status": snapshot_status}


def main():
    kcl_files = find_files(path=Path(__file__).parent, valid_suffixes=[".kcl"])

    # run concurrently
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(process_single_kcl, kcl_file) for kcl_file in kcl_files]
    results = [future.result() for future in futures]

    if False in [i["export_status"] for i in results]:
        comment_body = "The following files failed to export to STEP format:\n"
        for i in results:
            if not i["export_status"]:
                comment_body += f"{i['filename']}\n"

        url = f"https://api.github.com/repos/{os.getenv('GH_REPO')}/issues/{os.getenv('GH_PR')}/comments"

        headers = {
            'Authorization': f'token {os.getenv("GH_TOKEN")}',
        }

        json_data = {
            'body': comment_body,
        }

        requests.post(url, headers=headers, json=json_data, timeout=60)


if __name__ == "__main__":
    main()
