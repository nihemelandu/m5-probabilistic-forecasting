---

## 2025-02-17: Hierarchical Series Builder Complete

### Implementation: `src/series_builder.py`

**Business Problem Solved:**  
Created 42,840 time series from raw sales data to enable multi-level forecasting aligned with organizational decision-making hierarchy.

**Technical Achievement:**  
- Built 12 hierarchy levels spanning corporate to operational decisions
- Single-dimension levels (1-5, 10): Geography OR product aggregation
- Two-dimension levels (6-9, 11-12): Geography AND product combinations

**Series Count Breakdown:**
| Level | Description | Series | Business Stakeholder |
|-------|-------------|--------|---------------------|
| 1 | Total | 1 | CEO / Executives |
| 2 | State | 3 | Regional VPs |
| 3 | Store | 10 | Store Managers |
| 4 | Category | 3 | Category Buyers |
| 5 | Department | 7 | Department Managers |
| 6 | State × Category | 9 | Regional Category Managers |
| 7 | State × Dept | 21 | Regional Dept Managers |
| 8 | Store × Category | 30 | Store Category Leads |
| 9 | Store × Dept | 70 | Store Dept Leads |
| 10 | Item | 3,049 | Product Managers |
| 11 | State × Item | 9,147 | Regional SKU Managers |
| 12 | Store × Item | 30,490 | Operational Execution |
| **Total** | | **42,840** | |

**Key Insights:**
1. **Aggregation reduces uncertainty**: Level 1 (total) is smooth; Level 12 (item×store) contains both smooth and intermittent demand
2. **Portfolio effect**: Volatility of individual SKUs averages out at higher levels
3. **Model selection must adapt**: Croston's needed for intermittent bottom-level series; ARIMA works well for smooth aggregates

**Code Quality:**
- Modular design (each level has dedicated function)
- Comprehensive logging (progress tracking)
- Business context documented in docstrings
- Generic naming (`Agg_Level_1`, `Agg_Level_2`) works across all levels
