#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libvirt
Version  : 1.3.4
Release  : 82
URL      : http://libvirt.org/sources/libvirt-1.3.4.tar.gz
Source0  : http://libvirt.org/sources/libvirt-1.3.4.tar.gz
Summary  : Library providing a simple virtualization API
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 LGPL-2.1+
Requires: libvirt-bin
Requires: libvirt-config
Requires: libvirt-lib
Requires: libvirt-data
Requires: libvirt-doc
Requires: libvirt-locales
BuildRequires : LVM2
BuildRequires : attr-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bridge-utils
BuildRequires : curl-dev
BuildRequires : dbus-dev
BuildRequires : dnsmasq
BuildRequires : ebtables
BuildRequires : fuse-dev
BuildRequires : gettext-bin
BuildRequires : gettext-dev
BuildRequires : gnutls-dev
BuildRequires : iptables
BuildRequires : kmod-bin
BuildRequires : libcap-ng-dev
BuildRequires : libnl-dev
BuildRequires : libpcap-dev
BuildRequires : libpciaccess-dev
BuildRequires : libtasn1-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : libxslt
BuildRequires : m4
BuildRequires : ncurses-dev
BuildRequires : nfs-utils
BuildRequires : numactl-dev
BuildRequires : open-iscsi
BuildRequires : openssh
BuildRequires : openssl-dev
BuildRequires : parted-dev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(devmapper)
BuildRequires : pkgconfig(libnl-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : readline-dev
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : util-linux-dev
BuildRequires : yajl-dev
BuildRequires : yajl-lib
Patch1: 0001-Default-to-0770-permissions-with-group-libvirt-for-t.patch
Patch2: 0002-Move-default-nwfilters-to-datadir.patch
Patch3: 0003-remove-apparmor-from-unit-file.patch
Patch4: 0004-Use-libsystemd-instead-of-libsystemd-daemon.patch
Patch5: 0005-remove-empty-environment-file-from-unit-file.patch
Patch6: 0006-drop-timeout-ping.patch
Patch7: 0007-set-default-ciphers.patch

%description
Libvirt is a C toolkit to interact with the virtualization capabilities
of recent versions of Linux (and other OSes). The main package includes
the libvirtd server exporting the virtualization support.

%package bin
Summary: bin components for the libvirt package.
Group: Binaries
Requires: libvirt-data
Requires: libvirt-config

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
Requires: libvirt-lib
Requires: libvirt-bin
Requires: libvirt-data
Provides: libvirt-devel

%description dev
dev components for the libvirt package.


%package doc
Summary: doc components for the libvirt package.
Group: Documentation

%description doc
doc components for the libvirt package.


%package lib
Summary: lib components for the libvirt package.
Group: Libraries
Requires: libvirt-data
Requires: libvirt-config

%description lib
lib components for the libvirt package.


%package locales
Summary: locales components for the libvirt package.
Group: Default

%description locales
locales components for the libvirt package.


%prep
%setup -q -n libvirt-1.3.4
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
%reconfigure --disable-static ac_cv_path_EBTABLES_PATH=%{_bindir}/ebtables \
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
--without-polkit \
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
--with-yajl
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
rm -rf %{buildroot}
%make_install
%find_lang libvirt
## make_install_append content
mkdir %{buildroot}/usr/lib/systemd/system/sockets.target.wants
ln -s ../libvirtd.socket %{buildroot}/usr/lib/systemd/system/sockets.target.wants/libvirtd.socket
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/libvirtd
/usr/bin/virsh
/usr/bin/virt-admin
/usr/bin/virt-host-validate
/usr/bin/virt-login-shell
/usr/bin/virt-pki-validate
/usr/bin/virt-xml-validate
/usr/bin/virtlockd
/usr/bin/virtlogd
/usr/libexec/libvirt-guests.sh
/usr/libexec/libvirt_iohelper
/usr/libexec/libvirt_leaseshelper
/usr/libexec/libvirt_lxc
/usr/libexec/libvirt_parthelper

%files config
%defattr(-,root,root,-)
/usr/lib/sysctl.d/60-libvirtd.conf
/usr/lib/systemd/system/libvirt-guests.service
/usr/lib/systemd/system/libvirtd.service
/usr/lib/systemd/system/sockets.target.wants/libvirtd.socket
/usr/lib/systemd/system/virtlockd.service
/usr/lib/systemd/system/virtlockd.socket
/usr/lib/systemd/system/virtlogd.service
/usr/lib/systemd/system/virtlogd.socket

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
/usr/share/augeas/lenses/tests/test_virtlockd.aug
/usr/share/augeas/lenses/tests/test_virtlogd.aug
/usr/share/augeas/lenses/virtlockd.aug
/usr/share/augeas/lenses/virtlogd.aug
/usr/share/libvirt/api/libvirt-api.xml
/usr/share/libvirt/api/libvirt-lxc-api.xml
/usr/share/libvirt/api/libvirt-qemu-api.xml
/usr/share/libvirt/cpu_map.xml
/usr/share/libvirt/libvirtLogo.png
/usr/share/libvirt/nwfilter/allow-arp.xml
/usr/share/libvirt/nwfilter/allow-dhcp-server.xml
/usr/share/libvirt/nwfilter/allow-dhcp.xml
/usr/share/libvirt/nwfilter/allow-incoming-ipv4.xml
/usr/share/libvirt/nwfilter/allow-ipv4.xml
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
/usr/share/libvirt/schemas/domain.rng
/usr/share/libvirt/schemas/domaincaps.rng
/usr/share/libvirt/schemas/domaincommon.rng
/usr/share/libvirt/schemas/domainsnapshot.rng
/usr/share/libvirt/schemas/interface.rng
/usr/share/libvirt/schemas/network.rng
/usr/share/libvirt/schemas/networkcommon.rng
/usr/share/libvirt/schemas/nodedev.rng
/usr/share/libvirt/schemas/nwfilter.rng
/usr/share/libvirt/schemas/secret.rng
/usr/share/libvirt/schemas/storagecommon.rng
/usr/share/libvirt/schemas/storagepool.rng
/usr/share/libvirt/schemas/storagevol.rng

%files dev
%defattr(-,root,root,-)
/usr/include/libvirt/libvirt-common.h
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
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libvirt/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*
/usr/share/gtk-doc/html/libvirt/general.html
/usr/share/gtk-doc/html/libvirt/home.png
/usr/share/gtk-doc/html/libvirt/index.html
/usr/share/gtk-doc/html/libvirt/left.png
/usr/share/gtk-doc/html/libvirt/libvirt-virterror.html
/usr/share/gtk-doc/html/libvirt/libvirt.devhelp
/usr/share/gtk-doc/html/libvirt/right.png
/usr/share/gtk-doc/html/libvirt/style.css
/usr/share/gtk-doc/html/libvirt/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/libvirt/connection-driver/libvirt_driver_interface.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_lxc.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_network.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_nodedev.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_nwfilter.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_qemu.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_secret.so
/usr/lib64/libvirt/connection-driver/libvirt_driver_storage.so
/usr/lib64/libvirt/lock-driver/lockd.so

%files locales -f libvirt.lang 
%defattr(-,root,root,-)

