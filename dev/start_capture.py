import sys
sys.path.append('../')

from src.capture import TrafficAnalyzer

analyzer = TrafficAnalyzer(new_flow_handle = lambda *args: None)

print("TrafficAnalyzer initialized")
