# rustimport_jupyter

[![PyPI - Version](https://img.shields.io/pypi/v/rustimport_jupyter.svg)](https://pypi.org/project/rustimport_jupyter)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/rustimport_jupyter.svg)](https://pypi.org/project/rustimport_jupyter)

Jupyter and iPython magic for compiling Python extensions written in Rust. This project builds on top of [rustimport](https://github.com/mityax/rustimport) by adding a iPython magic.

-----

**Table of Contents**

- [Installation](#installation)
- [How To Use](#how-to-use)
- [Examples](#examples)
- [License](#license)

## Installation

0. Install Rust by following the Rust's [Getting started page](https://www.rust-lang.org/learn/get-started).

1. Install `rustimport_jupyter`:
```console
pip install rustimport_jupyter
```

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

## Examples

- For Google Colab, `rustimport_jupyter` and the `rust` toolchain needs to be installed first. This
[notebook](https://github.com/thomasjpfan/rustimport_jupyter/blob/main/examples/rust_import_colab.ipynb)
showcases this use case and is available in [Google Colab](http://colab.research.google.com/github/thomasjpfan/rustimport_jupyter/blob/main/examples/rust_import_colab.ipynb).
- You can use `rustimport_jupyter` to quickly iterate on [Polars expression plugins](https://pola-rs.github.io/polars/user-guide/expressions/plugins/). This [notebook](https://github.com/thomasjpfan/rustimport_jupyter/blob/main/examples/polars_expression_plugins.ipynb) showcases this use case and is available in [Google Colab](http://colab.research.google.com/github/thomasjpfan/rustimport_jupyter/blob/main/examples/polars_expression_plugins.ipynb).

The `--module-path-variable` parameter outputs the module path

## License

`rustimport_jupyter` is distributed under the terms of the MIT license.
