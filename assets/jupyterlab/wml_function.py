import urllib3, requests, json
from tornado.escape import json_encode, json_decode, url_escape

# Define scoring function
def callModel(payload_scoring):

    print(json.dumps(payload_scoring))
    predictions =[]
    for value in payload_scoring:
        sums = []
        for value in payload_scoring["input_data"][0]["values"]:
            first = value[0]
            second = value[1]
            sums.append([first, second, first + second])
        predictions.append({"fields": ["FIRST", "SECOND", "SUM"],"values": sums})
    
    return {"predictions": predictions}


#wml_python_function
def score(input):
    
    """AI function example.

    Example:
      {"input_data": [{"fields":["FIRST","SECOND","values":[[1,2]]}]}
    """
    
    # Score using the pre-defined model 
    prediction = callModel(input);

    return prediction