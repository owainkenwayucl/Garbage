#!/bin/bash

qemu-system-ppc \
	-L pc-bios \
	-boot c \
	-M mac99,via=pmu \
	-cpu g3 \
	-m 640 \
	-g 1920x1080x32 \
	-prom-env 'auto-boot?=true' \
	-prom-env 'boot-args=-v' \
	-prom-env 'vga-ndrv?=true' \
	-drive file=/home/owain/Disks/Macintosh.img,format=raw,media=disk \
	-display sdl \
	-full-screen \
	-nic none


