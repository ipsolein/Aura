from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="AURA")

# Serve the static website from the site/ directory.
app.mount("/", StaticFiles(directory="site", html=True), name="site")
