#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将 .agents 下的配置（agents、skills、commands）同步到 .cursor/.opencode 等。"""

import shutil
import sys
from pathlib import Path

def repo_root() -> Path:
    root = Path(__file__).resolve().parent
    if not (root / ".agents").is_dir():
        raise SystemExit("fatal: 未找到 .agents，请在项目根目录下保留 .agents 后重试")
    return root


def sync_dir(src: Path, dst: Path, name: str) -> None:
    if not src.is_dir():
        return
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    print(f"  {name}: {src} -> {dst}")


def main() -> None:
    root = repo_root()
    agents = root / ".agents"
    targets = [
        (root / ".claude", ".claude"),
        (root / ".opencode", ".opencode"),
    ]

    for base, label in targets:
        if not base.exists():
            base.mkdir(parents=True)
        for part in ("agents", "skills", "commands"):
            src = agents / part
            dst = base / part
            if src.is_dir():
                sync_dir(src, dst, f"{label}/{part}")
            else:
                print(f"  skip (missing): {agents / part}")

    print("done: .agents 已同步到 .claude、.opencode")


if __name__ == "__main__":
    main()
    sys.exit(0)
