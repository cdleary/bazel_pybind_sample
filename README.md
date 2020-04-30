# Bazel / pybind11 sample

Simple, working pybind11-via-bazel example on Linux/x64 (tested on Ubuntu).

Background info provided by:

* pybind11 basics: https://pybind11.readthedocs.io/en/stable/basics.html
* `pybind11_bazel` readme: https://github.com/pybind/pybind11_bazel

If you're observing segfaults, it may be that the DSO is being built for
Python2 while the `bazel test` interpreter is Python 3.

You can observe what Python headers were used for building by observing the file in a path similar to:

`bazel-out/k8-fastbuild/bin/external/local_config_python/python_include/patchlevel.h`

And you can help point at the right Python binary by providing it to the
`python_configure.bzl` script in `pybind11_bazel` through an environment variable:

```
PYTHON_BIN_PATH=/usr/bin/python3 bazel test -c dbg :example_test --test_output=all
```
