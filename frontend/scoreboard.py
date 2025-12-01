import json
import os
from typing import List, Dict, Any

SCORES_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets', 'highscores.json')


def load_scores() -> List[Dict[str, Any]]:
    try:
        with open(SCORES_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []


def save_score(entry: Dict[str, Any]) -> None:
    scores = load_scores()
    scores.append(entry)
    try:
        os.makedirs(os.path.dirname(SCORES_PATH), exist_ok=True)
        with open(SCORES_PATH, 'w', encoding='utf-8') as f:
            json.dump(scores, f, ensure_ascii=False, indent=2)
    except Exception:
        # Silent failure is acceptable for optional persistence
        pass
