"""System & API health monitoring for the dashboard."""
from __future__ import annotations

import shutil
import time
from datetime import datetime

import psutil

from ..config import settings
from ..core.utils import ffmpeg_available, mask_key

_start = time.time()


def system_stats() -> dict:
    data_path = settings.data_path
    du = shutil.disk_usage(str(data_path))
    return {
        "cpu_pct": psutil.cpu_percent(interval=0.2),
        "ram_pct": psutil.virtual_memory().percent,
        "ram_used_gb": round(psutil.virtual_memory().used / 1e9, 1),
        "ram_total_gb": round(psutil.virtual_memory().total / 1e9, 1),
        "disk_total_gb": round(du.total / 1e9, 1),
        "disk_used_gb": round(du.used / 1e9, 1),
        "uptime_min": round((time.time() - _start) / 60, 1),
    }


def storage_breakdown() -> dict:
    out = {}
    for sub in ("media", "output", "music", "thumbnails", "logs", "tokens"):
        p = settings.path(settings.data_dir, sub)
        total = sum(f.stat().st_size for f in p.rglob("*") if f.is_file()) if p.exists() else 0
        out[sub] = round(total / 1e6, 1)  # MB
    return out


def api_health() -> dict:
    caps = settings.capability_report()
    return {
        "services": caps,
        "ffmpeg": "ok" if ffmpeg_available() else "MISSING — install ffmpeg",
        "keys": {
            "openrouter": mask_key(settings.openrouter_api_key),
            "gemini": mask_key(settings.gemini_api_key),
            "grok": mask_key(settings.grok_api_key),
            "pexels": mask_key(settings.pexels_api_key),
            "pixabay": mask_key(settings.pixabay_api_key),
            "jamendo": mask_key(settings.jamendo_client_id),
            "acoustid": mask_key(settings.acoustid_api_key),
            "huggingface": mask_key(settings.huggingface_token),
            "amazon_pa": mask_key(settings.amazon_pa_api_key),
            "amazon_pa_secret": mask_key(settings.amazon_pa_secret),
            "amazon_tag": mask_key(settings.amazon_affiliate_tag),
            "reddit_client": mask_key(settings.reddit_client_id),
            "reddit_secret": mask_key(settings.reddit_secret),
            "news": mask_key(settings.news_api_key),
        },
        "youtube_dry_run": settings.youtube_dry_run,
        "checked_at": datetime.utcnow().isoformat(),
    }
