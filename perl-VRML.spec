%include	/usr/lib/rpm/macros.perl
Summary:	VRML perl module
Summary(pl):	Modu³ perla VRML
Name:		perl-VRML
Version:	1.04
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/VRML/VRML-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VRML perl module.

%description -l pl
Modu³ perla VRML.

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
