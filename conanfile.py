from conans import ConanFile, CMake, tools


class PiorunConan(ConanFile):
    name = "Piorun"
    version = "0.0.1"
    license = "MIT license"
    author = "enrique.chen@live.cn"
    url = "github.com/enriqueChen/Piorun"
    description = "message queue consumer powered by C++"
    topics = ("worker")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = ["ycm", "cmake", "cmake_find_package"]

    def source(self):
        self.run("git clone https://github.com/enriqur/Piorun.git")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("hello/CMakeLists.txt", "PROJECT(HelloWorld)",
                              '''PROJECT(HelloWorld)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="hello")
        self.copy("*hello.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Piorun"]

    def requirements(self):
        self.requires("docopt/0.6.2@conan/stable", private=False, override=False)
