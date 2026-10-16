# Contributing FHE use cases

Contributions from other companies and the wider community are welcome.
The [repository contribution terms](../CONTRIBUTING.md) apply to all contributions.

1. Start with the [Markdown template](templates/use-case-template.md) or
   [RFCXML section template](templates/use-case-template.xml).
2. Describe the actors, useful service, sensitive information, and trust boundary.
3. Provide a high-level example flow and the intended post-conditions.
4. Explain how existing non-HE methods provide the functionality, their relevant
   limits under the stated assumptions, and the specific benefit of FHE.
5. Identify potential requirements and map them to G1/G2 where appropriate.
   Propose and explain a new gap when neither mapping fits. FHE does not
   automatically solve traffic analysis, source anonymity, authorization, or
   result correctness.
6. Cite primary sources and distinguish measured results from proposals.
   Outline relevant evaluation criteria without inventing performance numbers.

Open an issue with the completed template for discussion, or submit a pull
request against the root editor source, `draft-li-pearg-fhe-use-cases.xml`.
Insert an agreed use case under `uc-details`; update the gap summary, use-case
mapping, evaluation, and references as needed. Editors assign the final UC
number and requirement identifiers. Keep the literal **UCx** and **Gx** labels
for the existing further-study placeholders.

The published `draft IETF-IRTF/draft-li-pearg-fhe-use-cases-00.xml` and its
renderings are archival snapshots. Make substantive edits in the root-level
editor source rather than rewriting an already published version. Retain the
draft's scenario/four-part structure; detailed protocol specification is not
required for a use-case contribution.

Please discuss the proposal on GitHub or the PEARG list (`pearg@irtf.org`).
Opening an issue or pull request does not itself send an email to that list.
