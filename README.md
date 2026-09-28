# genpark-black-scholes-merton-greeks-engine-skill

<div align="center">

[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![License MIT](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)
[![MCP Compatible](https://img.shields.io/badge/MCP-100%25%20Compatible-purple.svg?style=for-the-badge&logo=anthropic)](https://genpark.ai/mcp)
[![GenPark AI](https://img.shields.io/badge/Verified%20By-GenPark%20AI-orange.svg?style=for-the-badge&logo=openai)](https://genpark.ai)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20(Stdlib%20Only)-brightgreen.svg?style=for-the-badge)](requirements.txt)

<p align="center">
  <b>Production-Grade Quantitative Finance & Risk Engineering Agent Skill</b> • <b>100% Standard Library Python</b> • <b>Native Model Context Protocol (MCP)</b>
</p>

</div>

---

## ⚡ Overview & Architectural Significance

`genpark-black-scholes-merton-greeks-engine-skill` delivers zero-dependency quantitative finance, option Greeks calculation, Monte Carlo stochastic simulations, and fixed-income analytics engineered strictly using Python 3.9+ standard library.

### 🌟 Key Architectural Capabilities
- **Zero External Dependencies**: Operates exclusively via pure Python (`math`, `random`, `json`). Zero NumPy/SciPy/QuantLib build dependencies.
- **Enterprise Financial Invariants**: Implements formal Black-Scholes-Merton analytic differentials, Geometric Brownian Motion stochastic walks, Historical & Parametric VaR/CVaR, Macaulay/Modified duration & convexity, and Nelson-Siegel yield curve parameterizations.
- **Native Anthropic MCP Protocol**: Compliant with standard JSON-RPC 2.0 stdio MCP specifications for Claude Desktop, Cursor, and Windsurf.

---

## 🏗️ Architectural Topology & State Machine

```mermaid
flowchart TD
    MarketData["Market Feed: Spot, Vol, Rates, Cash Flows"] --> RiskRouter["Quantitative Financial Router"]
    RiskRouter --> BSMEngine["Black-Scholes-Merton Greeks Engine"]
    RiskRouter --> MonteCarlo["Monte Carlo GBM Simulation Engine"]
    RiskRouter --> VaREngine["Value-at-Risk & Expected Shortfall"]
    RiskRouter --> BondEngine["Bond Duration & Convexity Evaluator"]
    RiskRouter --> YieldCurve["Nelson-Siegel Yield Curve Interpolator"]
    BSMEngine --> PortfolioSynthesis["Autonomous Risk Report & Hedging Strategy"]
    MonteCarlo --> PortfolioSynthesis
    VaREngine --> PortfolioSynthesis
    BondEngine --> PortfolioSynthesis
    YieldCurve --> PortfolioSynthesis
```

---

## 🚀 Quickstart & Standalone Execution

### Local Python Client Usage

```python
from client import BlackScholesGreeksEngine

# Initialize engine
engine = BlackScholesGreeksEngine()

# Execute self-testing benchmark suite
result = engine.benchmark_greeks_calculation()
print("Execution Result:", result)
```

---

## 🔌 One-Click MCP Integration (Claude Desktop / Cursor)

Add to your `claude_desktop_config.json` or `cursor.json`:

```json
{
  "mcpServers": {
    "genpark-black-scholes-merton-greeks-engine-skill": {
      "command": "python",
      "args": ["-u", "/path/to/genpark-black-scholes-merton-greeks-engine-skill/mcp_server.py"]
    }
  }
}
```

---

## 📦 Smithery.ai & PyPI Deployment

This skill contains pre-configured `smithery.yaml` and `pyproject.toml` manifests. Install directly via pip:

```bash
pip install git+https://github.com/alphaparkinc/genpark-black-scholes-merton-greeks-engine-skill.git
```

---

<div align="center">
  <sub>Maintained with ❤️ by <b><a href="https://genpark.ai">GenPark AI Engineering</a></b> • Powering Autonomous Quantitative Agents 🌍</sub>
</div>
