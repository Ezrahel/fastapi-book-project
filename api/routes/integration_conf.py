from fastapi import APIRouter
from fastapi.responses import JSONResponse

from core.config import settings

router=APIRouter()

integration_json={
  "data": {
    "date": {
      "created_at": "2025-02-16",
      "updated_at": "2025-02-16"
    },
    "descriptions": {
      "app_name": "ci-cd-notification",
      "app_description": "a simple telex/slack integration",
      "app_logo": "https://img.freepik.com/free-vector/golden-elegant-logo-with-frame_52683-13462.jpg?semt=ais_hybrid",
      "app_url": "http://102.37.138.135/",
      "background_color": "#fff"
    },
    "is_active": true,
    "integration_type": "modifier",
    "key_features": [
      "real time updates",
      "slack notifications"
    ],
    "author": "Di-Tech Inc.",
    "settings": [
      {
        "label": "slack channel",
        "type": "text",
        "required": true,
        "default": "#DevOpsAlert"
      },
      {
        "label": "Time Interval",
        "type": "dropdown",
        "required": true,
        "default": "immediate",
        "options": [
          "immediate",
          "every 1 mins",
          "every 2 mins",
          "every 5 mins"
        ]
      },
      {
        "label": "event type",
        "type": "dropdown",
        "required": true,
        "default": "ci_pipeline",
        "options": [
          "ci_pipeline",
          "cd_pipeline",
          "deployment"
        ]
      },
      {
        "label": "message",
        "type": "text",
        "required": true,
        "default": "basic"
      },
      {
        "label": "include log",
        "type": "checkbox",
        "required": true,
        "default": "true"
      }
    ],
    "target_url": settings.SLACK_TARGET_URL,
    "tick_url": settings.BASE_URL_IP
  }
}

@router.get("/integration-json")
async def get_integration_json():
    return JSONResponse(content=integration_json)