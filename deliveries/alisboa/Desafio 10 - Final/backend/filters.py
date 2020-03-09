"""Jinja custom filters."""
from pathlib import Path


def get_all_apis_router(_type: str, root_path: str) -> (Path, Path):
    """Return api files and definition files just put the file on folder swagger."""

    swagger_path = Path(root_path)
    all_files = list(x.name for x in swagger_path.glob("**/*.yaml"))
    schemas_files = [x for x in all_files if "schemas" in x]
    api_files = [x for x in all_files if "schemas" not in x and "main" not in x]
    return api_files if _type == "api" else schemas_files

def get_entity_fields() -> dict:
    """Extract all fields from entities."""
    return {}