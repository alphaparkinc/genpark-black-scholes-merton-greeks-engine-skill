from client import BlackScholesGreeksEngine

def run_example():
    print("=== GenPark Black-Scholes Greeks Engine Example ===")
    engine = BlackScholesGreeksEngine()
    print("Greeks:", engine.benchmark_greeks_calculation())

if __name__ == "__main__":
    run_example()
