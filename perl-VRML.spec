%include	/usr/lib/rpm/macros.perl
Summary:	VRML - Specification independent VRML methods (1.0, 2.0, 97)
Name:		perl-VRML
Version:	1.04
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/VRML/VRML-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These modules were conceived for the production of VRML worlds on WWW
servers via GCI and/or for generating abstract worlds. They are the
clarity of Perl scripts with VRML code to increase and (hopefully)
for VRML beginners the entrance in VRML facilitate. In the following
the modules are described briefly.

%prep
%setup -q -n VRML-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf *.TXT 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/VRML.pm
%{perl_sitelib}/VRML
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
