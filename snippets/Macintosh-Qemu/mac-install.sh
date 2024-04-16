#!/bin/bash

qemu-system-ppc \
	-L pc-bios \
	-boot d \
	-M mac99,via=pmu \
	-m 640 \
	-g 1920x1080x32 \
	-prom-env 'auto-boot?=true' \
	-prom-env 'boot-args=-v' \
	-prom-env 'vga-ndrv?=true' \
	-drive file=/home/owain/Disks/Macintosh.img,format=raw,media=disk \
	-drive file=/home/owain/Disks/macos922_ibookg3.iso,format=raw,media=cdrom \
	-display sdl \
	-full-screen \
	-nic none


