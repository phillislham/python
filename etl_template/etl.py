from os.path import exists, realpath
from os import unlink
import json
from pprint import pprint

# un archivo CSV cuyo separador es ;
PATH_SOURCE_FILE = "./data/source.txt"
# archivo destino
PATH_TARGET_FILE = "./data/target.json"


def get_file_content(path: str) -> str:
    if not exists(path):
        return ""
    with open(path) as f:
        return f.read()


def file_put_contents(path: str, data: str) -> None:
    with open(path, "a") as f:
        f.write(data)


def extract(path: str) -> str:
    content = get_file_content(path)
    if not content:
        return ""
    content = content.strip(" ")
    pprint(content)
    return content


def load(data: str, path: str) -> None:
    if exists(path):
        unlink(path)
    print(data)
    file_put_contents(path, data)


def handle_exception(ex: Exception) -> None:
    print("ERROR:")
    if hasattr(ex, "message"):
        print(ex.message)
    else:
        print(repr(ex))


def transform(data: str) -> str:
    if not data:
        return ""

    lines = data.split("\n")
    pprint(lines)
    content = []
    for line in lines:
        values = line.split(";")
        content.append({
            "id": values[0] if 0 < len(values) else "",
            "value": values[1] if 1 < len(values) else ""
        })
    return json.dumps(content, sort_keys=True, indent=2)


def main():
    print("process start")
    try:
        print("- Extracting (1/3)...\n")
        data = extract(PATH_SOURCE_FILE)
        print("\n- Transforming (2/3)...\n")
        data = transform(data)
        print("\n- Loading (3/3)...\n")
        load(data, PATH_TARGET_FILE)
        target_path = realpath(PATH_TARGET_FILE)
        print(f"\nETL finished!\nrun command:\n\ncat {target_path}\n")
    except Exception as ex:
        handle_exception(ex)


main()
