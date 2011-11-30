%define rel 1

Summary:	Telepathy KDE Integration module
Name:		telepathy-kde-integration-module
Version:	0.2.0
Release:	%mkrel %{rel}
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-kded-module
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%name-%version.tar.bz2
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildRequires:	kdelibs4-devel
BuildRequires:	telepathy-qt4-devel

%description
This module sits in KDED and takes care of various bits of system
integration like setting user to auto-away or handling connection
errors.

%files  -f telepathy-common-internals.lang
%{_kde_libdir}/kde4/kcm_telepathy_kded_module_config.so
%{_kde_libdir}/kde4/kded_telepathy_module.so
%{_kde_services}/kcm_telepathy_kded_module_config.desktop
%{_kde_services}/kded/telepathy_kded_module.desktop
#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang telepathy-common-internals


