"""Tools to parse markdown files."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .base import Metadata

def parse_metadata(section: str) -> Metadata:
    """Converts the `metadata` section of a file into a `Metadata` instance.

    Args:
        section: `str` from the metadata section of a source file.

    Returns:
        The metadata converted into a `Metadata` instance.

    """


def parse_notes(section: str) -> str:
    """Converts the `notes` section of a file from markdown to output format.

    Args:
        section: `str` from the notes section of a source file.

    Returns:
        The notes converted to the output format.

    """


def parse_slides(section: str) -> str:
    """Converts the `slides` section of a file from markdown to output format.

    Args:
        section: `str` from the slides section of a source file.

    Returns:
        The slides converted to the output format.

    """


def parse_text(section: str) -> str:
    """Converts the `text` section of a file from markdown to output format.

    Args:
        section: `str` from the text section of a source file.

    Returns:
        The text converted to the output format.

    """

