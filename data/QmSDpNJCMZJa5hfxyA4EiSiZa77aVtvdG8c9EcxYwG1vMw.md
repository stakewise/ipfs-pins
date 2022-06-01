# StakeWise Proposal Acceptance Criteria
In order for StakeWise's SnapSafe module to execute a transaction, any corresponding proposal must have passed, as reported by Reality.eth.

The reality.eth question should conform to this template (the required template ID is defined by the installed Snapsafe Module):
```json
{"lang":"en",
"type":"bool",
"category":"DAO proposal",
"title":"Did the Snapshot proposal with the id %s in the stakewise.eth space pass the execution of the array of Module transactions that have the hash 0x%s and does it meet the requirements of the document referenced in the daorequirements record at stakewise.eth? The hash is the keccak of the concatenation of the individual EIP-712 hashes of the Module transactions. If this question was asked before the corresponding Snapshot proposal was resolved, it should ALWAYS be resolved to INVALID!"
}
```

Reality.eth should resolve the question to **“yes”** only for proposals that:
* the number of votes **FOR** is greater than the number of votes against **AGAINST**.
* were initiated as a Snapshot proposal in the `stakewise.eth` Snapshot space.
* had no significant service outages or availability issues that could have reasonably restricted SWISE holders from casting their votes in the proposal.
* the module transaction hash in the Reality.eth question is the keccak hash of the concatenation of the individual EIP-712 hashes of the module transactions defined in the Snapshot proposal.
* the plain description of the transactions, and their intended result, in the proposal is complete and accurate.
* did not occur during, in, or as a result of any unauthorized or malicious changes to the stakewise.eth Snapshot space.
* were not filtered from the default view in the stakewise.eth Snapshot space during the voting period.

Reality.eth should resolve the question to **“invalid”** if:
* the Reality.eth question meets the above requirements but was created prior to the end of the proposal vote period and/or the snapshot block for the vote. i.e. the final results of the vote are not yet known.

In all other cases, the Reality.eth question should be resolved to **“no”**.