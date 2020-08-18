Summary:	rpcsvc proto.x files and rpcgen tool
Summary(pl.UTF-8):	Pliki rpcsvc proto.x oraz narzędzie rpcgen
Name:		rpcsvc-proto
Version:	1.4.2
Release:	1
License:	BSD
Group:		Libraries
Source0:	https://github.com/thkukuk/rpcsvc-proto/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	629c91bbc8281fcdf64442f59a9d1705
# based on glibc 2.31
Patch0:		%{name}-locales.patch
URL:		https://github.com/thkukuk/rpcsvc-proto
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
# glibc used to include proto.x files in glibc-headers and rpcgen in main package
Requires:	glibc-headers >= 6:2.32
Conflicts:	glibc < 6:2.32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains rpcsvc proto.x files from glibc, which are
missing in libtirpc. Additionally it contains rpcgen, which is needed
to create header files and sources from protocol files.

This package is only needed for glibc versions without the deprecated
sunrpc functionality and libtirpc should replace it.

%description -l pl.UTF-8
Ten pakiet zawiera pliki rpcsvc proto.x z glibc, których brakuje w
libtirpc. Dodatkowo zawiera narzędzie rpcgen, potrzebne do tworzenia
plików nagłówkowych i źródłowych z plików protokołów.

Ten pakiet jest potrzebny tylko dla wersji glibc bez przestarzałej
funkcjonalności sunrpc, kiedy libtirpc ma ją zastąpić.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/rpcgen
%{_mandir}/man1/rpcgen.1*
%{_includedir}/rpcsvc
