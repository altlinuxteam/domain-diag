Name: domain-diag
Version: 0.2.6
Release: alt1

Summary: Active Directory domain environment diagnostic tool
License: GPLv3
Group: System/Configuration/Other
BuildArch: noarch

Url: https://gitea.basealt.ru/saratov/domain-diag

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-alterator
BuildRequires: shellcheck

%description
Active Directory domain environment diagnostic tool.

%prep
%setup

%build
sed -i 's/^VERSION=.*/VERSION=%version/' %name
sed -i 's/@VERSION@/%version/g' %name.man

%install
install -p -D -m755 %name %buildroot%_bindir/%name
install -p -D %name.man %buildroot%_mandir/man1/%name.1
install -p -D alterator/%name.backend %buildroot%_alterator_datadir/backends/%name.backend
install -p -D alterator/%name.desktop %buildroot%_alterator_datadir/backends/%name.desktop

%check
shellcheck -e SC1090,SC1091,SC2004,SC2015,SC2034,SC2086,SC2154,SC2001,SC2120,SC2119 %name

%files
%_bindir/%name
%_mandir/man1/%name.*
%_alterator_datadir/backends/%name.*

%changelog
* Tue Oct 17 2023 Andrey Limachko <liannnix@altlinux.org> 0.2.6-alt1
- chore: change methods names to alterator-manager interface
  0.1.8-alt1 (thx Aleksey Saprunov)
- chore: add actions_ids (thx Aleksey Saprunov)
- change run method signature (thx Aleksey Saprunov)

* Tue Jun 27 2023 Andrey Limachko <liannnix@altlinux.org> 0.2.5-alt1
- Add ADT backend bindings

* Tue Jun 27 2023 Andrey Limachko <liannnix@altlinux.org> 0.2.4-alt1
- Add license information
- Add man page

* Wed Apr 19 2023 Andrey Limachko <liannnix@altlinux.org> 0.2.3-alt1
- Fixed script return codes
- Fixed nothing to grep bug
- Added resolv.conf search multidomain support
- Fixed script failure when default_realm commented in krb5.conf

* Tue Jan 10 2023 Andrey Limachko <liannnix@altlinux.org> 0.2.2-alt1
- Added kinit from system keytab when run as root
- Fixed ldapsearch timeout limit

* Wed Dec 21 2022 Andrey Limachko <liannnix@altlinux.org> 0.2.1-alt1
- Initial build

