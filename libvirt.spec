#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
# Source0 file verified with key 0xCA68BE8010084C9C (jdenemar@redhat.com)
#
Name     : libvirt
Version  : 9.5.0
Release  : 154
URL      : https://libvirt.org/sources/libvirt-9.5.0.tar.xz
Source0  : https://libvirt.org/sources/libvirt-9.5.0.tar.xz
Source1  : https://libvirt.org/sources/libvirt-9.5.0.tar.xz.asc
Summary  : Library providing a simple virtualization API
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-2.0+ LGPL-2.1 LGPL-2.1+ LGPL-2.1-only OFL-1.1
Requires: libvirt-bin = %{version}-%{release}
Requires: libvirt-config = %{version}-%{release}
Requires: libvirt-data = %{version}-%{release}
Requires: libvirt-lib = %{version}-%{release}
Requires: libvirt-libexec = %{version}-%{release}
Requires: libvirt-license = %{version}-%{release}
Requires: libvirt-locales = %{version}-%{release}
Requires: libvirt-man = %{version}-%{release}
Requires: libvirt-services = %{version}-%{release}
Requires: polkit
Requires: qemu-setuid
BuildRequires : LVM2
BuildRequires : LVM2-dev
BuildRequires : LVM2-extras
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : bash-completion-dev
BuildRequires : bridge-utils
BuildRequires : buildreq-meson
BuildRequires : curl-dev
BuildRequires : dbus-dev
BuildRequires : dmidecode
BuildRequires : dnsmasq
BuildRequires : ebtables
BuildRequires : fuse-dev
BuildRequires : gettext-dev
BuildRequires : iproute2
BuildRequires : iptables
BuildRequires : kmod-bin
BuildRequires : libcap-ng-dev
BuildRequires : libnl-dev
BuildRequires : libpcap-dev
BuildRequires : libpciaccess-dev
BuildRequires : libssh-dev
BuildRequires : libssh2-dev
BuildRequires : libtasn1-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt
BuildRequires : ncurses-dev
BuildRequires : nfs-utils
BuildRequires : numactl
BuildRequires : numactl-dev
BuildRequires : open-iscsi
BuildRequires : openssh
BuildRequires : openssl-dev
BuildRequires : openvswitch
BuildRequires : parted-dev
BuildRequires : pkgconfig(audit)
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(libiscsi)
BuildRequires : pkgconfig(libssh)
BuildRequires : pkgconfig(libtirpc)
BuildRequires : polkit-dev
BuildRequires : pypi-docutils
BuildRequires : qemu-setuid
BuildRequires : readline-dev
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : util-linux-dev
BuildRequires : xfsprogs-dev
BuildRequires : yajl-dev
BuildRequires : yajl-lib
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Default-to-0770-permissions.patch
Patch2: 0002-drop-timeout-ping.patch
Patch3: 0003-Arjan-s-patch-for-locale.patch

%description
Libvirt is a C toolkit to interact with the virtualization capabilities
of recent versions of Linux (and other OSes). The main package includes
the libvirtd server exporting the virtualization support.

%package autostart
Summary: autostart components for the libvirt package.
Group: Default

%description autostart
autostart components for the libvirt package.


%package bin
Summary: bin components for the libvirt package.
Group: Binaries
Requires: libvirt-data = %{version}-%{release}
Requires: libvirt-libexec = %{version}-%{release}
Requires: libvirt-config = %{version}-%{release}
Requires: libvirt-license = %{version}-%{release}
Requires: libvirt-services = %{version}-%{release}

%description bin
bin components for the libvirt package.


%package config
Summary: config components for the libvirt package.
Group: Default

%description config
config components for the libvirt package.


%package data
Summary: data components for the libvirt package.
Group: Data

%description data
data components for the libvirt package.


%package dev
Summary: dev components for the libvirt package.
Group: Development
Requires: libvirt-lib = %{version}-%{release}
Requires: libvirt-bin = %{version}-%{release}
Requires: libvirt-data = %{version}-%{release}
Provides: libvirt-devel = %{version}-%{release}
Requires: libvirt = %{version}-%{release}

%description dev
dev components for the libvirt package.


