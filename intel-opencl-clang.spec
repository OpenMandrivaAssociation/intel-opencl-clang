Name: intel-opencl-clang
Version: 21.1.1
Release: 1
Summary: Library to compile OpenCL C kernels to SPIR-V modules

License: NCSA
URL:     https://github.com/intel/opencl-clang
Source0: %{url}/archive/%{version}/opencl-clang-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: clang
BuildRequires: pkgconfig(libffi)
BuildRequires: make
BuildRequires: llvm-devel
BuildRequires: clang-devel
BuildRequires: pkgconfig(LLVMSPIRVLib)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(zlib)

%description
opencl-clang is a thin wrapper library around clang. The library has OpenCL-oriented API and
is capable to compile OpenCL C kernels to SPIR-V modules.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains libraries and header files for
developing against %{name}

%prep
%autosetup -n opencl-clang-%{version} -p1
#sed -i 's/$<TARGET_FILE:clang>/$<TARGET_FILE:clang%{?llvm_compat}>/' cl_headers/CMakeLists.txt

%build
%cmake \
    -DPREFERRED_LLVM_VERSION=21.1.8
#DLLVM_DIR=%{_libdir}/llvm%{?llvm_compat}/lib/cmake/llvm/
%make_build

%install
%make_install -C build

%files
%license LICENSE
%{_libdir}/libopencl-clang.so.*

%files devel
%{_libdir}/libopencl-clang.so
#{_includedir}/cclang/common_clang.h
%{_includedir}/cclang/opencl-c.h
%{_includedir}/cclang/opencl-c-base.h
%{_includedir}/cclang/module.modulemap
