from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from supabase import create_client

db_url = "https://hwzesweqxpdvmeibodki.supabase.co"
db_key = "sb_publishable_vMghZCTf8pkCG9Ew7_vMcA_Arbx7OgL"

db = create_client(db_url,db_key)


app = FastAPI()

@app.get('/tasks')
def get_all_tasks():
    result = db.table('tasks').select('*').execute()
    tasks = result.data
    return tasks