# Async Swap whitepaper

The paper presents the problem, market model, and matching mechanism: feasible exchange,
exact eligibility within price buckets, priority bids, integer settlement, escrow conservation,
and bounded execution cost. It distinguishes mathematical guarantees from economic tradeoffs.

## Build

```sh
tectonic -X compile whitepaper.tex
```

`whitepaper.tex` includes `sections/eligible-matching.tex` and the mathematical illustration
`figures/matching-limits.png`. The illustration can be regenerated with:

```sh
uv run --with matplotlib python figures/plot_matching.py
```

The `evidence/` directory, gas plots, and the generated `sections/gas-results.tex` and
`sections/receipt-results.tex` are supporting engineering records; they are not included in
the paper. Their experimental measurements should not be interpreted as worst-case bounds.
