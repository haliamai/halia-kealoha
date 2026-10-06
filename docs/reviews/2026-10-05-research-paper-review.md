# Haliʻamai Kealoha — feedback, sweep of 2026-10-05

This pull request answers #10, #11 and #12.

## Research paper review — pre-deadline read

You told me on #11 that this is the final paper, so this read is short, and nothing in it blocks the paper. All four items from my last read are closed. The best sentence in the paper is the one that admits a limit: "I don't think the evidence lets me credibly place V_public anywhere within the $10 million–$100 million range Figure 1 tests, so I can't identify the break-even Δp the Legislature should actually be looking for." A recommendation that says what the evidence cannot yet settle, and then tells the Legislature what it would need to see, is a stronger recommendation, not a weaker one. The break-even arithmetic checks at every point on the curve, and the $5 million traces to your sources file.

**Is avoiding a dry hole part of the public value?** Your expected-value formula counts public value only when development succeeds: Δp × V_public. The paper also says better information can show "whether to walk away." When characterization tells a developer not to drill, the exploration money that is never spent is a saving too. Is that part of the public value of characterization, and if you counted it, would the break-even move? Answer it in a sentence or two if you think it belongs; leaving the formula as is and saying why is also a choice.

**One fix and one check.** On the Figure 1 page the title appears twice: once as the heading above the figure, and again in bold inside the image, which `figures/breakeven_curve.py` draws at lines 105–107. Keep one. The simplest is to delete those three lines and rerun the script, so the heading above the figure is the only title:

- On **github.com**: open `figures/breakeven_curve.py`, click the pencil icon, delete lines 105–107, commit, and rerun the script so the image updates.
- Or, in **Claude Code or Codex** opened in your portfolio repository: "Remove the title drawn inside Figure 1 at lines 105–107 of `figures/breakeven_curve.py`, rerun the script, and show me the new figure." And the HRS § 182-7(c) reference carries no year, though your spec's newest entry discusses adding one; confirm which you intend.

The paper you uploaded to Lamaku matches the one I read, word for word, apart from the date on the title page. You can upload a revised copy to Lamaku before the deadline, and the latest upload is the one I will grade. If you do, this is the order I would work in:

**In order:**

1. Decide whether exploration money not spent belongs in the public value, and answer it in the text or say why the formula leaves it out.
2. Remove the second Figure 1 title, and settle the year on the HRS reference.
