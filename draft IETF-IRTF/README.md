# IETF / IRTF Drafts

This directory collects **both** individual Internet-Drafts associated with the
Homomorphic-CatPrivacy project, including their published XML, HTML, and text.
Both documents are contributions for discussion in PEARG; neither is an adopted
research-group document.

## Published drafts

| Document | Version | Published files | GitHub release |
| --- | --- | --- | --- |
| Fully Homomorphic Encryption Use Cases and Gap Analysis for Network Services | -00 | [XML](draft-li-pearg-fhe-use-cases-00.xml) · [HTML](draft-li-pearg-fhe-use-cases-00.html) · [Text](draft-li-pearg-fhe-use-cases-00.txt) | [Use-case release](https://github.com/lihjacky/Homomorphic-CatPrivacy/releases/tag/draft-li-pearg-fhe-use-cases-00) |
| Ciphertext-Based AI Inference Tool Design for the Model Context Protocol (MCP) | -00 | [XML](draft-li-pearg-ciphertext-inference-tool-mcp-00.xml) · [HTML](draft-li-pearg-ciphertext-inference-tool-mcp-00.html) · [Text](draft-li-pearg-ciphertext-inference-tool-mcp-00.txt) | [Earlier MCP release](https://github.com/lihjacky/Homomorphic-CatPrivacy/releases/tag/draft-li-pearg-ciphertext-inference-tool-mcp-00) |

The use-case draft broadens the application and gap analysis beyond the earlier
MCP ciphertext-inference contribution. The two are separate documents, each
with its own `-00` version; the new document does not replace the MCP draft.

- [Use-case draft on Datatracker](https://datatracker.ietf.org/doc/draft-li-pearg-fhe-use-cases/)
- [MCP draft on Datatracker](https://datatracker.ietf.org/doc/draft-li-pearg-ciphertext-inference-tool-mcp/)

All six published files in this directory were downloaded from the IETF archive
and verified on 16 October 2026. [published-drafts.json](published-drafts.json)
records their source URLs and SHA-256 hashes. The use-case XML is also
byte-identical to the authors' final `[1.3]` attachment, as recorded in
[source-verification.json](source-verification.json).

## Editor sources and builds

The versioned files above are fixed publication snapshots. To retain the
repository's existing [IETF draft build conventions](https://github.com/martinthomson/i-d-template/blob/main/doc/REPO.md),
the two unversioned editor sources remain at the repository root:

- [Use-case editor source](../draft-li-pearg-fhe-use-cases.xml)
- [MCP editor source](../draft-li-pearg-ciphertext-inference-tool-mcp.xml)

Make substantive revisions in the appropriate editor source, keeping the
published snapshots unchanged. From the repository root:

```sh
make
```

The [editor-copy workflow](https://github.com/lihjacky/Homomorphic-CatPrivacy/actions/workflows/ghpages.yml)
builds both sources, validates this directory, and provides HTML/TXT build
artifacts. Version tags use the form `draft-<name>-NN`. The current release
packages the verified IETF publication snapshots. The repository's existing
automation and permissions are retained; this repository update does not
resubmit either draft to the IETF Datatracker.

## Contribute additional use cases

Contributions from other companies and the wider community are welcome.

- [Use-case template: Markdown](templates/use-case-template.md)
- [Use-case template: RFCXML section](templates/use-case-template.xml)
- [Contribution instructions](CONTRIBUTING.md)
- [GitHub issues](https://github.com/lihjacky/Homomorphic-CatPrivacy/issues)
- [PEARG mailing list](https://mailman3.irtf.org/mailman3/lists/pearg.irtf.org/)

The existing [IETF contribution terms](../CONTRIBUTING.md) and
[license notice](../LICENSE.md) apply.
