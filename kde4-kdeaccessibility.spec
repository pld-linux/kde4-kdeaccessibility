
%define		_state		stable
%define		origname	kdeaccessibility
%define		qtver		4.7.0

Summary:	Accessibility support for KDE
Summary(pl.UTF-8):	Ułatwienia dostępu dla KDE
Name:		kde4-kdeaccessibility
Version:	4.5.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{origname}-%{version}.tar.bz2
# Source0-md5:	8866b1594bcb426234a70640bfed5472
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{qtver}
BuildRequires:	QtSvg-devel >= %{qtver}
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	speech-dispatcher-devel >= 0.6.6
BuildRequires:	xorg-lib-libXtst-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Accessibility support for KDE.

%description -l pl.UTF-8
Ułatwienia dostępu dla KDE.

%package devel
Summary:	Accessibility support for KDE - header files
Summary(pl.UTF-8):	Ułatwienia dostępu dla KDE - pliki nagłówkowe
Group:		X11/Applications
Requires:	kde4-kdelibs-devel = %{version}

%description devel
Accessibility support for KDE - header files.

%description devel -l pl.UTF-8
Ułatwienia dostępu dla KDE - pliki nagłówkowe.

%package ColorSchemes
Summary:	KDE Color Schemes
Summary(pl.UTF-8):	Motywy kolorów dla KDE
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}

%description ColorSchemes
KDE Color Schemes.

%description ColorSchemes -l pl.UTF-8
Motyw kolorów dla KDE.

%package -n kde-icons-mono
Summary:	KDE Icons Theme - mono
Summary(pl.UTF-8):	Motyw ikon dla KDE - mono
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}

%description -n kde-icons-mono
KDE Icons Theme - mono.

%description -n kde-icons-mono -l pl.UTF-8
Motyw ikon dla KDE - mono.

%package -n kde-icons-actions
Summary:	KDE Icons Theme - actions
Summary(pl.UTF-8):	Motyw ikon dla KDE - actions
Group:		X11/Amusements
Requires:	kde4-kdelibs >= %{version}

%description -n kde-icons-actions
KDE Icons Theme - actions.

%description -n kde-icons-actions -l pl.UTF-8
Motyw ikon dla KDE - actions.

%package kmag
Summary:	A KDE magnifying tool
Summary(pl.UTF-8):	Lupa dla środowiska KDE
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description kmag
A KDE magnifying tool.

%description kmag -l pl.UTF-8
Lupa dla środowiska KDE.

%package kmousetool
Summary:	KMouseTool - a program that clicks the mouse for you
Summary(pl.UTF-8):	KMouseTool - narzędzie do klikania myszką bez naciskania jej przycisków
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description kmousetool
KMouseTool is a program that clicks the mouse for you. KMouseTool
clicks the mouse whenever the mouse cursor pauses briefly. It was
designed to help those with repetitive strain injuries, for whom
pressing buttons hurts. It can also drag the mouse, although this
takes a bit more practice.

%description kmousetool -l pl.UTF-8
KMouseTool jest narzędziem do klikania myszką bez naciskania jej
przycisków. KMouseTool klika myszką za każdym razem gdy kursor
zatrzymuje się na krótko. Narzędzie to zostało zaprojektowane by pomóc
osobom z uszkodzeniami mięśni, dla których naciskanie przycisków jest
bolesne. Ponadto może ono przeciągać myszą, aczkolwiek wymaga to
pewnej praktyki.

%package kmouth
Summary:	A frontend for speech synthesizers
Summary(pl.UTF-8):	Frontend do syntezatorów mowy
Group:		X11/Applications
Requires:	kde4-kdebase >= %{version}

%description kmouth
KMouth is a frontend for speech synthesizers. It is a program that
enables persons that cannot speak to let their computers speak. It
includes a history of spoken sentences from which the user can select
sentences to be re-spoken.

Note that KMouth does not include speech synthesizer. Instead it
requires a speech synthesizer installed in the system.

%description kmouth -l pl.UTF-8
KMouth jest frontendem do syntezatorów mowy. Jest to narzędzie dzięki
któremu osoby nieme mogą pozwolić komputerowi mówić za nie. Zawiera on
historię wypowiedzianych zdań, z której to użytkownik może wybrać
zdanie do ponownego wypowiedzenia.

UWAGA! KMouth nie zawiera syntezatora mowy. Zamiast tego wykorzystuje
syntezator zainstalowany w systemie.

%package kttsd
Summary:	KDE Text-to-Speech
Summary(pl.UTF-8):	KDE Tekst-w-Mowę
Group:		X11/Applications
Requires:	kde4-kdelibs >= %{version}
Obsoletes:	kttsd

