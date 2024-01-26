#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v3
# autospec commit: fae1327
#
Name     : perl-URI
Version  : 5.24
Release  : 63
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/URI-5.24.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/URI-5.24.tar.gz
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution URI,
version 5.24:
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
%setup -q -n URI-5.24
cd %{_builddir}/URI-5.24
pushd ..
cp -a URI-5.24 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
cp %{_builddir}/URI-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-URI/46f8922a53eef3bc16b11460b9091e42c3351881 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/share/man/man3/URI::icap.3
/usr/share/man/man3/URI::icaps.3
/usr/share/man/man3/URI::ldap.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-URI/46f8922a53eef3bc16b11460b9091e42c3351881

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
