import sys
sys.path.insert(0, 'backend')
from app.config import settings
print('OPENROUTER:', bool(settings.openrouter_api_key))
print('GEMINI:', bool(settings.gemini_api_key))
print('GROK:', bool(settings.grok_api_key))
print('FORCE_MOCK:', settings.force_mock_llm)
