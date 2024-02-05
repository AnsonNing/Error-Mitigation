import numpy as np
from scipy import interpolate, optimize
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor

def xgboost_extrapolation(values, x):
    target_x = 0
    x_vals = np.arange(1, len(values) + 1)
    x_vals_reshaped = x_vals.reshape(-1, 1)
    values_reshaped = np.array(values).reshape(-1, 1)
    target_x_reshaped = np.array([[target_x]])

    xgb_model = XGBRegressor(objective='reg:squarederror', n_estimators=1000, max_depth=10)
    xgb_model.fit(x_vals_reshaped, values_reshaped.ravel())

    return xgb_model.predict(target_x_reshaped)[0]

def mlp_extrapolation(values, x):
    target_x = 0
    x_vals = np.arange(1, len(values) + 1)
    x_vals_reshaped = x_vals.reshape(-1, 1)
    values_reshaped = np.array(values).reshape(-1, 1)
    target_x_reshaped = np.array([[target_x]])
    
    mlp_model = MLPRegressor(hidden_layer_sizes=(800, 800), max_iter=800000)
    mlp_model.fit(x_vals_reshaped, values_reshaped)
    
    return mlp_model.predict(target_x_reshaped)[0]

def linear_extrapolation(values,x):
    f = interpolate.interp1d(x, values, fill_value="extrapolate")
    return f(0)

def exponential_extrapolation(values,x):
    def exp_func(x, a, b):
        return a * np.exp(b * x)
    
    params, _ = optimize.curve_fit(exp_func, x, values)
    return exp_func(0, *params)

def richardson_extrapolation(values,x):
    f_h = interpolate.interp1d(x, values, fill_value="extrapolate")(1)
    f_2h = interpolate.interp1d(x, values, fill_value="extrapolate")(2)
    return (4 * f_h - f_2h) / 3

def cubic_spline_extrapolation(values,x):
    f = interpolate.CubicSpline(x, values, extrapolate=True)
    return f(0)

def polynomial_extrapolation(values,x):
    p = np.polyfit(x, values, deg=3)  # 使用5次多項式作為示例
    return np.polyval(p, 0)
