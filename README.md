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

Write to file (Not supported yet, see [#3](https://github.com/RomuloOliveira/gist-index-generator/issues/3)):

```bash
$ python generate-gist-index.py RomuloOliveira -o gist.md
```

Select an output format (Currently, only `markdown` is supported):

```bash
$ python generate-gist-index.py RomuloOliveira -f markdown
```

For more help:

```bash
$ python generate-gist-index.py -h
```

## Tests

```bash
$ make test
```
