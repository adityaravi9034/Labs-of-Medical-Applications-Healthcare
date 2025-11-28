# Medical Applications & Healthcare - Laboratory Work

**Course Instructor:** Prof. Arianna Dagliati
**Institution:** University of Pavia

---

## 📋 Overview

This repository contains a comprehensive laboratory sequence applying advanced statistical and machine learning methods to real-world clinical datasets. The work demonstrates hands-on expertise in missing data imputation, hierarchical modeling, survival analysis, and dimensionality reduction—core competencies for biomedical data science and health informatics research.

### Learning Objectives Achieved
- Implement rigorous missing data workflows with proper diagnostics and validation
- Build and interpret mixed-effects models for longitudinal and repeated-measures data
- Conduct complete survival analyses from exploratory to machine learning approaches
- Apply dimensionality reduction techniques to high-dimensional clinical data
- Create publication-quality visualizations for biomedical research

---

## 📂 Repository Structure

```
├── Lab1/           # R Programming Foundations
├── Lab2/           # Missing Data Imputation with MICE
├── Lab3/           # Advanced Missing Data & Dimensionality Reduction
├── Lab5/           # Mixed-Effects Models for Hierarchical Data
└── Lab6/           # Survival Analysis & Competing Risks
```

---

## 🔬 Laboratory Contents

### **Lab 1: R Programming Foundations** ([`Lab1/Intro.Rmd`](Lab1/Intro.Rmd))

**Purpose:** Establish foundational R programming skills for biomedical data analysis.

**Topics Covered:**
- **Core R Programming**
  - Data structures: vectors, matrices, lists, data frames
  - Control flow: loops, conditional statements, functions
  - Apply family functions for vectorized operations

- **Data Manipulation**
  - Subsetting and indexing strategies
  - Merging and reshaping datasets (reshape2: melt/dcast)
  - Handling missing values (na.omit, imputation basics)

- **Modern Data Wrangling (dplyr)**
  - Pipeline operations with `%>%`
  - Core verbs: filter, select, mutate, summarize, group_by
  - Data aggregation and transformation

- **Visualization**
  - Base R plots: scatter, histogram, boxplot
  - Advanced ggplot2 graphics (geoms, aesthetics, facets)
  - Bar charts with position adjustments (stack, dodge, fill)

- **Statistical Tables**
  - Descriptive statistics with table1 package
  - Creating "Table 1" for clinical research manuscripts

**Key Skills:** Data wrangling, exploratory data analysis, reproducible reporting with R Markdown

---

### **Lab 2: Missing Data Imputation with MICE** ([`Lab2/Mice_Practical.rmd`](Lab2/Mice_Practical.rmd))

**Purpose:** Master multiple imputation techniques for handling missing data in clinical research.

**Dataset:** NHANES (National Health and Nutrition Examination Survey)
- 25 observations with missing values in BMI, hypertension, and cholesterol
- Non-monotone missingness pattern

**Methods Implemented:**

1. **Diagnostic Phase**
   - Missing data pattern analysis with `md.pattern()`
   - Assessment of complete-case analysis limitations
   - Quantification of information loss (48% of cases excluded)

2. **Multiple Imputation via MICE**
   - **Predictive Mean Matching (PMM):** Hot-deck method preserving observed data distribution
   - **Bayesian Linear Regression (norm):** Proper posterior draws with parameter uncertainty
   - **Non-Bayesian Linear Regression (norm.nob):** Regression-based imputation
   - **Logistic Regression (logreg):** For binary variables (hypertension status)

3. **Convergence Diagnostics**
   - Trace plots for monitoring algorithm convergence
   - Iteration tuning (5, 10, 20, 40 iterations)
   - Visit sequence optimization for monotone patterns

4. **Validation & Quality Assessment**
   - Strip plots comparing observed vs. imputed distributions
   - Density plots for distributional similarity
   - RMSE comparison against ground truth

5. **Pooled Inference**
   - `with()` for fitting models on each imputed dataset
   - `pool()` for combining results via Rubin's rules
   - Fraction of missing information (FMI) and lambda statistics

**Key Results:**
- Multiple imputation recovered 12 additional cases (48% → 100% data utilization)
- Standard errors properly account for imputation uncertainty
- PMM preserves data features (e.g., clustering around cholesterol = 187)

