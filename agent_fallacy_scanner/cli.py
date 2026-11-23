"""CLI for Agent Fallacy Scanner."""
import argparse
from .core import FallacyScanner

def main():
    parser = argparse.ArgumentParser(description="Agent Fallacy Scanner CLI")
    parser.add_argument("--demo", action="store_true", help="Run logical fallacy scanning demo")
    args = parser.parse_args()

    argument = "We must either adopt this exact architecture or our startup will fail completely. Everyone knows that all microservices succeed."
    fallacies = FallacyScanner.scan(argument)
    print("Argument:", argument)
    print(f"Detected {len(fallacies)} logical fallacies:")
    for f in fallacies:
        print(f"  [{f.fallacy_type.upper()}] {f.matched_text} -> {f.explanation}")

if __name__ == "__main__":
    main()
