"""Writes amiKey-update-<arch>.txt, the manifest the Windows updater reads from the newest GitHub release.

usage: AMIKEY_UPDATE_KEY=<base64 Ed25519 seed> python sign_update.py <version> <arch> <installer> <download url> <out>

The signature is Ed25519 over b"amiKey <version> <arch>\n" + the installer's bytes (Windows/App/Updater.cpp verify()).
"""
import base64
import os
import re
import sys

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey

version, arch, installer, url, out = sys.argv[1:6]
key = Ed25519PrivateKey.from_private_bytes(base64.b64decode(os.environ["AMIKEY_UPDATE_KEY"].strip()))
data = open(installer, "rb").read()
sig = key.sign(f"amiKey {version} {arch}\n".encode() + data)
with open(out, "w", newline="\n") as f:
    f.write(f"version={version}\nurl={url}\nlength={len(data)}\nsignature={base64.b64encode(sig).decode()}\n")

# Check the manifest the way the app will: with the public key compiled into Windows/App/Updater.cpp.
# A wrong AMIKEY_UPDATE_KEY secret fails here instead of in every installed copy.
updater = open(os.path.join(os.path.dirname(__file__), "../../Windows/App/Updater.cpp"), encoding="utf-8").read()
pub = Ed25519PublicKey.from_public_bytes(base64.b64decode(re.search(r'PUBKEY_B64 = "([^"]+)"', updater).group(1)))
fields = dict(line.split("=", 1) for line in open(out, encoding="utf-8").read().splitlines() if "=" in line)
assert fields["version"] == version and int(fields["length"]) == len(data) and fields["url"].endswith("/" + os.path.basename(installer))
pub.verify(base64.b64decode(fields["signature"]), f"amiKey {fields['version']} {arch}\n".encode() + data)
print(f"{out}: {version} {arch} {len(data)} bytes, verified with the app's public key")
