# CSMuseum

### Troubleshooting
- Serial Connection Permission Denied
  - Run : sudo usermod -a -G dialout www-data
  - Reboot
- Serial Connection Closing After a Few Seconds
  - raspi-config -> Interfacing Options -> Serial
    - "Would you like a login shell to be accessible over serial?" (NO)
    - "Would you like the serial port hardware to be enabled?" (YES)
