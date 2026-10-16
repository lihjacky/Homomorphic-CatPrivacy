# FHE Use Cases and Gap Analysis for Network Services

Working materials for the individual Internet-Draft
**Fully Homomorphic Encryption Use Cases and Gap Analysis for Network Services**,
prepared for discussion in the Privacy Enhancements and Assessments Research Group (PEARG).

- [Datatracker](https://datatracker.ietf.org/doc/draft-li-pearg-fhe-use-cases/)
- [Published -00 HTML](https://www.ietf.org/archive/id/draft-li-pearg-fhe-use-cases-00.html)
- [Published -00 text](https://www.ietf.org/archive/id/draft-li-pearg-fhe-use-cases-00.txt)
- [Published -00 XML, preserved in this repository](draft-li-pearg-fhe-use-cases-00.xml)
- [Local HTML rendering](draft-li-pearg-fhe-use-cases-00.html)
- [Local text rendering](draft-li-pearg-fhe-use-cases-00.txt)
- [Editable source for the next revision](../draft-li-pearg-fhe-use-cases.xml)
- [Use-case template: Markdown](templates/use-case-template.md)
- [Use-case template: RFCXML section](templates/use-case-template.xml)
- [Contribution guidance](CONTRIBUTING.md)

The draft was published on **15 October 2026**. It is an individual contribution;
publication does not imply PEARG adoption or consensus.

## Source preservation

`draft-li-pearg-fhe-use-cases-00.xml` is the unchanged XML from the authors'
`[1.3]draft-li-pearg-fhe-use-cases-00.zip`. On 16 October 2026, it was verified
to be byte-identical to the XML published by the IETF:

```text
SHA-256: 12da0569ae4468f4acff7101006423659038978de7c79f886b8399f09222ac87
```

See [source-verification.json](source-verification.json). The original snapshot
keeps its original bytes, including line endings. Local HTML/TXT renderings
are generated with xml2rfc 3.34.1 and the publication date.

The root-level editor source follows this repository's existing
[i-d-template conventions](https://github.com/martinthomson/i-d-template/blob/main/doc/REPO.md):
its filename has no version suffix, its `docName` uses `-latest`, and a matching
`seriesInfo` is present. Only that metadata and whitespace differ from the
published snapshot; the draft's substantive content is preserved.

## Build and review

From the repository root, use the existing draft build:

```sh
make
```

The existing **Update Editor's Copy** workflow discovers the root-level source,
builds the editor's HTML/TXT, and archives the outputs. The existing release
workflow continues to operate on draft-version tags; adding these files does
not submit another version to the IETF.

To reproduce the publication snapshot separately:

```sh
python -m pip install -r "draft IETF-IRTF/requirements.txt"
python -m xml2rfc "draft IETF-IRTF/draft-li-pearg-fhe-use-cases-00.xml" --no-network --date 2026-10-15 --html --text
```

## Discussion and contributions

Contributions from other companies and the wider community are welcome. Use
the template to describe an additional use case or propose a supported gap
analysis, then open a [GitHub issue](https://github.com/lihjacky/Homomorphic-CatPrivacy/issues)
or pull request. Discussion can also take place on the
[PEARG mailing list](https://mailman3.irtf.org/mailman3/lists/pearg.irtf.org/).
Repository contributions are subject to the existing root-level
[IETF contribution terms](../CONTRIBUTING.md) and [license notice](../LICENSE.md).
