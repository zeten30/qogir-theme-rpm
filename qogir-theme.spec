Name:           qogir-theme
Version:        2020.12
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
for file in Qogir Qogir-dark Qogir-light Qogir-manjaro Qogir-manjaro-dark Qogir-manjaro-light Qogir-manjaro-win Qogir-manjaro-win-dark Qogir-manjaro-win-light Qogir-ubuntu Qogir-ubuntu-dark Qogir-ubuntu-light Qogir-ubuntu-win Qogir-ubuntu-win-dark Qogir-ubuntu-win-light Qogir-win Qogir-win-dark Qogir-win-light ; do
  %{__cp} -pr ${file} %{buildroot}%{_datadir}/themes
done


%files
%defattr(-,root,root)
%{_datadir}/themes/Qogir
%{_datadir}/themes/Qogir-dark
%{_datadir}/themes/Qogir-light
%{_datadir}/themes/Qogir-manjaro
%{_datadir}/themes/Qogir-manjaro-dark
%{_datadir}/themes/Qogir-manjaro-light
%{_datadir}/themes/Qogir-manjaro-win
%{_datadir}/themes/Qogir-manjaro-win-dark
%{_datadir}/themes/Qogir-manjaro-win-light
%{_datadir}/themes/Qogir-ubuntu
%{_datadir}/themes/Qogir-ubuntu-dark
%{_datadir}/themes/Qogir-ubuntu-light
%{_datadir}/themes/Qogir-ubuntu-win
%{_datadir}/themes/Qogir-ubuntu-win-dark
%{_datadir}/themes/Qogir-ubuntu-win-light
%{_datadir}/themes/Qogir-win
%{_datadir}/themes/Qogir-win-dark
%{_datadir}/themes/Qogir-win-light


%changelog
* Fri Oct 18 2019 Milan Zink <zeten30@gmail.com> - 2019.10.3
- include latest patches from upstream

* Tue Oct 15 2019 Milan Zink <zeten30@gmail.com> - 2019.10.2
- latest fixes for gnome-shell

* Mon Sep 30 2019 Milan Zink <zeten30@gmail.com> - 2019.09.2
- gnome-shell-theme.gresource added
- new color variants

* Thu Sep 26 2019 Milan Zink <zeten30@gmail.com> - 2019.09.1
- initial release
