# This file is generated by numpy's build process
# It contains system_info results at the time of building this package.
from enum import Enum
from numpy._core._multiarray_umath import (
    __cpu_features__,
    __cpu_baseline__,
    __cpu_dispatch__,
)

__all__ = ["show"]
_built_with_meson = True


class DisplayModes(Enum):
    stdout = "stdout"
    dicts = "dicts"


def _cleanup(d):
    """
    Removes empty values in a `dict` recursively
    This ensures we remove values that Meson could not provide to CONFIG
    """
    if isinstance(d, dict):
        return {k: _cleanup(v) for k, v in d.items() if v and _cleanup(v)}
    else:
        return d


CONFIG = _cleanup(
    {
        "Compilers": {
            "c": {
                "name": "msvc",
                "linker": r"link",
                "version": "19.29.30154",
                "commands": r"cl",
                "args": r"",
                "linker args": r"",
            },
            "cython": {
                "name": "cython",
                "linker": r"cython",
                "version": "3.0.11",
                "commands": r"cython",
                "args": r"",
                "linker args": r"",
            },
            "c++": {
                "name": "msvc",
                "linker": r"link",
                "version": "19.29.30154",
                "commands": r"cl",
                "args": r"",
                "linker args": r"",
            },
        },
        "Machine Information": {
            "host": {
                "cpu": "x86_64",
                "family": "x86_64",
                "endian": "little",
                "system": "windows",
            },
            "build": {
                "cpu": "x86_64",
                "family": "x86_64",
                "endian": "little",
                "system": "windows",
            },
            "cross-compiled": bool("False".lower().replace("false", "")),
        },
        "Build Dependencies": {
            "blas": {
                "name": "scipy-openblas",
                "found": bool("True".lower().replace("false", "")),
                "version": "0.3.27",
                "detection method": "pkgconfig",
                "include directory": r"C:/Users/runneradmin/AppData/Local/Temp/cibw-run-4yyn90e0/cp312-win_amd64/build/venv/Lib/site-packages/scipy_openblas64/include",
                "lib directory": r"C:/Users/runneradmin/AppData/Local/Temp/cibw-run-4yyn90e0/cp312-win_amd64/build/venv/Lib/site-packages/scipy_openblas64/lib",
                "openblas configuration": r"OpenBLAS 0.3.27  USE64BITINT DYNAMIC_ARCH NO_AFFINITY Haswell MAX_THREADS=24",
                "pc file directory": r"D:/a/numpy/numpy/.openblas",
            },
            "lapack": {
                "name": "scipy-openblas",
                "found": bool("True".lower().replace("false", "")),
                "version": "0.3.27",
                "detection method": "pkgconfig",
                "include directory": r"C:/Users/runneradmin/AppData/Local/Temp/cibw-run-4yyn90e0/cp312-win_amd64/build/venv/Lib/site-packages/scipy_openblas64/include",
                "lib directory": r"C:/Users/runneradmin/AppData/Local/Temp/cibw-run-4yyn90e0/cp312-win_amd64/build/venv/Lib/site-packages/scipy_openblas64/lib",
                "openblas configuration": r"OpenBLAS 0.3.27  USE64BITINT DYNAMIC_ARCH NO_AFFINITY Haswell MAX_THREADS=24",
                "pc file directory": r"D:/a/numpy/numpy/.openblas",
            },
        },
        "Python Information": {
            "path": r"C:\Users\runneradmin\AppData\Local\Temp\build-env-3q5ctiia\Scripts\python.exe",
            "version": "3.12",
        },
        "SIMD Extensions": {
            "baseline": __cpu_baseline__,
            "found": [
                feature for feature in __cpu_dispatch__ if __cpu_features__[feature]
            ],
            "not found": [
                feature for feature in __cpu_dispatch__ if not __cpu_features__[feature]
            ],
        },
    }
)


def _check_pyyaml():
    import yaml

    return yaml


def show(mode=DisplayModes.stdout.value):
    """
    Show libraries and system information on which NumPy was built
    and is being used

    Parameters
    ----------
    mode : {`'stdout'`, `'dicts'`}, optional.
        Indicates how to display the config information.
        `'stdout'` prints to console, `'dicts'` returns a dictionary
        of the configuration.

    Returns
    -------
    out : {`dict`, `None`}
        If mode is `'dicts'`, a dict is returned, else None

    See Also
    --------
    get_include : Returns the directory containing NumPy C
                  header files.

    Notes
    -----
    1. The `'stdout'` mode will give more readable
       output if ``pyyaml`` is installed

    """
    if mode == DisplayModes.stdout.value:
        try:  # Non-standard library, check import
            yaml = _check_pyyaml()

            print(yaml.dump(CONFIG))
        except ModuleNotFoundError:
            import warnings
            import json

            warnings.warn("Install `pyyaml` for better output", stacklevel=1)
            print(json.dumps(CONFIG, indent=2))
    elif mode == DisplayModes.dicts.value:
        return CONFIG
    else:
        raise AttributeError(
            f"Invalid `mode`, use one of: {', '.join([e.value for e in DisplayModes])}"
        )
