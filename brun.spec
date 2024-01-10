#define snapshot 20220107

Name:		brun
Version:	0.0.5
Release:	%{?snapshot:0.%{snapshot}.}3
Summary:	Simple calculator application built with MauiKit.
URL:    	https://mauikit.org
Source0:	https://invent.kde.org/maui/brun/-/archive/%{?snapshot:master}%{!?snapshot:v%{version}}/%{name}-%{?snapshot:master}%{!?snapshot:v%{version}}.tar.bz2%{?snapshot:#/%{name}-%{snapshot}.tar.bz2}
Patch0:   fix-build-with-mauikit-3.0.2.patch
License:	GPLv3
Group:		Development/Tools
BuildRequires:  bison
BuildRequires:	cmake
BuildRequires:  flex
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:  cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5UnitConversion)
BuildRequires:	cmake(MauiKit3)
BuildRequires:  cmake(MauiKitFileBrowsing3)
BuildRequires:	gettext
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:	cmake(Qt5QuickCompiler)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5QmlModels)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Widgets)

%description
Simple calculator application built with MauiKit.

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/brun
%{_datadir}/applications/org.kde.brun.desktop
%{_datadir}/metainfo/org.kde.brun.appdata.xml
%{_iconsdir}/hicolor/scalable/apps/brun.svg
