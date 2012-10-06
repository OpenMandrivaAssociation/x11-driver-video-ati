# When updating this driver, please update ldetect-lst with new pci ids.
# for example:
# merge2pcitable.pl ati_pciids_csv src/pcidb/ati_pciids.csv pcitable > pcitable.new
# - Anssi

Name:		x11-driver-video-ati
Epoch:		1
Version:	6.14.6
Release:	4
Summary:	X.org driver for ATI Technologies
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-ati-%{version}.tar.bz2
# Abort the build if we can't build in KMS/DRI2 support.
# Better to fail the build than to get a non-working driver!
Patch0:		xf86-video-ati-6.14.4-error-on-no-kms.patch
Patch1:		xf86-video-ati-6.14.6-lack-of-dri2-is-an-error.patch
BuildRequires:	pkgconfig(libdrm) >= 2.4.36
BuildRequires:	pkgconfig(libdrm_radeon) >= 2.4.36
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(x11-server) >= 1.13
BuildRequires:	pkgconfig(gl)
%if %mdvver >= 201200
BuildRequires:	pkgconfig(udev) >= 186
%else
BuildRequires:	pkgconfig(udev)
%endif
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
Conflicts:	xorg-x11-server < 7.0
Conflicts:	x11-driver-video-ati_6.7
Suggests:	x11-driver-video-r128
Suggests:	x11-driver-video-mach64
Suggests:	radeon-firmware

%description
x11-driver-video-ati is the X.org driver for ATI Technologies.

%prep
%setup -qn xf86-video-ati-%{version}
%apply_patches
autoconf

%build
%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%{_libdir}/xorg/modules/drivers/radeon_drv.so
%{_libdir}/xorg/modules/drivers/ati_drv.so
%{_libdir}/xorg/modules/multimedia/theatre200_drv.so
%{_libdir}/xorg/modules/multimedia/theatre_detect_drv.so
%{_libdir}/xorg/modules/multimedia/theatre_drv.so
%{_mandir}/man4/ati.*
%{_mandir}/man4/radeon.*
