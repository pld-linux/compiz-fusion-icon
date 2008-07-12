%define		_rel	080712git
%define		_name	fusion-icon
Summary:	Small program to control your GL Desktop
Summary(pl.UTF-8):	Mały program do kontroli pulpitu GL
Name:		compiz-%{_name}
Version:	0.1.0
Release:	0.%{_rel}.1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers/Tools
# It's from git://anongit.compiz-fusion.org/users/crdlb/fusion-icon
Source0:	%{_name}-%{_rel}.tar.bz2
# Source0-md5:	767c3ec198b780eb83656c48f92add1d
URL:		http://compiz-fusion.org/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	%{name}-interface = %{epoch}:%{version}-%{release}
Requires:	compiz >= 0.5.1
Requires:	python-compizconfig
Requires:	xorg-app-xvinfo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compiz Fusion Icon is a small program written in Python which lets you
control your GL Desktop it handles your different decorators
(non-GL/GL) and configurators.

%description -l pl.UTF-8
Compiz Fusion Icon jest małym programem napisanym w Pythonie, który
pozwala na kontrolę pulpitu GL. Obsługuje różne dekoratory (GL/nie-GL)
i konfiguratory.

%package interface-gtk
Summary:	GTK+ interface for Compiz Fusion Icon
Summary(pl.UTF-8):	Compiz Fusion Icon - interfejs GTK+
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-pygtk-gtk >= 2:2.10.0
Suggests:	compizconfig-backend-gconf
Provides:	%{name}-interface = %{epoch}:%{version}-%{release}

%description interface-gtk
GTK+ interface for Compiz Fusion Icon.

%description interface-gtk -l pl.UTF-8
Compiz Fusion Icon - interfejs GTK+.

%package interface-qt4
Summary:	Qt4 interface for Compiz Fusion Icon
Summary(pl.UTF-8):	Compiz Fusion Icon - interfejs Qt4+
Group:		X11/Window Managers/Tools
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	python-PyQt4
Suggests:	compizconfig-backend-kconfig
Provides:	%{name}-interface = %{epoch}:%{version}-%{release}

%description interface-qt4
Qt4 interface for Compiz Fusion Icon.

%description interface-qt4 -l pl.UTF-8
Compiz Fusion Icon - interfejs Qt4.

%prep
%setup -q -n %{_name}

%build
%{__python} setup.py build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	-O1 \
	--skip-build \
	--root $RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fusion-icon
%{_desktopdir}/fusion-icon.desktop
%dir %{py_sitescriptdir}/FusionIcon
%{py_sitescriptdir}/FusionIcon/*.py[co]
%{py_sitescriptdir}/fusion_icon-*.egg-info
%{_iconsdir}/hicolor/*x*/apps/fusion-icon.png
%{_iconsdir}/hicolor/scalable/apps/fusion-icon.svg

%files interface-gtk
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/FusionIcon/interface_gtk
%{py_sitescriptdir}/FusionIcon/interface_gtk/*.py[co]

%files interface-qt4
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/FusionIcon/interface_qt4
%{py_sitescriptdir}/FusionIcon/interface_qt4/*.py[co]
