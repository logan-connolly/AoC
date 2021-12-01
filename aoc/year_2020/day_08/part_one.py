from .parse import parse_command
from .accumulate import loop_accumulate


def solve(commands: list[str]) -> int:
    """Day 08: Handheld Halting (part 1)"""
    parsed = [parse_command(cmd) for cmd in commands]
    _, acc = loop_accumulate(parsed, idx_set=set(), values=(0, 0))
    return acc
