from agents.diagnostic import DiagnosticAgent
from agents.offer import OfferAgent
from agents.assets import AssetsAgent
from agents.learn import LearnAgent

# Agent instances (loaded once at startup so prompts are read once)
AGENTS = {
    "diagnose": DiagnosticAgent(),
    "offer": OfferAgent(),
    "assets": AssetsAgent(),
    "log": LearnAgent(),
}

META_COMMANDS = {"start", "help", "project", "history"}
ALL_COMMANDS = set(AGENTS.keys()) | META_COMMANDS


def parse_message(text: str) -> tuple[str, str]:
    """
    Parse a Telegram message into (command_name, args).
    Supports multiline input: command on line 1, context pasted below.

    /diagnose
    Here is the client situation...

    or inline: /diagnose some quick context
    """
    text = text.strip()
    lines = text.split("\n", 1)
    first_line = lines[0].strip()
    multiline_rest = lines[1].strip() if len(lines) > 1 else ""

    parts = first_line.split(None, 1)
    command_raw = parts[0].lstrip("/").split("@")[0].lower()
    inline_args = parts[1].strip() if len(parts) > 1 else ""

    args = (inline_args + "\n" + multiline_rest).strip() if multiline_rest else inline_args

    return command_raw, args


def route(command: str, args: str) -> tuple[str | None, str | None]:
    """
    Returns (agent_key, cleaned_input) for agent commands.
    Returns (None, error_message) if args are missing.
    Returns (None, None) if command is not an agent command (caller handles it).
    """
    if command not in AGENTS:
        return None, None

    if not args.strip():
        return None, (
            f"Please provide context after /{command}.\n\n"
            f"You can paste it inline:\n/{command} your situation here\n\n"
            f"Or on the next line:\n/{command}\nyour situation here"
        )

    return command, args.strip()
