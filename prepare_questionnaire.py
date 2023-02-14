#!/usr/bin/env python3

from os import makedirs
from os.path import join
import sys
import pandas as pd

wdr = sys.argv[1] if len(sys.argv) > 1 else "/data/derivatives/cvr_bp"
qdr = sys.argv[2] if len(sys.argv) > 2 else "/data/phenotype"

data = pd.read_csv(join(qdr, 'questionnaire.tsv'), sep='\t')

wdr = join(wdr, 'phenotype')
makedirs(wdr, exist_ok=True)

for col in ['mean_arterial_pressure', 'pulse_pressure', 'pulse_avg']:
    series = data[col] - data.groupby('subject')[col].transform('mean')
    series.to_csv(join(wdr, f"{col}_demeaned.csv",), index=False)    

for col in ['subject', 'session', 'sex']:
    data[col].to_csv(join(wdr, f"{col}.csv"), index=False)
