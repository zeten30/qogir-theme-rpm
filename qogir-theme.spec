Name:           qogir-theme
Version:        2022.01
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
for file in Qogir Qogir-dark Qogir-light Qogir-manjaro Qogir-manjaro-dark Qogir-manjaro-light Qogir-ubuntu Qogir-ubuntu-dark Qogir-ubuntu-light; do
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
%{_datadir}/themes/Qogir-ubuntu
%{_datadir}/themes/Qogir-ubuntu-dark
%{_datadir}/themes/Qogir-ubuntu-light


%changelog
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
