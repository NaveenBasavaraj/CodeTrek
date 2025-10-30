from pathlib import Path
import sys

# Ensure project root (directory that contains &#34;navcodes&#34;) is on sys.path
# This makes &#34;import navcodes...&#34; work regardless of where pytest is invoked
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
