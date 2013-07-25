%define upstream_name    File-ChangeNotify
%define upstream_version 0.23

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(IO::KQueue\\)'
%else
%define _requires_exceptions perl(IO::KQueue)
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.23
Release:	1

Summary:	Inotify-based watcher subclass
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/File-ChangeNotify-0.23.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::MOP)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Module::Pluggable::Object)
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Params::Validate)
BuildRequires:	perl(MooseX::SemiAffordanceAccessor)
BuildRequires:	perl(namespace::autoclean)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::HiRes)

BuildArch: noarch

%description
This module provides an API for creating a the File::ChangeNotify::Watcher
manpage subclass that will work on your platform.

Most of the documentation for this distro is in the
File::ChangeNotify::Watcher manpage.

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
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.190.0-2mdv2011.0
+ Revision: 656911
- rebuild for updated spec-helper

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.190.0-1mdv2011.0
+ Revision: 596034
- update to new version 0.19

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2011.0
+ Revision: 552700
- update to 0.16

* Mon Mar 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.130.0-1mdv2010.1
+ Revision: 528782
- adding missing buildrequires:
- update to 0.13

* Fri Jan 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.120.0-1mdv2010.1
+ Revision: 497913
- update to 0.12

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.110.0-1mdv2010.1
+ Revision: 474657
- update to 0.11

* Tue Nov 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.1
+ Revision: 463916
- update to 0.09

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-2mdv2010.1
+ Revision: 461716
- require exception for io::kqueue, which is bsd-only

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.1
+ Revision: 461278
- update to 0.08

* Wed Jul 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 393645
- import perl-File-ChangeNotify


* Wed Jul 08 2009 cpan2dist 0.07-1mdv
- initial mdv release, generated with cpan2dist

