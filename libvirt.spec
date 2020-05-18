#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x15588B26596BEA5D (Daniel.Veillard@w3.org)
#
Name     : libvirt
Version  : 5.8.0
Release  : 117
URL      : https://libvirt.org/sources/libvirt-5.8.0.tar.xz
Source0  : https://libvirt.org/sources/libvirt-5.8.0.tar.xz
Source1  : https://libvirt.org/sources/libvirt-5.8.0.tar.xz.asc
Summary  : Library providing a simple virtualization API
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 LGPL-2.1+ OFL-1.1
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
BuildRequires : LVM2
BuildRequires : LVM2-dev
BuildRequires : LVM2-extras
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : audit-dev
BuildRequires : bridge-utils
BuildRequires : curl-dev
BuildRequires : dbus-dev
BuildRequires : dnsmasq
BuildRequires : ebtables
BuildRequires : fuse-dev
BuildRequires : gettext-dev
BuildRequires : glibc-locale
BuildRequires : intltool-dev
BuildRequires : iptables
BuildRequires : kmod-bin
BuildRequires : libcap-ng-dev
BuildRequires : libnl-dev
BuildRequires : libpcap-dev
BuildRequires : libpciaccess-dev
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
BuildRequires : parted-dev
BuildRequires : pkgconfig(gnutls)
BuildRequires : polkit
BuildRequires : polkit-dev
BuildRequires : readline-dev
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : util-linux-dev
BuildRequires : yajl-dev
BuildRequires : yajl-lib
Patch1: 0001-Default-to-0770-permissions-with-group-libvirt-for-t.patch
Patch2: 0002-Load-default-nwfilters-from-datadir.patch
Patch3: 0003-drop-timeout-ping.patch
Patch4: 0004-set-default-ciphers.patch
Patch5: 0005-release-unused-memory-back-to-the-system.patch
Patch6: 0006-Arjan-s-patch-for-locale.patch

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

%description services
services components for the libvirt package.


%prep
%setup -q -n libvirt-5.8.0
cd %{_builddir}/libvirt-5.8.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589821977
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$FFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static ac_cv_path_EBTABLES_PATH=%{_bindir}/ebtables \
ac_cv_path_IP_PATH= \
--disable-dependency-tracking \
--enable-nls \
--with-dbus \
--with-init-script=systemd \
--with-interface \
--with-libvirtd \
--with-lxc \
--with-macvtap=yes \
--with-numactl \
--without-apparmor \
--without-dtrace \
--without-esx \
--without-firewalld \
--without-fuse \
--without-hyperv \
--without-libxl \
--without-netcf \
--without-openvz \
--without-phyp \
--without-pm-utils \
--without-sasl \
--without-selinux \
--without-uml \
--without-vbox \
--without-vmware \
--without-xen \
--without-xenapi \
--without-xen-inotify \
--with-pciaccess \
--with-qemu-group=qemu \
--with-qemu-user=qemu \
--with-qemu=yes \
--with-remote \
--with-test=yes \
--with-udev \
--with-yajl \
--with-openssl \
--with-polkit \
--with-loader-nvram=/usr/share/qemu/OVMF.fd:/usr/share/qemu/OVMF.fd:/usr/share/qemu/OVMF_CODE.fd:/usr/share/qemu/OVMF_VARS.fd \
--with-firewalld \
--with-firewalld-zone
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1589821977
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libvirt
cp %{_builddir}/libvirt-5.8.0/COPYING %{buildroot}/usr/share/package-licenses/libvirt/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/libvirt-5.8.0/COPYING.LESSER %{buildroot}/usr/share/package-licenses/libvirt/3704f4680301a60004b20f94e0b5b8c7ff1484a9
cp %{_builddir}/libvirt-5.8.0/docs/fonts/LICENSE.md %{buildroot}/usr/share/package-licenses/libvirt/395cbfe3e7e4a5da6e5f41c406fcb0eab7e38426
%make_install
%find_lang libvirt
## Remove excluded files
rm -f %{buildroot}/etc/logrotate.d/libvirtd
rm -f %{buildroot}/etc/logrotate.d/libvirtd.lxc
rm -f %{buildroot}/etc/logrotate.d/libvirtd.qemu
rm -f %{buildroot}/etc/logrotate.d/libvirtd.uml
rm -f %{buildroot}/etc/sysconfig/libvirtd
rm -f %{buildroot}/etc/sysconfig/libvirt-guests
rm -f %{buildroot}/etc/sysconfig/virtlockd
rm -f %{buildroot}/etc/libvirt/libvirt.conf
rm -f %{buildroot}/etc/libvirt/libvirtd.conf
rm -f %{buildroot}/etc/libvirt/lxc.conf
rm -f %{buildroot}/etc/libvirt/qemu.conf
rm -f %{buildroot}/etc/libvirt/qemu-lockd.conf
rm -f %{buildroot}/etc/libvirt/virtlockd.conf
rm -f %{buildroot}/etc/libvirt/virt-login-shell.conf
rm -f %{buildroot}/etc/libvirt/qemu/networks/autostart/default.xml
rm -f %{buildroot}/etc/libvirt/qemu/networks/default.xml
## install_append content
mkdir %{buildroot}/usr/lib/systemd/system/multi-user.target.wants
ln -s ../libvirtd.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/libvirtd.service
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/firewalld/zones/libvirt.xml

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/libvirtd.service

