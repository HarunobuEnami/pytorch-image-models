import glob
import csv

topks = glob.glob('outputs/*/topk_ids.csv')

outputs = [['filename', 'expected', 'infered']]

for topk in topks:
    with open(topk) as f:
        s = f.read()
        s = s.split(',')
        filename = s[0]
        if filename.startswith('1img'):
            expected = '0'
        else:
            expected = '1'

        infered = s[1]
        outputs.append([filename, expected, infered])

with open('cross_val_result.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(outputs)
