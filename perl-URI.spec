#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-URI
Version  : 5.10
Release  : 48
URL      : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/URI-5.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OA/OALDERS/URI-5.10.tar.gz
Summary  : 'Uniform Resource Identifiers (absolute and relative)'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-URI-perl = %{version}-%{release}
Requires: perl(Business::ISBN)
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Needs)

%description
This archive contains the distribution URI,
version 5.10:
Uniform Resource Identifiers (absolute and relative)

%package dev
Summary: dev components for the perl-URI package.
Group: Development
Provides: perl-URI-devel = %{version}-%{release}
Requires: perl-URI = %{version}-%{release}

%description dev
dev components for the perl-URI package.


%package perl
Summary: perl components for the perl-URI package.
Group: Default
Requires: perl-URI = %{version}-%{release}

%description perl
perl components for the perl-URI package.


%prep
%setup -q -n URI-5.10
cd %{_builddir}/URI-5.10

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

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/URI.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/Escape.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/Heuristic.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/IRI.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/QueryParam.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/Split.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/URL.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/WithBase.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/_foreign.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/_generic.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/_idna.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/_ldap.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/_login.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/_punycode.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/_query.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/_segment.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/_server.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/_userpass.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/data.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/file.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/file/Base.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/file/FAT.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/file/Mac.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/file/OS2.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/file/QNX.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/file/Unix.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/file/Win32.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/ftp.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/gopher.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/http.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/https.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/ldap.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/ldapi.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/ldaps.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/mailto.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/mms.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/news.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/nntp.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/nntps.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/pop.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/rlogin.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/rsync.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/rtsp.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/rtspu.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/sftp.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/sip.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/sips.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/snews.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/ssh.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/telnet.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/tn3270.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/urn.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/urn/isbn.pm
/usr/lib/perl5/vendor_perl/5.34.0/URI/urn/oid.pm
