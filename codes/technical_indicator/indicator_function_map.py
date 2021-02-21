import codes.technical_indicator.indicator_helper as ih

indicator_function_map = {
    'y_period': ih.y_period,
    'rsi': ih.rsi,
    'macd': ih.macd,
    'mfi': ih.mfi,
    'ma': ih.ma,
    'sma': ih.sma,
    'slope': ih.slope,
    'border': ih.border,
    'compare': ih.compare,
    'shift': ih.shift,
    'step': ih.step,
    'div': ih.divergence,
    'hcl': ih.hcl,
    'range': ih.range_function,
    'diff': ih.diff_func,
    'momentum': ih.momentum,
    'bbands': ih.bbands,
    'bbands_lower': ih.bbands_lower,
    'bbands_upper': ih.bbands_upper,
    'stoch': ih.stoch,
    'sar': ih.sar,
    'bband_ma': ih.bband_ma,
    'sar_ma': ih.sar_ma,
    'ma_ma': ih.ma_ma,
    'mfi_ma': ih.mfi_ma,
    'stoch_ma': ih.stoch_ma,
    'rsi_ma': ih.rsi_ma,
    'doji': ih.doji,
    'engulfing': ih.engulfing,
    'abandoned_baby': ih.abandoned_baby,
    'gravestone_doji': ih.gravestone_doji,
    'hammer': ih.hammer,
    'hanging_man': ih.hanging_man,
    'inverted_hammer': ih.inverted_hammer,
    'logistic': ih.logistic,
    'distance_max_local': ih.distance_max_local,
    'distance_min_local': ih.distance_min_local,
    'adx': ih.adx,
    'candle_type': ih.candle_type,
    'index_minima': ih.index_minima,
    'index_maxima': ih.index_maxima,
}


def run_indicator_function(func_name, params):
    return indicator_function_map[func_name](**params)
