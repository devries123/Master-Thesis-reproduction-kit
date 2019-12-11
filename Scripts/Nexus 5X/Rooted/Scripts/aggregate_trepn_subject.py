import csv
import os
import sys
from collections import OrderedDict


def list_subdir(a_dir):
    """List immediate subdirectories of a_dir"""
    # https://stackoverflow.com/a/800201
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]


def aggregate_trepn_subject(logs_dir):
    def add_row(accum, new):
        row = {key: value + float(new[key]) for key, value in accum.items() if key not in ['Component', 'count']}
        count = accum['count'] + 1
        return dict(row, **{'count': count})

    runs = []
    for run_file in [f for f in os.listdir(logs_dir) if os.path.isfile(os.path.join(logs_dir, f))]:
        with open(os.path.join(logs_dir, run_file), 'rb') as run:
            run_dict = {}
            reader = csv.DictReader(run)
            column_readers = split_reader(reader)
            for k, v in column_readers.items():
                init = dict({k: 0}, **{'count': 0})
                run_total = reduce(add_row, v, init)
                if not run_total['count'] == 0:
                    run_dict[k] = run_total[k] / run_total['count']
            runs.append(run_dict)
    return runs


def split_reader(reader):
    column_dicts = {fn: [] for fn in reader.fieldnames if not fn.split('[')[0].strip() == 'Time'}
    for row in reader:
        for k, v in row.items():
            if not k.split('[')[0].strip() == 'Time' and not v == '':
                column_dicts[k].append({k: v})
    return column_dicts


def write_to_file(filename, rows):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


# noinspection PyUnusedLocal
def main(dummy, data_dir):
    print 'Subject aggregation: {}'.format(data_dir)
    filename = os.path.join(data_dir, 'Aggregated.csv')
    run_rows = aggregate_trepn_subject(data_dir)
    write_to_file(filename, run_rows)
