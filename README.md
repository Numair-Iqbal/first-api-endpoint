# First API Endpoint

A minimal Flask backend built for the FlyRank Backend AI Engineering track.

## Endpoints
- `GET /` — returns a welcome message
- `GET /status` — returns developer and status info

## Run Locally
```bash
pip install -r requirements.txt
python app.py
```

Then visit `http://127.0.0.1:5000/` in your browser, or run:
```bash
curl http://127.0.0.1:5000/status
```