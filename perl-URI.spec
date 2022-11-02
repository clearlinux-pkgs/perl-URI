#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-URI
Version  : 5.17
Release  : 56
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/URI-5.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/URI-5.17.tar.gz
Summary  : 'Uniform Resource Identifiers (absolute and relative)'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-URI-license = %{version}-%{release}
Requires: perl-URI-perl = %{version}-%{release}
Requires: perl(Business::ISBN)
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Test::Warnings)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution URI,
version 5.17:
Uniform Resource Identifiers (absolute and relative)

%package dev
Summary: dev components for the perl-URI package.
Group: Development
Provides: perl-URI-devel = %{version}-%{release}
Requires: perl-URI = %{version}-%{release}

%description dev
dev components for the perl-URI package.


%package license
Summary: license components for the perl-URI package.
Group: Default

%description license
license components for the perl-URI package.


%package perl
Summary: perl components for the perl-URI package.
Group: Default
Requires: perl-URI = %{version}-%{release}

%description perl
perl components for the perl-URI package.


%prep
%setup -q -n URI-5.17
cd %{_builddir}/URI-5.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-URI
cp %{_builddir}/URI-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-URI/1901d391230618a9285903a4c6442ebf9affa678 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/URI.3
/usr/share/man/man3/URI::Escape.3
/usr/share/man/man3/URI::Heuristic.3
/usr/share/man/man3/URI::QueryParam.3
/usr/share/man/man3/URI::Split.3
/usr/share/man/man3/URI::URL.3
/usr/share/man/man3/URI::WithBase.3
/usr/share/man/man3/URI::_punycode.3
/usr/share/man/man3/URI::data.3
/usr/share/man/man3/URI::file.3
/usr/share/man/man3/URI::ldap.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-URI/1901d391230618a9285903a4c6442ebf9affa678

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
