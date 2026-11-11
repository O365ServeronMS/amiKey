"""Writes amiKey-update-<arch>.txt, the manifest the Windows updater reads from the newest GitHub release.

usage: AMIKEY_UPDATE_KEY=<base64 Ed25519 seed> python sign_update.py <version> <arch> <installer> <download url> <out>

The signature is Ed25519 over b"amiKey <version> <arch>\n" + the installer's bytes (Windows/App/Updater.cpp verify()).
"""
import base64
import os
import sys

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

version, arch, installer, url, out = sys.argv[1:6]
key = Ed25519PrivateKey.from_private_bytes(base64.b64decode(os.environ["AMIKEY_UPDATE_KEY"].strip()))
data = open(installer, "rb").read()
sig = key.sign(f"amiKey {version} {arch}\n".encode() + data)
with open(out, "w", newline="\n") as f:
    f.write(f"version={version}\nurl={url}\nlength={len(data)}\nsignature={base64.b64encode(sig).decode()}\n")
print(f"{out}: {version} {arch} {len(data)} bytes")
