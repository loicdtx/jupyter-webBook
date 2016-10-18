# Jupyter webBook

A webBook authoring framework inspired by [R bookdown](https://github.com/rstudio/bookdown).

See demo [here](http://www.loicdutrieux.net/jupyter-webBook/intro.html)

## Usage

- Write individual chapters as jupyter notebooks
- Define book structure in the `_book.json` file
- Run `nb2book` command to compile the webBook

## Install

`Jupyter-webBook` depends on a version of `nbconverts` that is not yet on PyPi. You therefore need to first install the development version of `nbconvert` directly from github.

```sh
pip install git+https://github.com/jupyter/nbconvert.git
```

Then install `Jupyter-webBook`

```sh
pip install git+https://github.com/loicdtx/jupyter-webbook.git
```
