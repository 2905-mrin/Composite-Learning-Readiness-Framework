# Results

## Monte Carlo cohort

The supplied cohort contains 10,000 synthetic learners with:

- CEI
- API
- BWI

## Weighting results

| Method | CEI | API | BWI |
|---|---:|---:|---:|
| Equal | 0.333 | 0.333 | 0.333 |
| Entropy | 0.722 | 0.123 | 0.155 |
| CRITIC | 0.362 | 0.312 | 0.326 |
| PCA | 0.355 | 0.341 | 0.304 |

CRITIC and PCA were retained as the strongest final weighting candidates, with CRITIC selected for the final framework.

## Reported project result

**CLRI = 78.6 / 100**

**Readiness = Very High**

**94.38% category agreement between CRITIC and PCA.**

## Supplied CSV

`outputs/CLRI_Final_Results.csv` contains 10,000 rows and:

```text
CLRI_Equal
CLRI_Entropy
CLRI_CRITIC
CLRI_PCA
Equal_Category
Entropy_Category
CRITIC_Category
PCA_Category
```

The supplied CSV stores CLRI values in normalized 0–1 form.
