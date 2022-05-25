Name:           qogir-theme
Version:        2022.05
Release:        1%{?dist}
Summary:        Qogir is a flat Design theme for GTK

License:        GPLv2
URL:            https://github.com/vinceliuice/Qogir-theme.git
Source0:        qogir-theme.tar.gz

BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  bc
BuildRequires:  %{_bindir}/glib-compile-resources
Requires:       gtk-murrine-engine
Requires:       gtk2-engines

%description
Qogir is a flat Design theme for GTK 3, GTK 2 and Gnome-Shell which supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Cinnamon Pantheon, XFCE, Mate, etc.


%prep
%setup -q -n qogir-theme


%build
# Nothing to build
%install
%{__install} -d -m755 %{buildroot}%{_datadir}/themes/
THEME_DIRS="Qogir
Qogir-Dark
Qogir-Dark-hdpi
Qogir-Dark-xhdpi
Qogir-hdpi
Qogir-Light
Qogir-Light-hdpi
Qogir-Light-xhdpi
Qogir-Manjaro
Qogir-Manjaro-Dark
Qogir-Manjaro-Light
Qogir-Ubuntu
Qogir-Ubuntu-Dark
Qogir-Ubuntu-Light
Qogir-xhdpi"
for file in ${THEME_DIRS}
do
  %{__cp} -pr ${file} %{buildroot}%{_datadir}/themes
done


%files
%defattr(-,root,root)
%{_datadir}/themes/Qogir
%{_datadir}/themes/Qogir-Dark
%{_datadir}/themes/Qogir-Dark-hdpi
%{_datadir}/themes/Qogir-Dark-xhdpi
%{_datadir}/themes/Qogir-hdpi
%{_datadir}/themes/Qogir-Light
%{_datadir}/themes/Qogir-Light-hdpi
%{_datadir}/themes/Qogir-Light-xhdpi
%{_datadir}/themes/Qogir-Manjaro
%{_datadir}/themes/Qogir-Manjaro-Dark
%{_datadir}/themes/Qogir-Manjaro-Light
%{_datadir}/themes/Qogir-Ubuntu
%{_datadir}/themes/Qogir-Ubuntu-Dark
%{_datadir}/themes/Qogir-Ubuntu-Light
%{_datadir}/themes/Qogir-xhdpi


%changelog
* Wed May 25 2022 Milan Zink <zeten30@gmail.com> - 2022.05.1
- adapt upstream changes

* Tue Jan 04 2022 Milan Zink <zeten30@gmail.com> - 2022.01.1
- adapt upstream changes

* Wed Aug 18 2021 Milan Zink <zeten30@gmail.com> - 2021.08.1
- fedora logo in nautilus
- sync latest upstream version
- adapt to a new install.sh script

* Wed May 05 2021 Milan Zink <zeten30@gmail.com> - 2021.05.1
- include latest patches from upstream, remove local patches

* Fri Oct 18 2019 Milan Zink <zeten30@gmail.com> - 2019.10.3
- include latest patches from upstream

* Tue Oct 15 2019 Milan Zink <zeten30@gmail.com> - 2019.10.2
- latest fixes for gnome-shell

* Mon Sep 30 2019 Milan Zink <zeten30@gmail.com> - 2019.09.2
- gnome-shell-theme.gresource added
- new color variants

* Thu Sep 26 2019 Milan Zink <zeten30@gmail.com> - 2019.09.1
- initial release
