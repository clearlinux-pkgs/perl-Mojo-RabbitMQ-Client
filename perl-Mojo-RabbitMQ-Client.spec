#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mojo-RabbitMQ-Client
Version  : 0.2.1
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/S/SE/SEBAPOD/Mojo-RabbitMQ-Client-0.2.1.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SE/SEBAPOD/Mojo-RabbitMQ-Client-0.2.1.tar.gz
Summary  : 'Mojo::IOLoop based RabbitMQ client'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Mojo-RabbitMQ-Client-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
[![Build Status](https://travis-ci.org/inway/mojo-rabbitmq-client.svg?branch=master)](https://travis-ci.org/inway/mojo-rabbitmq-client) [![MetaCPAN Release](https://badge.fury.io/pl/Mojo-RabbitMQ-Client.svg)](https://metacpan.org/release/Mojo-RabbitMQ-Client)
# NAME

%package dev
Summary: dev components for the perl-Mojo-RabbitMQ-Client package.
Group: Development
Provides: perl-Mojo-RabbitMQ-Client-devel = %{version}-%{release}

%description dev
dev components for the perl-Mojo-RabbitMQ-Client package.


%package license
Summary: license components for the perl-Mojo-RabbitMQ-Client package.
Group: Default

%description license
license components for the perl-Mojo-RabbitMQ-Client package.


%prep
%setup -q -n Mojo-RabbitMQ-Client-0.2.1

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

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Mojo-RabbitMQ-Client
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Mojo-RabbitMQ-Client/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/RabbitMQ/Client.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/RabbitMQ/Client/Channel.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/RabbitMQ/Client/Consumer.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/RabbitMQ/Client/LocalQueue.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/RabbitMQ/Client/Method.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/RabbitMQ/Client/Method/Publish.pm
/usr/lib/perl5/vendor_perl/5.28.1/Mojo/RabbitMQ/Client/Publisher.pm
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/dist/Mojo-RabbitMQ-Client/amqp0-9-1.stripped.extended.xml
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/dist/Mojo-RabbitMQ-Client/fixed_amqp0-8.xml

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mojo::RabbitMQ::Client.3
/usr/share/man/man3/Mojo::RabbitMQ::Client::Channel.3
/usr/share/man/man3/Mojo::RabbitMQ::Client::Consumer.3
/usr/share/man/man3/Mojo::RabbitMQ::Client::LocalQueue.3
/usr/share/man/man3/Mojo::RabbitMQ::Client::Method.3
/usr/share/man/man3/Mojo::RabbitMQ::Client::Method::Publish.3
/usr/share/man/man3/Mojo::RabbitMQ::Client::Publisher.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Mojo-RabbitMQ-Client/LICENSE
