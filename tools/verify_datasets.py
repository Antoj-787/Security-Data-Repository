#!/usr/bin/env python3
import os

def verify():
    datasets = {
        '1-Phishing Emails': 'datasets/1-phishing-emails/',
        '2-Enron Emails':    'datasets/2-enron-emails/',
        '3-Malware URLs':    'datasets/3-malware-urls/',
        '4-Malware Emails':  'datasets/4-malware-emails/'
    }

    print('=' * 60)
    print('DATASET VERIFICATION REPORT')
    print('=' * 60)

    all_good = True
    for name, path in datasets.items():
        if os.path.exists(path):
            print(f'OK    {name}: Folder Found')
            if os.path.exists(os.path.join(path, 'README.md')):
                print(f'      README.md: Found')
            else:
                print(f'      README.md: MISSING')
                all_good = False
        else:
            print(f'MISS  {name}: Folder Not Found')
            all_good = False

    print('=' * 60)
    if all_good:
        print('ALL DATASETS VERIFIED SUCCESSFULLY!')
    else:
        print('WARNING: SOME DATASETS OR READMES ARE MISSING')
    print('=' * 60)

if __name__ == '__main__':
    verify()
```

