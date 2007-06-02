#
Summary:	Maemo osso-help library
Name:		libosso-help
Version:	2.0.9
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://repository.maemo.org/pool/bora/free/source/libosso-help_2.0.9-1.tar.gz
# Source0-md5:	eb53cc209a7b86b5957df7395400a14e
Patch0:	%{name}-configure.patch
Patch1:	%{name}-gtkhtml.patch
URL:		http://maemo.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	intltool
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In-place editor library for the Maemo platform.

%package devel
Summary:	Header files for libosso-help
Group:		Development/Libraries

%description devel
Header files for libosso-help.

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
%patch0 -p1
%patch1 -p1

%build
%{__glib_gettextize}
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
%doc AUTHORS ChangeLog NEWS README

%files devel
%defattr(644,root,root,755)

%files static
%defattr(644,root,root,755)
