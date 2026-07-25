%define modname	XML-XQL
%define modver	0.68

Summary:	XML::XQL - query XML tree structures with XQL
Name:		perl-%{modname}
Version:	%{modver}
Release:	18
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/XML-XQL
Source0:	https://cpan.metacpan.org/authors/id/T/TJ/TJMATHER/XML-XQL-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-XML-DOM >= 1.29
BuildRequires:	perl(Date::Manip) >= 5.33
BuildRequires:	perl-Parse-Yapp
BuildRequires:	perl-XML-Parser >= 2.30

%description
This is a Perl extension that allows you to perform XQL queries on XML
object trees. Currently only the XML::DOM module is supported, but
other implementations, like XML::Grove, may soon follow.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/XML/XQL
%{perl_vendorlib}/XML/XQL.pm
%{perl_vendorlib}/XML/XQL/*.pm
%{perl_vendorlib}/XML/XQL/*.pod
%{_mandir}/man3/*

