# MCU name
MCU = atmega32u4

# Bootloader selection
BOOTLOADER = atmel-dfu

# Build Options
#   change yes to no to disable
#
BOOTMAGIC_ENABLE = yes      # Enable Bootmagic Lite
MOUSEKEY_ENABLE = no        # Mouse keys
EXTRAKEY_ENABLE = yes       # Audio control and System control
CONSOLE_ENABLE = no         # Console for debug
COMMAND_ENABLE = no         # Commands for debug and configuration
BACKLIGHT_ENABLE = no       # Enable keyboard backlight functionality
RGBLIGHT_ENABLE = no        # Enable keyboard RGB underglow
WS2812_DRIVER = i2c


# escd
# https://docs.qmk.fm/#/feature_split_keyboard?id=firmware-configuration
SPLIT_KEYBOARD = yes

# https://docs.qmk.fm/#/squeezing_avr?id=rulesmk-settings
LTO_ENABLE = yes
