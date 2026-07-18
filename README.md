# Homomorphic-CatPrivacy

Privacy-preserving image classification under **Fully Homomorphic Encryption
(FHE)**. A CNN decides *cat / not-cat* on a 32×32 image while the inference
server computes **only on ciphertext** — it never sees your image, the
plaintext result, or any secret key.

> Created for the Hackathon associated with the IETF (ciphertext-based AI inference).

This repository ships two standalone Windows tools. Download them, run them,
done. No Python, no build step, no source required.

![Live demo — real FHE classification in the web UI](docs/fhe-cat-demo.gif)

*Real run, sped up: encrypt locally → upload ciphertext → encrypted CNN
inference on the server → decrypt locally → "That's a cat. 79.9%".*

Dual-domain architecture (Figure 1 of the IETF draft). The two tools map onto
it directly: **`fhe-crypto-tool`** is the trusted Local Domain (MCP Client +
Local Crypto MCP Server), **`fhe-infer-tool`** is the untrusted Remote Domain
(Remote Inference MCP Server).

```
      (0) Key provisioning (init) -> obtain 'Key Reference'
+-------------------------------------------------------------+
|                 Local Domain (Trusted Zone)                 |   == fhe-crypto-tool
|                                                             |
|  +------------+ (1) tools/call: fhe_encrypt +------------+  |
|  |            |============================>| Local      |  |
|  |            | (2) Response: ciphertext    | Crypto     |  |
|  |            |<============================| MCP Server |  |
|  | MCP Client |                             | [Secret &  |  |
|  | (Agent)    | (5) tools/call: fhe_decrypt | Eval Key]  |  |
|  |            |============================>|            |  |
|  |            | (6) Response: plaintext     |            |  |
|  +------------+<============================+------------+  |
|      ^      |                                               |
+------|------|-----------------------------------------------+
       |      |
       |      | (3) tools/call: remote_inference {client_id, session_id, auth_token}
       |      |     (preceded by N x upload_ciphertext_chunk, by session_id)
+------|------|-----------------------------------------------+
|      |      |          Remote Domain (Untrusted)            |   == fhe-infer-tool
|  +---|------V--------------------------------------------+  |
|  |  (4) Response:         Remote Inference MCP Server    |  |
|  |      encrypted     [Homomorphic Model, Eval Key Cache]|  |
|  |      result                                           |  |
|  +-------------------------------------------------------+  |
+-------------------------------------------------------------+
```

## Download

Grab the packages from the [**Releases**](../../releases) page:

| Package | What it does | Run on |
|---------|--------------|--------|
| `fhe-crypto-tool-win64.zip` | key generation, encryption, decryption — everything sensitive, all local | Windows x64 |
| `fhe-infer-tool-win64.zip`  | ciphertext CNN inference | Windows x64 (localhost) **or** a real server |
| `fhe-crypto-tool-linux-x64.tar.gz` | same crypto client + web UI | Linux x64 (glibc 2.36+) |
| `fhe-infer-tool-linux-x64.tar.gz`  | same inference server | Linux x64 (glibc 2.36+) |

Unzip each into its own folder. On Windows, double-clicking works: the infer
tool starts the inference server on `127.0.0.1:8080`, the crypto tool prints
its usage.

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

## Web UI (chat front-end)

The same pipeline with a browser chat interface — this is what the demo GIF
above shows:

```powershell
cd fhe-crypto-tool
.\fhe-crypto-tool.exe webui --url http://127.0.0.1:8080/mcp
```

Open `http://127.0.0.1:5000`, drop an image, ask *"is this a cat?"*.

Two chat modes (toggle with the MODE button in the header):

* **Templated** — default, fully offline, no API key needed.
* **LLM** — bring your own key for the conversational layer.

Either way, the FHE pipeline is identical — the LLM only powers the chat
wording and never sees your keys or the server's ciphertext.

### Bring your own LLM — configure `.env` (optional)

**You choose the API endpoint and the model — nothing is prescribed.** The
download contains **no API keys**; your configuration lives in a `.env` file
that stays on your machine.

Each tool folder ships a `.env.example`. Copy it to `.env` (same folder as
the executable), open it in any text editor, and fill in your values:

```ini
# ANY OpenAI-compatible endpoint (OpenAI, DeepSeek, Groq, OpenRouter,
# self-hosted vLLM / Ollama, ...) + ANY model id it serves:
FHE_LLM_BASE_URL=https://api.deepseek.com
FHE_LLM_API_KEY=sk-your-key-here
FHE_LLM_MODEL=deepseek-chat
```

or, for Anthropic's native API:

```ini
ANTHROPIC_API_KEY=sk-ant-your-key-here
FHE_LLM_MODEL=claude-sonnet-4-5
```

Restart the tool, click MODE in the web UI header, done. `FHE_LLM_MODEL` is
always used **verbatim** — the model choice is entirely yours. Shortcut
variables `OPENAI_API_KEY` / `DEEPSEEK_API_KEY` also work (base URL inferred).

Notes:

* Without a `.env`, the UI runs in the offline **Templated** mode — no key
  needed; if you try to switch to LLM it tells you exactly what to configure.
* Ordinary environment variables (`export` / `setx`) work too and take
  precedence over `.env`.
* Never commit or share your `.env`.

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

* Windows x64 and Linux x64 native builds. Non-UTF-8 consoles are handled
  automatically.
* The inference server accepts any Host header when bound to a network
  interface (`0.0.0.0`); set `FHE_ALLOWED_HOSTS=your.host:8080` to re-enable
  strict Host filtering. Localhost binds keep DNS-rebinding protection on.
* Keys and per-run data live in `runtime_mcp\` next to each executable; delete
  that folder to reset.
* The binaries bundle OpenFHE (BSD-2-Clause) and the MinGW/GCC runtime
  (GPL + Runtime Library Exception) — see `THIRD-PARTY-LICENSES.txt` inside
  each zip.

## Slides

Hackathon slide deck: **slides/slides-126-hackathon-cat-privacy.pptx**

## License

The distributed binaries are provided free of charge for evaluation and
research. See `LICENSE` and the bundled third-party notices.
