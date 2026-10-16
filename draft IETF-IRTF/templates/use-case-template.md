# UCx: Use-case title

Use this template for a proposed contribution. Replace the guidance below
with your analysis. Editors assign the final UC number. This file is a
contribution aid, not a completed or adopted use case.

**Scenario:** Describe the useful service, actors, sensitive inputs and outputs,
and who is trusted to see plaintext or hold decryption keys. State the privacy
need and why remote computation or retrieval is useful.

**(1) Example Flows:**

1. The requester specifies the task, authorized inputs, and permitted output.
2. The trusted party prepares and encrypts the required data, retaining the
   decryption secret under the stated key arrangement.
3. The evaluator performs the agreed high-level operation on ciphertexts.
4. The encrypted result returns to the authorized trusted party for decryption.
5. The authorized recipient uses the permitted output.

Adapt these illustrative steps to the actual scenario. Identify plaintext
observations, metadata, and disclosures outside the encrypted computation.

**(2) Post-conditions:** State the intended functional outcome, protected
information, and any authorized disclosure. Map the privacy objectives to
G1/G2 where applicable; identify a proposed new gap separately if needed.

**(3) Existing Non-HE Solutions Covering the Use-Case Functionality:** Explain
the relevant existing approaches in one concise paragraph. State their trust
assumptions and the limitation that motivates encrypted computation; avoid
claiming that every alternative is insecure or that FHE is the only option.

**(4) Potential New Requirements Needed to Support the Use Case:**

- **UCx-R1 (G1, where applicable): Protected computation or selection.** State
  the useful operation and precisely what must stay confidential.
- **UCx-R2 (G2, where applicable): Controlled decryption and release.** State
  who holds the secret, who receives the result, and permitted disclosure.

Explain briefly how FHE could meet those objectives and which complementary
controls are required. Describe the relevant evaluation dimensions, such as
accuracy, latency, communication, key arrangements, and output granularity.
Support feasibility claims with primary references. Keep the analysis at use-case
level rather than introducing a detailed protocol.
