%define major 1
%define libname %mklibname git2 %{major}
%define devname %mklibname git2 -d

Name: libgit2
Version:	1.5.0
Release:	1
Source0: https://github.com/libgit2/libgit2/archive/v%{version}/%{name}-%{version}.tar.gz
Summary: Git core methods provided as a re-entrant linkable library
URL: http://libgit2.github.com
License: GPLv2 with linking exception
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: python
BuildRequires: http-parser-devel
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libssh2)
BuildRequires: pkgconfig(zlib)
Requires: %{libname} = %{EVRD}

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
	  -DSHA1_BACKEND=OpenSSL \
	  -DUSE_SSH=ON

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja install -C build

%files
%{_bindir}/git2_cli

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
