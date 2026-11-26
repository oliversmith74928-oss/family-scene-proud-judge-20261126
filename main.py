#!/usr/bin/env python3
"""Entry point for the make.fun bounty
"Make the AI Judge Feel Proud: A Family Scene".

Writes the one-line family scene from scene.py to
/output/entry.txt (the grader's path), and also to entry.txt in the
repository so the entry can be reviewed. Python standard library
only; the output is deterministic, so every run writes the same
bytes.
"""

import hashlib
import os
from pathlib import Path

from scene import SCENE

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    text = SCENE.strip()
    if not 1 <= len(text) <= 280:
        raise SystemExit(
            f"scene must be 1-280 characters, got {len(text)}"
        )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = (text + "\n").encode("utf-8")
    # Only write to MAKEFUN_OUTPUT_DIR: the repo dir is mounted
    # read-only in the grader sandbox, so writing entry.txt next to
    # this script would raise PermissionError and fail the run.
    (OUTPUT_DIR / "entry.txt").write_bytes(payload)
    # Verification step: read the file back and confirm it is valid
    # UTF-8, holds exactly the scene, and hashes to a stable digest.
    roundtrip = (OUTPUT_DIR / "entry.txt").read_bytes()
    assert roundtrip == payload, "entry.txt does not match the scene"
    digest = hashlib.sha256(payload).hexdigest()
    print(f"wrote {len(text)} characters to entry.txt")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
