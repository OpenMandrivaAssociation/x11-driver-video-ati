%define debug_package	%{nil}

Name: x11-driver-video-ati
Version: 6.7.197
Release: %mkrel 1
Epoch: 1
Summary: The X.org driver for ATI Technologies
Group: System/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/drivers/xf86-video-ati xorg/drivers/xf86-video-ati
# cd xorg/drivers/xf86-video/ati
# git-archive --format=tar --prefix=xf86-video-ati-6.7.197/ xf86-video-ati-6.7.197 | bzip2 -9 > xf86-video-ati-6.7.197.tar.bz2
########################################################################
Source0: xf86-video-ati-%{version}.tar.bz2
License: MIT
########################################################################
# git-format-patch xf86-video-ati-6.7.197..origin/mandriva+gpl
Patch1: 0001-Update-for-new-policy-of-hidden-symbols-and-common-m.patch
Patch2: 0002-Fix-several-symbol-export-problems-due-to-only-acc.patch
########################################################################
BuildRequires: x11-util-macros >= 1.1.5-4mdk
BuildRequires: libdrm-devel		>= 2.3.0
BuildRequires: libpixman-1-devel	>= 0.9.6
BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: libmesagl-devel		>= 7.0.2
BuildRequires: x11-server-devel		>= 1.4

BuildRequires: GL-devel
Conflicts: xorg-x11-server < 7.0
Conflicts: x11-driver-video-ati_6.7

%description
The X.org driver for ATI Technologies

%prep
%setup -q -n xf86-video-ati-%{version}

%patch1 -p1
%patch2 -p1

%build
autoreconf -ifs
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/xorg/modules/drivers/*.la
rm -f %{buildroot}/%{_libdir}/xorg/modules/multimedia/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/radeon_drv.so
%{_libdir}/xorg/modules/drivers/r128_drv.so
%{_libdir}/xorg/modules/drivers/atimisc_drv.so
%{_libdir}/xorg/modules/drivers/ati_drv.so
%{_libdir}/xorg/modules/multimedia/theatre200_drv.so
%{_libdir}/xorg/modules/multimedia/theatre_detect_drv.so
%{_libdir}/xorg/modules/multimedia/theatre_drv.so
%{_mandir}/man4/r128.*
%{_mandir}/man4/ati.*
%{_mandir}/man4/radeon.*
