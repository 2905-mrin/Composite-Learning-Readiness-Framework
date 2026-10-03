# Data

CLRF uses three independent data sources.

## EEG / Cognitive Domain

The EEG development pipeline uses extracted theta, beta and theta/beta-ratio features.

Expected feature input:

```text
theta
beta
theta_beta_ratio
```

The raw EEG recordings and original extraction dataset are not included.

## Lifestyle / Digital Wellness Domain

The wellness notebook uses the College Experience Dataset.

Relevant source tables:

```text
EMA / general_ema.csv
Sensing / sensing.csv
```

Learner-level features include:

- stress
- mental health
- social level
- social support
- sleep duration

## Academic Domain

The academic notebook uses the Open University Learning Analytics Dataset.

Relevant source tables:

```text
studentInfo.csv
studentAssessment.csv
studentVle.csv
```

Derived features include:

- engagement
- assessment
- performance

## Licensing

Raw datasets are intentionally not redistributed here. Obtain them from their original sources and follow their licensing and research-use requirements.
