cmake_minimum_required(VERSION 3.20 FATAL_ERROR)
project(12865 VERSION 1.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

if (MSVC)
    set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)
else ()
    set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin/${CMAKE_BUILD_TYPE})
endif ()

set(OUTPUT_ELF ${CMAKE_PROJECT_NAME})

set(SRC_FILES
        ${CMAKE_PROJECT_NAME}.cpp
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
