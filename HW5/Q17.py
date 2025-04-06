import numpy as np
from time import time

# Set random seed for reproducibility
np.random.seed(int(time()) )

# Constants
N = 100
mu_b, sigma_b = 0, 1
mu_m1, sigma_m = 10, 0.5      # For parts (a) and (c)
mu_m2 = 0.8                   # For part (b)

# Generate benign and malicious sequences
benign = np.random.normal(mu_b, sigma_b, N)
malicious1 = np.random.normal(mu_m1, sigma_m, N)
malicious2 = np.random.normal(mu_m2, sigma_m, N)

# Labels: 0 for benign, 1 for malicious
true_labels = np.array([0]*N + [1]*N)

# Combine sequences
aggregate1 = np.concatenate([benign, malicious1])
aggregate2 = np.concatenate([benign, malicious2])

def classify_simple(x, mu_b, mu_m):
    return np.where(abs(x - mu_b) < abs(x - mu_m), 0, 1)

pred_labels_a = classify_simple(aggregate1, mu_b, mu_m1)

# Evaluation function
def evaluate(true, pred):
    TP = np.sum((true == 1) & (pred == 1))
    FP = np.sum((true == 0) & (pred == 1))
    TN = np.sum((true == 0) & (pred == 0))
    FN = np.sum((true == 1) & (pred == 0))
    return TP, FP, TN, FN

tp_a, fp_a, tn_a, fn_a = evaluate(true_labels, pred_labels_a)

print("a) μ_m = 10:")
print(f"TP = {tp_a}, FP = {fp_a}, TN = {tn_a}, FN = {fn_a}")

pred_labels_b = classify_simple(aggregate2, mu_b, mu_m2)
tp_b, fp_b, tn_b, fn_b = evaluate(true_labels, pred_labels_b)

print("\nb) μ_m = 0.8:")
print(f"TP = {tp_b}, FP = {fp_b}, TN = {tn_b}, FN = {fn_b}")

def classify_anomaly(x, mu_b, sigma_b, threshold=2):
    return np.where(abs(x - mu_b) >= threshold * sigma_b, 1, 0)

pred_labels_c = classify_anomaly(aggregate1, mu_b, sigma_b)
tp_c, fp_c, tn_c, fn_c = evaluate(true_labels, pred_labels_c)

print("\nc) Anomaly detection with μ_m = 10:")
print(f"TP = {tp_c}, FP = {fp_c}, TN = {tn_c}, FN = {fn_c}")
