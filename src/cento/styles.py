"""Built-in subclasses of Style."""

from __future__ import annotations

from typing import ClassVar


from . import base


class LawReview(base.Style):
    """Style rules for a law review article.

    Args:
        base (_type_): _description_

    """

    text: str = ''
    slides: str = ''
    sections: ClassVar[base.GenericList[str]] = ['text', 'slides']
    default: ClassVar[str] = 'text'
    text_format: ClassVar[str] = 'word'
    text_reference: ClassVar[str] = 'law_review'


class Textbook(base.Style):
    """

    Args:
        base (_type_): _description_

    """

    text: str = ''
    notes: str = ''
    slides: str = ''
    sections: ClassVar[base.GenericList[str]] = ['text', 'notes', 'slides']
    default: ClassVar[str] = 'text'
