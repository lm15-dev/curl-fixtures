#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

import yaml

ROOT = Path(__file__).parent
FEATURES = ROOT / 'features.yaml'
LATEST = ROOT / 'results' / 'latest.json'


def load_features():
    with open(FEATURES) as f:
        return yaml.safe_load(f)


def load_latest():
    if LATEST.exists():
        with open(LATEST) as f:
            data = json.load(f)
        return data.get('cases', {})
    return {}


def fmt(v):
    if v is None or v == '':
        return '—'
    return str(v)


def short_status(result):
    if not result:
        return 'not_tested'
    return result.get('result', 'not_tested')


def done_flag(status):
    return 'yes' if status == 'covered' else ('no' if status == 'todo' else 'skip')


def todo_flag(status):
    return 'yes' if status == 'todo' else 'no'


def tested_flag(result):
    if not result:
        return 'no'
    return 'yes' if result.get('result') in {'pass', 'fail', 'skipped'} else 'no'


def pass_fail(result):
    if not result:
        return 'not_tested'
    return result.get('result', 'not_tested')


def body_link(result):
    if not result:
        return '—'
    rel = result.get('body_path')
    if not rel:
        return '—'
    return f'[{Path(rel).name}]({rel})'


def provider_summary(provider, pdata, latest):
    features = pdata['features']
    total = len(features)
    covered = sum(1 for x in features.values() if x['status'] == 'covered')
    todo = sum(1 for x in features.values() if x['status'] == 'todo')
    passed = failed = skipped = tested = 0
    for feature in features:
        r = latest.get(f'{provider}.{feature}')
        if not r:
            continue
        tested += 1
        if r['result'] == 'pass':
            passed += 1
        elif r['result'] == 'fail':
            failed += 1
        elif r['result'] == 'skipped':
            skipped += 1
    return total, covered, todo, tested, passed, failed, skipped


def make_readme(data, latest):
    lines = []
    lines.append('# Curl Fixtures')
    lines.append('')
    lines.append('Comprehensive repository of curl requests for the OpenAI, Anthropic, and Gemini APIs.')
    lines.append('')
    lines.append('## What this repo tracks')
    lines.append('')
    lines.append('- fixture coverage from provider docs')
    lines.append('- live test status for each covered case')
    lines.append('- last test timestamp')
    lines.append('- last test duration')
    lines.append('- estimated test cost when available')
    lines.append('- link to the last saved response body')
    lines.append('')
    lines.append('## Workflow')
    lines.append('')
    lines.append('```bash')
    lines.append('# update provider docs')
    lines.append('bash api-references/openai/update.sh')
    lines.append('bash api-references/anthropic/update.sh')
    lines.append('bash api-references/gemini/update.sh')
    lines.append('')
    lines.append('# check feature coverage')
    lines.append('python3 extract_features.py')
    lines.append('python3 check_coverage.py')
    lines.append('')
    lines.append('# run live tests and persist results')
    lines.append('bash validate_live.sh')
    lines.append('')
    lines.append('# regenerate this README matrix')
    lines.append('python3 generate_readme.py')
    lines.append('```')
    lines.append('')
    lines.append('## Provider summary')
    lines.append('')
    lines.append('| Provider | Total features | Done | Todo | Last tested cases | Pass | Fail | Skipped |')
    lines.append('|---|---:|---:|---:|---:|---:|---:|---:|')
    for provider, pdata in data.items():
        total, covered, todo, tested, passed, failed, skipped = provider_summary(provider, pdata, latest)
        lines.append(f'| {provider} | {total} | {covered} | {todo} | {tested} | {passed} | {failed} | {skipped} |')
    lines.append('')
    lines.append('## Fixture matrix')
    lines.append('')
    lines.append('| Provider | Feature | Done | Todo | Tested | Last result | Last tested at | HTTP | Duration s | Cost USD | Response body | Description |')
    lines.append('|---|---|---|---|---|---|---|---:|---:|---:|---|---|')
    for provider, pdata in data.items():
        for feature, finfo in pdata['features'].items():
            r = latest.get(f'{provider}.{feature}')
            lines.append(
                f"| {provider} | {feature} | {done_flag(finfo['status'])} | {todo_flag(finfo['status'])} | {tested_flag(r)} | {pass_fail(r)} | {fmt(r.get('tested_at') if r else None)} | {fmt(r.get('http_code') if r else None)} | {fmt(r.get('duration_seconds') if r else None)} | {fmt(r.get('estimated_cost_usd') if r else None)} | {body_link(r)} | {finfo.get('description','')} |"
            )
    lines.append('')
    lines.append('## Results format')
    lines.append('')
    lines.append('- Latest run summary: `results/latest.json`')
    lines.append('- Run history: `results/history.jsonl`')
    lines.append('- Response bodies: `results/bodies/<case-id>/<timestamp>.txt`')
    lines.append('')
    lines.append(f'_README generated at {datetime.utcnow().isoformat()}Z by `generate_readme.py`._')
    lines.append('')
    return '\n'.join(lines)


def main():
    data = load_features()
    latest = load_latest()
    content = make_readme(data, latest)
    (ROOT / 'README.md').write_text(content)
    print('Wrote README.md')


if __name__ == '__main__':
    main()
