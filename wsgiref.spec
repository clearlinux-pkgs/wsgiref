#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wsgiref
Version  : 0.1.2
Release  : 15
URL      : https://pypi.python.org/packages/source/w/wsgiref/wsgiref-0.1.2.zip
Source0  : https://pypi.python.org/packages/source/w/wsgiref/wsgiref-0.1.2.zip
Summary  : WSGI (PEP 333) Reference Library
Group    : Development/Tools
License  : Python-2.0 ZPL-2.0
Requires: wsgiref-python
BuildRequires : python-dev
BuildRequires : setuptools

%description
This is a standalone release of the ``wsgiref`` library to be included in
Python 2.5.  For the standalone version's documentation, see:

%package python
Summary: python components for the wsgiref package.
Group: Default

%description python
python components for the wsgiref package.


%prep
%setup -q -n wsgiref-0.1.2

%build
python2 setup.py build -b py2

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
python2 setup.py test
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
