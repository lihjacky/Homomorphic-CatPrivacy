<!-- regenerate: off (this README documents the demo/ directory) -->

# Ciphertext-Based AI Inference Tool Design for the Model Context Protocol (MCP)

This is the working area for the individual Internet-Draft, "Ciphertext-Based AI Inference Tool Design for the Model Context Protocol (MCP)".

* [Editor's Copies](https://agent-security-labs.github.io/Homomorphic-CatPrivacy/)
* [Datatracker Page](https://datatracker.ietf.org/doc/draft-li-pearg-ciphertext-inference-tool-mcp)
* [Individual Draft](https://datatracker.ietf.org/doc/html/draft-li-pearg-ciphertext-inference-tool-mcp)
* [Compare Editor's Copy to Individual Draft](https://agent-security-labs.github.io/Homomorphic-CatPrivacy/#go.draft-li-pearg-ciphertext-inference-tool-mcp.diff)


## FHE Use Cases and Gap Analysis

The individual draft **Fully Homomorphic Encryption Use Cases and Gap Analysis for Network Services**
was published on 15 October 2026 for discussion in PEARG.

* [Published draft on Datatracker](https://datatracker.ietf.org/doc/draft-li-pearg-fhe-use-cases/)
* [Published XML snapshot](draft%20IETF-IRTF/draft-li-pearg-fhe-use-cases-00.xml)
* [Editor source](draft-li-pearg-fhe-use-cases.xml)
* [Use-case contribution template](draft%20IETF-IRTF/templates/use-case-template.md)
* [RFCXML contribution template](draft%20IETF-IRTF/templates/use-case-template.xml)
* [Draft materials and contribution guide](draft%20IETF-IRTF/README.md)

Contributions from other companies and the wider community are welcome through
GitHub issues, pull requests, and the PEARG mailing list (pearg@irtf.org).
Publication does not imply research-group adoption or consensus.


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

## Contributing

See the
[guidelines for contributions](CONTRIBUTING.md).

The contributing file also has tips on how to make contributions, if you
don't already know how to do that.

## Command Line Usage

Formatted text and HTML versions of the draft can be built using `make`.

```sh
$ make
```

Command line usage requires that you have the necessary software installed.  See
[the instructions](https://github.com/martinthomson/i-d-template/blob/main/doc/SETUP.md).

