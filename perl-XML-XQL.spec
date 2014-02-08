%define upstream_name    XML-XQL
%define upstream_version 0.68

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	XML::XQL - query XML tree structures with XQL
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-XML-DOM >= 1.29
BuildRequires:	perl(Date::Manip) >= 5.33
BuildRequires:	perl-Parse-Yapp
BuildRequires:	perl-XML-Parser >= 2.30
BuildArch:	noarch

%description
This is a Perl extension that allows you to perform XQL queries on XML
object trees. Currently only the XML::DOM module is supported, but
other implementations, like XML::Grove, may soon follow.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make
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
%{_mandir}/*/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.680.0-2mdv2011.0
+ Revision: 667464
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.680.0-1mdv2011.0
+ Revision: 401812
- rebuild using %%perl_convert_version
- fixed license field

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.68-6mdv2009.1
+ Revision: 351654
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.68-5mdv2009.0
+ Revision: 224677
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.68-4mdv2008.1
+ Revision: 180664
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.68-3mdv2007.0
+ Revision: 85630
- Import perl-XML-XQL

* Mon Nov 20 2006 Oden Eriksson <oeriksson@mandriva.com> 0.68-3
- use the %%mkrel macro

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.68-2mdk
- fix deps

* Sat Jul 16 2005 Oden Eriksson <oeriksson@mandriva.com> 0.68-1mdk
- initial Mandriva package

