#
# Conditional build:
%bcond_without	java	# Java bindings
%bcond_without	perl	# Perl bindings
%bcond_without	python	# Python 3 bindings

%{?with_java:%{?use_default_jdk}}

Summary:	Link Grammar - a syntactic parser of English
Summary(pl.UTF-8):	Link Grammar - składniowy analizator języka angielskiego
Name:		link-grammar
Version:	5.12.3
Release:	5
License:	LGPL v2.1
Group:		Libraries
Source0:	http://www.nl.abisource.com/downloads/link-grammar/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8550f72456a51d495ee020f9ece89411
Patch0:		%{name}-modules.patch
URL:		http://www.link.cs.cmu.edu/link/
%{?with_java:BuildRequires:	ant}
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gcc >= 6:4.7
%{?with_java:%buildrequires_jdk}
BuildRequires:	hunspell-devel
BuildRequires:	libedit-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2
BuildRequires:	pcre2-8-devel
%{?with_perl:BuildRequires:	perl-devel}
BuildRequires:	pkgconfig
%{?with_perl:BuildRequires:	swig-perl >= 2.0.0}
%if %{with python}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	swig-python >= 2.0.0
%endif
BuildRequires:	rpmbuild(macros) >= 2.021
BuildRequires:	sqlite3-devel >= 3.0.0
BuildRequires:	zlib-devel
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

%package -n java-link-grammar
Summary:	Java binding for link-grammar library
Summary(pl.UTF-8):	Wiązanie Javy do biblioteki link-grammar
Group:		Libraries/Java
Requires:	%{name} = %{version}-%{release}

%description -n java-link-grammar
Java binding for link-grammar library.

%description -n java-link-grammar -l pl.UTF-8
Wiązanie Javy do biblioteki link-grammar.

%package -n perl-linkgrammar
Summary:	Perl binding for link-grammar library
Summary(pl.UTF-8):	Wiązanie Perla do biblioteki link-grammar
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description -n perl-linkgrammar
Perl binding for link-grammar library.

%description -n perl-linkgrammar -l pl.UTF-8
Wiązanie Perla do biblioteki link-grammar.

%package -n python3-linkgrammar
Summary:	Python 3 binding for link-grammar library
Summary(pl.UTF-8):	Wiązanie Pythona 3 do biblioteki link-grammar
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-libs >= 1:3.4

%description -n python3-linkgrammar
Python 3 binding for link-grammar library.

%description -n python3-linkgrammar -l pl.UTF-8
Wiązanie Pythona 3 do biblioteki link-grammar.

%prep
%setup -q
%patch -P 0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%{?with_java:export JAVA_HOME="%{java_home}"}
%configure \
	%{!?with_java:--disable-java-bindings} \
	%{?with_perl:--enable-perl-bindings} \
	%{!?with_python:--disable-python-bindings} \
	--disable-silent-rules

%{__make} -j1 \
	pkgperldir=%{perl_vendorarch}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgperldir=%{perl_vendorarch}

%if %{with java}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/liblink-grammar-java.la \
	$RPM_BUILD_ROOT%{_libdir}/liblink-grammar-java.a
%endif
%if %{with perl}
%{__rm}	$RPM_BUILD_ROOT%{perl_vendorarch}/clinkgrammar.la \
	$RPM_BUILD_ROOT%{perl_vendorarch}/clinkgrammar.a
%endif
%if %{with python}
%{__rm}	$RPM_BUILD_ROOT%{py3_sitedir}/linkgrammar/_clinkgrammar.la \
	$RPM_BUILD_ROOT%{py3_sitedir}/linkgrammar/_clinkgrammar.a

%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE MAINTAINERS NEWS README.md TODO
%attr(755,root,root) %{_bindir}/link-generator
%attr(755,root,root) %{_bindir}/link-parser
%attr(755,root,root) %{_libdir}/liblink-grammar.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblink-grammar.so.5
%{_datadir}/link-grammar
%{_mandir}/man1/link-generator.1*
%{_mandir}/man1/link-parser.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblink-grammar.so
%{_libdir}/liblink-grammar.la
%{_includedir}/link-grammar
%{_pkgconfigdir}/link-grammar.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/liblink-grammar.a

%if %{with java}
%files -n java-link-grammar
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblink-grammar-java.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblink-grammar-java.so.5
%attr(755,root,root) %{_libdir}/liblink-grammar-java.so
%{_javadir}/linkgrammar-%{version}.jar
%{_javadir}/linkgrammar.jar
%endif

%if %{with perl}
%files -n perl-linkgrammar
%defattr(644,root,root,755)
%attr(755,root,root) %{perl_vendorarch}/clinkgrammar.so
%{perl_vendorarch}/clinkgrammar.pm
%endif

%if %{with python}
%files -n python3-linkgrammar
%defattr(644,root,root,755)
%dir %{py3_sitedir}/linkgrammar
%attr(755,root,root) %{py3_sitedir}/linkgrammar/_clinkgrammar.so
%{py3_sitescriptdir}/linkgrammar
%{py3_sitescriptdir}/linkgrammar.pth
%endif