**Key Skills:** Missing data diagnostics, MICE implementation, convergence validation, pooled statistical inference

---

### **Lab 3: Advanced Missing Data & Dimensionality Reduction** ([`Lab3/LAB 3 Missing Data Solution (1).Rmd`](Lab3/LAB%203%20Missing%20Data%20Solution%20(1).Rmd))

**Purpose:** Apply missing data methods to complex clinical datasets and visualize high-dimensional patient phenotypes.

**Dataset:** Mosaic Diabetes Cohort
- Baseline measurements from diabetes patients
- Variables: HbA1c, BMI, blood pressure, lipids, smoking status, age at T2D diagnosis
- Significant missingness requiring careful imputation strategy

**Workflow:**

1. **Data Preprocessing**
   - Filtering baseline observations (time = 0)
   - Excluding variables with >50% missingness (CreatCl, MicroAln)
   - Type conversion (factors for categorical variables)

2. **Missingness Analysis**
   - Pattern assessment revealing non-monotone structure
   - Complete-case analysis showing substantial data loss

3. **Regression Modeling for HbA1c Prediction**
   - Baseline model: `lm(hba1c ~ gender + smoke + age + t2d + bmi + sbp + colTot + trigl)`
   - Challenge: Standard errors biased due to listwise deletion

4. **Systematic Imputation Comparison**
   - **Strategy 1:** Default MICE methods (pmm for continuous, logreg for binary)
   - **Strategy 2:** Custom method selection
     - Continuous normally-distributed: `norm` (Bayesian)
     - Continuous skewed: `norm.nob` (non-Bayesian)
     - Categorical: `sample` (random sampling from observed)
     - Multi-class: `lda` (linear discriminant analysis)

5. **Hyperparameter Tuning**
   - Number of imputations: m = 5, 10
   - Iterations: maxit = 5, 10, 20
   - Visit sequence optimization

6. **RMSE-Based Method Selection**
   - Created amputed complete-case dataset as ground truth
   - Compared imputation strategies quantitatively
   - Selected best-performing method for final analysis

7. **Dimensionality Reduction on Imputed Data**

   **PCA (Principal Component Analysis):**
   - Linear projection maximizing variance
   - First two components explain X% of variance
   - Interpretable loadings for clinical variables

   **t-SNE (t-Distributed Stochastic Neighbor Embedding):**
   - Non-linear manifold learning
   - Perplexity tuning (perplexity = 50)
   - Preserves local neighborhood structure
   - Reveals patient clusters by HbA1c severity

   **UMAP (Uniform Manifold Approximation and Projection):**
   - Balance of local and global structure preservation
   - Hyperparameter optimization:
     - n_neighbors = 10 (local neighborhood size)
     - min_dist = 0.1 (minimum distance between points)
   - Faster than t-SNE with better global structure

**Key Results:**
- **40% more observations** retained vs. complete-case analysis
- Lower RMSE with proper imputation vs. listwise deletion
- Clear patient stratification visible in UMAP embedding colored by HbA1c
- Imputed values cluster appropriately in reduced dimensional space

**Key Skills:** Clinical data preprocessing, systematic method comparison, RMSE validation, manifold learning, high-dimensional visualization

---

### **Lab 5: Mixed-Effects Models for Hierarchical Data** ([`Lab5/Lesson5_MixedEffectsModels.Rmd`](Lab5/Lesson5_MixedEffectsModels.Rmd))

**Purpose:** Model correlated data structures arising from repeated measures and hierarchical sampling.

---

#### **Example 1: Politeness & Voice Pitch Study**

**Research Question:** Do people speak at higher pitch in polite vs. informal scenarios, accounting for gender and individual variation?

**Study Design:**
- Multiple subjects (male and female)
- Each subject responds to multiple scenarios (7 situations)
- Each scenario presented in polite and informal framing
- **Challenge:** Repeated measures violate independence assumption

**Modeling Progression:**

1. **Baseline Fixed-Effects Model (Incorrect)**
   ```r
   frequency ~ attitude + gender
   ```
   - Ignores within-subject correlation
   - Standard errors underestimated
   - p-values anti-conservative

2. **Random Intercepts Model**
   ```r
   lmer(frequency ~ attitude + gender + (1|subject) + (1|scenario))
   ```
   - Different baseline pitch for each subject (subjects F1–F3, M3–M7)
   - Different baseline pitch for each scenario
   - Accounts for non-independence
   - Variance decomposition:
     - Subject variance: σ²_subject
     - Scenario variance: σ²_scenario (much smaller)
     - Residual variance: σ²_ε

