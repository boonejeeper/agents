#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from financial_researcher.crew import FinancialResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    
    inputs = {
        'company': 'Apple Inc.',
    }
    result = FinancialResearcher().crew().kickoff(inputs=inputs)
    print(f"Final result: {result.raw}")


if __name__ == "__main__":
    start_time = datetime.now()
    print(f"Starting crew at {start_time}")
    run()
    end_time = datetime.now()
    print(f"Finished crew at {end_time}, total time: {end_time - start_time}")

