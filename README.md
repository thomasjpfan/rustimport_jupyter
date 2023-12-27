# rustimport_jupyter

[![PyPI - Version](https://img.shields.io/pypi/v/rustimport_jupyter.svg)](https://pypi.org/project/rustimport_jupyter)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rustimport_jupyter.svg)](https://pypi.org/project/rustimport_jupyter)

Jupyter and iPython magic for compiling Python extensions written in Rust. This project builds on top of [rustimport](https://github.com/mityax/rustimport) by adding a iPython magic.

## Installation

0. Install Rust by following Rust's [Getting started Guide](https://www.rust-lang.org/learn/get-started).
1. Install `rustimport_jupyter`: `pip install rustimport_jupyter`

## How To Use

`rustimport_jupyter` compiles Python extensions written in Rust in Jupyter notebooks.
To enable this feature load the `rustimport_jupyter` extension from within the Jupyter notebook:

```python
%load_ext rustimport
```

Then, prefix a cell with the `%%rustimport` marker to compile it:

```rust
%%rustimport
use pyo3::prelude::*;

#[pyfunction]
fn square(x: i32) -> i32 {
    x * x
}
```

## Notebook Examples

- [Running in Google Colab](https://github.com/thomasjpfan/rustimport_jupyter/blob/main/examples/rust_import_colab.ipynb) - For Google Colab, `rustimport_jupyter` and the `rust` toolchain needs to be installed first. [Run in Google Colab 💻](http://colab.research.google.com/github/thomasjpfan/rustimport_jupyter/blob/main/examples/rust_import_colab.ipynb).
- [Polars Expression Plugins](https://github.com/thomasjpfan/rustimport_jupyter/blob/main/examples/rust_import_colab.ipynb) - You can use `rustimport_jupyter` to quickly iterate on [Polars expression plugins](https://pola-rs.github.io/polars/user-guide/expressions/plugins/). [Run in Google Colab 💻](http://colab.research.google.com/github/thomasjpfan/rustimport_jupyter/blob/main/examples/polars_expression_plugins.ipynb).

## License

`rustimport_jupyter` is distributed under the terms of the MIT license.
