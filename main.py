import os
import json
from core.autogen.golden_ratio_autogen import generate_text
from core.state_management.current_state import get_current_state, update_state
from core.utils.helpers import log_activity

def main():
    """The main entry point for the ChitAkasha Live Directory."""

    # Load environment settings
    settings = load_settings()

    # Get current state
    current_state = get_current_state()

    # Load inbox prompts
    prompts = load_prompts()

    # Generate text based on golden ratio
    generated_text = generate_text(prompts, current_state, settings)

    # Update current state
    new_state = update_state(current_state, generated_text)

    # Log activity
    log_activity(generated_text, new_state)

    print("ChitAkasha Live Directory successfully updated.")

def load_settings():
    """Loads the environment settings from `config/settings.json`."""

    with open("config/settings.json", "r") as f:
        settings = json.load(f)

    return settings

def load_prompts():
    """Loads the inbox prompts from `data/inbox/prompts.json`."""

    with open("data/inbox/prompts.json", "r") as f:
        prompts = json.load(f)

    return prompts

if __name__ == "__main__":
    main()