%files bin
%defattr(-,root,root,-)
/usr/bin/libvirtd
/usr/bin/virsh
/usr/bin/virt-admin
/usr/bin/virt-host-validate
/usr/bin/virt-login-shell
/usr/bin/virt-pki-validate
/usr/bin/virt-xml-validate
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
/usr/share/libvirt/api/libvirt-admin-api.xml
/usr/share/libvirt/api/libvirt-api.xml
/usr/share/libvirt/api/libvirt-lxc-api.xml
/usr/share/libvirt/api/libvirt-qemu-api.xml
/usr/share/libvirt/cpu_map/index.xml
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
/usr/share/libvirt/cpu_map/x86_Cascadelake-Server.xml
/usr/share/libvirt/cpu_map/x86_Conroe.xml
/usr/share/libvirt/cpu_map/x86_EPYC-IBPB.xml
/usr/share/libvirt/cpu_map/x86_EPYC.xml
/usr/share/libvirt/cpu_map/x86_Haswell-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Haswell-noTSX-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Haswell-noTSX.xml
/usr/share/libvirt/cpu_map/x86_Haswell.xml
/usr/share/libvirt/cpu_map/x86_Icelake-Client.xml
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
/usr/share/libvirt/cpu_map/x86_Skylake-Client-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Skylake-Client.xml
/usr/share/libvirt/cpu_map/x86_Skylake-Server-IBRS.xml
/usr/share/libvirt/cpu_map/x86_Skylake-Server.xml
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
/usr/share/libvirt/nwfilter/allow-arp.xml
/usr/share/libvirt/nwfilter/allow-dhcp-server.xml
/usr/share/libvirt/nwfilter/allow-dhcp.xml
/usr/share/libvirt/nwfilter/allow-incoming-ipv4.xml
/usr/share/libvirt/nwfilter/allow-ipv4.xml
/usr/share/libvirt/nwfilter/clean-traffic-gateway.xml
/usr/share/libvirt/nwfilter/clean-traffic.xml
/usr/share/libvirt/nwfilter/no-arp-ip-spoofing.xml
/usr/share/libvirt/nwfilter/no-arp-mac-spoofing.xml
/usr/share/libvirt/nwfilter/no-arp-spoofing.xml
/usr/share/libvirt/nwfilter/no-ip-multicast.xml
/usr/share/libvirt/nwfilter/no-ip-spoofing.xml
/usr/share/libvirt/nwfilter/no-mac-broadcast.xml
/usr/share/libvirt/nwfilter/no-mac-spoofing.xml
/usr/share/libvirt/nwfilter/no-other-l2-traffic.xml
/usr/share/libvirt/nwfilter/no-other-rarp-traffic.xml
/usr/share/libvirt/nwfilter/qemu-announce-self-rarp.xml
/usr/share/libvirt/nwfilter/qemu-announce-self.xml
/usr/share/libvirt/schemas/basictypes.rng
/usr/share/libvirt/schemas/capability.rng
/usr/share/libvirt/schemas/cputypes.rng
/usr/share/libvirt/schemas/domain.rng
/usr/share/libvirt/schemas/domaincaps.rng
/usr/share/libvirt/schemas/domaincheckpoint.rng
/usr/share/libvirt/schemas/domaincommon.rng
/usr/share/libvirt/schemas/domainsnapshot.rng
/usr/share/libvirt/schemas/interface.rng
/usr/share/libvirt/schemas/network.rng
/usr/share/libvirt/schemas/networkcommon.rng
/usr/share/libvirt/schemas/networkport.rng
/usr/share/libvirt/schemas/nodedev.rng
/usr/share/libvirt/schemas/nwfilter.rng
/usr/share/libvirt/schemas/nwfilter_params.rng
/usr/share/libvirt/schemas/nwfilterbinding.rng
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
%doc /usr/share/doc/libvirt/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnss_libvirt.so.2
/usr/lib64/libnss_libvirt_guest.so.2
/usr/lib64/libvirt-admin.so.0
/usr/lib64/libvirt-admin.so.0.5008.0
/usr/lib64/libvirt-lxc.so.0
/usr/lib64/libvirt-lxc.so.0.5008.0
/usr/lib64/libvirt-qemu.so.0
/usr/lib64/libvirt-qemu.so.0.5008.0
/usr/lib64/libvirt.so.0
/usr/lib64/libvirt.so.0.5008.0
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
/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_iscsi.so
/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_logical.so
/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_mpath.so
/usr/lib64/libvirt/storage-backend/libvirt_storage_backend_scsi.so
/usr/lib64/libvirt/storage-file/libvirt_storage_file_fs.so

%files libexec
%defattr(-,root,root,-)
/usr/libexec/libvirt-guests.sh
/usr/libexec/libvirt_iohelper
/usr/libexec/libvirt_leaseshelper
/usr/libexec/libvirt_lxc
/usr/libexec/libvirt_parthelper
/usr/libexec/virt-login-shell-helper

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libvirt/3704f4680301a60004b20f94e0b5b8c7ff1484a9
/usr/share/package-licenses/libvirt/395cbfe3e7e4a5da6e5f41c406fcb0eab7e38426
/usr/share/package-licenses/libvirt/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/virsh.1
/usr/share/man/man1/virt-admin.1
/usr/share/man/man1/virt-host-validate.1
/usr/share/man/man1/virt-login-shell.1
/usr/share/man/man1/virt-pki-validate.1
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
/usr/share/man/man8/libvirtd.8
/usr/share/man/man8/virtlockd.8
/usr/share/man/man8/virtlogd.8

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

