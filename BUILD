load("@pybind11_bazel//:build_defs.bzl", "pybind_extension")

pybind_extension(
    name = "my_pb_mod",  # This name is not actually created!
    srcs = ["my_pb_mod.cc"],
)

py_library(
    name = "my_pb_mod",
    data = [":my_pb_mod.so"],
)

py_test(
    name = "example_test",
    srcs = ["example_test.py"],
    deps = [
        ":my_pb_mod"
    ],
)