%package doc
Summary: doc components for the libvirt package.
Group: Documentation
Requires: libvirt-man = %{version}-%{release}

%description doc
doc components for the libvirt package.


%package lib
Summary: lib components for the libvirt package.
Group: Libraries
Requires: libvirt-data = %{version}-%{release}
Requires: libvirt-libexec = %{version}-%{release}
Requires: libvirt-license = %{version}-%{release}

%description lib
lib components for the libvirt package.


%package libexec
Summary: libexec components for the libvirt package.
Group: Default
Requires: libvirt-config = %{version}-%{release}
Requires: libvirt-license = %{version}-%{release}

%description libexec
libexec components for the libvirt package.


%package license
Summary: license components for the libvirt package.
Group: Default

%description license
license components for the libvirt package.


%package locales
Summary: locales components for the libvirt package.
Group: Default

%description locales
locales components for the libvirt package.


%package man
Summary: man components for the libvirt package.
Group: Default

%description man
man components for the libvirt package.


%package services
Summary: services components for the libvirt package.
Group: Systemd services
Requires: systemd

%description services
services components for the libvirt package.


%prep
%setup -q -n libvirt-9.5.0
cd %{_builddir}/libvirt-9.5.0
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
pushd ..
cp -a libvirt-9.5.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688407376
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dapparmor=disabled \
-Dapparmor_profiles=disabled \
-Ddriver_esx=disabled \
-Ddriver_hyperv=disabled \
-Ddriver_interface=enabled \
-Ddriver_libvirtd=enabled \
-Ddriver_libxl=disabled \
-Ddriver_lxc=enabled \
-Ddriver_openvz=disabled \
-Ddriver_qemu=enabled \
-Ddriver_remote=enabled \
-Ddriver_test=enabled \
-Ddriver_vbox=disabled \
-Ddriver_vmware=disabled \
-Ddtrace=disabled \
-Dfirewalld=enabled \
-Dfirewalld_zone=enabled \
-Dfuse=disabled \
-Dinit_script=systemd \
-Dloader_nvram=/usr/share/qemu/OVMF.fd:/usr/share/qemu/OVMF.fd:/usr/share/qemu/OVMF_CODE.fd:/usr/share/qemu/OVMF_VARS.fd \
-Dnetcf=disabled \
-Dnls=enabled \
-Dopenwsman=disabled \
-Dpciaccess=enabled \
-Dpm_utils=disabled \
-Dpolkit=enabled \
-Dqemu_group=qemu \
-Dqemu_user=qemu \
-Dsanlock=disabled \
-Dsasl=disabled \
-Dsecdriver_apparmor=disabled \
-Dselinux=disabled \
-Dtls_priority="SECURE128" \
-Dudev=enabled \
-Dyajl=enabled  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dapparmor=disabled \
-Dapparmor_profiles=disabled \
-Ddriver_esx=disabled \
-Ddriver_hyperv=disabled \
-Ddriver_interface=enabled \
-Ddriver_libvirtd=enabled \
-Ddriver_libxl=disabled \
-Ddriver_lxc=enabled \
-Ddriver_openvz=disabled \
-Ddriver_qemu=enabled \
-Ddriver_remote=enabled \
-Ddriver_test=enabled \
-Ddriver_vbox=disabled \
-Ddriver_vmware=disabled \
-Ddtrace=disabled \
-Dfirewalld=enabled \
-Dfirewalld_zone=enabled \
-Dfuse=disabled \
-Dinit_script=systemd \
-Dloader_nvram=/usr/share/qemu/OVMF.fd:/usr/share/qemu/OVMF.fd:/usr/share/qemu/OVMF_CODE.fd:/usr/share/qemu/OVMF_VARS.fd \
-Dnetcf=disabled \
-Dnls=enabled \
-Dopenwsman=disabled \
-Dpciaccess=enabled \
-Dpm_utils=disabled \
-Dpolkit=enabled \
-Dqemu_group=qemu \
-Dqemu_user=qemu \
-Dsanlock=disabled \
-Dsasl=disabled \
-Dsecdriver_apparmor=disabled \
-Dselinux=disabled \
-Dtls_priority="SECURE128" \
-Dudev=enabled \
-Dyajl=enabled  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/libvirt
cp %{_builddir}/libvirt-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libvirt/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/libvirt-%{version}/COPYING.LESSER %{buildroot}/usr/share/package-licenses/libvirt/3704f4680301a60004b20f94e0b5b8c7ff1484a9 || :
cp %{_builddir}/libvirt-%{version}/docs/fonts/LICENSE.rst %{buildroot}/usr/share/package-licenses/libvirt/f4e4f4ac8fa716d051ac27a5415491544c8f456e || :
cp %{_builddir}/libvirt-%{version}/subprojects/keycodemapdb/LICENSE.BSD %{buildroot}/usr/share/package-licenses/libvirt/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8 || :
cp %{_builddir}/libvirt-%{version}/subprojects/keycodemapdb/LICENSE.GPL2 %{buildroot}/usr/share/package-licenses/libvirt/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang libvirt
## Remove excluded files
rm -f %{buildroot}*/etc/logrotate.d/libvirtd
rm -f %{buildroot}*/etc/logrotate.d/libvirtd.lxc
rm -f %{buildroot}*/etc/logrotate.d/libvirtd.qemu
rm -f %{buildroot}*/etc/logrotate.d/libvirtd.uml
rm -f %{buildroot}*/etc/sysconfig/libvirtd
rm -f %{buildroot}*/etc/sysconfig/libvirt-guests
rm -f %{buildroot}*/etc/sysconfig/virtlockd
rm -f %{buildroot}*/etc/libvirt/libvirt.conf
rm -f %{buildroot}*/etc/libvirt/libvirtd.conf
rm -f %{buildroot}*/etc/libvirt/lxc.conf
rm -f %{buildroot}*/etc/libvirt/qemu.conf
rm -f %{buildroot}*/etc/libvirt/qemu-lockd.conf
rm -f %{buildroot}*/etc/libvirt/virtlockd.conf
rm -f %{buildroot}*/etc/libvirt/virt-login-shell.conf
rm -f %{buildroot}*/etc/libvirt/qemu/networks/autostart/default.xml
rm -f %{buildroot}*/etc/libvirt/qemu/networks/default.xml
## install_append content
mkdir %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../libvirtd.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/libvirtd.service
mv %{buildroot}/usr/sbin/*  %{buildroot}/usr/bin/
rmdir %{buildroot}/usr/sbin
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib/firewalld/policies/libvirt-routed-in.xml
/usr/lib/firewalld/policies/libvirt-routed-out.xml
/usr/lib/firewalld/policies/libvirt-to-host.xml
/usr/lib/firewalld/zones/libvirt-routed.xml
/usr/lib/firewalld/zones/libvirt.xml

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/libvirtd.service

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/libvirtd
/V3/usr/bin/virsh
/V3/usr/bin/virt-admin
/V3/usr/bin/virt-host-validate
/V3/usr/bin/virt-login-shell
/V3/usr/bin/virt-pki-query-dn
/V3/usr/bin/virt-qemu-run
/V3/usr/bin/virt-ssh-helper
/V3/usr/bin/virtchd
/V3/usr/bin/virtinterfaced
/V3/usr/bin/virtlockd
/V3/usr/bin/virtlogd
/V3/usr/bin/virtlxcd
/V3/usr/bin/virtnetworkd
/V3/usr/bin/virtnodedevd
/V3/usr/bin/virtnwfilterd
/V3/usr/bin/virtproxyd
/V3/usr/bin/virtqemud
/V3/usr/bin/virtsecretd
/V3/usr/bin/virtstoraged
/usr/bin/libvirtd
/usr/bin/virsh
/usr/bin/virt-admin
/usr/bin/virt-host-validate
/usr/bin/virt-login-shell
/usr/bin/virt-pki-query-dn
/usr/bin/virt-pki-validate
/usr/bin/virt-qemu-qmp-proxy
/usr/bin/virt-qemu-run
/usr/bin/virt-qemu-sev-validate
/usr/bin/virt-ssh-helper
/usr/bin/virt-xml-validate
/usr/bin/virtchd
/usr/bin/virtinterfaced
/usr/bin/virtlockd
/usr/bin/virtlogd
/usr/bin/virtlxcd
/usr/bin/virtnetworkd
/usr/bin/virtnodedevd
/usr/bin/virtnwfilterd
/usr/bin/virtproxyd
/usr/bin/virtqemud
/usr/bin/virtsecretd
/usr/bin/virtstoraged

%files config
%defattr(-,root,root,-)
/usr/lib/sysctl.d/60-libvirtd.conf
/usr/lib/sysctl.d/60-qemu-postcopy-migration.conf

%files data
%defattr(-,root,root,-)
/usr/share/augeas/lenses/libvirt_lockd.aug
/usr/share/augeas/lenses/libvirtd.aug
/usr/share/augeas/lenses/libvirtd_lxc.aug
/usr/share/augeas/lenses/libvirtd_qemu.aug
/usr/share/augeas/lenses/tests/test_libvirt_lockd.aug
/usr/share/augeas/lenses/tests/test_libvirtd.aug
/usr/share/augeas/lenses/tests/test_libvirtd_lxc.aug
/usr/share/augeas/lenses/tests/test_libvirtd_qemu.aug
/usr/share/augeas/lenses/tests/test_virtchd.aug
/usr/share/augeas/lenses/tests/test_virtinterfaced.aug
/usr/share/augeas/lenses/tests/test_virtlockd.aug
/usr/share/augeas/lenses/tests/test_virtlogd.aug
/usr/share/augeas/lenses/tests/test_virtlxcd.aug
/usr/share/augeas/lenses/tests/test_virtnetworkd.aug
/usr/share/augeas/lenses/tests/test_virtnodedevd.aug
/usr/share/augeas/lenses/tests/test_virtnwfilterd.aug
/usr/share/augeas/lenses/tests/test_virtproxyd.aug
/usr/share/augeas/lenses/tests/test_virtqemud.aug
/usr/share/augeas/lenses/tests/test_virtsecretd.aug
/usr/share/augeas/lenses/tests/test_virtstoraged.aug
/usr/share/augeas/lenses/virtchd.aug
/usr/share/augeas/lenses/virtinterfaced.aug
/usr/share/augeas/lenses/virtlockd.aug
/usr/share/augeas/lenses/virtlogd.aug
/usr/share/augeas/lenses/virtlxcd.aug
/usr/share/augeas/lenses/virtnetworkd.aug
/usr/share/augeas/lenses/virtnodedevd.aug
/usr/share/augeas/lenses/virtnwfilterd.aug
/usr/share/augeas/lenses/virtproxyd.aug
/usr/share/augeas/lenses/virtqemud.aug
/usr/share/augeas/lenses/virtsecretd.aug
/usr/share/augeas/lenses/virtstoraged.aug
/usr/share/bash-completion/completions/virsh
/usr/share/bash-completion/completions/virt-admin
/usr/share/libvirt/api/libvirt-admin-api.xml
/usr/share/libvirt/api/libvirt-api.xml
/usr/share/libvirt/api/libvirt-lxc-api.xml
/usr/share/libvirt/api/libvirt-qemu-api.xml
/usr/share/libvirt/cpu_map/arm_FT-2000plus.xml
/usr/share/libvirt/cpu_map/arm_Falkor.xml
/usr/share/libvirt/cpu_map/arm_Kunpeng-920.xml
/usr/share/libvirt/cpu_map/arm_Neoverse-N1.xml
/usr/share/libvirt/cpu_map/arm_Neoverse-N2.xml
/usr/share/libvirt/cpu_map/arm_Neoverse-V1.xml
/usr/share/libvirt/cpu_map/arm_Tengyun-S2500.xml
/usr/share/libvirt/cpu_map/arm_ThunderX299xx.xml
/usr/share/libvirt/cpu_map/arm_a64fx.xml
/usr/share/libvirt/cpu_map/arm_cortex-a53.xml
/usr/share/libvirt/cpu_map/arm_cortex-a57.xml
/usr/share/libvirt/cpu_map/arm_cortex-a72.xml
/usr/share/libvirt/cpu_map/arm_features.xml
/usr/share/libvirt/cpu_map/arm_vendors.xml
/usr/share/libvirt/cpu_map/index.xml
/usr/share/libvirt/cpu_map/ppc64_POWER10.xml
/usr/share/libvirt/cpu_map/ppc64_POWER6.xml
/usr/share/libvirt/cpu_map/ppc64_POWER7.xml
/usr/share/libvirt/cpu_map/ppc64_POWER8.xml
/usr/share/libvirt/cpu_map/ppc64_POWER9.xml
/usr/share/libvirt/cpu_map/ppc64_POWERPC_e5500.xml
/usr/share/libvirt/cpu_map/ppc64_POWERPC_e6500.xml
/usr/share/libvirt/cpu_map/ppc64_vendors.xml
/usr/share/libvirt/cpu_map/x86_486.xml
/usr/share/libvirt/cpu_map/x86_Broadwell-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Broadwell-noTSX-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Broadwell-noTSX.xml
/usr/share/libvirt/cpu_map/x86_Broadwell.xml
/usr/share/libvirt/cpu_map/x86_Cascadelake-Server-noTSX.xml
/usr/share/libvirt/cpu_map/x86_Cascadelake-Server.xml
/usr/share/libvirt/cpu_map/x86_Conroe.xml
/usr/share/libvirt/cpu_map/x86_Cooperlake.xml
/usr/share/libvirt/cpu_map/x86_Dhyana.xml
/usr/share/libvirt/cpu_map/x86_EPYC-IBPB.xml
/usr/share/libvirt/cpu_map/x86_EPYC-Milan.xml
/usr/share/libvirt/cpu_map/x86_EPYC-Rome.xml
/usr/share/libvirt/cpu_map/x86_EPYC.xml
/usr/share/libvirt/cpu_map/x86_Haswell-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Haswell-noTSX-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Haswell-noTSX.xml
/usr/share/libvirt/cpu_map/x86_Haswell.xml
/usr/share/libvirt/cpu_map/x86_Icelake-Client-noTSX.xml
/usr/share/libvirt/cpu_map/x86_Icelake-Client.xml
/usr/share/libvirt/cpu_map/x86_Icelake-Server-noTSX.xml
/usr/share/libvirt/cpu_map/x86_Icelake-Server.xml
/usr/share/libvirt/cpu_map/x86_IvyBridge-IBRS.xml
/usr/share/libvirt/cpu_map/x86_IvyBridge.xml
/usr/share/libvirt/cpu_map/x86_Nehalem-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Nehalem.xml
/usr/share/libvirt/cpu_map/x86_Opteron_G1.xml
/usr/share/libvirt/cpu_map/x86_Opteron_G2.xml
/usr/share/libvirt/cpu_map/x86_Opteron_G3.xml
/usr/share/libvirt/cpu_map/x86_Opteron_G4.xml
/usr/share/libvirt/cpu_map/x86_Opteron_G5.xml
/usr/share/libvirt/cpu_map/x86_Penryn.xml
/usr/share/libvirt/cpu_map/x86_SandyBridge-IBRS.xml
/usr/share/libvirt/cpu_map/x86_SandyBridge.xml
/usr/share/libvirt/cpu_map/x86_SapphireRapids.xml
/usr/share/libvirt/cpu_map/x86_Skylake-Client-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Skylake-Client-noTSX-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Skylake-Client.xml
/usr/share/libvirt/cpu_map/x86_Skylake-Server-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Skylake-Server-noTSX-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Skylake-Server.xml
/usr/share/libvirt/cpu_map/x86_Snowridge.xml
/usr/share/libvirt/cpu_map/x86_Westmere-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Westmere.xml
/usr/share/libvirt/cpu_map/x86_athlon.xml
/usr/share/libvirt/cpu_map/x86_core2duo.xml
/usr/share/libvirt/cpu_map/x86_coreduo.xml
/usr/share/libvirt/cpu_map/x86_cpu64-rhel5.xml
/usr/share/libvirt/cpu_map/x86_cpu64-rhel6.xml
/usr/share/libvirt/cpu_map/x86_features.xml
/usr/share/libvirt/cpu_map/x86_kvm32.xml
/usr/share/libvirt/cpu_map/x86_kvm64.xml
/usr/share/libvirt/cpu_map/x86_n270.xml
/usr/share/libvirt/cpu_map/x86_pentium.xml
/usr/share/libvirt/cpu_map/x86_pentium2.xml
/usr/share/libvirt/cpu_map/x86_pentium3.xml
/usr/share/libvirt/cpu_map/x86_pentiumpro.xml
/usr/share/libvirt/cpu_map/x86_phenom.xml
/usr/share/libvirt/cpu_map/x86_qemu32.xml
/usr/share/libvirt/cpu_map/x86_qemu64.xml
/usr/share/libvirt/cpu_map/x86_vendors.xml
/usr/share/libvirt/schemas/basictypes.rng
/usr/share/libvirt/schemas/capability.rng
/usr/share/libvirt/schemas/cpu.rng
/usr/share/libvirt/schemas/cputypes.rng
/usr/share/libvirt/schemas/domain.rng
/usr/share/libvirt/schemas/domainbackup.rng
/usr/share/libvirt/schemas/domaincaps.rng
/usr/share/libvirt/schemas/domaincheckpoint.rng
/usr/share/libvirt/schemas/domaincommon.rng
/usr/share/libvirt/schemas/domainoverrides.rng
/usr/share/libvirt/schemas/domainsnapshot.rng
/usr/share/libvirt/schemas/inactiveDomain.rng
/usr/share/libvirt/schemas/interface.rng
/usr/share/libvirt/schemas/network.rng
/usr/share/libvirt/schemas/networkcommon.rng
/usr/share/libvirt/schemas/networkport.rng
/usr/share/libvirt/schemas/nodedev.rng
/usr/share/libvirt/schemas/nwfilter.rng
/usr/share/libvirt/schemas/nwfilter_params.rng
/usr/share/libvirt/schemas/nwfilterbinding.rng
/usr/share/libvirt/schemas/privatedata.rng
/usr/share/libvirt/schemas/secret.rng
/usr/share/libvirt/schemas/storagecommon.rng
/usr/share/libvirt/schemas/storagepool.rng
/usr/share/libvirt/schemas/storagepoolcaps.rng
/usr/share/libvirt/schemas/storagevol.rng
/usr/share/libvirt/test-screenshot.png
/usr/share/polkit-1/actions/org.libvirt.api.policy
/usr/share/polkit-1/actions/org.libvirt.unix.policy
/usr/share/polkit-1/rules.d/50-libvirt.rules

%files dev
%defattr(-,root,root,-)
/usr/include/libvirt/libvirt-admin.h
/usr/include/libvirt/libvirt-common.h
/usr/include/libvirt/libvirt-domain-checkpoint.h
/usr/include/libvirt/libvirt-domain-snapshot.h
/usr/include/libvirt/libvirt-domain.h
/usr/include/libvirt/libvirt-event.h
/usr/include/libvirt/libvirt-host.h
/usr/include/libvirt/libvirt-interface.h
/usr/include/libvirt/libvirt-lxc.h
/usr/include/libvirt/libvirt-network.h
/usr/include/libvirt/libvirt-nodedev.h
/usr/include/libvirt/libvirt-nwfilter.h
/usr/include/libvirt/libvirt-qemu.h
/usr/include/libvirt/libvirt-secret.h
/usr/include/libvirt/libvirt-storage.h
/usr/include/libvirt/libvirt-stream.h
/usr/include/libvirt/libvirt.h
/usr/include/libvirt/virterror.h
/usr/lib64/libvirt-admin.so
/usr/lib64/libvirt-lxc.so
/usr/lib64/libvirt-qemu.so
/usr/lib64/libvirt.so
/usr/lib64/pkgconfig/libvirt-admin.pc
/usr/lib64/pkgconfig/libvirt-lxc.pc
/usr/lib64/pkgconfig/libvirt-qemu.pc
/usr/lib64/pkgconfig/libvirt.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/libvirt/*

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libnss_libvirt.so.2
/V3/usr/lib64/libnss_libvirt_guest.so.2
/V3/usr/lib64/libvirt-admin.so.0.9005.0
/V3/usr/lib64/libvirt-lxc.so.0.9005.0
/V3/usr/lib64/libvirt-qemu.so.0.9005.0
/V3/usr/lib64/libvirt.so.0.9005.0
/V3/usr/lib64/libvirt/connection-driver/libvirt_driver_ch.so
/V3/usr/lib64/libvirt/connection-driver/libvirt_driver_interface.so
/V3/usr/lib64/libvirt/connection-driver/libvirt_driver_lxc.so
/V3/usr/lib64/libvirt/connection-driver/libvirt_driver_network.so
/V3/usr/lib64/libvirt/connection-driver/libvirt_driver_nodedev.so
/V3/usr/lib64/libvirt/connection-driver/libvirt_driver_nwfilter.so
/V3/usr/lib64/libvirt/connection-driver/libvirt_driver_qemu.so
/V3/usr/lib64/libvirt/connection-driver/libvirt_driver_secret.so
/V3/usr/lib64/libvirt/connection-driver/libvirt_driver_storage.so
/V3/usr/lib64/libvirt/lock-driver/lockd.so
/V3/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_disk.so
/V3/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_fs.so
/V3/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_iscsi-direct.so
/V3/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_iscsi.so
/V3/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_logical.so
/V3/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_mpath.so
/V3/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_scsi.so
/V3/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_vstorage.so
/V3/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_zfs.so
/V3/usr/lib64/libvirt/storage-file/libvirt_storage_file_fs.so
/usr/lib64/libnss_libvirt.so.2
/usr/lib64/libnss_libvirt_guest.so.2
/usr/lib64/libvirt-admin.so.0
/usr/lib64/libvirt-admin.so.0.9005.0
/usr/lib64/libvirt-lxc.so.0
/usr/lib64/libvirt-lxc.so.0.9005.0
/usr/lib64/libvirt-qemu.so.0
/usr/lib64/libvirt-qemu.so.0.9005.0
/usr/lib64/libvirt.so.0
/usr/lib64/libvirt.so.0.9005.0
/usr/lib64/libvirt/connection-driver/libvirt_driver_ch.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_interface.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_lxc.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_network.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_nodedev.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_nwfilter.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_qemu.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_secret.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_storage.so
/usr/lib64/libvirt/lock-driver/lockd.so
/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_disk.so
/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_fs.so
/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_iscsi-direct.so
/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_iscsi.so
/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_logical.so
/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_mpath.so
/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_scsi.so
/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_vstorage.so
/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_zfs.so
/usr/lib64/libvirt/storage-file/libvirt_storage_file_fs.so

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/libvirt_iohelper
/V3/usr/libexec/libvirt_leaseshelper
/V3/usr/libexec/libvirt_lxc
/V3/usr/libexec/libvirt_parthelper
/V3/usr/libexec/virt-login-shell-helper
/usr/libexec/libvirt-guests.sh
/usr/libexec/libvirt_iohelper
/usr/libexec/libvirt_leaseshelper
/usr/libexec/libvirt_lxc
/usr/libexec/libvirt_parthelper
/usr/libexec/virt-login-shell-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libvirt/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/libvirt/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/libvirt/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/libvirt/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
/usr/share/package-licenses/libvirt/f4e4f4ac8fa716d051ac27a5415491544c8f456e

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/virsh.1
/usr/share/man/man1/virt-admin.1
/usr/share/man/man1/virt-host-validate.1
/usr/share/man/man1/virt-login-shell.1
/usr/share/man/man1/virt-pki-query-dn.1
/usr/share/man/man1/virt-pki-validate.1
/usr/share/man/man1/virt-qemu-qmp-proxy.1
/usr/share/man/man1/virt-qemu-run.1
/usr/share/man/man1/virt-qemu-sev-validate.1
/usr/share/man/man1/virt-xml-validate.1
/usr/share/man/man7/virkeycode-atset1.7
/usr/share/man/man7/virkeycode-atset2.7
/usr/share/man/man7/virkeycode-atset3.7
/usr/share/man/man7/virkeycode-linux.7
/usr/share/man/man7/virkeycode-osx.7
/usr/share/man/man7/virkeycode-qnum.7
/usr/share/man/man7/virkeycode-usb.7
/usr/share/man/man7/virkeycode-win32.7
/usr/share/man/man7/virkeycode-xtkbd.7
/usr/share/man/man7/virkeyname-linux.7
/usr/share/man/man7/virkeyname-osx.7
/usr/share/man/man7/virkeyname-win32.7
/usr/share/man/man8/libvirt-guests.8
/usr/share/man/man8/libvirtd.8
/usr/share/man/man8/virt-ssh-helper.8
/usr/share/man/man8/virtinterfaced.8
/usr/share/man/man8/virtlockd.8
/usr/share/man/man8/virtlogd.8
/usr/share/man/man8/virtlxcd.8
/usr/share/man/man8/virtnetworkd.8
/usr/share/man/man8/virtnodedevd.8
/usr/share/man/man8/virtnwfilterd.8
/usr/share/man/man8/virtproxyd.8
/usr/share/man/man8/virtqemud.8
/usr/share/man/man8/virtsecretd.8
/usr/share/man/man8/virtstoraged.8

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/libvirtd.service
/usr/lib/systemd/system/libvirt-guests.service
/usr/lib/systemd/system/libvirtd-admin.socket
/usr/lib/systemd/system/libvirtd-ro.socket
/usr/lib/systemd/system/libvirtd-tcp.socket
/usr/lib/systemd/system/libvirtd-tls.socket
/usr/lib/systemd/system/libvirtd.service
/usr/lib/systemd/system/libvirtd.socket
/usr/lib/systemd/system/virt-guest-shutdown.target
/usr/lib/systemd/system/virtchd-admin.socket
/usr/lib/systemd/system/virtchd-ro.socket
/usr/lib/systemd/system/virtchd.service
/usr/lib/systemd/system/virtchd.socket
/usr/lib/systemd/system/virtinterfaced-admin.socket
/usr/lib/systemd/system/virtinterfaced-ro.socket
/usr/lib/systemd/system/virtinterfaced.service
/usr/lib/systemd/system/virtinterfaced.socket
/usr/lib/systemd/system/virtlockd-admin.socket
/usr/lib/systemd/system/virtlockd.service
/usr/lib/systemd/system/virtlockd.socket
/usr/lib/systemd/system/virtlogd-admin.socket
/usr/lib/systemd/system/virtlogd.service
/usr/lib/systemd/system/virtlogd.socket
/usr/lib/systemd/system/virtlxcd-admin.socket
/usr/lib/systemd/system/virtlxcd-ro.socket
/usr/lib/systemd/system/virtlxcd.service
/usr/lib/systemd/system/virtlxcd.socket
/usr/lib/systemd/system/virtnetworkd-admin.socket
/usr/lib/systemd/system/virtnetworkd-ro.socket
/usr/lib/systemd/system/virtnetworkd.service
/usr/lib/systemd/system/virtnetworkd.socket
/usr/lib/systemd/system/virtnodedevd-admin.socket
/usr/lib/systemd/system/virtnodedevd-ro.socket
/usr/lib/systemd/system/virtnodedevd.service
/usr/lib/systemd/system/virtnodedevd.socket
/usr/lib/systemd/system/virtnwfilterd-admin.socket
/usr/lib/systemd/system/virtnwfilterd-ro.socket
/usr/lib/systemd/system/virtnwfilterd.service
/usr/lib/systemd/system/virtnwfilterd.socket
/usr/lib/systemd/system/virtproxyd-admin.socket
/usr/lib/systemd/system/virtproxyd-ro.socket
/usr/lib/systemd/system/virtproxyd-tcp.socket
/usr/lib/systemd/system/virtproxyd-tls.socket
/usr/lib/systemd/system/virtproxyd.service
/usr/lib/systemd/system/virtproxyd.socket
/usr/lib/systemd/system/virtqemud-admin.socket
/usr/lib/systemd/system/virtqemud-ro.socket
/usr/lib/systemd/system/virtqemud.service
/usr/lib/systemd/system/virtqemud.socket
/usr/lib/systemd/system/virtsecretd-admin.socket
/usr/lib/systemd/system/virtsecretd-ro.socket
/usr/lib/systemd/system/virtsecretd.service
/usr/lib/systemd/system/virtsecretd.socket
/usr/lib/systemd/system/virtstoraged-admin.socket
/usr/lib/systemd/system/virtstoraged-ro.socket
/usr/lib/systemd/system/virtstoraged.service
/usr/lib/systemd/system/virtstoraged.socket

%files locales -f libvirt.lang
%defattr(-,root,root,-)

