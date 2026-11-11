#pragma once
#define IDI_APP 101
#define IDR_SOUND_VI 201
#define IDR_SOUND_EN 202
#define IDR_EMOJI_JSON 203
#ifndef AMIKEY_VERSION
#define AMIKEY_VERSION "0.1.0"
#endif
#ifndef AMIKEY_VERSION_NUM
#define AMIKEY_VERSION_NUM 0,1,0,0
#endif
#define AMIKEY_W2(x) L##x
#define AMIKEY_W(x) AMIKEY_W2(x)
#define AMIKEY_VERSION_W AMIKEY_W(AMIKEY_VERSION)
