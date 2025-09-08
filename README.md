# Vercel + FastAPI (Serverless Functions)

**Structure**
```
api/
  index.py   # FastAPI app (ASGI)
requirements.txt
vercel.json  # correct name
```

**Deploy on Vercel**
- Framework Preset: Other
- Install Command: `pip install -r requirements.txt`
- Build Command: *(leave empty)*
- Output Directory: *(leave empty)*

Open your domain:
- `/`      -> `{"hello":"world"}`
- `/ping`  -> `{"ok": true}`
