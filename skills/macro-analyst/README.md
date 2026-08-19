# Macro analyst

A Claude skill that classifies the current economic regime and translates it into portfolio positioning. It does not pick stocks.

The premise is that markets are regime-driven rather than narrative-driven, and that the same asset behaves differently depending on which regime you are in. So the skill sorts the environment into one of six states, from expansion through stagflation, reads the rate, inflation, growth, liquidity, credit and policy variables behind that call, and then works forward to sector leadership, growth versus value, small versus large cap, and what the portfolio is quietly exposed to. Scenarios get explicit probabilities rather than adjectives.

## Install

```bash
git clone https://github.com/Vidwaansinghania/Claude-Skills.git
cp -r Claude-Skills/skills/macro-analyst ~/.claude/skills/
```

Claude Code picks it up on the next session. For Claude Desktop, add the folder through the skills interface.

## Using it

```
What regime are we in, and what does it mean for a portfolio tilted toward consumer discretionary?
```

Give it current rate and inflation data. Claude's training cutoff means it will otherwise reason from stale numbers, which is the one failure mode this skill cannot catch on its own.

## What it returns

Current regime with a probability, key macro drivers broken out by variable, market implications across equities and sectors and factors, portfolio overweights and underweights with risks to current positioning, probabilities across soft landing, recession, re-acceleration and stagflation, and a final risk-on/neutral/risk-off verdict.

## Part of a set

Four skills that split an investment committee across separate roles, so each argument gets made properly instead of one voice hedging against itself:

- [buy-side-equity-analyst](../buy-side-equity-analyst) — builds the case
- [chief-risk-officer](../chief-risk-officer) — attacks it
- [macro-analyst](../macro-analyst) — sets the regime
- [portfolio-manager](../portfolio-manager) — sizes the position

This one runs independently of any single name. Use it to set context before the analyst starts, or to check what a portfolio is betting on without meaning to.

## Licence

MIT. See [LICENSE](../../LICENSE).

## Disclaimer

This is a prompt, not an investment adviser. Output is generated text and can be wrong, stale or confidently mistaken about facts. Nothing it produces is investment advice. Verify every number against primary sources before acting on any of it.
