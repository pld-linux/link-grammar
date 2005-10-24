Summary:	Link Grammar - a syntactic parser of English
Summary(pl):	Link Grammar - sk³adniowy analizator jêzyka angielskiego
Name:		link-grammar
Version:	4.1.3
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://www.abisource.com/downloads/link-grammar/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5edbeab4b9e3f61b343e68206708703e
URL:		http://www.link.cs.cmu.edu/link/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Link Grammar Parser is a syntactic parser of English, based on
link grammar, an original theory of English syntax. Given a sentence,
the system assigns to it a syntactic structure, which consists of a
set of labeled links connecting pairs of words. The parser also
produces a "constituent" representation of a sentence (showing noun
phrases, verb phrases, etc.).

%description -l pl
Parser Link Grammar to sk³adniowy analizator jêzyka angielskiego
oparty na gramatyce ³±czeñ - oryginalnej teorii sk³adni jêzyka
angielskiego. Po podaniu zdania system przypisuje mu strukturê
sk³adniow±, sk³adaj±c± siê ze zbioru oznaczonych ³±czeñ wi±¿±cych pary
s³ów. Analizator tworzy tak¿e sk³adow± reprezentacjê zdania
(pokazuj±c± frazy rzeczownika, frazy czasownika itp.).

%package devel
Summary:	Header files for link-grammar library
Summary(pl):	Pliki nag³ówkowe biblioteki link-grammar
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for link-grammar library.

%description devel -l pl
Pliki nag³ówkowe biblioteki link-grammar.

%package static
Summary:	Static link-grammar library
Summary(pl):	Statyczna biblioteka link-grammar
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static link-grammar library.

%description static -l pl
Statyczna biblioteka link-grammar.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure \
	--disable-binreloc

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
%doc LICENSE README
%attr(755,root,root) %{_bindir}/grammar-parse
%attr(755,root,root) %{_libdir}/liblink-grammar.so.*.*.*
%{_datadir}/link-grammar

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblink-grammar.so
%{_libdir}/liblink-grammar.la
%{_includedir}/link-grammar
%{_pkgconfigdir}/link-grammar.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblink-grammar.a
