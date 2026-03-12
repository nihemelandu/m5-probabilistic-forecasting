# M5 Probabilistic Demand Forecasting

A professional implementation of probabilistic forecasting methods for retail demand, demonstrating applied data science best practices on the M5 Forecasting Competition dataset.

---

## 🎯 Project Overview

This project implements and evaluates **24 probabilistic forecasting benchmarks** across **42,840 time series** spanning 12 hierarchical aggregation levels of Walmart sales data. 

Unlike point forecasts that produce a single prediction, probabilistic forecasts quantify **uncertainty** through prediction intervals and quantiles — critical for inventory optimization, safety stock calculations, and risk-aware decision making.

**Key Outcomes:**
- End-to-end demand forecasting pipeline from data exploration to model evaluation
- Quantile forecasts (9 quantiles per horizon) for 28-day ahead predictions
- Comparative analysis of statistical, ML, and ensemble methods
- Scalable implementation processing 10M+ forecast combinations

---

## 📊 Business Context

**The Problem:** Retailers need forecasts that answer not just "what will we sell?" but "how confident are we?" to make optimal inventory decisions.

**The Solution:** Probabilistic forecasts provide:
- **Lower bounds** (q0.05) → minimum inventory to avoid stockouts
- **Median** (q0.50) → central tendency for planning
- **Upper bounds** (q0.95) → maximum inventory to avoid excess

**Impact:** Properly calibrated prediction intervals reduce both stockout costs and holding costs by enabling risk-based inventory policies.

---

## 🏗️ Project Structure
```
├── config/
│   └── config.yaml                  # All model and runtime parameters
├── data/
│   └── README.md                    # Data download instructions
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb    # Data patterns and insights
│   ├── 02_baseline_evaluation.ipynb     # Simple benchmark performance
│   ├── 03_advanced_models.ipynb         # Statistical and ML methods
│   └── 04_results_analysis.ipynb        # Model comparison and selection
├── src/
│   ├── data_loader.py               # Data loading and validation
│   ├── series_builder.py            # Hierarchical aggregation (12 levels)
│   ├── baseline_models.py           # Naive, sNaive, SES
│   ├── statistical_models.py        # ETS, ARIMA, Croston variants
│   ├── ml_models.py                 # Random Forest, ensemble methods
│   └── evaluation.py                # Scaled Pinball Loss (SPL) metric
├── tests/
│   └── test_*.py                    # Unit tests for all modules
├── results/
│   ├── forecasts/                   # Serialized predictions
│   └── metrics/                     # Performance summaries
├── run_pipeline.py                  # Single-command execution
└── README.md
```

---

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/yourusername/m5-probabilistic-forecasting.git
cd m5-probabilistic-forecasting
pip install -r requirements.txt
```

### Download Data
Follow instructions in `data/README.md` to download the M5 dataset from Kaggle.

### Run Pipeline
```bash
python run_pipeline.py --config config/config.yaml
```

### Explore Results
```bash
jupyter notebook notebooks/04_results_analysis.ipynb
```

---

## 📈 Methods Implemented

### Baseline Models (Simple, Fast)
- **Naive**: Last observed value
- **Seasonal Naive**: Last observed seasonal period
- **Simple Exponential Smoothing (SES)**: Weighted average with optimized smoothing

### Statistical Models (Industry Standard)
- **ETS**: Exponential smoothing with trend and seasonality
- **ARIMA**: Auto-regressive integrated moving average
- **Croston's Method**: Specialized for intermittent demand
- **TSB, ADIDA, iMAPA**: Advanced intermittent demand methods

### Machine Learning Models
- **Random Forest**: Ensemble of decision trees on lagged features
- **Global Models**: Single model across all series (vs local per-series)

### Ensemble Methods
- **Model Averaging**: Combine forecasts from multiple methods
- **Top-Down vs Bottom-Up**: Compare aggregation strategies

---

## 📊 Key Results

**Dataset Scale:**
- 30,490 SKU-store combinations (bottom level)
- 42,840 total time series (across 12 hierarchy levels)
- 1,969 days of historical data
- 10.7M quantile forecasts generated

**Best Performing Models** *(metrics in notebooks)*:
1. ETS with seasonality
2. ARIMA with external regressors
3. Ensemble (ETS + ARIMA)

**Key Insights:**
- Simple baselines (Naive, sNaive) are hard to beat for short horizons
- Intermittent demand requires specialized methods (Croston's)
- Global ML models outperform local models at higher aggregation levels

---

## 🛠️ Technical Highlights

**Engineering Best Practices:**
- Configuration-driven (no hardcoded parameters)
- Comprehensive logging (reproducibility)
- Unit tested (critical functions validated)
- Modular design (easy to extend with new models)
- Efficient parallelization (joblib for CPU-bound tasks)

**Data Science Rigor:**
- Walk-forward validation (realistic backtest)
- Proper train/test splits (no data leakage)
- Coverage analysis (are 90% intervals actually 90%?)
- Scaled Pinball Loss (official M5 uncertainty metric)

---

## 📚 Learning Outcomes

This project demonstrates proficiency in:

**Statistical Forecasting:**
- Time series decomposition (trend, seasonality, remainder)
- Prediction interval construction (normal approximation)
- Intermittent demand modeling (Croston's, SBA, TSB)

**Machine Learning:**
- Feature engineering for time series (lags, rolling statistics)
- Global vs local model trade-offs
- Hyperparameter tuning for tree-based models

**Applied Data Science:**
- Exploratory data analysis for time series
- Model selection via backtesting
- Communicating uncertainty to stakeholders
- Production-ready code structure

---

## 📖 References

- [M5 Forecasting Competition](https://www.kaggle.com/c/m5-forecasting-accuracy)
- Makridakis et al. (2022). "M5 accuracy competition: Results, findings, and conclusions"
- Hyndman & Athanasopoulos. [Forecasting: Principles and Practice](https://otexts.com/fpp3/)

---

## 👤 Author

**Ngozi Ihemelandu**  
Applied Data Scientist  

---

## 📝 License

MIT License - see LICENSE file for details

---

## 🙏 Acknowledgments

- M5 Competition organizers for the dataset
- Original R benchmark implementations by Spiliotis et al.
