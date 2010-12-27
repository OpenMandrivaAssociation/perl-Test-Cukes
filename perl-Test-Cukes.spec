%define upstream_name    Test-Cukes
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    A BBD test tool inspired by Cucumber
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Any::Moose)
BuildRequires: perl(Carp::Assert)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::Builder::Module)
BuildRequires: perl(Test::More)
BuildRequires: perl(Try::Tiny)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Test::Cukes is a testing tool inspired by Cucumber (the http://cukes.info
manpage). It lets your write your module test with scenarios. It may be
used with the Test::More manpage or other family of TAP 'Test::*' modules.
It uses the Test::Builder::note manpage function internally to print
messages.

This module implements the Given-When-Then clause only in English. To uses
it in the test programs, feed the feature text into 'feature' function,
defines your step handlers, and then run all the tests by calling
'runtests'. Step handlers may be defined in separate modules, as long as
those modules are included before 'runtests' is called. Each step may use
either 'assert' or standard TAP functions such as 'Test::Simple''s 'ok' or
'Test::More''s 'is' to verify desired result. If you specify a plan
explicitly, you should be aware that each step line in your scenario runs
an additional test, and will therefore add to the number of tests you must
indicate.

If any assertion in the Given block failed, the following 'When' and 'Then'
blocks are all skipped.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


