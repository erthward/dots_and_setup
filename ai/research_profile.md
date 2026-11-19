# research profile (distilled from my portfolio by Claude Code, 2026-11)

## core question
How does the **geography of timing** (spatial variation in the timing of environmental cycles and
shifts) shape the processes that generate, distribute, and maintain biodiversity? Lab name: Where of
When Lab (WoW Lab). Ambition: establish the geography of timing as a core concept in ecology and biogeography.

## signature ideas and coined terms (use them exactly; don't paraphrase)
- **allochrony by allopatry (AxA)**: reproductive isolation from asynchronous breeding between populations
- **isoclimatic phenological asynchrony**: asynchrony between climatically similar sites (expected stronger in the tropics)
- **phenocycle**: a location's long-term average annual phenology (harmonic-regression fit)
- **asynchrony of seasons hypothesis (ASH)** (Martin et al. 2009), **LSP** (land surface phenology), **NIRv**, **SIF**
- season-agnostic, multivariate phenology over scalar phenometrics (SOS/EOS); skeptical of the "temperate phenological paradigm"
- **poylgenicitiy** to describe the mono-<->oligo-<->poly-<->omnigenic spectrum along which a trait falls

## current agenda (URF/DECRA era)
- WP1: global atlas of multidimensional LSP shifts (shape, phase, amplitude, predictability; sliding-window harmonics on
  MODIS NIRv; Monte Carlo; causal attribution with ERA5-Land; distributional regression; CMIP6 projection)
- WP2: Macrogenetics Unified Database (MUD) + `MUDpy` API; MMRR tests of genetic isolation by AxA (tropical montane vs
  Mediterranean/semi-arid; plants vs animals)
- WP3-4: tropical montane cloud forest observatories (i.e., the Global Alliance of Tropical Observatories (GATO), which aims to start at Cloudbridge, Costa Rica): microclimate sensor networks, fog, foliar water uptake, dendrometers, drone phenology, terrain-mediated light seasonality (opposite slopes six months out of phase)
- Side threads: coffee as a "found network" of phenology sensors (Cenicafé), sea surface phenology (UQ), phenological anomalies and animal movement (CSIRO, UQ, elsewhere potentially)

## applied work (day job, past and present)
- CSIRO: koala monitoring and food-tree habitat, Nature Repair Market / biodiversity credits (NBAS), citizen-science trend frameworks, `lovebirds` (virtual-ecologist community simulation).
- TNC: agroforestry and reforestation as natural climate solutions, albedo-adjusted climate benefits.

## methods toolkit (demonstrated in published work)
Harmonic regression; EOF analysis; k-means clustering; random forests + SHAP; MMRR (matrix regression on distance matrices); permutation and Monte Carlo nulls; forward-time spatially explicit genomic simulation (Geonomics, my own package); remote sensing at scale (GEE, MODIS, OCO-2, GOES, Landsat, PhenoCam, FLUXNET); HPC (Savio/SLURM).

## how I frame science
- Gap move: "X is fundamental, yet ecologists neglect the intersection of space and time."
- Nested scales: global → regional → landscape; theory + observation + simulation + data science.
- Mechanism first (topoclimate, airflow, solar geometry), then pattern; explicit, falsifiable hypotheses (H1a, H1b…).
- I value open, reusable data and code; interactive viewers and animations for communication.
- Strong applied/impact orientation alongside fundamental theory; inclusive teaching and mentoring are core values.
