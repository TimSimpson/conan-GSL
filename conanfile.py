from conans import ConanFile, CMake, tools
import os


class GSLConan(ConanFile):
    name = "GSL"
    version = "0.0.0.0-1"
    license = "The MIT License"
    url = "https://github.com/TimSimpson/conan-GSL"

    def source(self):
       self.run("git clone https://github.com/Microsoft/GSL.git")
       self.run("cd GSL && git checkout 0535138459d0f78e39a2e558bc239f5727eaa13c")

    def package(self):
        self.copy("*", dst="include", src="GSL/include")
