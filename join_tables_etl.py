import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import os
from dotenv import load_dotenv
import os

load_dotenv()

DB_URI = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
# DB connection
# DB_URI = "postgresql+psycopg2://postgres:4342@localhost:5432/world"

# Output folder
OUTPUT_DIR = "/Users/moses/automation_input"

def run_etl():

    print("Starting ETL job...")

    engine = create_engine(DB_URI)

    query = """
    SELECT
        s.user_id,
        s.user_name,
        s.department,
        s.location,
        s.project,
        s.salary,
        s.performance_rating,
        d.certification,
        d.project_code,
        d.project_status,
        d.client_name,
        d.project_budget
    FROM sde_automation s
    JOIN dpe_automation d
    ON s.user_id = d.user_id
    """

    df = pd.read_sql(query, engine)

    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    filename = f"joined_data_{timestamp}.csv"

    filepath = os.path.join(OUTPUT_DIR, filename)

    df.to_csv(filepath, index=False)

    print(f"ETL completed. File saved at: {filepath}")


# if __name__ == "__main__":
#     run_etl()