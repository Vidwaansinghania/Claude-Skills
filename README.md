# Claude skills

Skills I have written for Claude, kept in one repo so they can be installed together or picked apart.

Each one lives in its own folder under `skills/` with a `SKILL.md` holding the prompt and a `README.md` explaining what it does and how it behaves.

## Catalog

Every skill in this repo. The trigger column is the `description` field from each `SKILL.md` frontmatter, which is what Claude reads when deciding whether to load the skill.

| Skill | What it does | Trigger description | Status | Source of truth |
|---|---|---|---|---|
| [buy-side-equity-analyst](skills/buy-side-equity-analyst) | Builds the case: fundamental research on one company, ending in a probability-weighted view and a position suitability call | Institutional-quality equity research for public companies, including business quality, valuation, moat, risks, catalysts, and investment recommendations. | Live | This repo, `skills/buy-side-equity-analyst` |
| [chief-risk-officer](skills/chief-risk-officer) | Attacks the case: assumes the thesis is wrong, models failure scenarios and drawdown, rates the risk | Institutional portfolio risk manager focused on preventing permanent capital loss and challenging investment assumptions. | Live | This repo, `skills/chief-risk-officer` |
| [macro-analyst](skills/macro-analyst) | Sets the regime: classifies the macro environment and translates it into sector and factor positioning | Institutional macroeconomic analyst focused on economic regimes, interest rates, inflation, liquidity conditions, and market implications for portfolio positioning. | Live | This repo, `skills/macro-analyst` |
| [portfolio-manager](skills/portfolio-manager) | Sizes the position: turns the other three outputs and your holdings into a position size and verdict | Institutional portfolio manager responsible for capital allocation, position sizing, portfolio construction, and risk-adjusted returns. | Live | This repo, `skills/portfolio-manager` |

## The investment committee set

The four skills above split an investment committee across separate roles, so each argument gets made properly instead of one voice hedging against itself.

| Skill | Role | Runs |
|---|---|---|
| [buy-side-equity-analyst](skills/buy-side-equity-analyst) | Builds the case | First, or after the macro read |
| [chief-risk-officer](skills/chief-risk-officer) | Attacks it | After the analyst |
| [macro-analyst](skills/macro-analyst) | Sets the regime | Independently of any single name |
| [portfolio-manager](skills/portfolio-manager) | Sizes the position | Last, on the other three outputs |

The order matters. The analyst produces a thesis, the risk officer tries to break it, and the portfolio manager decides whether it gets capital and how much. The macro analyst sets context and does not pick stocks.

## Install

Clone the repo and copy the skills you want into your skills directory:

```bash
git clone https://github.com/Vidwaansinghania/Claude-Skills.git
cp -r Claude-Skills/skills/* ~/.claude/skills/
```

For a single skill, copy just that folder:

```bash
cp -r Claude-Skills/skills/macro-analyst ~/.claude/skills/
```

Claude Code picks them up on the next session. For Claude Desktop, add the folders through the skills interface.

## Related

The multi-agent equity research pipeline is a larger project and lives in its own repo: [Multi-Agent-Equity-Research](https://github.com/Vidwaansinghania/Multi-Agent-Equity-Research).

## Licence

MIT. See [LICENSE](LICENSE).

## Disclaimer

These are prompts, not an investment adviser. Output is generated text and can be wrong, stale or confidently mistaken about facts. Nothing they produce is investment advice. Verify every number against primary sources before acting on any of it.
