# cento

<p align="center">
<img src="https://github.com/WithPrecedent/cento/blob/main/docs/images/logo.jfif?raw=true" alt="logo" style="width:200px;"/>
</p>

| | |
| --- | --- |
| Version | [![PyPI Latest Release](https://img.shields.io/pypi/v/cento.svg?style=for-the-badge&color=steelblue&label=PyPI&logo=PyPI&logoColor=yellow)](https://pypi.org/project/cento/) [![GitHub Latest Release](https://img.shields.io/github/v/tag/WithPrecedent/cento?style=for-the-badge&color=navy&label=GitHub&logo=github)](https://github.com/WithPrecedent/cento/releases)
| Status | [![Build Status](https://img.shields.io/github/actions/workflow/status/WithPrecedent/cento/ci.yml?branch=main&style=for-the-badge&color=cadetblue&label=Tests&logo=pytest)](https://github.com/WithPrecedent/cento/actions/workflows/ci.yml?query=branch%3Amain) [![Development Status](https://img.shields.io/badge/Development-Active-seagreen?style=for-the-badge&logo=git)](https://www.repostatus.org/#active) [![Project Stability](https://img.shields.io/pypi/status/cento?style=for-the-badge&logo=pypi&label=Stability&logoColor=yellow)](https://pypi.org/project/cento/)
| Documentation | [![Hosted By](https://img.shields.io/badge/Hosted_by-Github_Pages-blue?style=for-the-badge&color=navy&logo=github)](https://WithPrecedent.github.io/cento)
| Tools | [![Documentation](https://img.shields.io/badge/MkDocs-magenta?style=for-the-badge&color=deepskyblue&logo=markdown&labelColor=gray)](https://squidfunk.github.io/mkdocs-material/) [![Linter](https://img.shields.io/endpoint?style=for-the-badge&url=https://raw.githubusercontent.com/charliermarsh/Ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/Ruff) [![Dependency Manager](https://img.shields.io/badge/PDM-mediumpurple?style=for-the-badge&logo=affinity&labelColor=gray)](https://PDM.fming.dev) [![Pre-commit](https://img.shields.io/badge/pre--commit-darkolivegreen?style=for-the-badge&logo=pre-commit&logoColor=white&labelColor=gray)](https://github.com/TezRomacH/python-package-template/blob/master/.pre-commit-config.yaml) [![CI](https://img.shields.io/badge/GitHub_Actions-navy?style=for-the-badge&logo=githubactions&labelColor=gray&logoColor=white)](https://github.com/features/actions) [![Editor Settings](https://img.shields.io/badge/Editor_Config-paleturquoise?style=for-the-badge&logo=editorconfig&labelColor=gray)](https://editorconfig.org/) [![Repository Template](https://img.shields.io/badge/snickerdoodle-bisque?style=for-the-badge&logo=cookiecutter&labelColor=gray)](https://www.github.com/WithPrecedent/cento) [![Dependency Maintainer](https://img.shields.io/badge/dependabot-navy?style=for-the-badge&logo=dependabot&logoColor=white&labelColor=gray)](https://github.com/dependabot)
| Compatibility | [![Compatible Python Versions](https://img.shields.io/pypi/pyversions/cento?style=for-the-badge&color=steelblue&label=Python&logo=python&logoColor=yellow)](https://pypi.python.org/pypi/cento/) [![Linux](https://img.shields.io/badge/Linux-lightseagreen?style=for-the-badge&logo=linux&labelColor=gray&logoColor=white)](https://www.linux.org/) [![MacOS](https://img.shields.io/badge/MacOS-snow?style=for-the-badge&logo=apple&labelColor=gray)](https://www.apple.com/macos/) [![Windows](https://img.shields.io/badge/windows-blue?style=for-the-badge&logo=Windows&labelColor=gray&color=orangered)](https://www.microsoft.com/en-us/windows?r=1)
| Stats | [![PyPI Download Rate (per month)](https://img.shields.io/pypi/dm/cento?style=for-the-badge&color=steelblue&label=Downloads%20💾&logo=pypi&logoColor=yellow)](https://pypi.org/project/cento) [![GitHub Stars](https://img.shields.io/github/stars/WithPrecedent/cento?style=for-the-badge&color=navy&label=Stars%20⭐&logo=github)](https://github.com/WithPrecedent/cento/stargazers) [![GitHub Contributors](https://img.shields.io/github/contributors/WithPrecedent/cento?style=for-the-badge&color=navy&label=Contributors%20🙋&logo=github)](https://github.com/WithPrecedent/cento/graphs/contributors) [![GitHub Issues](https://img.shields.io/github/issues/WithPrecedent/cento?style=for-the-badge&color=navy&label=Issues%20📘&logo=github)](https://github.com/WithPrecedent/cento/graphs/contributors) [![GitHub Forks](https://img.shields.io/github/forks/WithPrecedent/cento?style=for-the-badge&color=navy&label=Forks%20🍴&logo=github)](https://github.com/WithPrecedent/cento/forks)
| | |

-----

## What is cento?

*CENTO: "A composition formed by joining scrapes from other authours."* - [Samuel
Johnson's Dictionary of the English Language](https://johnsonsdictionaryonline.com/views/search.php?term=cento)

## Why use cento?

`cento` allows a user to create a text, accompanying slides, and notes from a
simple configuration file and markdown documents.

## Getting started

### Requirements

To use `cento`, you need:

* A markdown editor (any text editor may suffice)
* Python 3.10 or later

### Installation

To install `cento`, use `pip`:

```sh
pip install cento
```

### Usage

First, you create a simple configuration file named "project" with a file
extension matching one of the supported file configuration types. This should be
stored in the same folder as your markdown files that will form the produced
texts. Metadata goes in the first section titled "Project." The "Outline"
section contains the substructure of the intended documents (text, slides,
and/or notes).

```ini
[Project]
Name: Crazy Idea
Style: book
Include: text, slides
Slides Template: chalkboard
Output Folder: output

[Outline]
I: Introduction
II: Literature Review
III: My Cool Idea
A: Interesting Premise 1
1: Underlying Facts
2: Supporting Work
B: Interesting Premise 2
IV: Conclusion
```

The names of the files should correspond to the names of subsections in the
Outline with spaces replaced with underscores. If the operating system you use
has case-sensitive file names, all files should be named with lower case
letters (and an extension of ".md"). The above configuration file is from the
`cento` tests folder. So, you can see how the markdown files are named inside
the tests folder in the "test_project_book" subfolder.

Second, write the content of your markdown files. The files may contain YAML
front-matter for specific instructions and settings related to that file. All
generally applicable instructions and settings should be in the project
configuration file.

By default, the sections of your markdown file should be named within "<" and
">":

| divider | usage |
| --- | --- |
| \<text\> | Contents of the book or article |
| \<slides\> | Contents of slides accompanying the book or article |
| \<notes\> | Contents of notes or accompanying guidebook |

You do not have to have all of the section types. Any unmarked section will be
assumed to be part of the book or article text.

Any visualizations, images, charts, or graphs should be stored in a subfolder
titled "visuals" by default.

Third, you run `cento` from the command line. If you are in the folder where
your configuration and markdown files are located, executing `cento` is simple:

```sh
python cento
```

If you are in a different folder, you just need to list that after `cento` as
follows:

```sh
python cento {folder path}
```

## Contributing

Contributors are always welcome. Feel free to grab an
[issue](https://www.github.com/WithPrecedent/cento/issues) to work on or make a
suggested improvement. If you wish to contribute, please read the [Contribution
Guide](https://www.github.com/WithPrecedent/cento/contributing.md) and [Code of
Conduct](https://www.github.com/WithPrecedent/cento/code_of_conduct.md).

## Similar Projects

* [quarto](https://quarto.org/): an R based project for dynamically creating
academic publications from markdown files.

## Acknowledgments

I would like to thank the University of Kansas School of Law for tolerating and
supporting this law professor's coding efforts, an endeavor which is well
outside the typical scholarly activities in the discipline.

## License

Use of this repository is authorized under the [Apache Software License
2.0](https://www.github.com/WithPrecedent/cento/blog/main/LICENSE).
