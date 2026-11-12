# News Summary — make.fun bounty entry

Entry for make.fun bounty **"Write the best summary of 11 November's world news"**
(news-summary-01), by **Bayu Prasetya (0xby)** — https://make.fun/bounty/news-summary-01

## What it does

`main.py` (Python 3, standard library only) writes the summary held in this
repository (`summary.txt`) to `/output/entry.txt`, byte for byte. It uses no
network, and two runs always produce identical bytes, as the bounty requires.
After writing, the program reads the output back and verifies both its length
and its bytes against the source, failing loudly on any mismatch, and prints
the SHA-256 of what it wrote plus the summary's first line.

## The summary

The summary (under 2,000 characters, English) was written by the AI agent
from the day's reporting across multiple independent news digests: the
US-mediated Russia–Ukraine talks in Abu Dhabi, the settled US midterms,
Trump's "effectively over" remark on Iran, US October CPI, COP31 in Antalya,
TSMC's chip demand and Anthropic's IPO filing, Haiti, Bangladesh, and Delhi's
air. The build is documented in `TRANSCRIPT.md`; the agent's session
transcripts are bundled with the submission itself.

## License

MIT — see `LICENSE`.
