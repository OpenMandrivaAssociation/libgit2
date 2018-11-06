%define major 26
%define libname %mklibname git2 %{major}
%define devname %mklibname git2 -d

Name: libgit2
Version: 0.26.8
Release: 1
Source0: https://github.com/%{name}/%{name}/archive/%{name}-%{version}.tar.gz
Summary: Git core methods provided as a re-entrant linkable library
URL: http://libgit2.github.com
License: GPLv2 with linking exception
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: python2
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(zlib)

%description
Git core methods provided as a re-entrant linkable library

%package -n %{libname}
Summary: Git core methods provided as a re-entrant linkable library
Group: System/Libraries

%description -n %{libname}
Git core methods provided as a re-entrant linkable library

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake -G Ninja \
	-DPYTHON_EXECUTABLE:FILEPATH=%{_bindir}/python2

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/*.so.0*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
