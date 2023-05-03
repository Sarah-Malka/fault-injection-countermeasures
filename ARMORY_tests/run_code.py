#!/usr/bin/python3

import os
import sys
import shutil

folder_name = sys.argv[1]
opt = sys.argv[2]

# def run_game(opt, folder_name):
# build ARMORY
if not os.path.exists("build/"):
    if os.system("meson -Db_lto=true --buildtype=release build") != 0: sys.exit(1)
if os.system("meson compile -C build/") != 0: sys.exit(1)

# dir for tmp data
os.makedirs(f"{folder_name}/tmp_data/", exist_ok=True)

# build the ARM binary
if os.system(f"arm-none-eabi-gcc -Wall -Wpedantic -std=c11 -ffreestanding -nostdlib -mthumb -march=armv7-m -O{opt} -Wl,-T{folder_name}/linker.ld -Wl,-Map,{folder_name}/tmp_data/binary.map {folder_name}/{folder_name}.c -o {folder_name}/tmp_data/binary.elf") != 0: sys.exit(1)

# create disassembly for looking up armory results later
if os.system(f"arm-none-eabi-objdump {folder_name}/tmp_data/binary.elf -d > disassembled.txt") != 0: sys.exit(1)

# start fault simulation
if os.system(f"cd {folder_name} && python3 start_emulation.py") != 0: sys.exit(1)

# cleanup tmp data
shutil.rmtree(f"{folder_name}/tmp_data/")