3. **Random Slopes Model** (Most flexible)
   ```r
   lmer(frequency ~ attitude + gender + (1+attitude|subject) + (1+attitude|scenario))
   ```
   - Allows politeness effect to vary by subject
   - Allows politeness effect to vary by scenario
   - Captures individual differences in politeness response

**Statistical Testing:**
- Likelihood Ratio Tests comparing nested models
- REML=FALSE for model comparison
- Significant effect of politeness: χ²(1) = X, p < 0.05

**Key Finding:** After adding gender as fixed effect, subject variance decreased substantially (gender variance previously confounded with subject variance)

---

#### **Example 2: Sleep Deprivation & Reaction Time**

**Research Question:** How does sleep deprivation affect reaction time, accounting for individual differences?

**Dataset:** sleepstudy
- 18 truck drivers restricted to 3 hours sleep/night
- Reaction time measured over 10 days
- **Challenge:** Multiple measurements per subject are correlated

**Analysis:**

1. **Naive Fixed-Effects Model**
   ```r
   lm(Reaction ~ Days)
   ```
   - Positive slope (reaction time increases with sleep deprivation)
   - High residual error: σ = X ms
   - Ignores subject-specific trajectories

2. **Random Slopes & Intercepts Model**
   ```r
   lmer(Reaction ~ Days + (Days|Subject))
   ```
   - Each subject has unique baseline reaction time (intercept)
   - Each subject has unique rate of degradation (slope)
   - Some subjects show increasing, neutral, or even decreasing trends

**Model Comparison:**
- Residual error reduction: σ_fixed = X ms → σ_mixed = Y ms
- AIC/BIC strongly favor mixed-effects model
- Likelihood ratio test: χ²(3) = X, p < 0.001

**Visualization:**
- Faceted plots showing individual trajectories
- Variation in both intercepts and slopes across subjects

**Key Skills:** Hierarchical model specification (lme4), random intercepts vs. slopes, likelihood ratio tests, variance partitioning, handling repeated measures

---

### **Lab 6: Survival Analysis & Competing Risks** ([`Lab6/SurvivalAnalysis.Rmd`](Lab6/SurvivalAnalysis.Rmd))

**Purpose:** Conduct comprehensive time-to-event analyses for clinical outcomes.

---

#### **Part 1: Kaplan-Meier Analysis**

**Dataset:** Lung Cancer (survival package)
- N = 228 patients
- Survival time in days
- Censoring status (recoded: 0=alive, 1=dead)
- Covariates: sex, age, performance status

**Methods:**

1. **Creating Survival Objects**
   ```r
   Surv(time, status)  # Encodes event times + censoring
   ```

2. **Non-Parametric Survival Estimation**
   ```r
   survfit(Surv(time, status) ~ 1)  # Overall survival
   survfit(Surv(time, status) ~ sex) # By sex
   ```

3. **Survival Probabilities at Time Points**
   - 1-year survival: S(365.25 days) with 95% CI
   - Median survival time

4. **Group Comparison**
   - Log-rank test: `survdiff(Surv(time, status) ~ sex)`
   - Null hypothesis: S_male(t) = S_female(t) for all t
   - Result: Significant difference (χ² = X, p < 0.05)

5. **Visualization**
   - Survival curves with 95% confidence intervals
   - Color-coded by group (sex)
   - Risk tables showing number at risk at each time point
   - Created with ggsurvfit for publication quality

---

#### **Part 2: Cox Proportional Hazards Regression**

**Purpose:** Multivariable survival analysis adjusting for covariates.

**Models:**

1. **Univariable Cox Model**
   ```r
   coxph(Surv(time, status) ~ sex)
   ```
   - Hazard ratio (HR) for sex with 95% CI
   - Interpretation: HR = X means male/female have X-times hazard

2. **Multivariable Cox Model**
   ```r
   coxph(Surv(time, status) ~ sex + age + ph.ecog + ph.karno + pat.karno + meal.cal + wt.loss)
   ```
   - Simultaneous adjustment for multiple predictors
   - Each HR is adjusted for all other variables
   - Identification of independent prognostic factors

