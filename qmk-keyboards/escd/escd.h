// Copyright 2021 shukie (@shukie)
// SPDX-License-Identifier: GPL-2.0-or-later

#pragma once

#include "quantum.h"

/* This is a shortcut to help you visually see your layout.
 *
 * The first section contains all of the arguments representing the physical
 * layout of the board and position of the keys.
 *
 * The second converts the arguments into a two-dimensional array which
 * represents the switch matrix.
 */
#define LAYOUT_escd( \
  L00,                                                          R00, \
  L10, L11, L12, L13, L14, L15,        R10, R11, R12, R13, R14, R15, \
  L20, L21, L22, L23, L24, L25,        R20, R21, R22, R23, R24, R25, \
  L30, L31, L32, L33, L34, L35,        R30, R31, R32, R33, R34, R35, \
              L42, L43, L44, L45,    R40, R41, R42, R43 \
  ) \
  { \
    {   L00, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO }, \
    {   L10,   L11,   L12,   L13,   L14,   L15 }, \
    {   L20,   L21,   L22,   L23,   L24,   L25 }, \
    {   L30,   L31,   L32,   L33,   L34,   L35 }, \
    { KC_NO, KC_NO,   L42,   L43,   L44,   L45 }, \
 \
    {   R00, KC_NO, KC_NO, KC_NO, KC_NO, KC_NO }, \
    {   R15,   R14,   R13,   R12,   R11,   R10 }, \
    {   R25,   R24,   R23,   R22,   R21,   R20 }, \
    {   R35,   R34,   R33,   R32,   R31,   R30 }, \
    { KC_NO, KC_NO,   R43,   R42,   R41,   R40 } \
  }


enum layer_escd {
    _BASE_LAYER = 0,
    _LOWER_LAYER,
    _RAISE_LAYER,
    _ADJUST_LAYER
};
