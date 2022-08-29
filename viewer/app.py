import hashlib
import hmac
import io
import json
import os
import zipfile
import flask
import requests

app = flask.Flask(__name__)

COMMITS_DIRECTORY = "commits"
LATEST_DIRECTORY_NAME = "latest"

PAPER_PDF_FILE = "paper.pdf"
INFO_JSON_FILE = "info.json"


def get_commit_directory(commit_id: str):
    return f"{COMMITS_DIRECTORY}/{commit_id}"


def validate_signature(response: flask.Request, secret):
    """
    derived from: https://gist.github.com/andrewfraley/0229f59a11d76373f11b5d9d8c6809bc
    """

    # Get the signature from the payload
    signature_header = response.headers['X-Hub-Signature']
    sha_name, github_signature = signature_header.split('=')
    if sha_name != 'sha1':
        print('ERROR: X-Hub-Signature in payload headers was not sha1=****')
        return False
      
    # Create our own signature
    local_signature = hmac.new(secret.encode('utf-8'), msg=response.data, digestmod=hashlib.sha1)

    # See if they match
    return hmac.compare_digest(local_signature.hexdigest(), github_signature)


@app.route("/assets/<path:path>")
def assets(path):
    return flask.send_from_directory("assets", path)


@app.route(f"/{PAPER_PDF_FILE}")
def paper():
    return flask.send_file(f"{get_commit_directory(LATEST_DIRECTORY_NAME)}/{PAPER_PDF_FILE}")


@app.route(f"/{INFO_JSON_FILE}")
def info():
    return flask.send_file(f"{get_commit_directory(LATEST_DIRECTORY_NAME)}/{INFO_JSON_FILE}")


@app.route("/")
def index():
    return flask.send_file("app.html")


@app.route("/webhook", methods=['POST'])
def webhook():
    validate_signature(flask.request, os.environ['GITHUB_WEBHOOK_SECRET'])
    payload = flask.request.json

    workflow = payload.get("workflow_run")
    if payload.get("action") != "completed" or workflow is None:
        return "not a completed workflow"

    commit = workflow["head_commit"]
    commit_id = commit["id"]

    artifacts_url = workflow["artifacts_url"]
    artifacts = requests.get(artifacts_url).json()["artifacts"]

    artefact = next(filter(lambda x: x["name"] == "paper", artifacts), None)
    if artefact is None:
        return "paper artifact not found"

    archive_download_url = artefact["archive_download_url"]
    zip = zipfile.ZipFile(io.BytesIO(requests.get(archive_download_url, headers={
        "Authorization": f"Token {os.environ['GITHUB_TOKEN']}"
    }).content))

    if PAPER_PDF_FILE not in zip.namelist():
        return "paper.pdf not in the zip"

    commit_directory = get_commit_directory(commit_id)
    os.makedirs(commit_directory, exist_ok=True)

    zip.extract(PAPER_PDF_FILE, commit_directory)
    with open(f"{commit_directory}/{INFO_JSON_FILE}", "w") as fd:
        json.dump(commit, fd, indent=4)

    latest_symlink = get_commit_directory(LATEST_DIRECTORY_NAME)
    if os.path.exists(latest_symlink):
        os.remove(latest_symlink)
    
    os.symlink(commit_id, LATEST_DIRECTORY_NAME, target_is_directory=True)
    os.rename(LATEST_DIRECTORY_NAME, latest_symlink)

    return "ok"
