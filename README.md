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
| [lecture-notes-builder](skills/lecture-notes-builder) | Merges a lecture transcript and the slides into one exam-ready note, filed in the right Obsidian course folder | Turns a lecture transcript (Granola or similar) plus the lecture slides into a structured, exam-ready class note filed in the right Obsidian course folder. Use when the user shares a class transcript, lecture slides, or asks to write up a lecture or class. | Live | This repo, `skills/lecture-notes-builder` |
| [pdf-to-profile-note](skills/pdf-to-profile-note) | Turns a personality report, assessment or study guide PDF into a short, page-cited Profile note, flagging conflicts with what is already there | Ingests a PDF (personality or psychometric report, assessment results, study guide, career report) into a structured, cited Obsidian Profile note, and merges it with what the Profile already says. Use when the user shares a PDF about themselves or a study guide and wants it added to their vault or Profile. | Live | This repo, `skills/pdf-to-profile-note` |
| [project-readme-publisher](skills/project-readme-publisher) | Turns a project's Obsidian notes into tab-style GitHub docs and publishes them on a branch through a pull request | Writes tab-style GitHub README documentation for a project kept in an Obsidian vault (or any folder) and publishes it to a GitHub repository on a branch with a pull request. Use when the user wants a project documented on GitHub, a README written or refreshed, or vault project notes pushed to a repo. | Live | This repo, `skills/project-readme-publisher` |
| [timetable-to-ics](skills/timetable-to-ics) | Converts a timetable into an .ics file with a bundled script that re-reads the output and checks every event against the source | Converts a class or exam timetable (PDF, screenshot, spreadsheet or pasted text) into an .ics calendar file with strict, scripted accuracy checks against the source. Use when the user wants a timetable, schedule or term dates turned into a calendar or .ics file. | Live | This repo, `skills/timetable-to-ics` (includes `scripts/build_ics.py`) |
| [vault-health-check](skills/vault-health-check) | Audits an Obsidian vault with a read-only script, applies the unambiguous fixes and asks before anything destructive | Audits an Obsidian vault for orphan notes, broken links, duplicate names, unused attachments and stale index notes, then proposes and applies fixes. Use when the user asks to clean up, audit, tidy or check their vault, find orphans or broken links, or update index notes. | Live | This repo, `skills/vault-health-check` (includes `scripts/audit_vault.py`) |

## The investment committee set

The four finance skills above split an investment committee across separate roles, so each argument gets made properly instead of one voice hedging against itself.

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
