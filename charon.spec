%global owner Commonjava
%global modulename charon

%global charon_version 1.1.2
%global sdist_tar_name %{modulename}-%{charon_version}

%global python3_pkgversion 3

Name:     %{modulename}
Summary:  Charon CLI
Version:  %{charon_version}
Release:  1%{?dist}
URL:      https://github.com/%{owner}/%{modulename}
Source0:  %{url}/archive/%{charon_version}.tar.gz
Provides: %{modulename} = %{version}-%{release}

Group:    Development/Tools
License:  APLv2

# Build Requirements
BuildArch: x86_64

BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-devel

Requires: python%{python3_pkgversion}-boto3
Requires: python%{python3_pkgversion}-botocore
Requires: python%{python3_pkgversion}-jinja2
Requires: python%{python3_pkgversion}-markupsafe
Requires: python%{python3_pkgversion}-dateutil
Requires: python%{python3_pkgversion}-six
Requires: python%{python3_pkgversion}-jmespath
Requires: python%{python3_pkgversion}-urllib3
Requires: python%{python3_pkgversion}-s3transfer
Requires: python%{python3_pkgversion}-click
Requires: python%{python3_pkgversion}-requests
Requires: python%{python3_pkgversion}-idna
Requires: python%{python3_pkgversion}-chardet
Requires: python%{python3_pkgversion}-cryptography
Requires: python%{python3_pkgversion}-cffi
Requires: python%{python3_pkgversion}-pycparser
Requires: python%{python3_pkgversion}-certifi
Requires: python%{python3_pkgversion}-pyOpenSSL
Requires: python%{python3_pkgversion}-ruamel-yaml
Requires: python%{python3_pkgversion}-defusedxml
Requires: python%{python3_pkgversion}-semantic-version
Requires: python%{python3_pkgversion}-subresource-integrity
Requires: python%{python3_pkgversion}-jsonschema
Requires: python%{python3_pkgversion}-importlib-metadata
Requires: python%{python3_pkgversion}-zipp
Requires: python%{python3_pkgversion}-attrs
Requires: python%{python3_pkgversion}-pyrsistent


%description
Simple Python tool with command line interface for charon init,
upload, delete, gen and ls functions.

%prep
%autosetup -p1 -n %{sdist_tar_name}

%build
# Disable debuginfo packages
%define _enable_debug_package 0
%define debug_package %{nil}
%py3_build


%install
export LANG=en_US.UTF-8 LANGUAGE=en_US.en LC_ALL=en_US.UTF-8
%py3_install


%files
%defattr(-,root,root)
%doc README.md
%{_bindir}/%{modulename}*
%{python3_sitelib}/*
%{!?_licensedir:%global license %doc}
%license LICENSE


%changelog
* Tue Sep 20 2022 Harsh Modi <hmodi@redhat.com>
- 1.1.2 release
- add configuration schema and validation
- allow specifying multiple target buckets

* Thu Aug 25 2022 Harsh Modi <hmodi@redhat.com>
- 1.1.1 release
