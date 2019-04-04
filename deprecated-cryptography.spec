#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : deprecated-cryptography
Version  : 2.5
Release  : 111
URL      : https://github.com/pyca/cryptography/archive/2.5.tar.gz
Source0  : https://github.com/pyca/cryptography/archive/2.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause Python-2.0
Requires: deprecated-cryptography-license = %{version}-%{release}
Requires: deprecated-cryptography-python = %{version}-%{release}
Requires: asn1crypto
Requires: cffi
Requires: six
BuildRequires : asn1crypto
BuildRequires : asn1crypto-python
BuildRequires : attrs-python
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : cffi
BuildRequires : cryptography_vectors
BuildRequires : deprecated-asn1crypto-legacypython
BuildRequires : deprecated-attrs-legacypython
BuildRequires : deprecated-cffi-legacypython
BuildRequires : deprecated-hypothesis-legacypython
BuildRequires : deprecated-pycparser-legacypython
BuildRequires : enum34
BuildRequires : hypothesis-python
BuildRequires : idna
BuildRequires : ipaddress
BuildRequires : iso8601
BuildRequires : openssl-dev
BuildRequires : packaging
BuildRequires : pretend
BuildRequires : pyparsing
BuildRequires : python-dev
BuildRequires : pytz
BuildRequires : setuptools-legacypython
BuildRequires : six
Patch1: 0002-Don-t-try-and-install-the-vectors-dependency.patch

%description
Example test files for PEM Serialization Backend tests
Contains
1. ec_private_key.pem - Contains an Elliptic Curve key generated using OpenSSL, from the curve secp256r1.
2. ec_private_key_encrypted.pem - Contains the same Elliptic Curve key as ec_private_key.pem, except that
it is encrypted with AES-256 with the password "123456".
3. ec_public_key.pem - Contains the public key corresponding to ec_private_key.pem, generated using OpenSSL.
4. rsa_private_key.pem - Contains an RSA 2048 bit key generated using OpenSSL, protected by the secret
"123456" with DES3 encryption.
5. rsa_public_key.pem - Contains an RSA 2048 bit public generated using OpenSSL from rsa_private_key.pem.
6. dsaparam.pem - Contains 2048-bit DSA parameters generated using OpenSSL; contains no keys.
7. dsa_private_key.pem - Contains a DSA 2048 bit key generated using OpenSSL from the parameters in
dsaparam.pem, protected by the secret "123456" with DES3 encryption.
8. dsa_public_key.pem - Contains a DSA 2048 bit key generated using OpenSSL from dsa_private_key.pem.

%package legacypython
Summary: legacypython components for the deprecated-cryptography package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-cryptography package.


%package license
Summary: license components for the deprecated-cryptography package.
Group: Default

%description license
license components for the deprecated-cryptography package.


%package python
Summary: python components for the deprecated-cryptography package.
Group: Default

%description python
python components for the deprecated-cryptography package.


%prep
%setup -q -n cryptography-2.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554343610
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-cryptography
cp LICENSE.APACHE %{buildroot}/usr/share/package-licenses/deprecated-cryptography/LICENSE.APACHE
cp LICENSE.BSD %{buildroot}/usr/share/package-licenses/deprecated-cryptography/LICENSE.BSD
cp LICENSE.PSF %{buildroot}/usr/share/package-licenses/deprecated-cryptography/LICENSE.PSF
cp vectors/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/deprecated-cryptography/vectors_LICENSE.APACHE
cp vectors/LICENSE.BSD %{buildroot}/usr/share/package-licenses/deprecated-cryptography/vectors_LICENSE.BSD
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-cryptography/LICENSE.APACHE
/usr/share/package-licenses/deprecated-cryptography/LICENSE.BSD
/usr/share/package-licenses/deprecated-cryptography/LICENSE.PSF
/usr/share/package-licenses/deprecated-cryptography/vectors_LICENSE.APACHE
/usr/share/package-licenses/deprecated-cryptography/vectors_LICENSE.BSD

%files python
%defattr(-,root,root,-)
