from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

OUTPUT_DIR = "/Users/moses/automation_output"
print("DB_USER:", os.getenv("DB_USER"))
DB_URI = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"


def store_to_postgres():

    if os.getenv("CI") == "true":
        print("Skipping DB write in CI")
        return

    files = [f for f in os.listdir(OUTPUT_DIR) if f.endswith(".csv")]
    files.sort(reverse=True)

    if not files:
        print("No output files found")
        return

    latest_file = os.path.join(OUTPUT_DIR, files[0])

    print(f"Storing file to DB: {latest_file}")

    df = pd.read_csv(latest_file)

    engine = create_engine(DB_URI)
        # "postgresql+psycopg2://postgres:4342@localhost:5432/world"
    # )

    df.to_sql("cleaned_data", engine, if_exists="replace", index=False)

    print("Data stored in PostgreSQL table: cleaned_data")