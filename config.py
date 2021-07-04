import os


def init_log() -> int:
    return (
        int(log_group)  # type: ignore
        if (log_group := os.environ.get("LOG_GROUP")) is not None
        else None
    )


class Config:
    BOT_TOKEN = os.environ["1854010658:AAG7mV47VuzxCu0QS7d_JOgsIOF7I_qja1o"]
    API_ID = int(os.environ["6587260"])
    API_HASH = os.environ["c2ca5eb4d7fe8ad25cb7a58905efa20f"]
    EXEC_PATH = os.environ.get("GOOGLE_CHROME_SHIM", None)
    # OPTIONAL
    LOG_GROUP = init_log()
    SUPPORT_GROUP_LINK = os.environ.get("SUPPORT_GROUP", "https://t.me/bytessupport")
