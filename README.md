# Homomorphic-CatPrivacy

Privacy-preserving image classification under **Fully Homomorphic Encryption
(FHE)**. A CNN decides *cat / not-cat* on a 32×32 image while the inference
server computes **only on ciphertext** — it never sees your image, the
plaintext result, or any secret key.

> Created for the Hackathon associated with the IETF (ciphertext-based AI inference).

This repository ships two standalone Windows tools. Download them, run them,
done. No Python, no build step, no source required.

```
  ┌─────────────────────────┐         ciphertext only          ┌────────────────────────┐
  │  fhe-crypto-tool  (you)  │  ───────────────────────────▶   │  fhe-infer-tool (server) │
  │  keygen · encrypt ·      │   encrypted image + eval keys    │  CNN inference over      │
  │  decrypt  (secret key    │                                  │  ciphertext (CKKS)       │
  │  never leaves this box)  │  ◀───────────────────────────    │  never sees plaintext    │
  └─────────────────────────┘        encrypted result           └────────────────────────┘
```

## Download

Grab the two zips from the [**Releases**](../../releases) page:

| Tool | What it does | Run on |
|------|--------------|--------|
| `fhe-crypto-tool-win64.zip` | key generation, encryption, decryption — everything sensitive, all local | your machine |
| `fhe-infer-tool-win64.zip`  | ciphertext CNN inference | your machine (localhost) **or** a real server |

Unzip each into its own folder.

## Quick start — one machine

**1. Start the inference server** (terminal 1):

```powershell
cd fhe-infer-tool
.\fhe-infer-tool.exe --transport streamable-http --host 127.0.0.1 --port 8080
```

**2. Classify an image** (terminal 2):

```powershell
cd fhe-crypto-tool
.\fhe-crypto-tool.exe classify --image C:\path\to\photo.jpg --url http://127.0.0.1:8080/mcp
```

The **first** run generates your CKKS key set and registers ~1.8 GB of public
evaluation keys with the server (one-time, a few minutes). After that each
image takes about 1–2 minutes.

Output:

```
cat   probability 0.80   (70 s)
```

## Deploy the inference server on a real machine

Run the same server binary on a Linux/Windows host and expose port 8080 behind
a TLS reverse proxy:

```
./fhe-infer-tool --transport streamable-http --host 0.0.0.0 --port 8080
```

Point the client at it:

```powershell
.\fhe-crypto-tool.exe classify --image photo.jpg --url https://your-server.example/mcp
```

The server still only ever receives ciphertext and public evaluation keys.

## Privacy properties

* The **secret key** is generated and stays inside `fhe-crypto-tool`'s folder
  (`runtime_mcp\`). It is never transmitted.
* Only **ciphertext** and **public evaluation keys** are sent to the inference
  server.
* The inference server produces an **encrypted** result; only your local tool
  can decrypt it.
* This mirrors the protocol described in the companion IETF draft on
  ciphertext-based AI inference.

## Notes

* Windows x64 build. Non-UTF-8 consoles are handled automatically.
* Keys and per-run data live in `runtime_mcp\` next to each executable; delete
  that folder to reset.
* The binaries bundle OpenFHE (BSD-2-Clause) and the MinGW/GCC runtime
  (GPL + Runtime Library Exception) — see `THIRD-PARTY-LICENSES.txt` inside
  each zip.

## License

The distributed binaries are provided free of charge for evaluation and
research. See `LICENSE` and the bundled third-party notices.
