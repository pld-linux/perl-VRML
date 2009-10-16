#
# Conditional build:
%bcond_with	tests	# perform "make test" (needs working, not busy /dev/audio!)
#
%include	/usr/lib/rpm/macros.perl
Summary:	VRML Perl module - specification independent VRML methods (1.0, 2.0, 97)
Summary(pl.UTF-8):	Moduł Perla VRML - metody VRML niezależne od specyfikacji (1.0, 2.0, 97)
Name:		perl-VRML
Version:	1.10
Release:	1
License:	GPL v2+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/VRML/VRML-%{version}.tar.gz
# Source0-md5:	989d97ca95b49a032ea1d932dd0576bc
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These modules were conceived for the production of VRML worlds on WWW
servers via CGI and/or for generating abstract worlds. They are the
clarity of Perl scripts with VRML code to increase and (hopefully)
for VRML beginners the entrance in VRML facilitate.

%description -l pl.UTF-8
Te moduły były pomyślane do tworzenia światów VRML na serwerach WWW
poprzez CGI i/lub generowania abstrakcyjnych światów. Łączą klarowność
skryptów Perla z kodem VRML, aby uprzystępnić tworzenie VRML,
szczególnie początkującym.

%prep
%setup -q -n VRML-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.TXT
%{perl_vendorlib}/VRML.pm
%{perl_vendorlib}/VRML
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
