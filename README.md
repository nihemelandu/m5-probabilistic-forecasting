# M5 Forecasting Competition — Python Benchmark Implementation

This repository contains a Python translation of the official R benchmark code for the
[M5 Forecasting Competition](https://github.com/Mcompetitions/M5-methods). The M5 competition
tasked participants with forecasting 28 days of unit sales across 30,490 product-store
combinations using Walmart data.

The original benchmarks were implemented in R. This project faithfully translates them to
Python, with improvements in code structure and efficiency where appropriate.

---

## Dataset

The M5 dataset consists of three files:

- **`sales_train_validation.csv`** — Historical daily unit sales for each product-store combination
- **`calendar.csv`** — Date information including events, holidays, and week identifiers
- **`sell_prices.csv`** — Weekly selling prices per product-store combination

Place all three files in a `data/` folder in the root of the project directory.

---

## Benchmark Models

The full suite of 24 point-forecast benchmarks spans four approaches:

### Summary by Category

| Category | Models | Count |
|----------|--------|-------|
| Naive | Simple, Seasonal | 2 |
| Statistical | SES, MA, Croston x3, TSB, ADIDA, iMAPA, ETS, ARIMA | 10 |
| Local ML | MLP_local, RF_local | 2 |
| Global ML | MLP_global, RF_global | 2 |
| Combinations | Various combinations of the above | 8 |
| **Total** | | **24** |

### Full Model List

| # | Model | Category | Approach |
|---|-------|----------|----------|
| 1 | Naive | Naive | Local |
| 2 | sNaive | Naive | Local |
| 3 | SES | Statistical | Local |
| 4 | MA | Statistical | Local |
| 5 | Croston | Intermittent Demand | Local |
| 6 | optCroston | Intermittent Demand | Local |
| 7 | SBA | Intermittent Demand | Local |
| 8 | TSB | Intermittent Demand | Local |
| 9 | ADIDA | Intermittent Demand | Local |
| 10 | iMAPA | Intermittent Demand | Local |
| 11 | ES_bu | Statistical | Local (Bottom-Up) |
| 12 | ARIMA_bu | Statistical | Local (Bottom-Up) |
| 13 | MLP_l | Machine Learning | Local |
| 14 | RF_l | Machine Learning | Local |
| 15 | MLP_g | Machine Learning | Global |
| 16 | RF_g | Machine Learning | Global |
| 17 | ES_td | Statistical | Top-Down |
| 18 | ESX | Statistical | Top-Down w/ External Variables |
| 19 | ARIMA_td | Statistical | Top-Down |
| 20 | ARIMAX | Statistical | Top-Down w/ External Variables |
| 21 | Com_b | Combination | Bottom-Up Average (ES_bu + ARIMA_bu) |
| 22 | Com_t | Combination | Top-Down Average (ES_td + ARIMA_td) |
| 23 | Com_tb | Combination | Mixed Average (ES_bu + ES_td) |
| 24 | Com_lg | Combination | Local-Global Average (MLP_l + MLP_g) |

### Forecasting Approaches Explained

| Approach | Description |
|----------|-------------|
| **Local** | A separate model is trained for each of the 30,490 series individually |
| **Global** | A single model is trained on all 30,490 series simultaneously |
| **Top-Down** | Forecast is made at the aggregate level then disaggregated using historical proportions |
| **Combination** | Simple average of two existing forecasts — no new model trained |

### External Variables (Top-Down Models)

The top-down models with external variables (ESX, ARIMAX) use:
- **SNAP benefits** — sum of SNAP indicators across CA, WI, and TX
- **Holiday indicator** — binary flag for days with a recorded event

---

## Project Structure
```
├── data/
│   ├── sales_train_validation.csv
│   ├── calendar.csv
│   └── sell_prices.csv
├── src/
│   ├── data_preparation.py      # Data loading and series preparation
│   ├── helper_functions.py      # intervals, demand, recompose, CreateSamples
│   ├── statistics.py            # Series statistics and demand classification
│   ├── local_benchmarks.py      # Local benchmark model implementations
│   ├── global_benchmarks.py     # Global ML model implementations
│   ├── topdown_benchmarks.py    # Top-down model implementations
│   └── benchmarks_pipeline.py  # Master forecasting pipeline
├── notebooks/
│   └── exploration.ipynb        # Data exploration and results analysis
├── requirements.txt
└── README.md
```

---

## Requirements
```
pandas
numpy
scipy
scikit-learn
statsmodels
joblib
psutil
```

Install dependencies with:
```bash
pip install -r requirements.txt
```

---

## Usage
```python
# Run the full benchmark pipeline
python src/benchmarks_pipeline.py
```

---

## References

- [M5 Competition GitHub](https://github.com/Mcompetitions/M5-methods)
- [M5 Competitors Guide](https://github.com/Mcompetitions/M5-methods/blob/master/M5-Competitors-Guide.pdf)
- Makridakis, S., Spiliotis, E., & Assimakopoulos, V. (2022). M5 accuracy competition:
  Results, findings, and conclusions. *International Journal of Forecasting*.
