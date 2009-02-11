%define major 5
%define api 0.7
%define libname	%mklibname %{name}%{api}_ %{major}
%define develname %mklibname %{name} -d

Summary:	3D modeling, animation, and rendering system
Name:		gts
Version:	0.7.6
Release:	%mkrel 8
License:	LGPLv2+
Group:		System/Libraries
URL:		http://gts.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/gts/%{name}-%{version}.tar.bz2
Patch0:		gts-0.7.6-fix-underlinking.patch
BuildRequires:	netpbm-devel
BuildRequires:	glib2-devel
%ifarch x86_64
BuildRequires:	chrpath
%endif
Requires:	%{libname} = %{version}-%{release}
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This is the GTS library. GTS stands for the GNU Triangulated
Surface Library. It includes a number of useful functions to deal with
triangulated surfaces including, but not limited to, multi-resolution
models, Delaunay and Constrained Delaunay triangulations, set operations on
surfaces (intersection, union etc ...), bounding-boxes trees for efficient
collision and intersection detection, triangle strips generation for fast
rendering.

%package -n %{libname}
Summary:	Libraries for %{name}
Group:		System/Libraries
Obsoletes:	%mklibname gts 3
Requires:	%{name} = %{version}-%{release}

%description -n	%{libname}
Libraries for %{name}.

%package -n %{develname}
Summary:	Headers for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname gts 3 -d}
Obsoletes:	%{mklibname %{name}0.7_ 5 -d} < 0.7.6-8
Provides:	%{mklibname %{name}0.7_ 5 -d}

%description -n	%{develname}
Development headers and libraries for %{name}.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi

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

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README
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

%files -n %{develname}
%defattr(-,root,root)
%multiarch %{multiarch_bindir}/gts-config
%{_bindir}/gts-config
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/gts.pc
