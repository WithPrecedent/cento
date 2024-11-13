"""Subclasses of Section."""

from __future__ import annotations

import dataclasses

from . import base


@dataclasses.dataclass
class Metadata(base.Section):
    """Stores the metadata section of an individual source file.

    Args:
        name: short name of the file from which the metadata was extracted.
        visuals_in_notes: whether to include any visuals in the text section of
            the file in the notes section as well. Defaults to `True`.

    """

    name: str
    start: str | None = base.dividers["metadata"]
    visuals_in_notes: bool = True


@dataclasses.dataclass
class Notes(base.Section):
    """Stores the notes section of an individual source file.

    Args:
        name: short name of the file from which the metadata was extracted.

    """

    name: str
    start: str | None = base.dividers["notes"]


@dataclasses.dataclass
class Slides(base.Section):
    """Stores the slides section of an individual source file.

    Args:
        name: short name of the file from which the metadata was extracted.

    """

    name: str
    start: str | None = base.dividers["slides"]


@dataclasses.dataclass
class Text(base.Section):
    """Stores the text section of an individual source file.

    Args:
        name: short name of the file from which the metadata was extracted.

    """

    name: str
    start: str | None = base.dividers["text"]
