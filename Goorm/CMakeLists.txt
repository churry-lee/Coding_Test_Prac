cmake_minimum_required(VERSION 3.26 FATAL_ERROR)
project(out VERSION 1.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_C_COMPILER "/Library/Developer/CommandLineTools/usr/bin/clang")
set(CMAKE_CXX_COMPILER "/Library/Developer/CommandLineTools/usr/bin/clang++")

if (MSVC)
    set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
else ()
    set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin/${CMAKE_BUILD_TYPE})
endif ()

set(OUTPUT_ELF ${CMAKE_PROJECT_NAME})

set(SRC_FILES
        level2/체크카드.cpp
)

add_executable(${OUTPUT_ELF}
        ${SRC_FILES}
)

target_compile_definitions( ${OUTPUT_ELF} PUBLIC
        EXCUTABLE_OUTPUT_PATH="${EXECUTABLE_OUTPUT_PATH}"
        PROJECT_PATH="${PROJECT_SOURCE_DIR}"
        PROJECT_TITLE="${PROJECT_NAME}_v${PROJECT_VERSION_MAJOR}${PROJECT_VERSION_MINOR}"
)


if (MSVC)
    target_compile_options(${OUTPUT_ELF} PUBLIC /W3)
else()
    target_compile_options(${OUTPUT_ELF} PUBLIC -Wall -Wextra -O3)
endif(MSVC)
