Name: x11-driver-video-ati
Version: 6.7.195
Release: %mkrel 2
Epoch: 1
Summary: The X.org driver for ATI Technologies
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-ati-%{version}.tar.bz2
Patch1: git.diff

License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel

Conflicts: xorg-x11-server < 7.0
Conflicts: x11-driver-video-ati_6.7

%description
The X.org driver for ATI Technologies


%prep
%setup -q -n xf86-video-ati-%{version}
%patch1 -p1

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_libdir}/xorg/modules/drivers/radeon_drv.la
%{_libdir}/xorg/modules/drivers/radeon_drv.so
%{_libdir}/xorg/modules/drivers/r128_drv.la
%{_libdir}/xorg/modules/drivers/r128_drv.so
%{_libdir}/xorg/modules/drivers/atimisc_drv.la
%{_libdir}/xorg/modules/drivers/atimisc_drv.so
%{_libdir}/xorg/modules/drivers/ati_drv.la
%{_libdir}/xorg/modules/drivers/ati_drv.so
%{_libdir}/xorg/modules/multimedia/theatre200_drv.la
%{_libdir}/xorg/modules/multimedia/theatre200_drv.so
%{_libdir}/xorg/modules/multimedia/theatre_detect_drv.la
%{_libdir}/xorg/modules/multimedia/theatre_detect_drv.so
%{_libdir}/xorg/modules/multimedia/theatre_drv.la
%{_libdir}/xorg/modules/multimedia/theatre_drv.so
%{_mandir}/man4/r128.*
%{_mandir}/man4/ati.*
%{_mandir}/man4/radeon.*