3. **Visualization**
   - Forest plots with `ggforest()`
   - Hazard ratios with 95% CIs
   - Sorted by effect size

**Key Results:** [Your specific findings about which variables were significant predictors]

---

#### **Part 3: Competing Risks Analysis**

**Dataset:** Melanoma (MASS package)
- N = 205 melanoma patients
- Three possible outcomes:
  - 0 = Alive (censored)
  - 1 = Died from melanoma (primary event)
  - 2 = Died from other causes (competing event)
- Covariates: tumor thickness, ulceration, age, sex

**Challenge:** Standard survival analysis assumes single event type. Competing events require specialized methods.

**Methods:**

1. **Cumulative Incidence Functions (CIF)**
   ```r
   cuminc(Surv(time, status) ~ 1)  # Overall
   cuminc(Surv(time, status) ~ ulcer)  # By ulcer presence
   ```
   - Probability of melanoma death accounting for competing mortality
   - Separate curves for each event type
   - Sum of CIFs ≠ 1 (unlike Kaplan-Meier)

2. **Gray's Test for Group Comparison**
   - Null hypothesis: CIF_ulcer(t) = CIF_no_ulcer(t)
   - Chi-square test statistic
   - Result: Ulceration significantly associated with melanoma death

3. **Visualization**
   - Stacked CIF plots showing both competing events
   - 5-year cumulative incidence with 95% CI
   - Risk tables stratified by ulcer status

---

#### **Part 4: Machine Learning for Survival**

**Dataset:** Veteran's Administration Lung Cancer Trial

**Purpose:** Extend classical survival analysis with machine learning and explainability.

**Workflow:**

1. **Random Survival Forest**
   ```r
   model <- ranger(Surv(time, status) ~ ., data = veteran)
   ```
   - Ensemble of survival trees
   - Non-parametric, captures non-linear effects and interactions
   - No proportional hazards assumption required

2. **Model Evaluation**
   ```r
   explainer <- explain(model, data = veteran[, -c(3,4)], y = Surv(time, status))
   model_performance(explainer)
   ```
   - Concordance index (C-index): discrimination ability
   - Integrated Brier Score: calibration

3. **Feature Importance**
   ```r
   plot(model_parts(explainer))
   ```
   - Permutation-based importance
   - Which variables most affect predictions?
   - Ranking: [Your results, e.g., Karnofsky score, cell type, etc.]

4. **Individual Prediction Explanations (SurvSHAP)**
   ```r
   plot(predict_parts(explainer, veteran[1, ]))
   ```
   - SHAP values adapted for survival analysis
   - Contribution of each feature to predicted survival for specific patient
   - Positive/negative effects visualized over time
   - Enables clinical interpretation of ML predictions

**Key Advantage:** Combines predictive power of ML with interpretability required for clinical decision-making.

---

## 🛠️ Technical Stack

**Languages & Environments:**
- R 4.x with RStudio
- R Markdown for reproducible reporting

**Core Packages:**
- **Data Manipulation:** dplyr, tidyr, reshape2
- **Visualization:** ggplot2, ggsurvfit, survminer
- **Missing Data:** mice
- **Mixed Models:** lme4
- **Survival Analysis:** survival, survminer, tidycmprsk, condSURV
- **Machine Learning:** ranger, survex
- **Dimensionality Reduction:** Rtsne, umap
- **Tables:** table1, gtsummary, knitr

---

## 📊 Datasets Used

| Lab | Dataset | Source | Description | Key Variables |
|-----|---------|--------|-------------|---------------|
| 1 | iris, diamonds, starwars, airquality | R base/ggplot2 | Teaching datasets | Species, carat, cut, ozone |
| 2 | nhanes, nhanes2 | mice package | NHANES survey data | BMI, cholesterol, hypertension, age |
| 3 | Mosaic Diabetes | Course materials | Diabetes cohort (baseline) | HbA1c, BMI, lipids, blood pressure |
| 5 | politeness, sleepstudy | Course/lme4 | Psycholinguistics, cognitive | Voice pitch, reaction time |
| 6 | lung, Melanoma, veteran | survival/MASS | Cancer trials & registries | Survival time, tumor characteristics |

---

## 📈 Key Achievements

### **Statistical Rigor**
- Implemented proper missing data diagnostics before imputation
- Validated convergence of iterative algorithms (MICE, MCMC)
- Used RMSE and graphical diagnostics for method comparison
- Applied likelihood ratio tests for nested model comparison
- Computed proper pooled inference accounting for imputation uncertainty