%description kttsd
KTTS -- KDE Text-to-Speech -- is a subsystem within the KDE desktop
for conversion of text to audible speech. KTTS is currently under
development and aims to become the standard subsystem for all KDE
applications to provide speech output.

%description kttsd -l pl.UTF-8
KTTS -- KDE Tekst-w-Mowę -- jest podsystemem środowiska KDE służącym
do konwersji tekstu w słyszalną mowę. KTTS jest cały czas rozwijany,
jego celem jest zostanie standardowym podsystemem dostarczającym
wyjście mowy dla wszystkich aplikacji KDE.

%package kttsd-gstreamer
Summary:	KTTS GStreamer plugin
Summary(pl.UTF-8):	Wtyczka Gstreamer dla KTTS
Group:		X11/Applications
Requires:	%{name}-kttsd = %{version}-%{release}

%description kttsd-gstreamer
KTTS GStreamer plugin.

%description kttsd-gstreamer -l pl.UTF-8
Wtyczka Gstreamer dla KTTS.

%package jovie
Summary:	Jovie
Summary(pl.UTF-8):	Jovie
Group:		X11/Applications

%description jovie
Jovie.

%description jovie -l pl.UTF-8
Jovie.

%prep
%setup -q -n %{origname}-%{version}

%build
install -d build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang kmag		--with-kde
%find_lang kmousetool	--with-kde
%find_lang kmouth	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	kttsd	-p /sbin/ldconfig
%postun	kttsd	-p /sbin/ldconfig

%files ColorSchemes
%defattr(644,root,root,755)
%{_datadir}/apps/color-schemes/Zion.colors
%{_datadir}/apps/color-schemes/ZionReversed.colors

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkttsd.so

%files -n kde-icons-mono
%defattr(644,root,root,755)
%{_iconsdir}/mono
%exclude %{_iconsdir}/mono/*/apps/kmag.*
%exclude %{_iconsdir}/mono/*/apps/kmousetool.*
%exclude %{_iconsdir}/mono/*/apps/kmouth.*

%files -n kde-icons-actions
%defattr(644,root,root,755)
%{_iconsdir}/hicolor/*/actions/*

%files kmag -f kmag.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmag
%{_datadir}/apps/kmag
%{_desktopdir}/kde4/kmag.desktop
%{_iconsdir}/*/*/apps/kmag.*
%{_mandir}/man1/kmag.1.*

%files kmousetool -f kmousetool.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmousetool
%{_datadir}/apps/kmousetool
%{_desktopdir}/kde4/kmousetool.desktop
%{_iconsdir}/*/*/apps/kmousetool.*
%{_mandir}/man1/kmousetool.1.*

%files kmouth -f kmouth.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmouth
%{_datadir}/apps/kmouth
%{_datadir}/config/kmouthrc
%{_desktopdir}/kde4/kmouth.desktop
%{_iconsdir}/*/*/apps/kmouth.*
%{_mandir}/man1/kmouth.1.*

%files kttsd
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/kttsd
#%attr(755,root,root) %{_bindir}/kttsmgr
%attr(755,root,root) %{_libdir}/kde4/kcm_kttsd.so
#%attr(755,root,root) %{_libdir}/kde4/libkttsd_stringreplacerplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkttsd_talkerchooserplugin.so
#%attr(755,root,root) %{_libdir}/kde4/libkttsd_xmltransformerplugin.so
%attr(755,root,root) %ghost %{_libdir}/libkttsd.so.?
%attr(755,root,root) %{_libdir}/libkttsd.so.*.*.*
#%{_desktopdir}/kde4/kttsmgr.desktop
%{_datadir}/apps/kttsd
%{_datadir}/kde4/services/kcmkttsd.desktop
%{_datadir}/kde4/services/ktts*.desktop
#%{_datadir}/kde4/servicetypes/ktts*.desktop
%{_iconsdir}/*/*/*/female.*
%{_iconsdir}/*/*/*/male.*
%{_iconsdir}/*/*/*/*speak.png

%if %{with gstreamer}
%files kttsd-gstreamer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/libkttsd_gstplugin.so
%endif

%files jovie
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jovie
%attr(755,root,root) %{_libdir}/kde4/jovie_stringreplacerplugin.so
%attr(755,root,root) %{_libdir}/kde4/jovie_talkerchooserplugin.so
%attr(755,root,root) %{_libdir}/kde4/jovie_xmltransformerplugin.so
%{_datadir}/apps/jovie
%{_datadir}/kde4/services/jovie.desktop
%{_datadir}/kde4/services/jovie_stringreplacerplugin.desktop
%{_datadir}/kde4/services/jovie_talkerchooserplugin.desktop
%{_datadir}/kde4/services/jovie_xmltransformerplugin.desktop
%{_datadir}/kde4/servicetypes/jovie_filterplugin.desktop
%{_kdedocdir}/en/jovie
