%define		_rel	071103git
%define		_name	fusion-icon
Summary:	small program to control your GL Desktop
Summary(pl.UTF-8):	mały program do kontroli Pulpitu
Name:		compiz-%{_name}
Version:	5.2
Release:	0.1%{_rel}
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers/Tools
#Source0:	http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
Source0:	%{_name}-%{_rel}.tar.bz2
# Source0-md5:	7cf51276a0fb33a357f921e3f320b86f
URL:		http://beryl-project.org/
BuildRequires:	python-devel
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	rpm-pythonprov
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires:	compiz >= 0.5.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Compiz Fusion Icon is a small program written in python which lets you
control your GL Desktop it handles your different decorators
(non-GL/GL) and configurators.

%description -l pl.UTF-8
Compiz Fusion Icon jest małym programem napisanym w pythonie, który
pozwala na kontrolę pulpitu GL. Pozwala na przełączanie się między
różnymi dekoracjami i konfigurację.

%prep
%setup -q -n %{_name}

%build
%{__python} setup.py build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{_datadir}/fusion-icon
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/fusion-icon

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fusion-icon
%{_desktopdir}/fusion-icon.desktop
%dir %{py_sitescriptdir}/FusionIcon
%dir %{py_sitescriptdir}/FusionIcon/interface_gtk
%dir %{py_sitescriptdir}/FusionIcon/interface_qt4
%{py_sitescriptdir}/FusionIcon/*.py*
%{py_sitescriptdir}/FusionIcon/interface_gtk/*.py*
%{py_sitescriptdir}/FusionIcon/interface_qt4/*.py*
%{_iconsdir}/hicolor/*x*/apps/fusion-icon.png
%{_iconsdir}/hicolor/scalable/apps/fusion-icon.svg
