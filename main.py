from fastapi import FastAPI

app = FastAPI(title="AURA")

# Serve the static website from the site/ directory.
app.frontend("/", directory="site")
