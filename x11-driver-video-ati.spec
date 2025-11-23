%global _disable_ld_no_undefined 1
# When updating this driver, please update ldetect-lst with new pci ids.
# for example:
# merge2pcitable.pl ati_pciids_csv src/pcidb/ati_pciids.csv pcitable > pcitable.new
# - Anssi
%define abi 25.0

#define gitdate 20250724

Name:		x11-driver-video-ati
Version:	22.0.0.4
Release:	1
Summary:	X.org driver for ATI Technologies
Group:		System/X11
License:	MIT
URL:		https://xorg.freedesktop.org
# Use maintainded xlibre version instead of deprecated freedesktop (AP)
Source0:  https://github.com/X11Libre/xf86-video-ati/archive/refs/tags/xlibre-xf86-video-ati-%{version}.tar.gz
#Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-ati-%{version}.tar.xz
# upstream git:

# Fedora patches:
Patch10:	radeon-6.12.2-lvds-default-modes.patch
Patch13:	fix-default-modes.patch

BuildRequires:	pkgconfig(libdrm) >= 2.4.54
BuildRequires:	pkgconfig(libdrm_radeon) >= 2.4.54
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(xorg-server) >= 1.18
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(udev) >= 186
BuildRequires:	pkgconfig(gbm)
Requires:	udev
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
Conflicts:	xorg-x11-server < 7.0
Conflicts:	x11-driver-video-ati_6.7
Suggests:	radeon-firmware
Requires:	%{_lib}dri-drivers

%description
x11-driver-video-ati is the X.org driver for ATI Technologies.

%prep
%autosetup -n xf86-video-ati-xlibre-xf86-video-ati-%{version} -p1
sed -i '/USE_XAA, 1/d' configure.ac
autoreconf -ifs

%build
%configure --disable-static --enable-glamor
%make_build

%install
%make_install

# these only work in UMS, which is not supported
rm -rf %{buildroot}%{moduledir}/multimedia/

%files
%{_libdir}/xorg/modules/xlibre-%{abi}/drivers/radeon_drv.so
%{_libdir}/xorg/modules/xlibre-%{abi}/drivers/ati_drv.so
%{_datadir}/X11/xorg.conf.d/10-radeon.conf
%{_mandir}/man4/ati.*
%{_mandir}/man4/radeon.*
