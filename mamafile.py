import mama

class OpenBLAS(mama.BuildTarget):
    def dependencies(self):
        pass

    def configure(self):
        self.disable_cxx_compiler()
        self.add_cmake_options(
            'NOFORTRAN=TRUE',
            'BUILD_SHARED_LIBS=FALSE',
        #    'DYNAMIC_ARCH=TRUE',
        #    'BUILD_WITHOUT_LAPACK=TRUE',
        #    'BUILD_RELAPACK=TRUE'
        )
        if self.windows:
            self.add_cl_flags('/wd4244')
        if not self.windows:
            self.add_cl_flags('-fPIC')

