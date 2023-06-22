from glob import glob
import os


def _as_module(fixture_path: str) -> str:
    return fixture_path.replace("/", ".").replace("\\", ".").replace(".py", "")


if os.getcwd().endswith("monarch-app"):
    fixtures_dir = "backend/tests/fixtures"
elif os.getcwd().endswith("backend"):
    fixtures_dir = "tests/fixtures"
else:
    raise Exception("Could not find fixtures directory")


fixtures = glob(f"{fixtures_dir}/[!_]*.py")

print([_as_module(f) for f in fixtures if "__" not in f])
pytest_plugins = [
    _as_module(f).removeprefix("tests.") for f in fixtures if "__" not in f
]
