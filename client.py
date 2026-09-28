import math
from typing import Dict, Any

class BlackScholesGreeksEngine:
    @staticmethod
    def _cnd(d: float) -> float:
        return 0.5 * (1.0 + math.erf(d / math.sqrt(2.0)))

    @staticmethod
    def _pdf(d: float) -> float:
        return (1.0 / math.sqrt(2.0 * math.pi)) * math.exp(-0.5 * d * d)

    @classmethod
    def price_and_greeks(cls, S: float, K: float, T: float, r: float, sigma: float, option_type: str = "CALL") -> Dict[str, Any]:
        if T <= 0 or sigma <= 0:
            return {"error": "T and sigma must be positive"}
        d1 = (math.log(S / K) + (r + 0.5 * sigma * sigma) * T) / (sigma * math.sqrt(T))
        d2 = d1 - sigma * math.sqrt(T)
        cnd_d1 = cls._cnd(d1)
        cnd_d2 = cls._cnd(d2)
        pdf_d1 = cls._pdf(d1)
        gamma = pdf_d1 / (S * sigma * math.sqrt(T))
        vega = S * math.sqrt(T) * pdf_d1
        if option_type.upper() == "CALL":
            price = S * cnd_d1 - K * math.exp(-r * T) * cnd_d2
            delta = cnd_d1
            theta = -(S * pdf_d1 * sigma) / (2.0 * math.sqrt(T)) - r * K * math.exp(-r * T) * cnd_d2
            rho = K * T * math.exp(-r * T) * cnd_d2
        else:
            price = K * math.exp(-r * T) * cls._cnd(-d2) - S * cls._cnd(-d1)
            delta = cnd_d1 - 1.0
            theta = -(S * pdf_d1 * sigma) / (2.0 * math.sqrt(T)) + r * K * math.exp(-r * T) * cls._cnd(-d2)
            rho = -K * T * math.exp(-r * T) * cls._cnd(-d2)
        return {
            "option_type": option_type.upper(), "price": round(price, 4),
            "delta": round(delta, 4), "gamma": round(gamma, 6),
            "vega_per_pct": round(vega / 100.0, 4), "theta_daily": round(theta / 365.0, 4),
            "rho_per_pct": round(rho / 100.0, 4)
        }

    def benchmark_greeks_calculation(self) -> Dict[str, Any]:
        return self.price_and_greeks(100.0, 100.0, 1.0, 0.05, 0.20, "CALL")
