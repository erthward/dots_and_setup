@~/dots_and_setup/ai/about_me.md
@~/dots_and_setup/ai/python_style.md
@~/dots_and_setup/ai/data_viz.md

# how I work
- **workflows**:
  - I'm a Luddite at heart, compute-nerd in practice (they both make sense to me, though don't seem to to others).
  - I use a pure-Linux laptop since I started with computing. Work on the command line as much as possible (e.g., I mostly work in Python and I just use ipython right in the terminal, using ctrl+c+c to send Python code from a vim-edited script in a separate pane directly into the running ipython process... so basically, I ape an IDE rather than using one; same for R, etc , which I run through radian, not RStudio).
  - I work in a basic zsh-and-tmux setup, with a .zshrc that I've been cultivating for years. Exceptions are superbrowser for email and messaging, plain broswer for web use, Google Docs for papers/letters/apps/etc.
  - Thus, I prefer minimalist terminal workflows and hands-on-the-homerow keyboard shortcuts/hotkeys rather than mouse and GUI and browser, whenever possible and practical
- **tools**: Python (always my first stop for a computing job), R (for stats, tests, or other methods that have only been implemented there), Bash and zsh (use it all day as my 'glue', since I work >= 80% at the CLI), vim (for all editing except papers/emails/proposals/etc), SQL (build databases only if the use case calls for it, i.e., truly relational and hierarchical data), Julia (when Python isn't fast enough), Git (version-control everything), GEE (Python or JS), Microsoft Planetary Computer (MSPC; including cluster-computing and parallelization), HPC (i.e., traditional campus-type cluster environments), QGIS, Arc, Matlab (once upon a time...), basic HTML/etc literacy
- **order of preference**: 1.) Python, 2.) Bash, 3.) R, 4.) GEE, MSPC, 5.) SQL. Overall though, pick the right tool for the job, in your estimation, but when mutliple could work equally well, try to generally follow this list.
- **compute context**: I mostly work on laptop, as much as feasible; I often next move things to a basic Linux cluster with SLURM scheduler and `module`-based software loading functionality; I use GEE and/or MSPC for basic preprocessing or geocomputing on big spatial datasets that are already living there, such as MODIS; I have done a bit of other cloud-based computing, e.g., creation and use of VM instances, but that's a last resort, as I'm not a cloud devops architect and have no interest in becoming one; I have not done any GPGPU, but I'm not opposed to learning as needed
- **configs**: Most of my important, constant-use configs are in ~/.zshrc and ~/.vimrc. My ~/dots_and_setup repo is what I've been curating over the years, so those config files symlink there.
- **tmux**: My tmux leader key/prefix is <Ctrl>+<A>.
- **git commits**: Don't commit anything without seeking and receiving my express approval! My commit messages should err on the side of more detail about what was done, and will also include any important notes for my future self (because I grep the output of `git log` fairly often). I don't much care whether they're present tense or past, but past feels more natural to me.

# my goals and vision for working with AI:
- decide whether and how it can improve my life as a working scientist and make it more meaningful (since I'm still afraid it will be the opposite)
- develop robust, rigorous scientific code
- develop other tidbits (rigor less important) to support/reduce ancillary workflows and otherwise improve/support my life
- free up time spent on less-valuable tasks (even if enjoyable, like basic plot coding), to reinvest in the deep, focused reading, thinking, and work that typically brings out the biggest, most valuable scientific ideas

# how you should generally communicate/work with me:
- no sycophantic bullshit! please!
- direct, honest communication
- as concise and organized as possible
- I generally aim to understand everything from first principles, so I will be explicit when I find corners I'm willing to cut
- skip conversational filler and unnecessary apologies.
- always ask for confirmation before running destructive terminal commands
- when suggesting code changes, briefly explain the "why"
- Because I'm new to Claude Code and agentic AI: briefly explain new Claude Code features when you use them.
- If you notice repetitive steps, please suggest hotkeys and automations; when you suggest a workflow, include the binding/alias/script.

# rules about scientific rigor and scientific programming:
- **hallucination**: never invent citations, DOIs, or pre-existing software packages/functions
- **code is the doing of science**: my code is what connects my scientific vision to my data, so confer with me when making design decisions that need me to weigh in based on my scientific interpretation
- **significance**: use the word 'significant' in a strictly statistical sense, not a quotidian one
- **defense first!**: defensive programming is great; add assert/raise statements liberally, testing and sanity-checking values/data being produced against a priori expectations; loud bugs are better than quiet bugs and much better than silent bugs!
- **NAs**: never silently drop them; always explicitly handle them as needed; if not sure how, check with me for decision based on my scientific interpretation
- **analytical choices**: flag every choice that affects results (e.g., CRS/reprojection, resampling, priors, thresholds, secondary and/or default parameters in statistical tests or algorithms run, whether or not to include zeros in analyses, whether to interpolate NAs, etc, etc). Do this with a `#NOTE: ` line in Python or the equivalent in other languages, as much as possible
- **seed numbers**: Use seed numbers whenever reasonable, by setting a global `SEED=42` and then propagating it through `seed=None` arguments in functions, which will only set a seed if seed is not None. Use print-type statements to dump the seed number that is being used into STDOUT/logs/whatnot.
- **printing and verbosity**: Where useful (e.g., top-level/pipeline functions), include `verbose=True` default arguments and print useful high-level information. For example, number of files/records/rows/layers etc to be processed, and current number being processed (which can be batched reasonably, e.g., every 10,000 when millions will be processed); a brief mention of each of the main steps currently being worked on.
- **timing**: Where useful (e.g., top-level/pipeline functions), include `time_it=True` default arguments. This is, of course, not needed for operations where timing is unlikely to matter within a plausible scaling domain. When using them, print runtimes when `verbose=True`, if applicable, or else just by default.
- **built-in debugging**: Where useful (e.g., top-level/pipeline functions), include `debug=False` default arguments, and if `True` then print additional information that might help (e.g., intermediate variable values, summaries and structures/contents of larger objects, number of NAs or negative values encountered, etc.)
- **recursion**: recursive functions are great and are underused in scientific programming, in my opinion. Keep an eye out for situations where they might provide the cleverest solution to a problem.

