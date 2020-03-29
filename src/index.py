"""
    Wave Oracle: Surf Prediction Microservice
    Main entry for prediction system

    Date: 29/03/2020
"""

import ptvsd

# Debugging setup & await sockect connection
ptvsd.enable_attach(address=('0.0.0.0', 5890), redirect_output=True)
ptvsd.wait_for_attach()

def surf_predictor(event, context):
    print("SurfPredictor: Function launching")
    print("Function shutting down")
    return "Success"