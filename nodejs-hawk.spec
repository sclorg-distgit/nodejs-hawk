%{?scl:%scl_package nodejs-hawk}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

# this will not create .orig file
#%global _default_patch_flags --no-backup-if-mismatch

Name:       %{?scl_prefix}nodejs-hawk
Version:    3.1.3
Release:    2%{?dist}
Summary:    HTTP Hawk authentication scheme
License:    BSD
URL:        https://github.com/hueniverse/hawk
Source0:    http://registry.npmjs.org/hawk/-/hawk-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{ix86} x86_64 %{arm} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

Patch1: Deminified-crypto-functions.patch 

%description
Hawk is an HTTP authentication scheme using a message authentication code (MAC)
algorithm to provide partial HTTP request cryptographic verification.

%prep
%setup -q -n package
%patch1 -p3
#fix perms
chmod 0644 README.md LICENSE dist/* example/* images/* lib/* *.json

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/hawk
cp -pr lib dist package.json component.json %{buildroot}%{nodejs_sitelib}/hawk

%nodejs_symlink_deps

#Yet Another Unpackaged Test Framework (lab)
#%%check
#make test

%files
%{nodejs_sitelib}/hawk
%doc README.md LICENSE example images

%changelog
* Tue Feb 28 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.1.3-2
- Deminify bundled crypto-js (RHBZ#1419660)

* Tue Sep 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.1.3-1
- Updated with script

* Thu Feb 18 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-4
- Add option to not create .orig file

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- replace provides and requires with macro

* Fri Aug 09 2013 Tomas Hrcka <thrcka@redhat.com> - 0.12.1-3
- added patch to deminify implemented crypto functions

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-1
- new upstream release 1.0.0

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.15.0-1
- new upstream release 0.15.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.12.1-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.12.1-2
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.1    2.1-2 
- Add support for software collections

* Tue Apr 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.12.1-1
- new upstream release 0.12.1

* Mon Apr 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.11.1-2
- fix rpmlint warnings

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.11.1-1
- initial package
