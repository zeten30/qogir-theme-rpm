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
./install.sh --dest "${WDIR}/sources/qogir-theme"

# Modify sources
cd ../../sources || exit 1

# Compile gresources
for themedir in qogir-theme/Qogir*/gnome-shell; do
  cd "${themedir}" || exit 1
  echo "Patching $(pwd)"
  sed -i 's/font-size: 9pt;/font-size: 10.5pt;/g' gnome-shell.css
  sed -i 's/font-family: Futura Bk bt, Cantarell, Sans-Serif;/font-family: Noto Sans, Cantarell, Sans-Serif;/g' gnome-shell.css
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