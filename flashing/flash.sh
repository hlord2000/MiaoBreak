openocd -f "interface/stlink-dap.cfg" -f "angry_miao.cfg" -c "transport select dapdirect_swd; source [find target/nrf52.cfg]; init; sleep 2000; flash_bootloader;"
