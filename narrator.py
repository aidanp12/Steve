"""
Purpose: host the story
Input:
Output:
Created: 04/05/2025
Last Edited: 04/05/2025
Contributors:
"""

from openai import OpenAI
from pydantic import BaseModel
import json

STORY_PROMPT = """
You are a fantasy RPG narrator AI.
Your job is to describe what happens in the story and return structured game event data.
Limit the player with what they can do, as not to allow them to perform any actions that seem too unrealistic based on their current stats.
Avoid explicit content or activities as needed.

For every player input:
1. Generate a vivid `narrative` string (immersive storytelling).
2. Populate an `events` object with relevant structured data, based on this schema:

{
  "item_found": boolean,
  "item": {
    "name": string,
    "type": string,
    "rarity": string,
    "stats": {
      "damage_type": string (magic/physical),
      "damage": string (XdY where X is the number of dice and Y is either 4, 6, 8, 10, 12, or 20)
      "durability": number
      "piercing": number
    }
  },
  "enemy_encounter": boolean,
  "enemy": {
    "name": string,
    "type": string,
    "level": number,
    "count": number,
    "stats": {
        "enemy_damage": string (XdY where X is the number of dice and Y is either 4, 6, 8, 10, 12, or 20)
        "enemy_physical_def": number
        "enemy_magic_def": number
        "enemy_xp": number
        "enemy_dmg_type": string (magic/physical),
        "enemy_drop": item
  },
  "location_discovery": boolean,
  "location": {
    "name": string,
    "description": string,
    "features": [string]
  }
}

If any event type does not occur, set the corresponding flag to false and the object to null.

Always return a JSON object with keys: "narrative" and "events".
"""


rpg_tool = {
    "type": "function",
    "function": {
        "name": "process_rpg_event",
        "description": "Process RPG player input and generate a narrative with structured event metadata.",
        "parameters": {
            "type": "object",
            "properties": {
                "narrative": {
                    "type": "string",
                    "description": "The story text describing the result of the player's action."
                },
                "events": {
                    "type": "object",
                    "properties": {
                        "item_found": {"type": "boolean"},
                        "item": {
                            "type": ["object", "null"],
                            "properties": {
                                "name": {"type": "string"},
                                "type": {"type": "string"},
                                "rarity": {"type": "string"},
                                "damage": {"type": "string"},

                                    }
                                }
                            }
                        },
                        "enemy_encounter": {"type": "boolean"},
                        "enemy": {
                            "type": ["object", "null"],
                            "properties": {
                                "name": {"type": "string"},
                                "type": {"type": "string"},
                                "level": {"type": "integer"},
                                "abilities": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                }
                            }
                        },
                        "location_discovery": {"type": "boolean"},
                        "location": {
                            "type": ["object", "null"],
                            "properties": {
                                "name": {"type": "string"},
                                "description": {"type": "string"},
                                "features": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                }
                            }
                        }
                    }
                }
            },
            "required": ["narrative", "events"]
        }
    }
}
class narr():
    def __init__(self):
        self.client = OpenAI()
        self.narrator = self.client.beta.assistants.create(
            name="Steve",
            instructions=STORY_PROMPT,
            model="gpt-4o",
        )
        self.storyThread = self.client.beta.threads.create()

    def initiate_story(self):
        pass

    def initiate_encounter(self):
        pass

    def item_found(self):

    def progress_story(self, user_input):
        progression = self.client.beta.threads.messages.create(
            thread_id = self.storyThread.id,
            role="user",
            content=user_input,
        )

        run = self.client.beta.threads.runs.create_and_poll()


