"""Deterministic Maker-side recovery launcher binding (MIT). No runtime config."""
import argparse
from pathlib import Path
import re
import shlex

SOURCE = 'skills/brownfield-feature-planning/scripts/recover-triage'
SCRIPT = 'skills/brownfield-feature-planning/scripts/recover_triage.py'
TRANSFORM = 'bound-recovery-v1'


def render_launcher(template, binding, roles):
    if not isinstance(binding, dict) or set(binding) != {'python', 'script', 'db', 'planner_profile'}:
        raise ValueError('Confirmed triage_recovery binding required')
    for key, value in binding.items():
        if not isinstance(value, str) or not value.strip() or any(ord(c) < 32 or ord(c) == 127 for c in value):
            raise ValueError('Invalid recovery binding: ' + key)
        if key != 'planner_profile':
            path = Path(value)
            if not path.is_absolute() or '..' in path.parts or str(path) != value:
                raise ValueError('Canonical absolute recovery path required: ' + key)
    planner = roles['planner']
    if binding['planner_profile'] != planner['id'] or binding['script'] != str(Path(planner['home']) / SCRIPT):
        raise ValueError('Recovery binding differs from confirmed planner identity/path')
    text = template.decode()
    fields = re.findall(r'\{\{([^{}]+)\}\}', text)
    if sorted(fields) != sorted(binding):
        raise ValueError('Recovery launcher field contract changed')
    # One pass: substituted data is never interpreted as template or shell source.
    return re.sub(r'\{\{([^{}]+)\}\}', lambda m: shlex.quote(binding[m[1]]), text).encode()


def install(home):
    # Reuse the Maker's guarded writes and private setup parser, not a second config.
    from update_team import atomic, fingerprint, read, setup_data, state_dir
    home = Path(home)
    setup = setup_data(state_dir(home))
    bindings = setup['confirmed_bindings']
    roles = bindings['roles']
    if roles['planner']['home'] != str(home):
        raise ValueError('Planner home mismatch')
    template = Path(__file__).resolve().parents[1] / SOURCE
    content = render_launcher(template.read_bytes(), bindings.get('triage_recovery'), roles)
    target = home / SOURCE
    previous = read(target)
    if previous not in (None, template.read_bytes(), content):
        raise ValueError('Changed recovery launcher: reconcile before installation')
    atomic(target, content, fingerprint(target), 0o700)
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--home', required=True, type=Path)
    print(install(parser.parse_args().home))
