import json
from tqdm.auto import tqdm
import pandas as pd
import numpy as np

DB_CONNECTION = "postgresql://martin:F0hn1lcob.r@localhost:5432/patentmark"

raw_set = pd.read_csv("notes.csv", header=None, delimiter=';', usecols=[0,1])
raw_set.columns = ["epodoc", "category"]
raw_set.dropna(inplace=True)

matching_patents = pd.read_sql_query(sql="""
with patent_rows as (SELECT replace(document_id, '-', '') as epodoc, document_id, country_code, "serial", kind, family_id, priority_date, publication_date, filing_date, grant_date, title, abstract, description, claims, url, data_source, internal_id FROM public.patents)
select * from patent_rows
where epodoc in %(epodocs)s;""", con=DB_CONNECTION, params={"epodocs": tuple(raw_set.epodoc.values.tolist())})