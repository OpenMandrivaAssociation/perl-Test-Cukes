%define upstream_name    Test-Cukes
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A BBD test tool inspired by Cucumber
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(Carp::Assert)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::Builder::Module)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Try::Tiny)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2mdv2011.0
+ Revision: 657841
- rebuild for updated spec-helper

* Mon Dec 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 625381
- fix automatic dependencies
- update to new version 0.10

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 542847
- import perl-Test-Cukes


* Thu May 06 2010 cpan2dist 0.09-1mdv
- initial mdv release, generated with cpan2dist
