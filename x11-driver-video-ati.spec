%global _disable_ld_no_undefined 1
# When updating this driver, please update ldetect-lst with new pci ids.
# for example:
# merge2pcitable.pl ati_pciids_csv src/pcidb/ati_pciids.csv pcitable > pcitable.new
# - Anssi

Name:		x11-driver-video-ati
Epoch:		1
Version:	7.1.0
#Release:	0.201210910.1
Release:	1
Summary:	X.org driver for ATI Technologies
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
# ce1b745dcb60dc516ad999756240b78e72a7aa54
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-ati-%{version}.tar.bz2
BuildRequires:	pkgconfig(libdrm) >= 2.4.36
BuildRequires:	pkgconfig(libdrm_radeon) >= 2.4.36
BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1
BuildRequires:	pkgconfig(xorg-server) >= 1.12
BuildRequires:	pkgconfig(gl)
%if %mdvver >= 201200
BuildRequires:	pkgconfig(udev) >= 186
Requires:		udev
%else
BuildRequires:	pkgconfig(udev)
%endif
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)
Conflicts:	xorg-x11-server < 7.0
Conflicts:	x11-driver-video-ati_6.7
Suggests:	x11-driver-video-r128
Suggests:	x11-driver-video-mach64
Suggests:	radeon-firmware

Patch10:    radeon-6.12.2-lvds-default-modes.patch
Patch13:    fix-default-modes.patch

%description
x11-driver-video-ati is the X.org driver for ATI Technologies.

%prep
%setup -qn xf86-video-ati-%{version}
%patch10 -p1 -b .lvds
%patch13 -p1 -b .def

%build
autoreconf -iv
%configure2_5x --disable-static
%make

%install
%makeinstall_std

# these only work in UMS, which is not supported
rm -rf %{buildroot}%{moduledir}/multimedia/

%files
%{_libdir}/xorg/modules/drivers/radeon_drv.so
%{_libdir}/xorg/modules/drivers/ati_drv.so
#%{_libdir}/xorg/modules/multimedia/theatre200_drv.so
#%{_libdir}/xorg/modules/multimedia/theatre_detect_drv.so
#%{_libdir}/xorg/modules/multimedia/theatre_drv.so
%{_mandir}/man4/ati.*
%{_mandir}/man4/radeon.*


%changelog
* Thu Oct 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:6.99.99-0.20121016.1
+ Revision: 819724
- update to latest snapshot from git master branch to get working with new X
- fix drm check which resulted in '/usr/bin/yes' were invoked and ran on for
  ever during configure (P1)
- removal of .la files is now automatically handled by spec-helper

  + Bernhard Rosenkraenzer <bero@bero.eu>
    - Rebuild for xorg-server 1.13

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - rebuild for new udev >= 186

* Wed Jul 04 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:6.14.6-2
+ Revision: 808016
- Produce a fatal error at build time on libdrm version mismatch
  instead of building a driver that doesn't work

* Sun Jul 01 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:6.14.6-1
+ Revision: 807699
- Update to 6.14.6

* Sun Jul 01 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:6.14.5-1
+ Revision: 807673
- Update to 6.14.5

* Thu Apr 05 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:6.14.4-3
+ Revision: 789277
- Adjust x11-server build requirements

* Wed Apr 04 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:6.14.4-2
+ Revision: 789258
- Update build requirements
- Fail the build instead of building a non-working driver if KMS support can't
  be built

* Thu Mar 29 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:6.14.4-1
+ Revision: 788248
- Update to 6.14.4

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1:6.14.3-3
+ Revision: 787195
- Update BuildRequires
- Port to x11-server 1.12

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1:6.14.3-2
+ Revision: 748385
- rebuild cleaned up spec

* Fri Nov 04 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:6.14.3-1
+ Revision: 717701
- update to new version 6.14.3

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1:6.14.2-2
+ Revision: 703677
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1:6.14.2-1
+ Revision: 683756
- Drop P0.
- New version 6.14.2.

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1:6.14.1-3
+ Revision: 683544
- Rebuild for new x11-server

* Tue Mar 22 2011 Thomas Backlund <tmb@mandriva.org> 1:6.14.1-2
+ Revision: 647648
- add upstream bugfix for r6xx/r7xx ums mode

* Tue Mar 22 2011 Thomas Backlund <tmb@mandriva.org> 1:6.14.1-1
+ Revision: 647609
- update to 6.14.1
- drop P0 (merged)
- suggest radeon-firmware

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 1:6.14.0-3
+ Revision: 640294
- rebuild to obsolete old packages

