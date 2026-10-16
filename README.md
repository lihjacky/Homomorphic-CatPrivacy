<!-- regenerate: off (this README indexes both drafts and the demo) -->

# Homomorphic-CatPrivacy

This repository collects two individual Internet-Drafts discussed in PEARG,
together with the ciphertext-inference demonstration and contribution materials.
The [`draft IETF-IRTF/` directory](draft%20IETF-IRTF/) is the common entry point
for **both** published drafts.

## IETF / IRTF drafts

| Document | Published version | Files | Release |
| --- | --- | --- | --- |
| Fully Homomorphic Encryption Use Cases and Gap Analysis for Network Services | [draft-li-pearg-fhe-use-cases-00](https://datatracker.ietf.org/doc/draft-li-pearg-fhe-use-cases/) | [XML](draft%20IETF-IRTF/draft-li-pearg-fhe-use-cases-00.xml) · [HTML](https://www.ietf.org/archive/id/draft-li-pearg-fhe-use-cases-00.html) · [Text](https://www.ietf.org/archive/id/draft-li-pearg-fhe-use-cases-00.txt) | [Use-case release](https://github.com/lihjacky/Homomorphic-CatPrivacy/releases/tag/draft-li-pearg-fhe-use-cases-00) |
| Ciphertext-Based AI Inference Tool Design for the Model Context Protocol (MCP) | [draft-li-pearg-ciphertext-inference-tool-mcp-00](https://datatracker.ietf.org/doc/draft-li-pearg-ciphertext-inference-tool-mcp/) | [XML](draft%20IETF-IRTF/draft-li-pearg-ciphertext-inference-tool-mcp-00.xml) · [HTML](https://www.ietf.org/archive/id/draft-li-pearg-ciphertext-inference-tool-mcp-00.html) · [Text](https://www.ietf.org/archive/id/draft-li-pearg-ciphertext-inference-tool-mcp-00.txt) | [Earlier MCP release](https://github.com/lihjacky/Homomorphic-CatPrivacy/releases/tag/draft-li-pearg-ciphertext-inference-tool-mcp-00) |

The use-case draft was published on **15 October 2026**. It extends the
application and gap analysis beyond the earlier MCP contribution; the two
documents retain separate names and version histories. Both are individual
contributions, and neither publication implies PEARG adoption or consensus.

The common draft directory contains all six published XML/HTML/TXT files,
verified against the IETF archive. See its [overview](draft%20IETF-IRTF/README.md)
and [file-hash index](draft%20IETF-IRTF/published-drafts.json).

## Releases and downloads

- [Latest release](https://github.com/lihjacky/Homomorphic-CatPrivacy/releases/latest):
  FHE use-case draft, published XML/HTML/TXT, and contribution templates.
- The latest release also includes a compact ZIP bundle containing both drafts
  and their supporting materials.
- [All releases](https://github.com/lihjacky/Homomorphic-CatPrivacy/releases):
  the earlier MCP release remains available with its original attachments.

## Contribute use cases

Contributions from other companies and the wider community are welcome.

- [Use-case template: Markdown](draft%20IETF-IRTF/templates/use-case-template.md)
- [Use-case template: RFCXML section](draft%20IETF-IRTF/templates/use-case-template.xml)
- [Contribution instructions](draft%20IETF-IRTF/CONTRIBUTING.md)
- [Open an issue](https://github.com/lihjacky/Homomorphic-CatPrivacy/issues)
- Discuss on the PEARG mailing list: `pearg@irtf.org`.

## Editor sources and builds

The root-level unversioned sources retain compatibility with the existing
IETF draft repository tooling:

- [FHE use-case editor source](draft-li-pearg-fhe-use-cases.xml)
- [MCP editor source](draft-li-pearg-ciphertext-inference-tool-mcp.xml)

Build both editor copies from the repository root:

```sh
make
```

The [editor-copy workflow](https://github.com/lihjacky/Homomorphic-CatPrivacy/actions/workflows/ghpages.yml)
validates both publication snapshots and builds HTML/TXT editor copies,
available in its `drafts` artifacts. The current release packages the verified
IETF publication snapshots. Existing automation and permissions are retained;
this repository update does not submit new versions to the IETF Datatracker.

## Demo

The [`demo/`](demo/) directory holds the reference implementation of the
ciphertext-inference workflow described in this draft — privacy-preserving
cat / not-cat image classification under CKKS FHE, with the remote server
computing on ciphertext only:

* [`demo/README.md`](demo/README.md) — full usage guide (quick start, web UI,
  bring-your-own-LLM `.env` configuration, server deployment).
* [`fhe-crypto-tool-win64.zip`](demo/fhe-crypto-tool-win64.zip) /
  [`fhe-crypto-tool-linux-x64.tar.gz`](demo/fhe-crypto-tool-linux-x64.tar.gz) —
  standalone Local-Domain client (keygen, encrypt, decrypt, chat web UI).
* [`fhe-infer-tool-win64.zip`](demo/fhe-infer-tool-win64.zip) /
  [`fhe-infer-tool-linux-x64.tar.gz`](demo/fhe-infer-tool-linux-x64.tar.gz) —
  standalone Remote-Domain ciphertext-inference MCP server.
* [`slides-126-hackathon-cat-privacy.pptx`](demo/slides-126-hackathon-cat-privacy.pptx) —
  IETF 126 Hackathon slide.
* [`fhe-cat-demo.gif`](demo/fhe-cat-demo.gif) — one real end-to-end run,
  sped up.

These are illustrative artifacts and are not part of the Internet-Draft itself.

## Contribution terms

The [IETF contribution terms](CONTRIBUTING.md) and [license notice](LICENSE.md)
apply. For local build dependencies, see the
[i-d-template setup guide](https://github.com/martinthomson/i-d-template/blob/main/doc/SETUP.md).
