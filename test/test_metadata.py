import os
import glob

import pytest
import frontmatter  # pip install python-frontmatter

# Base directories to scan
SEARCH_PATHS = [
    os.path.join(os.path.dirname(__file__), '..', 'Projects', 'Extended-Team-Projects'),
    os.path.join(os.path.dirname(__file__), '..', 'Projects', 'Projects'),
]

# Allowed values
ALLOWED_SUBJECTS = {
    "CI-CD",
    "Performance and Architecture",
    "ML",
    "Containers and Virtualization",
    "Libraries",
    "Virtual Hardware",
    "Security",
    "Embedded Linux",
    "RTOS Fundamentals",
    "Storage",
    "Databases",
    "Web",
    "Migration to Arm",
    "Gaming",
    "Libraries",
    "Graphics",
    "AR-VR",
    "Edge AI",
    "Physical AI",
    "Cloud AI",
    "Mobile, Graphics, and Gaming"
}

ALLOWED_REQUIRES_TEAM = {"Yes", "No"}

ALLOWED_PLATFORMS = {
    "Servers and Cloud Computing",
    "Laptops and Desktops",
    "Mobile, Graphics, and Gaming",
    "Automotive",
    "IoT",
    "Embedded and Microcontrollers",
    "AI",
    "Install Guides"
}

ALLOWED_SW_HW = {"Software", "Hardware"}

ALLOWED_SUPPORT_LEVEL = {
    "Self-Service",
    "Arm Ambassador Support",
    "Direct Support from Arm",
}

ALLOWED_LICENSES = {
    "Apache-2.0",
    "MIT",
    "BSD-3-Clause",
    # …SPDX identifiers you support
}

REQUIRED_FIELDS = {
    "title",
    "subjects",
    "requires-team",
    "platform",
    "sw-hw",
    "support-level",
    "publication-date",
    "description",
}


def collect_markdown_files():
    """Return a list of all .md files under our two project directories."""
    files = []
    for base in SEARCH_PATHS:
        pattern = os.path.join(base, '**', '*.md')
        files.extend(glob.glob(pattern, recursive=True))
    return files


@pytest.fixture(params=collect_markdown_files(), ids=lambda p: os.path.relpath(p))
def md_frontmatter(request):
    path = request.param
    post = frontmatter.load(path)
    assert post.metadata, f"No front-matter found in {path}"
    return path, post.metadata


def test_required_fields_present(md_frontmatter):
    path, meta = md_frontmatter
    missing = REQUIRED_FIELDS - set(meta.keys())
    assert not missing, f"[{path}] Missing fields: {missing}"


@pytest.mark.parametrize("field,allowed", [
    ("subjects", ALLOWED_SUBJECTS),
    ("requires-team", ALLOWED_REQUIRES_TEAM),
    ("platform", ALLOWED_PLATFORMS),
    ("sw-hw", ALLOWED_SW_HW),
    ("support-level", ALLOWED_SUPPORT_LEVEL),
])
def test_list_fields_allowed(md_frontmatter, field, allowed):
    path, meta = md_frontmatter
    values = meta.get(field)
    assert isinstance(values, list), f"[{path}] `{field}` must be a list"
    invalid = set(values) - allowed
    assert not invalid, f"[{path}] Invalid `{field}` entries: {invalid}"


def test_publication_date_format(md_frontmatter):
    import re
    path, meta = md_frontmatter
    date = meta.get("publication-date", "")
    assert re.match(r"^\d{4}-\d{2}-\d{2}$", str(date)), (
        f"[{path}] `publication-date` must be YYYY-MM-DD, got: {date}"
    )