* Wed Feb 09 2011 Thomas Backlund <tmb@mandriva.org> 1:6.14.0-2
+ Revision: 637069
- UMS/DCE3.2: fix segfault (#62460)

* Fri Feb 04 2011 Thierry Vignaud <tv@mandriva.org> 1:6.14.0-1
+ Revision: 635742
- new release

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1:6.13.99-0.20101029.1mdv2011.0
+ Revision: 595705
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1:6.13.2-3mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Fri Oct 08 2010 Thomas Backlund <tmb@mandriva.org> 1:6.13.2-2mdv2011.0
+ Revision: 584091
- rebuild for new GL-devel

* Tue Sep 28 2010 Thierry Vignaud <tv@mandriva.org> 1:6.13.2-1mdv2011.0
+ Revision: 581561
- new release

* Wed Jul 14 2010 Thierry Vignaud <tv@mandriva.org> 1:6.13.1-1mdv2011.0
+ Revision: 553337
- drop patch 0 (uneeded)
- new release

* Fri May 14 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1:6.13.0-3mdv2010.1
+ Revision: 544807
- Add upstream patch for bug #58425
  CCBUG: 58425

* Fri Apr 09 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1:6.13.0-2mdv2010.1
+ Revision: 533531
- Suggest radeon-rlc-firmware

  + Anssi Hannula <anssi@mandriva.org>
    - add a reminder comment about updating ldetect-lst pci id lists

* Mon Apr 05 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1:6.13.0-1mdv2010.1
+ Revision: 531754
- New version: 6.13.0
- Remove autoreconf line

* Mon Mar 15 2010 Thierry Vignaud <tv@mandriva.org> 1:6.12.192-1mdv2010.1
+ Revision: 520386
- new release

* Wed Mar 03 2010 Thierry Vignaud <tv@mandriva.org> 1:6.12.191-1mdv2010.1
+ Revision: 513916
- new release

* Tue Feb 09 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1:6.12.99-0.20100209mdv2010.1
+ Revision: 502961
- Use git master version (as discussed in the mailing list)

* Mon Feb 01 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1:6.12.4-4mdv2010.1
+ Revision: 499207
- Add a patch to fix bug #56862

* Mon Dec 07 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1:6.12.4-3mdv2010.1
+ Revision: 474515
- Add a patch that fix the problems triggered by server 1.7.3

* Tue Nov 10 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1:6.12.4-2mdv2010.1
+ Revision: 464293
- Rebuild for new server

* Fri Sep 25 2009 Thierry Vignaud <tv@mandriva.org> 1:6.12.4-1mdv2010.0
+ Revision: 448656
- new release

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1:6.12.3-1mdv2010.0
+ Revision: 436477
- new release
- drop patch 1 (merged)

* Tue Jul 14 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1:6.12.2-4mdv2010.0
+ Revision: 395955
- Change default acceleration method to EXA.

* Tue Jul 14 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1:6.12.2-3mdv2010.0
+ Revision: 395921
- Sync with 6.12-branch
- Fix dual head cursor corruption (mdv #50560)

* Wed Apr 08 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1:6.12.2-1mdv2009.1
+ Revision: 365207
- New version 6.12.2

* Thu Mar 19 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1:6.12.1-1mdv2009.1
+ Revision: 357791
- New version 6.12.1

* Mon Mar 16 2009 Olivier Blin <blino@mandriva.org> 1:6.12.0-1mdv2009.1
+ Revision: 356182
- 6.12.0

* Thu Feb 19 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1:6.11.0-1mdv2009.1
+ Revision: 342874
- New version 6.11.0
- use %%configure2_5x instead of %%configure to silence ./configure warnings

* Wed Jan 07 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1:6.10.0-1mdv2009.1
+ Revision: 326556
- New version

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1:6.9.0-4mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 1:6.9.0-3mdv2009.1
+ Revision: 308163
- rebuild for new X server

  + Ander Conselvan de Oliveira <ander@mandriva.com>
    - Add suggests tag for r128 and mach64 to avoid backporting issues. (#41710)

* Fri Jun 27 2008 Thierry Vignaud <tv@mandriva.org> 1:6.9.0-1mdv2009.0
+ Revision: 229560
- new release

* Wed Jun 25 2008 Thierry Vignaud <tv@mandriva.org> 1:6.8.192-1mdv2009.0
+ Revision: 229042
- new release

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1:6.8.191-1mdv2009.0
+ Revision: 219466
- new release
- improved description
- add missing dot at end of description
- improved summary

* Tue Feb 19 2008 Thierry Vignaud <tv@mandriva.org> 1:6.8.0-1mdv2008.1
+ Revision: 173135
- new release

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 1:6.7.197-6mdv2008.1
+ Revision: 165422
- Attempt fix for bugs:
  o X hangs at startup with ati driver (http://qa.mandriva.com/show_bug.cgi?id=37209) and
  In this case, just used git-cherry-pick to match code in git master, where
  it has been reverted to match bios agp configuration, unless overriden
  by AgpMode option in xorg.conf.
  o X windows server will not start with new install of 2008.1 Beta 1 (http://qa.mandriva.com/show_bug.cgi?id=37292)
  Backport two commits to attempt to get a more sane output configuration,
  as the bug report shows that the driver got confused and did not understand
  that the monitor section already refered to the LVDS monitor.

* Fri Feb 08 2008 Paulo Andrade <pcpa@mandriva.com.br> 1:6.7.197-5mdv2008.1
+ Revision: 164303
- Must be rebuilt due to an incorrect change added in previous X Server
  build. Must be rebuilt with latest X Server sdk headers.

* Wed Jan 30 2008 Paulo Andrade <pcpa@mandriva.com.br> 1:6.7.197-3mdv2008.1
+ Revision: 160588
- Revert to use only upstream tarball and only mandatory patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1:6.7.197-2mdv2008.1
+ Revision: 156599
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1:6.7.197-1mdv2008.1
+ Revision: 154893
- Updated BuildRequires and resubmit package.
- Update to version 6.7.197.
  Rebase mandriva git branch to xf86-video-ati-6.7.197 and remake patches
  acordingly.
- Disable debug package.
  Update BuildRequires.
  Update to ati-6.7.197 deferred as there is no git tag for the proper version
  and signficant amount of ``compiled test-only'' commits. Need to have package
  in cooker before spending significant time on this package.
- Fix linkage problems with -fvisibility=hidden due to symbols being accessed
  using LoaderSymbol (basically dlsym) as such symbols must be made of default
  visibility.
  Also some "janitor" work by adding prototypes to functions without prototypes,
  converting to static functions without prototype and used in a single file
  and fixing incorrect declarations and also moving some declarations to header
  files.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Update ati module to use tarball from tag xf86-video-ati-6.7.196, and
  remake mandriva branches, and apply mandriva patches from that point.
  This probably won't make everybody happy, but was probably the major
  concern about the misunderstandings about the changes to Mandriva x11
  related packages.
- Update for new policy of hidden symbols and common macros.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 18 2007 Adam Williamson <awilliamson@mandriva.org> 1:6.7.196-1mdv2008.1
+ Revision: 110002
- drop git.diff (came from git so will be in this new version)
- new release 6.7.196

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1:6.7.195-4mdv2008.1
+ Revision: 98686
- minor spec cleanup
- build against new xserver (1.4)

* Fri Oct 12 2007 Thierry Vignaud <tv@mandriva.org> 1:6.7.195-3mdv2008.1
+ Revision: 97573
- patch 1: more git fixes (fixing fd.o #12770 regarding LCD monitor detection on xpress 200)

* Thu Oct 11 2007 Thierry Vignaud <tv@mandriva.org> 1:6.7.195-2mdv2008.1
+ Revision: 97064
- patch 1: git fixes (fixing fd.o #12770 regarding CRT monitor detection on xpress 200)

* Wed Oct 10 2007 Thierry Vignaud <tv@mandriva.org> 1:6.7.195-1mdv2008.1
+ Revision: 96856
- new release

* Wed Oct 10 2007 Thierry Vignaud <tv@mandriva.org> 1:6.7.194-3mdv2008.1
+ Revision: 96739
- kill old patch 0
- new release

* Wed Sep 19 2007 Paulo Andrade <pcpa@mandriva.com.br> 1:6.6.3-3mdv2008.0
+ Revision: 91016
- Possible fix to bugzilla #32553

* Mon Sep 10 2007 Thierry Vignaud <tv@mandriva.org> 1:6.6.3-2mdv2008.0
+ Revision: 84078
- explicitely conflicts with x11-driver-video-ati_6.7

* Thu Sep 06 2007 Thierry Vignaud <tv@mandriva.org> 1:6.6.3-1mdv2008.0
+ Revision: 81005
- do not harcode man pages extension
- reupload stable driver
- restore stable 6.6.3 driver


* Wed Jan 31 2007 Christiaan Welvaart <cjw@daneel.dyndns.org>
+ 2007-01-31 12:17:43 (115683)
- new upstream release (6.6.3)

* Sat Aug 26 2006 Antonio Hobmeir Neto <neto@mandriva.com> 6.6.2-1mdv2007.0
+ 2006-08-25 20:01:05 (58146)
- New release. Fixed Bugs, improves in exa, xaa and R300 support.
- from Gustavo Pichorim Boiko <boiko@mandriva.com>
    - new upstream release (6.6.1):
    Fixes suspend/resume on PCIE
    Fixes interrupt handling
    Lots of EXA fixes
    Other bug fixes and warning removals
    - removed patch radeon-prefer-db-visuals, applied upstream
    - rebuild to fix cooker uploading
    - adding a patch for radeon driver to prefer double-buffered visuals
    - Updated drivers for X11R7.1
    - increment release
    - Adding X.org 7.0 to the repository
- from Thierry Vignaud <tvignaud@mandriva.com>
    - fix group
    - rebuild with the proper ABI on x86_64
- from Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

