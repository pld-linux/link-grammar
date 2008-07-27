Summary:	Link Grammar - a syntactic parser of English
Summary(pl.UTF-8):	Link Grammar - składniowy analizator języka angielskiego
Name:		link-grammar
Version:	4.2.2
Release:	2
License:	BSD
Group:		Libraries
Source0:	http://www.abisource.com/downloads/link-grammar/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	798c165b7d7f26e60925c30515c45782
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

%description -l pl.UTF-8
Parser Link Grammar to składniowy analizator języka angielskiego
oparty na gramatyce łączeń - oryginalnej teorii składni języka
angielskiego. Po podaniu zdania system przypisuje mu strukturę
składniową, składającą się ze zbioru oznaczonych łączeń wiążących pary
słów. Analizator tworzy także składową reprezentację zdania
(pokazującą frazy rzeczownika, frazy czasownika itp.).

%package devel
Summary:	Header files for link-grammar library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki link-grammar
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for link-grammar library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki link-grammar.

%package static
Summary:	Static link-grammar library
Summary(pl.UTF-8):	Statyczna biblioteka link-grammar
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static link-grammar library.

%description static -l pl.UTF-8
Statyczna biblioteka link-grammar.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure \
	--disable-binreloc

%{__make} -j1

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
