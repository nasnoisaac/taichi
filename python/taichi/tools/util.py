import subprocess

from taichi._lib import core as _ti_core


def set_gdb_trigger(on=True):
    _ti_core.set_core_trigger_gdb_when_crash(on)


def dump_dot(filepath=None, rankdir=None, embed_states_threshold=0):
    d = _ti_core.dump_dot(rankdir, embed_states_threshold)
    if filepath is not None:
        with open(filepath, 'w') as fh:
            fh.write(d)
    return d


def dot_to_pdf(dot, filepath):
    assert filepath.endswith('.pdf')
    with subprocess.Popen(['dot', '-Tpdf'],
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE) as p:
        pdf_contents = p.communicate(input=dot.encode())[0]
        with open(filepath, 'wb') as fh:
            fh.write(pdf_contents)


def get_kernel_stats():
    return _ti_core.get_kernel_stats()
