# Buy-side equity analyst

A Claude skill that runs fundamental equity research on a public company the way a buy-side analyst would, and ends with a capital allocation call rather than a description of the business.

It works through business model, moat, financial quality, management, valuation, risks and catalysts, then forces three things most write-ups skip: the strongest bear case, what the market already believes, and where that consensus might be wrong. Output is a fixed template ending in a probability-weighted view, a confidence score out of ten, and a position suitability call.

## Install

Copy the skill into your skills directory:

```bash
git clone https://github.com/Vidwaansinghania/Claude-Skills.git
cp -r Claude-Skills/skills/buy-side-equity-analyst ~/.claude/skills/
```

Claude Code picks it up on the next session. For Claude Desktop, add the folder through the skills interface.

## Using it

Name a company and ask for research:

```
Run a full buy-side workup on Costco.
```

The skill asks for evidence over narrative, so give it filings or financials if you have them rather than letting it work from memory.

## What it returns

Thesis in three to five bullets, moat rated weak/moderate/strong, financial and management assessment, valuation view, bear case, risks, catalysts by horizon, bull/base/bear scenarios, expected return and time horizon, confidence out of ten, and a final recommendation with position suitability.

## Part of a set

Four skills that split an investment committee across separate roles, so each argument gets made properly instead of one voice hedging against itself:

- [buy-side-equity-analyst](../buy-side-equity-analyst) — builds the case
- [chief-risk-officer](../chief-risk-officer) — attacks it
- [macro-analyst](../macro-analyst) — sets the regime
- [portfolio-manager](../portfolio-manager) — sizes the position

Run this one first, then hand its output to the risk officer.

## Licence

MIT. See [LICENSE](../../LICENSE).

## Disclaimer

This is a prompt, not an investment adviser. Output is generated text and can be wrong, stale or confidently mistaken about facts. Nothing it produces is investment advice. Verify every number against primary sources before acting on any of it.
