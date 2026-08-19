# Portfolio manager

A Claude skill that decides whether an idea gets capital and how much. It does no research of its own; it takes the analyst's expected return, the risk officer's downside, and the macro regime, and turns them into a position size.

The framing is that capital is scarce and a good idea is not automatically a fundable one. Risk is assessed at the portfolio level rather than per stock, which means correlation with what you already own can sink an idea that looks fine standing alone. Sizing runs on a conviction band from under 1% for speculative through 10% plus for exceptional asymmetry, with a hard preference against exceeding 10% in any single name. Every decision has to answer what else the capital could have done.

## Install

```bash
git clone https://github.com/Vidwaansinghania/Claude-Skills.git
cp -r Claude-Skills/skills/portfolio-manager ~/.claude/skills/
```

Claude Code picks it up on the next session. For Claude Desktop, add the folder through the skills interface.

## Using it

Give it the analyst write-up, the risk review, and your current holdings:

```
Here's the thesis, the risk review, and my book. Size it.
```

The holdings matter. Without them the correlation and concentration checks have nothing to work against, which removes most of the reason to use this skill rather than a research one.

## What it returns

Decision and action, a recommended position size as a percentage, rationale, portfolio impact broken into risk, return and correlation, key portfolio risks, an opportunity cost note, a final verdict from add through exit, and a confidence score out of ten.

## Part of a set

Four skills that split an investment committee across separate roles, so each argument gets made properly instead of one voice hedging against itself:

- [buy-side-equity-analyst](../buy-side-equity-analyst) — builds the case
- [chief-risk-officer](../chief-risk-officer) — attacks it
- [macro-analyst](../macro-analyst) — sets the regime
- [portfolio-manager](../portfolio-manager) — sizes the position

This one runs last and needs the other outputs to work properly.

## Licence

MIT. See [LICENSE](../../LICENSE).

## Disclaimer

This is a prompt, not an investment adviser. Output is generated text and can be wrong, stale or confidently mistaken about facts. Nothing it produces is investment advice. Verify every number against primary sources before acting on any of it.
