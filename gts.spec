%define major 5
%define api 0.7
%define libname	%mklibname %{name}%{api}_ %{major}
%define develname %mklibname %{name} -d

Summary:	3D modeling, animation, and rendering system
Name:		gts
Version:	0.7.6
Release:	%mkrel 10
License:	LGPLv2+
Group:		System/Libraries
URL:		http://gts.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/gts/%{name}-%{version}.tar.bz2
Patch0:		gts-0.7.6-fix-underlinking.patch
Patch1:		gts-0.7.6-netpbm.patch
BuildRequires:	netpbm-devel
BuildRequires:	pkgconfig(glib-2.0)
%ifarch x86_64
BuildRequires:	chrpath
%endif
Requires:	%{libname} = %{version}-%{release}

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
%patch1 -p0

%build
autoreconf -fi

%configure2_5x
%make

%install

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
%{multiarch_bindir}/gts-config
%{_bindir}/gts-config
%{_includedir}/*.h
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/gts.pc


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.6-10mdv2011.0
+ Revision: 611018
- rebuild

* Fri Apr 30 2010 Funda Wang <fwang@mandriva.org> 0.7.6-9mdv2010.1
+ Revision: 541276
- correct fix for netpbm

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Feb 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.6-8mdv2009.1
+ Revision: 339362
- new devel library policy
- new license policy
- Patch0: fix underlinking
- spec file clean
- obsolete/provide old devel library

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.7.6-5mdv2008.1
+ Revision: 140744
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Feb 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.6-5mdv2007.0
+ Revision: 126553
- incerase release tag
- fix obsoletes
- obsoletes libgts3
- correct deps

* Mon Feb 26 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.6-3mdv2007.1
+ Revision: 125959
- fix libification
- nuke rpath
- set %%multiarch on gst-config
- some minor changes

* Wed Nov 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.6-2mdv2007.1
+ Revision: 88327
- fix buildrequires
- oops, forgot new files
- new version
  drop libtool patch (usage unknown, and break build)
- Import gts

* Sun Jun 05 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.7.3-1mdk  
- first mdk package, contributed by Morreale Jean Roc  (<ihatedaspam@enoreth.net>)

