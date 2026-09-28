import sys, json
from client import BlackScholesGreeksEngine

engine = BlackScholesGreeksEngine()

def handle_jsonrpc(line):
    global engine
    try:
        req = json.loads(line)
        req_id = req.get("id")
        method = req.get("method")
        if method == "initialize":
            return {"jsonrpc": "2.0", "id": req_id, "result": {"protocolVersion": "2024-11-05", "serverInfo": {"name": "genpark-black-scholes-merton-greeks-engine-skill", "version": "1.0.0"}, "capabilities": {"tools": {}}}}
        elif method == "tools/list":
            return {"jsonrpc": "2.0", "id": req_id, "result": {"tools": [
                {"name": "calculate_greeks", "description": "Calculate BSM price and Greeks.", "inputSchema": {"type": "object", "properties": {"S": {"type": "number"}, "K": {"type": "number"}, "T": {"type": "number"}, "r": {"type": "number"}, "sigma": {"type": "number"}, "option_type": {"type": "string"}}, "required": ["S", "K", "T", "r", "sigma"]}},
                {"name": "benchmark_greeks_calculation", "description": "Run Greeks benchmark.", "inputSchema": {"type": "object", "properties": {}}}
            ]}}
        elif method == "tools/call":
            params = req.get("params", {})
            tool = params.get("name")
            args = params.get("arguments", {})
            if tool == "calculate_greeks":
                res = engine.price_and_greeks(args.get("S"), args.get("K"), args.get("T"), args.get("r"), args.get("sigma"), args.get("option_type", "CALL"))
            elif tool == "benchmark_greeks_calculation":
                res = engine.benchmark_greeks_calculation()
            else:
                return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}
    except Exception as e:
        return {"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}

def main():
    for line in sys.stdin:
        if line.strip():
            print(json.dumps(handle_jsonrpc(line.strip())), flush=True)

if __name__ == "__main__":
    main()
