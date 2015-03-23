Gist index generator
======================

Simple script to generate beautiful indexes for your [gist](https://gist.github.com/).

## Setup

Please, use virtualenv (example with `virtualenvwrapper`):

```bash
$ mkvirtualenv gist_index_generator
```

Install dependencies:

```bash
$ make requirements-dev
```

## Usage

Print to stdout:

```bash
$ python generate-gist-index.py RomuloOliveira 

gist-files
==========

Index of  of my gist-files. Life is too short to access https://gist.github.com/RomuloOliveira
...
```

Write to file:
```bash
$ python generate-gist-index.py RomuloOliveira -o gist.md
```

Select an output format (Currently, only `markdown` is supported):

```bash
$ python generate-gist-index.py RomuloOliveira -f markdown
```

## Tests

```bash
$ make test
```
