#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#include <iostream>
#include <cstdint>

#include "pybind11/pybind11.h"

int add_them(int j, int  k){
    return j + k;
  }

namespace py = pybind11;

PYBIND11_PLUGIN(do_add) {

  py::module m("do_add", R"pbdoc(
        Pybind11 example plugin
    )pbdoc");

    m.def("add_them", &add_them, R"pbdoc(
       add two numbers
    )pbdoc");

#ifdef VERSION_INFO
    m.attr("__version__") = py::str(VERSION_INFO);
#else
    m.attr("__version__") = py::str("dev");
#endif

    return m.ptr();
}
