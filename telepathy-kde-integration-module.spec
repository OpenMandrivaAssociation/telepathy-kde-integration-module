%define srcname ktp-kded-integration-module
Summary:        Telepathy KDE Integration module
Name:           telepathy-kde-integration-module
Version:	0.5.1
Release:        1
Url:            https://projects.kde.org/projects/playground/network/telepathy/telepathy-kded-module
Source0:        ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%srcname-%version.tar.bz2
License:        GPLv2+
Group:          Networking/Instant messaging
BuildRequires:  telepathy-kde-common-internals-devel >= %{version}
Requires:       telepathy-kde-common-internals-core


%description
This module sits in KDED and takes care of various bits of system
integration like setting user to auto-away or handling connection
errors.

%files  -f kded_ktp_integration_module.lang
%{_kde_libdir}/kde4/kcm_ktp_integration_module.so
%{_kde_libdir}/kde4/kded_ktp_integration_module.so
%{_kde_services}/kded/kded_ktp_integration_module.desktop
%{_kde_services}/kcm_ktp_integration_module.desktop
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.KdedIntegrationModule.service

#--------------------------------------------------------------------

%prep
%setup -q -n %srcname-%version

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang kded_ktp_integration_module
