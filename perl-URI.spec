#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-URI
Version  : 1.74
Release  : 27
URL      : https://www.cpan.org/authors/id/E/ET/ETHER/URI-1.74.tar.gz
Source0  : https://www.cpan.org/authors/id/E/ET/ETHER/URI-1.74.tar.gz
Summary  : 'Uniform Resource Identifiers (absolute and relative)'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-URI-doc
BuildRequires : perl(Test::Needs)

%description
No detailed description available

%package doc
Summary: doc components for the perl-URI package.
Group: Documentation

%description doc
doc components for the perl-URI package.


%prep
%setup -q -n URI-1.74

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/URI.pm
/usr/lib/perl5/site_perl/5.26.1/URI/Escape.pm
/usr/lib/perl5/site_perl/5.26.1/URI/Heuristic.pm
/usr/lib/perl5/site_perl/5.26.1/URI/IRI.pm
/usr/lib/perl5/site_perl/5.26.1/URI/QueryParam.pm
/usr/lib/perl5/site_perl/5.26.1/URI/Split.pm
/usr/lib/perl5/site_perl/5.26.1/URI/URL.pm
/usr/lib/perl5/site_perl/5.26.1/URI/WithBase.pm
/usr/lib/perl5/site_perl/5.26.1/URI/_foreign.pm
/usr/lib/perl5/site_perl/5.26.1/URI/_generic.pm
/usr/lib/perl5/site_perl/5.26.1/URI/_idna.pm
/usr/lib/perl5/site_perl/5.26.1/URI/_ldap.pm
/usr/lib/perl5/site_perl/5.26.1/URI/_login.pm
/usr/lib/perl5/site_perl/5.26.1/URI/_punycode.pm
/usr/lib/perl5/site_perl/5.26.1/URI/_query.pm
/usr/lib/perl5/site_perl/5.26.1/URI/_segment.pm
/usr/lib/perl5/site_perl/5.26.1/URI/_server.pm
/usr/lib/perl5/site_perl/5.26.1/URI/_userpass.pm
/usr/lib/perl5/site_perl/5.26.1/URI/data.pm
/usr/lib/perl5/site_perl/5.26.1/URI/file.pm
/usr/lib/perl5/site_perl/5.26.1/URI/file/Base.pm
/usr/lib/perl5/site_perl/5.26.1/URI/file/FAT.pm
/usr/lib/perl5/site_perl/5.26.1/URI/file/Mac.pm
/usr/lib/perl5/site_perl/5.26.1/URI/file/OS2.pm
/usr/lib/perl5/site_perl/5.26.1/URI/file/QNX.pm
/usr/lib/perl5/site_perl/5.26.1/URI/file/Unix.pm
/usr/lib/perl5/site_perl/5.26.1/URI/file/Win32.pm
/usr/lib/perl5/site_perl/5.26.1/URI/ftp.pm
/usr/lib/perl5/site_perl/5.26.1/URI/gopher.pm
/usr/lib/perl5/site_perl/5.26.1/URI/http.pm
/usr/lib/perl5/site_perl/5.26.1/URI/https.pm
/usr/lib/perl5/site_perl/5.26.1/URI/ldap.pm
/usr/lib/perl5/site_perl/5.26.1/URI/ldapi.pm
/usr/lib/perl5/site_perl/5.26.1/URI/ldaps.pm
/usr/lib/perl5/site_perl/5.26.1/URI/mailto.pm
/usr/lib/perl5/site_perl/5.26.1/URI/mms.pm
/usr/lib/perl5/site_perl/5.26.1/URI/news.pm
/usr/lib/perl5/site_perl/5.26.1/URI/nntp.pm
/usr/lib/perl5/site_perl/5.26.1/URI/pop.pm
/usr/lib/perl5/site_perl/5.26.1/URI/rlogin.pm
/usr/lib/perl5/site_perl/5.26.1/URI/rsync.pm
/usr/lib/perl5/site_perl/5.26.1/URI/rtsp.pm
/usr/lib/perl5/site_perl/5.26.1/URI/rtspu.pm
/usr/lib/perl5/site_perl/5.26.1/URI/sftp.pm
/usr/lib/perl5/site_perl/5.26.1/URI/sip.pm
/usr/lib/perl5/site_perl/5.26.1/URI/sips.pm
/usr/lib/perl5/site_perl/5.26.1/URI/snews.pm
/usr/lib/perl5/site_perl/5.26.1/URI/ssh.pm
/usr/lib/perl5/site_perl/5.26.1/URI/telnet.pm
/usr/lib/perl5/site_perl/5.26.1/URI/tn3270.pm
/usr/lib/perl5/site_perl/5.26.1/URI/urn.pm
/usr/lib/perl5/site_perl/5.26.1/URI/urn/isbn.pm
/usr/lib/perl5/site_perl/5.26.1/URI/urn/oid.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*
