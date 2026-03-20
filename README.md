# Riemann Hypothesis Research Project

## 研究目标
探索黎曼猜想的证明

## 研究路径
素数定理 → ζ函数 → ξ函数 → 零点分布 → 黎曼猜想

## 项目结构
```
riemann-research/
├── README.md
├── requirements.txt
├── src/
│   ├── core.py      # 核心函数
│   └── phase2.py    # 高级分析
├── notebooks/
├── notes/
└── data/
```

## 核心成果

### 1. 验证结果
- ✅ 素数计数函数 π(x)
- ✅ 对数积分 Li(x)  
- ✅ 素数定理验证
- ✅ ζ函数实现
- ✅ ξ函数实现
- ✅ Hardy Z-函数
- ✅ 临界线零点验证
- ✅ Li系数计算
- ✅ 显式公式验证

### 2. 已验证的零点
前5个零点全部在临界线上：
- t₁ = 14.134725: |ζ| = 1.12e-7 ✓
- t₂ = 21.022040: |ζ| = 4.11e-7 ✓
- t₃ = 25.010858: |ζ| = 5.76e-7 ✓
- t₄ = 30.424876: |ζ| = 1.64e-7 ✓
- t₅ = 32.935062: |ζ| = 5.70e-7 ✓

### 3. 关键发现

#### Xi函数对称性
Xi(s) = Xi(1-s) - 完美对称性已验证！

#### 显式公式
ψ(x) = x - Σ x^ρ/ρ - log(2) - ...
ζ函数零点直接控制素数分布！

#### Li准则
λ_n ≥ 0 ⟺ RH
所有已知 λ_n 均为正数！

## 证明策略

1. **经典分析**: Hadamard乘积 + 全局性质
2. **谱理论**: 寻找 Hilbert-Pólya 算子
3. **Li准则**: 证明所有 λ_n ≥ 0
4. **随机矩阵**: GUE统计分析
5. **算术几何**: p进方法 + Galois表示

## 运行
```bash
pip install numpy sympy mpmath matplotlib
python3 src/core.py
python3 src/phase2.py
```

## 结论
黎曼猜想仍需新数学工具来证明！
