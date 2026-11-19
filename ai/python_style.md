# principles and rules of thumb
- **functional**: more but shorter, cleaner functions is best, when it works
- **environment tool**: Default to using conda/mamba, with one env and environment.yml per project
- **defensive programming**: I never tend to run python as `python -O`, so I'm not concerned about the choice between `assert` or `raise`, but just default to statements that will default to running in as many contexts as possible, and will provide informative error messages containing some demonstration of the failing data value/structure. 
- **formatter/linter**: I've never used. Don't reformat existing code.
- **docstring style**: numpy
- **type hints**: nice to have
- **default stack**: numpy, pandas, geopandas, rasterio, xarray, rioxarray, dask, matplotlib, seaborn, scipy, sklearn
- **preferred file formats**: CSV, shapefile or geojson, GeoTIFF (COG usually unnecessary and optional)
- **variable names**: explicit is great, but good to use very shortened ones for common variables (e.g., t for time, d for distance) and 'subscripted' ones for variations on that (e.g., d_geo, d_env, d_sea, d_gen for distances in geographic, environmental, seasonal, or genetic spaces), or for quick, simple, or content-agnostic objects (e.g. pd.DataFrame-> df, np.ndarray -> arr)
- **Heavy commenting**: historically, ~16-25% of my lines are comments, and they are used to explain explain *why* (scientific rationale), not just what. This way, my code is largely self-documenting.
- **continue my `# NOTE:` convention (already in use)** amply used to track analytical choices, sources, and caveats, e.g., "NOTE: chosen by scree plot inspection".
- **Assert-heavy defensive style** shape and value checks inline.
- **add a behavioral-params block at the top of scripts** under banner headers (`#####\n# BEHAVIORAL PARAMS...\n#####`), with boolean flags kept specifically to test sensitivity to a decision (e.g., `standardize_ts`). Not necessary for every piece of code, but any production code can probably benefit from this.
- **Seeds**: `set_seed = True; seed = 1; np.random.seed(seed)`.
- **Progress printing** every N iterations with percent complete.
- **Compute-or-load caching**: `if not os.path.isfile(path): compute and save; else: load`.
- **Laptop vs cluster switching** by inspecting the path (`os.getcwd()`), with data dirs for each. Not always necessary, so prompt me as to whether or not I anticipate using the code in both/multiple environments.
- **Package code (e.g., geonomics)**: classes, numpy-style docstrings, underscore-prefixed private helpers, tests dir, `verbose` args.
- **Script code (e.g., phen_asynch)**: flat, long (up to ~900 lines), numbered/banner-sectioned scripts organized by `calc/ anal/ eval/ viz/` per topic. A good research-repo layout.
- **Include stepwise READMEs** I like them to lay out the stepwise procedures for running the entire project and reproducing all published results, with notes as to runtimes for each (this often helps me plan reruns).
- **script layout**: banner-sectioned scripts; params block at top; `# NOTE:` for every analytical choice; cache
  expensive intermediates with compute-or-load.
- **paths**: never hard-code absolute paths; read data roots from a config or env var with laptop/cluster profiles.
- **vectorize**: prefer array operations/matrix algebra over Python loops for per-pixel or per-sample computations.
- **randomness**: `np.random.default_rng(seed)`, passed explicitly; print the seed.
- **suggest easy optimizations!**: I usually make my code work first, then make it better later on, if necessary. That said, AI-supported coding has so little human overhead, compared to the old days, so if there are simple refactoring/optimization gains I could easily make then please suggest them freely!

# weaknesses worth fixing (candid)
- **Hard-coded absolute paths and `sys.path.insert(...)`** to import helpers. Suggest: one `config.py` / env var for data roots, and install helpers as a local package (`pip install -e .`). This was not a general habit before, just one I fell into out of corner-cutting within a specific project. That said, let's definitely not do that again!
- **Python loops over pixels** where linear algebra would do. E.g., per-pixel `np.sum(coeffs_vec * dm, axis=1)` over millions of pixels is a single matrix multiply: `ts = dm @ coeffs.reshape(ncoef, -1)` (orders of magnitude faster).
- **Legacy `np.random.seed`**: prefer `rng = np.random.default_rng(seed)` passed explicitly (reproducible per function).
- **Commented-out alternatives as option records** (`#lat_weights = None` / `#lat_weights = 'cos'`). Better: one param with a `# NOTE:` listing options and why this one was chosen.
- **Plot styling duplicated per script** (figsize, fontdicts, spine loops). Better: a shared style module.
- **No type hints, few tests outside geonomics.** Fine for one-off analysis; for reusable functions, sanity-check tests on toy data are cheap insurance (matches your "defense first" rule). I've already started doing this betters. Let's continue this!

