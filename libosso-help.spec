Summary:	Maemo OSSO Help library
Summary(pl.UTF-8):	Biblioteka Maemo OSSO Help
Name:		libosso-help
Version:	2.0.9
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://repository.maemo.org/pool/bora/free/source/%{name}_%{version}-1.tar.gz
# Source0-md5:	eb53cc209a7b86b5957df7395400a14e
Patch0:		%{name}-configure.patch
Patch1:		%{name}-gtkhtml.patch
URL:		http://maemo.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	gtk+2-devel >= 2:2.6
BuildRequires:	gtkhtml-devel >= 3.14
BuildRequires:	hildon-libs-devel >= 0.9.4
BuildRequires:	libjpeg-devel
BuildRequires:	libosso-devel >= 1.0.0
BuildRequires:	libpng-devel
BuildRequires:	libxml2-devel >= 1:2.6.7
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OSSO Help library for Maemo platform.

%description -l pl.UTF-8
Biblioteka OSSO Help dla platformy Maemo.

%package devel
Summary:	Header files for libosso-help
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libosso-help
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.6
Requires:	gtk+2-devel >= 2:2.6
Requires:	gtkhtml-devel >= 3.14
Requires:	hildon-libs-devel >= 0.9.4
Requires:	libjpeg-devel
Requires:	libosso-devel >= 1.0.0
Requires:	libpng-devel
Requires:	libxml2-devel >= 1:2.6.7

%description devel
Header files for libosso-help.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libosso-help.

%package static
Summary:	Static libosso-help library
Summary(pl.UTF-8):	Statyczna biblioteka libosso-help
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libosso-help library.

%description static -l pl.UTF-8
Statyczna biblioteka libosso-help.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_libdir}/libossohelp.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libossohelp.so
%{_libdir}/libossohelp.la
%{_includedir}/osso-helplib*.h
%{_pkgconfigdir}/libossohelp.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libossohelp.a
