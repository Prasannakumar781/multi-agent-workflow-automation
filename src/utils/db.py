import os
import psycopg2

def get_conn():
    return psycopg2.connect(os.getenv("POSTGRES_URL"))
    
def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS workflow_runs (
            id SERIAL PRIMARY KEY,
            thread_id TEXT,
            node_name TEXT,
            event TEXT,
            details TEXT,
            created_at TIMESTAMP DEFAULT NOW()
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def log_event(thread_id, node_name, event, details=""):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO workflow_runs (thread_id, node_name, event, details)
        VALUES (%s, %s, %s, %s)
    """, (thread_id, node_name, event, details))
    conn.commit()
    cur.close()
    conn.close()