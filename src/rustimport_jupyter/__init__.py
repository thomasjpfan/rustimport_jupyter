from shutil import which

from ._ipython_magic import RustImportIPython


def load_ipython_extension(ipython):
    rustc_is_installed = which("rustc") is not None
    if not rustc_is_installed:
        msg = "rustc must be installed to ust rustimport_jupyter. See ____ for details"
        raise OSError(msg)

    ipython.register_magics(RustImportIPython)
