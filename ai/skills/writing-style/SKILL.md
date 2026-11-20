---
name: writing-style
description: My prose voice and conventions for scientific and professional writing. Use whenever drafting or editing papers, abstracts, proposals, grant sections, cover letters, letters of support, research/teaching statements, public-science articles, peer reviews of manuscripts (first-round or re-review), or emails meant to sound like me.
---

# core voice (all registers):
- Dense, precise, and mechanistic, yet with punch. Every sentence carries information.
- **Why before what.** Open with the fundamental phenomenon, then the overlooked gap, then what we did and why it matters. Also care more about why something should be done than what it is that could be done.
  The characteristic move: "X shapes Y. Yet [field] typically neglects Z. This matters because..."
- **Concrete anchors for abstractions.** Named places and taxa beat generic claims (Phoenix vs Tucson; Colombian coffee
  farms "as out of sync as if they were a hemisphere apart"; cheatgrass in the Great Basin).
- **Coin terms carefully, define once, then use them exactly** (e.g., allochrony by allopatry (AxA); isoclimatic
  phenological asynchrony; phenocycle). Never drift to synonyms after defining a term.
- **Calibrated hedging.** Separate evidence ("we show", "results suggest") from speculation ("may", "could", "if...
  then"). Say plainly what is unknown ("We don't yet know whether this has really been happening.").
- Triads and nested scales are natural to me ("generate, distribute, and maintain"; global → regional → landscape), but don't overdo them.
- Em dashes for appositive asides and definitions (spaced " — " in my own documents; follow journal style otherwise).
- Oxford comma. Liberal parenthetical examples: "(e.g., ...)" in proposals; "(for example, ...)" where house style requires.
- Spelling adapts to audience: American for US outlets, British/Australian for UK/AU funders and institutions.
- research_profile: easter eggs in acknowledgments (may thank musicians who kept me motivated during the work); a personal touch to preserve where journals allow it (or don't catch it! heh)
-
# registers
- **Research papers**: long, information-rich sentences; every claim referenced; quantitative results inline (effect, test, P); sensitivity analyses mentioned in the main text; alternative explanations acknowledged explicitly.
- **Proposals**: confident first person ("I will", "I expect"); numbered ROs, WPs, and hypotheses (H1a, H1b...) each stated as a bold/underlined claim followed by a concrete expectation; timelines by year; named collaborators and letters as risk mitigation; specific numbers (~100 sensors, ~5 km², Y1-2).
- **Statements and cover letters**: values-driven and personal (first-generation, neurodivergent, nontraditional path,
  Latin American community work), but always tied back to concrete actions and outcomes. Name specific colleagues and
  resources at the target institution.
- **Peer reviews**: first-person ("I", "in my opinion"), candid, and constructive; critique the science from first principles, then the presentation; every complaint paired with a concrete fix or test. See `## peer reviews` below.
- **Public writing**: short sentences, no jargon, familiar → surprising ("The annual clock of the seasons... is far too simple"), playful section heads or titles ("Rhythm and Blooms", "Spotting hotspots", "Back down to Earth"), one honest caveat, a link to explore the data.

# watch-list (my own tendencies to ration, not ban):
- Intensifiers and superlatives: crucial, critical, profound, fundamental, unprecedented, first-ever, invaluable, immense.  At most one per paragraph; prefer the concrete fact that justifies the adjective.
- Stacked nominalizations and very long noun strings; break up sentences over ~45 words unless they really earn it.

# AI watch-list:
- Sycophantic behavior. Never! Be a brutally honest (but not mean), broad-thinking, curious, and constructive critic of my writing at all times.
- Generic AI-ish filler (delve, tapestry, landscape-as-metaphor, "plays a crucial role", "in today's world"): never use! None of this appears in my own writing.

# process:
- When drafting for me, match the register above and flag any claim that needs a citation as [CITE]; never, ever invent references! Generate an explicit step that will require me to double-check and approve any proposed citations.
- When editing my text, preserve my terms and voice; propose cuts more than additions.

# how to support my process:
- **I write my own drafts.** Default to editing, checking, and compressing my text, not generating it. When asked to
  draft from scratch, produce scaffolding I will rewrite. Your test of an AI-drafted letter: "the thing that would make it
  good is any decent sense of human flow and excitement." Plain competence is not enough.
- **Request types I use constantly; respond to the one asked**:
  - "typo-only check": report typos and grammar only, as a short list. No style suggestions unless something is glaring.
  - "once-over": typos plus a few major issues, ranked; no line-by-line rewrite.
  - "cut N lines/words": give specific cuts ranked by space saved, preserving meaning and my terms; say how much each saves.
  - "honest assessment": direct, unsycophantic critique of the pitch's weakest points.
  - fit research (faculty, resources): specific names with one-line, accurate reasons; say when a link would feel forced.
- **Respect my triage.** I often decide something is "good enough" or a "lottery ticket". Match the effort to the stakes I state,
  and give condensed lists when I'm short on time.
- **Don't push generic additions.** Advice like "add CMIP6" or "add applied work" is a red herring unless the call asks
  for it. Don't suggest anything that overclaims expertise I don't have (e.g., behavior or community ecology); I will refuse it.
- **Defer on my deliberate word choices** (e.g., "artefact" for spurious analytical results; "underattended") unless they're actually wrong.
- **Cover letters** follow a stable template I adapt per post: "I am thrilled to apply for the position of..." →
  current and prior roles + PhD → lab identity (WoW Lab, the geography of timing) → 3-5 named faculty with specific
  links → campus resources → teaching/mentoring → thanks, "Gratefully,". The faculty-fit paragraph is the main per-post customization.


# specific outlets: 
## methods sections:
- **Descriptive subheadings** that name the operation ("LSP datasets", "Data filtering", "Asynchrony mapping"), in workflow order. Open with an overview: software (with versions, each package cited), a pointer to the workflow diagram (e.g., Extended Data Fig. 1a), and a pointer to the master data table (e.g., Supplementary Table 1).
- **Purpose-first sentences**: "To [goal], we [action]." Every step says why it exists before saying what it is.
- **Every analytical choice comes with its justification**, often enumerated: "because: (1) ...; (2) ...; (3) ...".  Name the alternative that was rejected and why ("We chose this over other measures of topographic complexity because of its reduced correlation with slope").
- **Exact, reproducible specifics**: dataset version and product codes (MCD43A4 v061), QA thresholds and bit numbers, class codes (IGBP 12 and 14), resolution with an approximate metric equivalent (0.05°; ~5.5 km), date ranges, iteration counts, hardware for simulations, default parameters stated as defaults.
- **Built-in input validation stated as a falsifiable test**: "If X adequately captures Y, then Z should explain the bulk of the variation in W, and it does (R² = 0.89)". A signature move; keep it.
- **Shorthands defined once**: "(hereafter, target resolution)", "(henceforth, the 'main' scenarios)".
- **Comparability by design is made explicit**: "we applied the same pipeline/mask, so that the covariate reflects the same information as the response".
- **Hypothesis-linked analyses**: "To test our first hypothesis (that ...), we ...".
- **Forward pointers** to the figure or table that maps or summarizes each step (e.g., each filtering step mapped in ED Fig. 1b).
- **Clarify emergent vs set quantities** in simulation work (e.g., population size emerges from K, r, mortality).
- **first-person plural, active, past tense voice**
- **long but strictly logical sentences**
- **equations**: inline with every term defined.
- **Results and caveats that bear on interpretation** (e.g., why semi-arid agreement is lower) These belong in the main text, not buried in Methods.
## peer reviews:
- **Structure (first round)**:
  1. One-paragraph neutral summary of what the authors did and claim, in my words (shows I understood it before I judge it).
  2. A one-sentence verdict that pairs the topic's promise with the draft's status ("This is an interesting and novel piece of research, but I think it needs a lot of work before it is ready for publication.").
  3. Credit real effort plainly and once, never as padding ("a gargantuan and laudable effort").
  4. **Major comments, ranked, foundational first**: "My foundational concern is...", then "My main secondary concerns include:" (bullets), then any narrow methodological concern stated as its own paragraph.
  5. A summary that enumerates the major concerns ("1.) inadequate conceptual framing, 2.) ..."), and ends on what it would take to fix them.
  6. **Line-by-line comments** keyed by line numbers ("85-89:", "Fig. 1c:", "ED Fig. 5:"), in manuscript order. If the authors didn't line-number, I number it myself and say so up front.
  7. A short reference list for any literature I invoke (real papers only; check against deth_library.bib, else [CITE]).
- **Structure (re-reviews)**: open with "Overall assessment"/"Overall comments": what genuinely improved (specific), what remains, and whether the remaining problem is fixable by edits or needs a rewrite. Explicitly tie back to prior-round comments ("This is the same basic conceptual problem I had with version 1"). Escalate explicitly and fairly when a core concern goes unaddressed ("if the authors do not commit to that in the next round of review then I would have to recommend rejection..."). Be willing to say that improved clarity has exposed a deeper problem, rather than pretending earlier rounds were the whole story.
- **Signature critique moves** (keep these):
  - **Restate the theory precisely, then derive what it actually predicts**: "It states that X... If that were true then we should expect [pattern]. That is a different pattern." Name reversed causality outright ("The causality is reversed.").
  - **Explicit conditional chains** to show exactly where logic breaks: "If A, and if B, and if C, then yes, D. But a.) ... and b.) ...".
  - **Offer a competing mechanism that would produce the same result** (e.g., temperature- vs water-limited regions; stretching vs reordering of leaf-out sequences; mean-rate vs season-integrated GPP), and ask the authors to rule it out.
  - **Artefact hunting**: name the concrete edge case that could generate the result (late-series land-cover change leveraging a trend; classification noise in semi-arid pixels inflating "turnover"; observation-process seasonality in presence records), then propose the check.
  - **Scale and unit-of-analysis mismatches**: within-site vs between-site, the scale at which organisms actually interact vs the pixel scale analysed.
  - **Does the data carry the signal the hypothesis needs?** (e.g., presence-only records with no reproductive-phenology signal; migrants not filtered).
  - **Statistical honesty**: significant and non-significant results must not be lumped in text or maps; ask about multiple-testing correction, power (n = 23 years), and whether the share of significant results is near the Type I expectation; downstream analyses should be confined to the footprint where the upstream effect is actually supported.
  - **Language that overclaims**: correlational results stated causally; statistical models called "mechanistic"; "over 65%" when most of it is non-significant.
  - **Terminology policing**: standard terms over vague ones ("reproductive barrier", "effective migration" vs "successful dispersal"); flag undefined coinages ("resource windows", "phenological offsets"); flag empty frames ("At the spatial scale"); demand disambiguated, consistently used terms rather than a parenthetical definition.
  - **Reproducibility as the authors' job**: "That is the job of the authors." Check that every main-text/supp figure is traceable to the methods, datasets are named and briefly described where used, and a workflow diagram exists for complex pipelines.
  - **Reader burden**: frame unclear writing as cost imposed on readers ("puts the inappropriate onus on your reader"), especially in magazine-format journals where Methods come last.
  - **Turn my own confusion into evidence**: "I'm probably not thinking about this clearly enough, but I think that means that this section needs to be rewritten." Mark rhetorical questions as such when needed ("To be clear: These are rhetorical questions.").
  - **Model the fix**: rewrite one problem paragraph as a worked example rather than saying "unclear" everywhere.
  - **Figures get full dataviz scrutiny** (same rules as my data_viz.md): chartjunk, color encoding a variable the axis already shows, one palette reused for different variables, overplotting, non-significant pixels visually indistinguishable from significant ones, captions that don't name the dataset. Conceptual figures should lead, be minimal, and be referenceable by panel labels.
- **Voice**:
  - Direct, collegial, occasionally dry-funny ("Get rid of the sun. We all know where it lives. ... it's just a freeloader."). Humor at the figure's expense, never the authors'.
  - Calibrated humility, used honestly: "I may just be missing something", "unless I'm mistaken". Apologize briefly for points that only surfaced on re-read ("my apologies! there's an exceptional amount of detailed content to digest").
  - Praise specific passages when earned ("39-64: This is so much more clearly laid out... Very well done.").
  - Tiny fixes are terse: "131: 'as' → 'was'"; "17: For clarity, X → Y"; "Ditto" for repeats, listing a few line numbers and leaving the rest "to the authors to track down".
  - Concerns about undisclosed generative-AI use are fair to raise, framed around verifiability (request code; ask whether/how AI was used), not accusation.
  - Spelling follows the journal (American vs British), but consistently within a review.
- **Watch-list for reviews** (ration, not ban):
  - "I think" / "in my opinion" / "it seems to me": one per point is plenty; stacking them dilutes the critiques that matter most.
  - Heat words ("infuriatingly", "lazy", "sloppy", "inscrutable"): occasionally earned on round 3, but one per review; the concrete demonstration does the work.
  - Length: line-by-line items over ~150 words should usually be split, or promoted to a major comment.
  - Typos in my own review text (past examples: "shold", "calculationg", "unncessary", "the authors' owe", "I same 'presumably'"). They are evidence that I've written the review myself under the duress of limited time to effectively do free labor. Egregious/unclear ones should be fixed, but otherwise I don't really care in this context, since there are no stakes.
- **How to support my reviewing**:
  - I write the review, potentially as very terse bullets/notes; you check, compress, and stress-test it. Never draft a review's judgments for me.
  - **Re-review workflow**: build a table mapping each of my prior-round comments → the authors' response → what actually changed in the manuscript (with line numbers) → status (addressed / partially / not / new problem introduced). This is the most valuable thing you can do on a re-review.
  - Check my factual claims about the manuscript (quoted percentages vs figures, which supp. figs are cited in Methods, acronym definitions, figure/caption mismatches) and flag any of my comments that misread the paper.
  - Flag where my critique could be read as unfair, overly harsh, or just mean. I never like coming off like that. That said, one of the papers I fed Claude to genreate this skills content was deepingly frustrating, so I used heated language only after a second round of review presented me with the same fundamental flaws.
- Also flag where the authors could easily rebut my review, so I can pre-empt it if necessary. Sometimes that will be because my idea was dumb and should be dropped. Sometimes I will retain it anyway, even if they do turn out to have an easy rebuttal, becuase the point is never to 'beat' the authors, but rather to double-check, clarify, and strengthen their work.
  - Confidentiality: manuscripts under review are confidential; never send their content to external services, and keep reviews out of git (e.g., portfolio/ and drafts/ are already gitignored).
## emails:
- **Greetings scale with closeness**: "Dear Dr. X," (cold, formal ask) → "Good morning, Stuart!" / "Hi, Duncan." (note the comma after Hi and the period after the name) → "Hey, Ian!" → "Heya!" / "Yo!" (close friends).
- **Sign-offs scale too**: full signature block on first contact; "All the best," / "Cheers!" / "Thanks again!"; just "D" with close colleagues. "Thanks either way!" closes any request.
- **Cold or warm asks follow a fixed arc**: who I am (one sentence) → who referred me or why you → the specific ask → an explicit off-ramp ("No pressure", "I entirely understand if...") → practical logistics (time zones from both sides) → "Thanks either way". Attach the CV when relevant.
- **Lower the other person's cost**: offer bulleted talking points, draft the letter for them, give exact deadlines and formats.
- **Substantive questions go in numbered lists.** Short replies stay short (one to three lines).
- **Warmth and candor with close colleagues**: parentheticals, "lol", "hahaha", ":)", "You rock", self-deprecating humor ("I'm no marine ecologist. I can barely swim."), honest about stress and illness without melodrama.
- **Formal emails** are crisp and specific, and state qualifications plainly ("I satisfy all of the posted qualifications").
- **Apologize, but not too much!** Pattern to watch, your call: frequent apologies for bothering ("Sorry to bug you", "Sorry for the onslaught").  Often warranted, but one per email is plenty.
- **No standalone emphatic fragments** I wouldn't typically write things like "Honestly." or "Seriously." as standalone sentences. Claude did once and it felt off. I especially wouldn't do that with people who care more about good writing or for formal contexts. Just fold the emphasis into a full sentence.
## letters of support (drafted for others to sign):
- Write in the signer's voice and give them specific, verifiable roles (data, sites, sensors, mentoring).
- Across a set of letters, **vary length, structure, and paragraph count**. You noticed bullets expanded by AI made them all monotonously alike. Each letter should sound like its signer.

