---
name: dataviz-style
description: My data visualization style for plots and maps. Use whenever writing any plotting, mapping, video, or other figure-generation code (e.g., matplotlib, seabon, ggplot2, etc)
---
# general rules:
- **precdence**: These conventions override any other dataviz guidance.
- **minimalism**: Less is more! Visually unencumbered. Don't add and actively remove clutter. Every component should earn its keep. Let the data speak loudly, clearly, and directly communicate the intended scientific point.
- **exploratory first, clean up for pub later**: no need to waste resources and time fine-tuning plotting code until I pull the trigger on including a plot in a publication. If in doubt, just leave something simple/unaddressed and then raise the thought/question with me and we can decide together whether and how to refine.

# libraries:
- **python**:
  - matplotlib
  - palettable
  - seaborn
  - rioxarray
  - geopandas
- **R**:
  - ggplot2

# palettes:
- **colorblind-friendliness**: ensure whenever possible, but let the science take precent (e.g, if it makes sense to render an RGB visualization of 3-dimensional results then I will defer to that and add a colorblind-friendly supplemental figure, if necessary)
- **sequential**: default to viridis
- **diverging**: default to coolwarm; center on a meaningful value (0, typically) and with TwoSlopeNorm. Don't let the midpoint drift with the data range. Note that I often wind up aactually forcing both sides of the divergence to have the same maximum absolute value, even if one side has much less extreme values in the actual dataset, for purposes of scientific interpretability, so please prompt me if unsure!l
- **discrete**: default to Paul Tol's "bright" (can prompt me if I might prefer "muted" or Okabe-Ito or your built-in Dark2 instead, on a case-by-case basis)

# axes:
- always include units and left and bottom spines
- I only tend to use gridlines if I feel they actually help make sense of a specific set of results

# maps:
- **precedence**: let these conventions override those from above, as necessary
- **usually don't need ticks and axis labels**: I will specify if I want axes to have ticks and labels, but default to getting rid of them
- **rasters and vectors together**: I often plot rasters and vectors together
- **projection**: I typically prefer equal-area projections (for global work, Equal Earth is great!)
- **cartography**: I don't have formal classwork/training in this, and I gather there are people who are precious about including compass symbols, scale bars, CRS/projection information, etc. I am not one of those people and will request such things if and when necessary. Prefer to default to minimalism without worrying about these minor concerns. I'm interested in the scientific ideas, not the presentational conventions, and my maps are usually part of a larger figure or embedded in a context that make this information clear (e.g., methods section will specify CRS).

# my 'calling card':
- aspects to leave my own personal 'fingerpint' on all plots:
  - **direct labels instead of legends**: text at the end of each line in a line plot, or next to clusters. Cleaner than a legend. 
- **one signature accent color**: use #fc0356 to accent/highlight the one "thing that matters" (focal series, highlighted region, p-value written inside the axes, circled key data point, and so forth) in a plot, with other things left in grays.
- **offset, trimmed axes** default to using `sns.despine(offset=4, trim=True))` for non-map axes
- **consistent panel-label treatment**: this includes position, weight, and maybe a short in-panel descriptor of the panel, next to the panel letter (e.g, "a.  Genetic distance")
- **lighter axes and ticks** use a dark gray, not black, so that the data sits visually in front
- **actively cultivate this!** would love to keep honing this little collection of tidbits into a super sharp style that has a sort of subtle classiness to it; always open to suggestted updates!

# outputs (universal defaults; tweak per outlet only if required)
- **core rule**: set figsize to the FINAL physical size (mm / 25.4 = inches) and never
  rescale afterward, so point sizes are true. One figure, one target size.
- **widths (print)**: single column = 85 mm; 1.5 column = 114 mm; double column = 174 mm.
  Max height 225 mm (170 mm if a caption must fit on the page). These fit inside Nature,
  Science (multi-column), Cell, PNAS, Elsevier, Wiley, PLOS. Outlier: Science 1-column = 55 mm.
- **fonts (print)**: sans-serif (Arial > Helvetica > DejaVu Sans fallback). Base 7 pt;
  allowed range 6–8 pt at final size; never < 5 pt. Panel labels 8 pt bold, lowercase by default (a, b, c: Nature style); switch to uppercase for Science/Cell/PNAS. Same font size for all equivalent elements across panels and figures.
- **lines/markers (print)**: line widths 0.5–1 pt (never < 0.25 pt); markers 2–4 pt.
- **presentations (16:9, 13.33 x 7.5 in)**: same figure code with a `mode='slide'` switch;
  base font 18 pt (min 14 pt), lines 1.5–2.5 pt; full-slide figure about 12 x 6 in, half-slide about 6 x 5.5 in.
- **proposals/reports (letter or A4, 6.5 in text width)**: widths 3.25 in (half) or 6.5 in (full); base font 8 pt (min 7 pt). Check agency rules (e.g., NSF/NIH figure-text legibility).
- **formats**: always vector PDF (with SVG as an editable copy); embed fonts as TrueType
  (matplotlib: `pdf.fonttype: 42`, `svg.fonttype: 'none'`), never Type 3. Rasterize
  dense layers only (images, maps, >10k points; `rasterized=True`) at 600 dpi inside the
  vector file. PNG at 300 dpi for slides, docs, and quick looks. TIFF only if an outlet demands it.
- **color**: RGB, colorblind-safe, readable in grayscale where feasible; never encode meaning by color alone if a second channel (shape, linestyle, label) is cheap.
- **implementation**: put all of this in one `.mplstyle` (plus a ggplot2 theme for R), version-controlled in ~/dots_and_setup, with a small helper `fig(width='single'|'double'|..., mode='paper'|'slide'|'proposal')`.
- **consider suggesting improvements**: Claude Code generated this whole block to satisfy the widest possible range of high-impact journals, presentation formats, and proposals, so I'll be keen to refine/enhance as I move forward.