### **Methodological Breadth**
- **Missing Data:** 6+ imputation methods (PMM, norm, norm.nob, logreg, LDA, sample)
- **Regression:** Linear, logistic, mixed-effects, Cox proportional hazards
- **Non-parametric:** Kaplan-Meier, cumulative incidence functions
- **Machine Learning:** Random survival forests with SHAP explanations
- **Dimensionality Reduction:** PCA, t-SNE, UMAP

### **Clinical Applications**
- Diabetes risk prediction from baseline clinical markers
- Cancer prognostic modeling with competing mortality
- Longitudinal cognitive performance under sleep deprivation
- Individual treatment effect heterogeneity via random slopes

### **Reproducible Research Practices**
- All analyses in R Markdown with integrated code/documentation
- Version control via Git/GitHub
- Publication-quality visualizations with ggplot2
- Structured data pipelines from raw data to final results

---

## 🎓 Learning Outcomes

By completing these laboratories, the following competencies were demonstrated:

1. **Data Science Fundamentals**
   - End-to-end data analysis pipelines
   - Exploratory data analysis and visualization
   - Statistical inference and hypothesis testing

2. **Advanced Statistical Methods**
   - Handling missing data with theoretical justification
   - Modeling correlated data structures
   - Time-to-event analysis with censoring and competing risks
   - Variance decomposition in hierarchical models

3. **Machine Learning for Healthcare**
   - Ensemble methods for survival prediction
   - Model evaluation metrics (C-index, Brier score)
   - Explainability techniques (SHAP) for clinical trust

4. **Research Skills**
   - Critical evaluation of methodological assumptions
   - Quantitative comparison of alternative approaches
   - Reproducible computational research
   - Communication of complex results through visualization

---

## 📚 References & Resources

### **Key Papers**
- van Buuren, S., & Groothuis-Oudshoorn, K. (2011). mice: Multivariate Imputation by Chained Equations in R. *Journal of Statistical Software*, 45(3), 1-67.
- Rubin, D. B. (1987). *Multiple Imputation for Nonresponse in Surveys*. Wiley.
- Bates, D., et al. (2015). Fitting Linear Mixed-Effects Models Using lme4. *Journal of Statistical Software*, 67(1), 1-48.
- Therneau, T. M., & Grambsch, P. M. (2000). *Modeling Survival Data*. Springer.
- McInnes, L., et al. (2018). UMAP: Uniform Manifold Approximation and Projection. *arXiv:1802.03426*.

### **Online Resources**
- mice vignettes by Gerko Vink and Stef van Buuren: https://www.gerkovink.com/miceVignettes/
- Winter, B. (2013). Linear models and linear mixed effects models in R: Tutorial: http://www.bodowinter.com/tutorial/bw_LME_tutorial2.pdf
- R for Data Science by Hadley Wickham: https://r4ds.had.co.nz/
- Survival Analysis in R (CRAN Task View): https://cran.r-project.org/web/views/Survival.html

---

## 🚀 How to Use This Repository

### **Prerequisites**
```r
# Install required packages
install.packages(c("mice", "lme4", "survival", "survminer", "ggsurvfit",
                   "gtsummary", "tidycmprsk", "ranger", "survex",
                   "Rtsne", "umap", "dplyr", "ggplot2", "reshape2",
                   "table1", "knitr"))
```

### **Running the Analyses**
1. Clone this repository
2. Open the desired `.Rmd` file in RStudio
3. Knit to HTML or run chunks interactively
4. Modify parameters and explore alternative approaches

### **Suggested Learning Path**
1. **Start with Lab1** to build R foundations
2. **Lab2** for missing data basics
3. **Lab3** to see real-world application
4. **Lab5** for hierarchical modeling
5. **Lab6** for survival analysis end-to-end

---

## 👤 Author

**Aditya Ravi**
[Your LinkedIn/Email if you want to include]

---

## 📜 License

This work is shared for educational purposes. If you use or adapt this material, please provide appropriate attribution.

---

## 🙏 Acknowledgments

Special thanks to **Prof. Arianna Dagliati** for exceptional instruction and carefully designed laboratory exercises that bridge statistical theory and clinical practice.

---

*Last Updated: November 2024*
