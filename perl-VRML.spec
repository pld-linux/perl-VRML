%include	/usr/lib/rpm/macros.perl
Summary:	VRML Perl module - specification independent VRML methods (1.0, 2.0, 97)
Summary(pl):	Modu³ Perla VRML - metody VRML niezale¿ne od specyfikacji (1.0, 2.0, 97)
Name:		perl-VRML
Version:	1.04
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/VRML/VRML-%{version}.tar.gz
# Source0-md5:	99899892d24042997d1b569fb64839b9
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These modules were conceived for the production of VRML worlds on WWW
servers via CGI and/or for generating abstract worlds. They are the
clarity of Perl scripts with VRML code to increase and (hopefully)
for VRML beginners the entrance in VRML facilitate.

%description -l pl
Te modu³y by³y pomy¶lane do tworzenia ¶wiatów VRML na serwerach WWW
poprzez CGI i/lub generowania abstrakcyjnych ¶wiatów. £±cz± klarowno¶æ
skryptów Perla z kodem VRML, aby uprzystêpniæ tworzenie VRML,
szczególnie pocz±tkuj±cym.

%prep
%setup -q -n VRML-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

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
