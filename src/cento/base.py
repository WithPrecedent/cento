"""Tools to configure and implement a `cento` project."""

from __future__ import annotations

import configparser
import dataclasses
from collections.abc import Hashable, MutableMapping, MutableSequence
from typing import TYPE_CHECKING, Any, ClassVar, TypeAlias

import wonka

from . import loaders, parsers, savers, utilities

if TYPE_CHECKING:
    import pathlib

GenericDict: TypeAlias = MutableMapping[Hashable, Any]
GenericList: TypeAlias = MutableSequence[Any]

_DEFAULT_SECTION: str = 'text'
_OUTLINE_SECTION: str = 'outline'
_PROJECT_SECTION: str = 'project'


@dataclasses.dataclass
class Sources:
    """Stores combined data extracted from source files.

    Args:
        metadata: `dict` of metadata in the source files. Keys are the short
            names (no extension or folder) of the files and the values are
            `Metadata` instances containing data from within those files.
        text: `dict` of the texts from the source files used to form the final
            manuscript. Keys are the names of the sections or files and values
            are the `str` text extracted from those files to form a manuscript.
        slides: `dict` of the slide data from the source files used to create a
            slide deck. Keys are the titles of the slides or names of the files
            and values are the content of the slides.
        notes: `dict` of the accompanying notes for the final manuscript. Keys
            are the names of the sections or files and values are the `str` text
            extracted from those files to form a manuscript.

    """

    metadata: GenericDict = dataclasses.field(default_factory = dict)
    text: GenericDict = dataclasses.field(default_factory = dict)
    slides: GenericDict = dataclasses.field(default_factory = dict)
    notes: GenericDict = dataclasses.field(default_factory = dict)

    @classmethod
    def create(cls, paths: list[str | pathlib.Path]) -> Sources:
        """Creates an instance by parsing data from source files.

        Args:
            paths: a `list` or `glob` of source files.

        Returns:
            An instance of `Documents` created from the source files.

        """
        documents = cls()
        for source in paths:
            loaded = cls.load(source)
            parsed = cls.parse(loaded)
            for key, value in parsed.items():
                getattr(documents, key).update(key, value)
        return documents

    @classmethod
    def load(cls, path: str | pathlib.Path) -> str:
        """Loads the text from a single source file.

        Args:
            path: a path to a source file.

        Returns:
            An instance of `Documents` created from the source files.

        """

    @classmethod
    def parse(cls, contents: str) -> GenericDict:
        """Parses a source file into its component parts.

        Args:
            contents: the `str` contents of the source file.

        Returns:
            A `dict` with keys being the name of the type of text (metadata,
                text, slides, etc.) and values as the parsed text from the
                corresponding section in that raw file.

        """


@dataclasses.dataclass
class Outline(MutableMapping):
    """Stores configuration settings extracted from a configuration file.

    Args:
        contents: configuration options. Defaults to an empty `dict`.

    Attributes:
        defaults: default options that should be used when a user does not
            provide the corresponding options in their configuration settings,
            but are otherwise necessary for the project. Defaults to an empty
            `dict`.

    """

    contents: GenericDict = dataclasses.field(default_factory = dict)
    defaults: ClassVar[GenericDict] = {}

    """ Properties """

    @property
    def options(self) -> GenericDict:
        """Returns project options of outline from `contents`.

        Returns:
            The section in contents matching the project section name in the
            global settings.

        """
        return self.contents[globals()["_PROJECT_SECTION"]]

    @property
    def structure(self) -> GenericDict:
        """Returns structure of outline from `contents`.

        Returns:
            The section in contents matching the outline section name in the
            global settings.

        """
        return self.contents[globals()["_OUTLINE_SECTION"]]

    """ Class Methods """

    @classmethod
    def create(cls, source: pathlib.Path | str, /, **kwargs:  Any) -> Outline:
        """Creates a settings `dict` from a file path to an `ini` file.

        Args:
            source: path to file with data to store in a settings `dict`.
            kwargs: additional parameters and arguments to pass to
                `configparser`.

        Raises:
            FileNotFoundError: if the `source` path does not correspond to a
                file.

        Returns:
            An instance with contents from the `source` file.

        """
        path = utilities._pathlibify(source)
        try:
            contents = configparser.ConfigParser(dict_type = dict, **kwargs)
            contents.optionxform = lambda option: option
            contents.read(path)
        except (KeyError, FileNotFoundError) as error:
            message = f'settings file {path} not found'
            raise FileNotFoundError(message) from error
        return cls(contents)

    """ Instance Methods """

    def add(
        self,
        key: Hashable,
        value: GenericDict) -> None:
        """Adds `key` and `value` to `contents`.

        If `key` is already a key in `contents`, the contents associated with
        that key are updated. If `key` doesn't exist, a new key/value pair is
        added to `contents`.

        Args:
            key: name of key to store `value`.
            value: values to be stored.

        Raises:
            TypeError: if `key` isn't hashable.

        """
        try:
            self[key].update(value)
        except KeyError:
            try:
                self[key] = value
            except TypeError as error:
                message = 'The key must be hashable'
                raise TypeError(message) from error
        return

    def delete(self, item: Hashable) -> None:
        """Deletes `item` in `contents`.

        Args:
            item: key in `contents` to delete the key/value pair.

        """
        del self.contents[item]
        return

    def items(self) -> tuple[tuple[Hashable, Any], ...]:
        """Emulates python `dict` `items` method.

        Returns:
            A `tuple` equivalent to `dict.items()`.

        """
        return tuple(zip(self.keys(), self.values(), strict = True))

    def keys(self) -> tuple[Hashable, ...]:
        """Emulates python `dict` `keys` method.

        Returns:
            A `tuple` equivalent to `dict.keys().`

        """
        return tuple(self.contents.keys())

    def values(self) -> tuple[Any, ...]:
        """Emulates python `dict` `values` method.

        Returns:
            A `tuple` equivalent to `dict.values().`

        """
        return tuple(self.contents.values())

    """ Dunder Methods """

    def __getitem__(self, key: Hashable) -> Any:
        """Returns value for `key` in `contents`.

        Args:
            key: key in `contents` for which a value is sought.

        Returns:
            Value stored in `contents`.

        """
        return self.contents[key]

    def __setitem__(self, key: str, value: GenericDict) -> None:
        """Creates new key/value pair(s) in a section of the active dictionary.

        Args:
            key: name of a section in the active dictionary.
            value: the dictionary to be placed in that section.

        """
        self.add(key, value)
        return


@dataclasses.dataclass
class Project:
    """Interface for a `cento` project.

    Args:


    """

@dataclasses.dataclass
class Section(wonka.Subclasser):
    """Base class for all section rules.

    By subclassing `wonka.Subclasser`, this class gains a `create` method that
    automatically allows creation of any subclass through an implicit registry
    where all of the key names for creating a subclass are the snakecase name of
    the subclass. To use this, just call `Genre.create({snakecase name of the
    subclass}).

    """

    name: str
    divider: str

    def parse(self, contents: str) -> GenericDict:
        """Parses a source file into its component parts.

        Args:
            contents: the `str` contents of the source file.

        Returns:
            A `dict` with keys being the name of the type of text (metadata,
                text, slides, etc.) and values as the parsed text from the
                corresponding section in that raw file.

        """


@dataclasses.dataclass
class Style:
    """

    Args:


    """

    sections: ClassVar[GenericList[str]] = []
