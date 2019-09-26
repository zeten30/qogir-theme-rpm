Name:           qogir-theme
Version:        2019.09
Release:        1%{?dist}
Summary:        Qogir is a flat Design theme for GTK

License:        GPLv2
URL:            https://github.com/vinceliuice/Qogir-theme.git
Source0:        qogir-theme.tar.gz

BuildArch:      noarch
BuildRequires:  bash
BuildRequires:  bc
Requires:       %{_bindir}/glib-compile-resources
Requires:       %{_datadir}/gtk-engines/murrine.xml
Requires:       gnome-themes-extra

%description
Qogir is a flat Design theme for GTK 3, GTK 2 and Gnome-Shell which supports GTK 3 and GTK 2 based desktop environments like Gnome, Unity, Budgie, Cinnamon Pantheon, XFCE, Mate, etc.


%prep
%setup -q -n qogir-theme


%build
# Nothing to build
%install
%{__install} -d -m755 %{buildroot}%{_datadir}/themes/
for file in Qogir  Qogir-dark  Qogir-light  Qogir-win  Qogir-win-dark  Qogir-win-light ; do
  %{__cp} -pr ${file} %{buildroot}%{_datadir}/themes
done


%files
%defattr(-,root,root)
%{_datadir}/themes/Qogir
%{_datadir}/themes/Qogir-dark
%{_datadir}/themes/Qogir-light
%{_datadir}/themes/Qogir-win
%{_datadir}/themes/Qogir-win-dark
%{_datadir}/themes/Qogir-win-light


%changelog
* Thu Sep 26 2019 Milan Zink <zeten30@gmail.com> - 2019.09.1
- initial release
