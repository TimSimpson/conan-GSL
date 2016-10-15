from conans import ConanFile, CMake, tools
import os


class GSLConan(ConanFile):
    name = "GSL"
    version = "0.0.0.0-2"
    license = "The MIT License"
    url = "https://github.com/TimSimpson/conan-GSL"

    def source(self):
       self.run("git clone https://github.com/Microsoft/GSL.git")
       self.run("cd GSL && git checkout 9ef335ce32a2287a810fc51dd2f9abd63e852ddf")

    def package(self):
        self.copy("*", dst="include/gsl", src="gsl/gsl")
