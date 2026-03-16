# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:23:05 2026

@author: ngozi
"""
import logging
logger = logging.getLogger(__name__)

def _build_level_1(sales, day_cols):
    """
    Level 1: Total aggregation across all products and stores.
    
    Business Context:
    -----------------
    CEO-level view: "What are total company sales?"
    Used for: Strategic planning, investor presentations, budget forecasting
    
    Returns
    -------
    list
        Single-element list with total aggregation
    """
    return [{
        'x': sales[day_cols].sum(axis=0).values,
        'Agg_Level_1': 'Total',
        'Agg_Level_2': 'X',
        'Hlevel': 1
    }]

def _build_level_2(sales, day_cols):
    """
    Level 2: By State (CA, TX, WI).
    
    Business Context:
    -----------------
    Regional VP view: "What are my state's total sales?"
    Used for: Regional budgeting, distribution planning, state-specific marketing
    
    Returns
    -------
    list
        3 dictionaries (one per state)
    """
    series_list = []
    for state in sales['state_id'].unique():
        sales_train = sales[sales['state_id'] == state][day_cols].sum(axis=0).values
        series_list.append({
            'x': sales_train,
            'Agg_Level_1': state,
            'Agg_Level_2': 'X',
            'Hlevel': 2
        })
    return series_list

def _build_level_3(sales, day_cols):
    """
    Level 3: By Store (10 stores across 3 states).
    
    Business Context:
    -----------------
    Store Manager view: "What are my store's total sales?"
    Used for: Staffing schedules, shelf space planning, local promotions
    
    Returns
    -------
    list
        10 dictionaries (one per store)
    """
    series_list = []
    for store in sales['store_id'].unique():
        sales_train = sales[sales['store_id'] == store][day_cols].sum(axis=0).values
        series_list.append({
            'x': sales_train, 
            'Agg_Level_1': store,
            'Agg_Level_2': 'X',
            'Hlevel': 3
        })
    return series_list

def _build_level_4(sales, day_cols):
    """
    Level 4: By Category (HOBBIES, FOODS, HOUSEHOLD).
    
    Business Context:
    -----------------
    Category Buyer view: "What are total HOBBIES sales across all stores?"
    Used for: Bulk purchasing, category performance analysis, product mix strategy
    
    Returns
    -------
    list
        3 dictionaries (one per category)
    """
    series_list = []
    for category in sales['cat_id'].unique():
        sales_train = sales[sales['cat_id'] == category][day_cols].sum(axis=0).values
        series_list.append({
            'x': sales_train,
            'Agg_Level_1': category,
            'Agg_Level_2': 'X',
            'Hlevel': 4
        })
    return series_list

def _build_level_5(sales, day_cols):
    """
    Level 5: By Department (7 departments across 3 categories).
    
    Business Context:
    -----------------
    Department Manager view: "What are total HOBBIES_1 sales across all stores?"
    Used for: Department-level purchasing, promotional planning, trend analysis
    
    Returns
    -------
    list
        7 dictionaries (one per department)
    """
    series_list = []
    for dept in sales['dept_id'].unique():
        sales_train = sales[sales['dept_id'] == dept][day_cols].sum(axis=0).values
        series_list.append({
            'x': sales_train,
            'Agg_Level_1': dept,
            'Agg_Level_2': 'X',
            'Hlevel': 5
        })
    return series_list

def _build_level_6(sales, day_cols):
    """
    Level 6: State × Category (9 combinations).
    
    Business Context:
    -----------------
    Regional Category Manager view: "How are HOBBIES selling in CA?"
    Used for: Regional product strategy, targeted marketing, regional supplier contracts
    
    Note: This is the first TWO-DIMENSIONAL level
    - Agg_Level_1: State (CA, TX, WI)
    - Agg_Level_2: Category (HOBBIES, FOODS, HOUSEHOLD) — NOT a placeholder
    
    Returns
    -------
    list
        9 dictionaries (3 states × 3 categories)
    """
    series_list = []
    for state in sales['state_id'].unique():
        for category in sales['cat_id'].unique():
            sales_train = sales[
                (sales['state_id'] == state) &
                (sales['cat_id'] == category)
            ][day_cols].sum(axis=0).values
            series_list.append({
                'x': sales_train,
                'Agg_Level_1': state,
                'Agg_Level_2': category,  # ← Actual value, not 'X'
                'Hlevel': 6
            })
    return series_list

def _build_level_7(sales, day_cols):
    """Level 7: State × Department (21 series)."""
    series_list = []
    for state in sales['state_id'].unique():
        for dept in sales['dept_id'].unique():
            sales_train = sales[
                (sales['state_id'] == state) &
                (sales['dept_id'] == dept)
            ][day_cols].sum(axis=0).values
            series_list.append({
                'x': sales_train,
                'Agg_Level_1': state,
                'Agg_Level_2': dept,
                'Hlevel': 7
            })
    return series_list


def _build_level_8(sales, day_cols):
    """Level 8: Store × Category (30 series)."""
    series_list = []
    for store in sales['store_id'].unique():
        for category in sales['cat_id'].unique():
            sales_train = sales[
                (sales['store_id'] == store) &
                (sales['cat_id'] == category)
            ][day_cols].sum(axis=0).values
            series_list.append({
                'x': sales_train,
                'Agg_Level_1': store,
                'Agg_Level_2': category,
                'Hlevel': 8
            })
    return series_list


def _build_level_9(sales, day_cols):
    """Level 9: Store × Department (70 series)."""
    series_list = []
    for store in sales['store_id'].unique():
        for dept in sales['dept_id'].unique():
            sales_train = sales[
                (sales['store_id'] == store) &
                (sales['dept_id'] == dept)
            ][day_cols].sum(axis=0).values
            series_list.append({
                'x': sales_train,
                'Agg_Level_1': store,
                'Agg_Level_2': dept,
                'Hlevel': 9
            })
    return series_list


def _build_level_10(sales, day_cols):
    """
    Level 10: By Item across all stores (3049 series).
    
    Business Context:
    -----------------
    Product Manager view: "How is HOBBIES_1_001 selling company-wide?"
    Used for: SKU-level lifecycle management, discontinuation decisions
    """
    series_list = []
    for item in sales['item_id'].unique():
        sales_train = sales[sales['item_id'] == item][day_cols].sum(axis=0).values
        series_list.append({
            'x': sales_train,
            'Agg_Level_1': item,
            'Agg_Level_2': 'X',
            'Hlevel': 10
        })
    return series_list


def _build_level_11(sales, day_cols):
    """Level 11: State × Item (9147 series)."""
    series_list = []
    for state in sales['state_id'].unique():
        for item in sales['item_id'].unique():
            sales_train = sales[
                (sales['state_id'] == state) &
                (sales['item_id'] == item)
            ][day_cols].sum(axis=0).values
            series_list.append({
                'x': sales_train,
                'Agg_Level_1': state,
                'Agg_Level_2': item,
                'Hlevel': 11
            })
    return series_list


def _build_level_12(sales, day_cols):
    """
    Level 12: Store × Item — Bottom level (30490 series).
    
    Business Context:
    -----------------
    Operational execution: "How many units of HOBBIES_1_001 should CA_1 stock?"
    This is the raw data — no aggregation needed.
    Used for: Daily stocking decisions, shelf allocation, individual SKU tracking
    
    Note: This is where intermittent demand is most common.
    """
    series_list = []
    for idx in range(len(sales)):
        row = sales.iloc[idx]
        sales_train = row[day_cols].astype(float).values
        series_list.append({
            'x': sales_train,
            'Agg_Level_1': row['item_id'],
            'Agg_Level_2': row['store_id'],
            'Hlevel': 12
        })
    return series_list

def build_all_levels(sales, day_cols):
    """..."""
    logger.info("Building time series for all 12 hierarchy levels...")
    time_series_b = []
    
    # Levels 1-4 (already added)
    time_series_b.extend(_build_level_1(sales, day_cols))
    logger.info(f"  Level 1 complete: {len(time_series_b)} series")
    
    level_2_start = len(time_series_b)
    time_series_b.extend(_build_level_2(sales, day_cols))
    logger.info(f"  Level 2 complete: {len(time_series_b) - level_2_start} series")
    
    level_3_start = len(time_series_b)
    time_series_b.extend(_build_level_3(sales, day_cols))
    logger.info(f"  Level 3 complete: {len(time_series_b) - level_3_start} series")
    
    level_4_start = len(time_series_b)
    time_series_b.extend(_build_level_4(sales, day_cols))
    logger.info(f"  Level 4 complete: {len(time_series_b) - level_4_start} series")
    
    # Level 5: By Department (7 series)
    level_5_start = len(time_series_b)
    time_series_b.extend(_build_level_5(sales, day_cols))
    logger.info(f"  Level 5 complete: {len(time_series_b) - level_5_start} series")
    
    # Level 6: State × Category (9 series)
    level_6_start = len(time_series_b)
    time_series_b.extend(_build_level_6(sales, day_cols))
    logger.info(f"  Level 6 complete: {len(time_series_b) - level_6_start} series")
    
    # Level 7: State × Department (21 series)
    level_7_start = len(time_series_b)
    time_series_b.extend(_build_level_7(sales, day_cols))
    logger.info(f"  Level 7 complete: {len(time_series_b) - level_7_start} series")
    
    # Level 8: Store × Category (30 series)
    level_8_start = len(time_series_b)
    time_series_b.extend(_build_level_8(sales, day_cols))
    logger.info(f"  Level 8 complete: {len(time_series_b) - level_8_start} series")
    
    # Level 9: Store × Department (70 series)
    level_9_start = len(time_series_b)
    time_series_b.extend(_build_level_9(sales, day_cols))
    logger.info(f"  Level 9 complete: {len(time_series_b) - level_9_start} series")
    
    # Level 10: By Item (3049 series)
    level_10_start = len(time_series_b)
    time_series_b.extend(_build_level_10(sales, day_cols))
    logger.info(f"  Level 10 complete: {len(time_series_b) - level_10_start} series")
    
    # Level 11: State × Item (9147 series)
    level_11_start = len(time_series_b)
    time_series_b.extend(_build_level_11(sales, day_cols))
    logger.info(f"  Level 11 complete: {len(time_series_b) - level_11_start} series")
    
    # Level 12: Store × Item (30490 series - bottom level)
    level_12_start = len(time_series_b)
    time_series_b.extend(_build_level_12(sales, day_cols))
    logger.info(f"  Level 12 complete: {len(time_series_b) - level_12_start} series")
    
    logger.info(f"✅ Total series built: {len(time_series_b)}")
    return time_series_b