# CoDMAV Methodology

## Domain-specific representation

CoDMAV keeps the three domains independent until representation/index construction.

### EEG

`theta + beta → PCA → Activation_PC1`

`theta_beta_ratio → Attention_TBR`

Final EEG representation:

`[Activation_PC1, Attention_TBR]`

### Wellness

`stress + mental_health + social_level + social_support + sleep`

→ median imputation

→ 1st/99th percentile clipping

→ standardization

→ PCA

→ `[Wellness_PC1, Wellness_PC2]`

### Academic

`engagement + assessment + performance`

→ missing-value handling

→ 1st/99th percentile clipping

→ standardization

→ PCA

→ `[Academic_PC1, Academic_PC2]`

## Composite framework

The project-level framework maps the domain representations to:

- CEI — Cognitive Engagement Index
- BWI — Behavioural Wellness Index
- API — Academic Preparedness Index

The three indices are modelled independently and used to generate a Monte Carlo population.

## Weighting

The documented weighting strategies are:

- Equal
- Entropy
- CRITIC
- PCA

The composite score is:

`CLRI = w1*CEI + w2*API + w3*BWI`

## Validation

The project evaluates:

- distribution fit
- weighting-method consistency
- rank correlation
- category agreement
- bootstrap stability
- weight perturbation
- leave-one-domain-out sensitivity
