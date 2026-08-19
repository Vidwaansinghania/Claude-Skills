# Chief risk officer

A Claude skill that reviews an investment thesis with the goal of breaking it. Its mandate is preventing permanent capital loss, not improving returns, so it is adversarial by design and never argues the bull side.

It starts from the assumption that the thesis is wrong and works to prove it: restating the assumptions being made, listing the ways they fail, modelling worst realistic outcomes, and hunting for risks that are non-linear, second-order or regime-dependent rather than the ones already in the disclosure. It closes with a drawdown estimate and one of four ratings, up to Unacceptable Risk.

## Install

```bash
git clone https://github.com/Vidwaansinghania/Claude-Skills.git
cp -r Claude-Skills/skills/chief-risk-officer ~/.claude/skills/
```

Claude Code picks it up on the next session. For Claude Desktop, add the folder through the skills interface.

## Using it

Feed it a thesis, ideally one written by the equity analyst skill:

```
Stress test this thesis. Where does it break?
```

Paste the write-up alongside the instruction. The skill is most useful on ideas you already like, since that is where the hidden risk sits.

## What it returns

Thesis summary and the assumptions underneath it, three primary failure scenarios, a worst case with revenue, earnings, valuation and drawdown impact, hidden risks, portfolio-level correlation and concentration exposure, liquidity risk, a verdict on whether the setup is asymmetric or fragile, a risk rating, and an action recommendation from approve through reject.

## Part of a set

Four skills that split an investment committee across separate roles, so each argument gets made properly instead of one voice hedging against itself:

- [buy-side-equity-analyst](../buy-side-equity-analyst) — builds the case
- [chief-risk-officer](../chief-risk-officer) — attacks it
- [macro-analyst](../macro-analyst) — sets the regime
- [portfolio-manager](../portfolio-manager) — sizes the position

Run this after the analyst and before the portfolio manager.

## Licence

MIT. See [LICENSE](../../LICENSE).

## Disclaimer

This is a prompt, not an investment adviser. Output is generated text and can be wrong, stale or confidently mistaken about facts. Nothing it produces is investment advice. Verify every number against primary sources before acting on any of it.
