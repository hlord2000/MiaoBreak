openocd -f "interface/stlink-dap.cfg" -f "angry_miao.cfg" -c "transport select dapdirect_swd; source [find target/nrf52.cfg]; init; flash_bootloader;"
