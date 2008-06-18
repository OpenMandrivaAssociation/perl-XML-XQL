%define real_name XML-XQL

Summary:	XML::XQL - query XML tree structures with XQL
Name:		perl-%{real_name}
Version:	0.68
Release:	%mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TJ/TJMATHER/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-XML-DOM >= 1.29
BuildRequires:	perl(Date::Manip) >= 5.33
BuildRequires:	perl-Parse-Yapp
BuildRequires:	perl-XML-Parser >= 2.30
BuildArch:	noarch
Provides:	perl-libxml-enno
Obsoletes:	perl-libxml-enno
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a Perl extension that allows you to perform XQL queries on XML
object trees. Currently only the XML::DOM module is supported, but
other implementations, like XML::Grove, may soon follow.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%dir %{perl_vendorlib}/XML/XQL
%{perl_vendorlib}/XML/XQL.pm
%{perl_vendorlib}/XML/XQL/*.pm
%{perl_vendorlib}/XML/XQL/*.pod
%{_mandir}/*/*


