import json
import requests


def lambda_handler(event, context):
    message = "{}".format(event["issue"]["html_url"])
    url = "Some link here"
    ret_obj = {"text": event["issue"]["html_url"]}
    response = requests.post(
        url,
        json={
            "text": "Issue "
            + str(event["action"]).capitalize()
            + ": "
            + str(event["issue"]["html_url"])
        },
        headers={"Content-Type": "application/json"},
    )
    return {"message": response.text}
