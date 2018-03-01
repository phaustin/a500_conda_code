cmake_minimum_required(VERSION 2.6)
#
#  expecting that CC and  FC environment variables
#  are set to the compilers
#
message("cmake source dir is ${CMAKE_SOURCE_DIR}")
if (NOT (DEFINED "ENV{PREFIX}"))
     set(PREFIX $ENV{CONDA_PREFIX})
else()
     set(PREFIX $ENV{PREFIX})
endif()
message("pha cmake installing in ${PREFIX}")
SET(CMAKE_C_COMPILER "$ENV{CC}")
SET(CMAKE_FORTRAN_COMPILER "$ENV{FC}")
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${PREFIX}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PREFIX}/lib)

enable_language(Fortran)
enable_language(C)

set (CMAKE_Fortran_FLAGS "-ffree-line-length-none -O2")
set(CMAKE_C_FLAGS "-DLINUX")
set(CMAKE_Fortran_MODULE_DIRECTORY  ${PREFIX}/include_fortran)
FILE(GLOB reader_f90 "${CMAKE_SOURCE_DIR}/fortran_src/*.f90")
set(SOURCES ${reader_f90})
message("here are the source files: ${SOURCES}")
INCLUDE_DIRECTORIES(${CMAKE_Fortran_MODULE_DIRECTORY})

set(LIBRARY_OUTPUT_PATH  ${PREFIX}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PREFIX/bin})

add_library(read3D STATIC ${SOURCES})
install(TARGETS read3D ARCHIVE DESTINATION ${PREFIX}/lib)
