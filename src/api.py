from fastapi import FastAPI, HTTPException

from schema.system_schema import InputModel
from module.segment import RoommateMatching

app = FastAPI()


@app.post("/recommend-roommates/")
def recommend_roommates(input):
    if not input:
        raise HTTPException(status_code=404, detail="No user data available.")
    
    input_model = InputModel(
        input_model=input
    )

    roommate_matching = RoommateMatching(inp=input_model)

    results = roommate_matching.run()

    return results
