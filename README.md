# Rewaita

[![OBS Build Status](https://build.opensuse.org/projects/home:ericfrs/packages/rewaita/badge.svg?type=default)](https://build.opensuse.org/package/show/home:ericfrs/rewaita)

This repository contains the Open Build Service (OBS) packaging files for [Rewaita](https://github.com/SwordPuffin/Rewaita).

Rewaita is a tool for recoloring GTK4/LibAdwaita apps to popular color schemes.

## Builds

Packages are built for **openSUSE** and available at the Open Build Service:
https://build.opensuse.org/package/show/home:ericfrs/rewaita


## Repository Contents

- **rewaita.spec**: The RPM spec file for building the package.
- **_service**: OBS service file for downloading sources.
- **fix-autostart.patch**: A patch applied during the build to fix autostart behavior and desktop entry paths.

## Build Information

This package is built as a `noarch` package and requires the following build dependencies:
- `meson`
- `python3-base`
- `gtk4-tools`
- `appstream-glib`
- `desktop-file-utils`

## Upstream

The upstream project can be found at: https://github.com/SwordPuffin/Rewaita
