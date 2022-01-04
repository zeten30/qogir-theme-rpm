#!/bin/bash

WDIR=$(pwd)

XML_HEADER='<?xml version="1.0" encoding="UTF-8"?>
<gresources>
<gresource prefix="/org/gnome/shell/theme">'
XML_FOOT='  </gresource>
</gresources>'

# Clean old sources
mkdir -p sources/
rm -rf sources/*
mkdir -p sources/qogir-theme

# Upstream sync
mkdir -p upstream
cd upstream || exit 1

if [ -d Qogir-theme ]; then
    rm -rf Qogir-theme
fi

git clone https://github.com/vinceliuice/Qogir-theme.git

# Install to sources
cd Qogir-theme || exit 1
# Default color + light & dark + win
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -c light
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -c dark
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora --tweaks square
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -c light --tweaks square
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -c dark --tweaks square
# Manjaro colors + light & dark
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -t manjaro
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -t manjaro -c light
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -t manjaro -c dark
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -t manjaro --tweaks square
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -t manjaro -c light --tweaks square
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -t manjaro -c dark --tweaks square
# Ubuntu color + light & dark
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -t ubuntu
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -t ubuntu -c light
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -t ubuntu -c dark
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -t ubuntu --tweaks square
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -t ubuntu -c light --tweaks square
./install.sh --dest "${WDIR}/sources/qogir-theme" --logo fedora -t ubuntu -c dark --tweaks square

# Modify sources
cd ../../sources || exit 1

# Compile gresources
for themedir in qogir-theme/Qogir*/gnome-shell; do
    cd "${themedir}" || exit 1
    echo "Patching $(pwd)"
    sed -i 's/font-size: 10pt;/font-size: 10.5pt;/g' gnome-shell.css
    
    # Patch gnome-shell background
    cp -rf "${WDIR}/assets-patch/background.jpeg" background.jpeg
    
    #   # Patch - https://gitlab.gnome.org/GNOME/gnome-shell/commit/a78527050ada988f30f00adaf8a9a395b381b8a1?merge_request_iid=110
    #   awk '/#searchResultsBin {/,/}/ { next } 1' gnome-shell.css > gnome-shell-patched.css
    #   sed -i 's/#searchResultsContent {/#searchResultsContent {\n  max-width: 1000px;/' gnome-shell-patched.css
    #   mv gnome-shell-patched.css gnome-shell.css
    
    # generate: gnome-shell-theme.gresource.xml
    echo -e "${XML_HEADER}" > gnome-shell-theme.gresource.xml
    find . -type f | sed -e 's/\.\//    <file>/' -e 's/$/<\/file>/' >> gnome-shell-theme.gresource.xml
    echo -e "${XML_FOOT}" >> gnome-shell-theme.gresource.xml
    # compile\
    glib-compile-resources gnome-shell-theme.gresource.xml
    cd ../../../ || exit 1
done

# Create source tarball
mkdir -p ../rpmbuild/
rm -rf ../rpmbuild/*.*
tar cfz qogir-theme.tar.gz qogir-theme
mv qogir-theme.tar.gz ../rpmbuild/

# Back to buildroot
cd ../ || exit 1
