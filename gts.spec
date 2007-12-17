%define major 5
%define api 0.7
%define libname	%mklibname %{name}%{api}_ %{major}

Name:    	gts
Version: 	0.7.6
Release: 	%mkrel 5
Summary: 	3D modeling, animation, and rendering system
License: 	GPL
Group: 	 	System/Libraries
URL:		http://gts.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/gts/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig
BuildRequires:	netpbm-devel
BuildRequires:	glib-devel
%ifarch x86_64
BuildRequires:	chrpath
%endif

%description
This is the GTS library. GTS stands for the GNU Triangulated
Surface Library. It includes a number of useful functions to deal with
triangulated surfaces including, but not limited to, multi-resolution
models, Delaunay and Constrained Delaunay triangulations, set operations on
surfaces (intersection, union etc ...), bounding-boxes trees for efficient
collision and intersection detection, triangle strips generation for fast
rendering.

%package -n	%{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries
Obsoletes:	%mklibname gts 3

%description -n	%{libname}
Libraries for %{name}.

%package -n	%{libname}-devel
Summary:	Headers for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d gts 3

%description -n	%{libname}-devel
Development headers and libraries for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%ifarch x86_64
chrpath -d %{buildroot}%{_bindir}/delaunay
chrpath -d %{buildroot}%{_bindir}/gts2dxf
chrpath -d %{buildroot}%{_bindir}/gts2oogl
chrpath -d %{buildroot}%{_bindir}/gts2stl
chrpath -d %{buildroot}%{_bindir}/gtscheck
chrpath -d %{buildroot}%{_bindir}/gtscompare
chrpath -d %{buildroot}%{_bindir}/happrox
chrpath -d %{buildroot}%{_bindir}/stl2gts
chrpath -d %{buildroot}%{_bindir}/transform
%endif

%multiarch_binaries %{buildroot}%{_bindir}/gts-config

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/gts2dxf
%{_bindir}/gts2oogl
%{_bindir}/gts2stl
%{_bindir}/gtscheck
%{_bindir}/stl2gts
%{_bindir}/transform
%{_bindir}/gtscompare
%{_bindir}/gtstemplate
%{_bindir}/delaunay
%{_bindir}/happrox
%{_datadir}/aclocal/gts.m4

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*%{api}.so.%{major}*

%files -n %{libname}-devel
%defattr(-,root,root)
%multiarch %{multiarch_bindir}/gts-config
%{_bindir}/gts-config
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/gts.pc


