"""
Riemann Hypothesis Research - Core Functions
黎曼猜想研究 - 核心函数
"""

import numpy as np
from sympy import isprime, primerange

try:
    from mpmath import mp, zeta as mp_zeta, li as mp_li
    mp.dps = 50
    HAS_MPMATH = True
except ImportError:
    HAS_MPMATH = False

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


# ============================================================
# Part 1: Prime Counting Function π(x)
# ============================================================

def prime_count(x: int) -> int:
    """Count primes up to x"""
    if x < 2:
        return 0
    return len(list(primerange(2, x + 1)))


# ============================================================
# Part 2: Logarithmic Integral Li(x)
# ============================================================

def log_integral(x: float) -> float:
    """Logarithmic integral Li(x)"""
    if x <= 2:
        return 0
    if HAS_MPMATH:
        return float(mp_li(x))
    return 0


# ============================================================
# Part 3: Prime Number Theorem Verification
# ============================================================

def verify_prime_number_theorem(x_values):
    """Verify PNT: π(x) ~ Li(x) ~ x/ln(x)"""
    import math
    results = []
    for x in x_values:
        pi_x = prime_count(x)
        x_ln = x / math.log(x) if x > 1 else 0
        li_x = log_integral(x)
        
        results.append({
            'x': x,
            'pi_x': pi_x,
            'x_ln_x': x_ln,
            'Li_x': li_x
        })
    return results


# ============================================================
# Part 4: Riemann Zeta Function
# ============================================================

def riemann_zeta(s):
    """Riemann Zeta Function ζ(s)"""
    if HAS_MPMATH:
        return mp_zeta(s)
    raise ImportError("mpmath required")


def find_zeta_zeros(t_start, t_end, num_points=1000):
    """Find zeros of ζ(1/2 + it)"""
    if not HAS_MPMATH:
        return []
    
    zeros = []
    t_values = np.linspace(t_start, t_end, num_points)
    
    for t in t_values:
        s = 0.5 + 1j * t
        zeta_val = abs(complex(mp_zeta(s)))
        if zeta_val < 0.01:
            zeros.append(float(t))
    
    return zeros


# ============================================================
# Part 5: Research Runner
# ============================================================

def run_research():
    """Run initial research"""
    print("=" * 60)
    print("RIEMANN HYPOTHESIS RESEARCH")
    print("=" * 60)
    
    # 1. Verify PNT
    print("\n1. Prime Number Theorem Verification")
    print("-" * 40)
    test_values = [10, 100, 1000, 10000]
    results = verify_prime_number_theorem(test_values)
    
    for r in results:
        print(f"x = {r['x']:>6}: π(x) = {r['pi_x']:>6}")
    
    # 2. Zeta zeros
    print("\n2. Finding Zeta Zeros")
    print("-" * 40)
    if HAS_MPMATH:
        print("Known zeros: t ≈ 14.13, 21.02, 25.01, 30.42, 32.93...")
        zeros = find_zeta_zeros(10, 40, 3000)
        print(f"Found {len(zeros)} potential zeros")
    else:
        print("Install mpmath: pip install mpmath")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    run_research()
