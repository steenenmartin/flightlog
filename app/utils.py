

def format_hhmm(hours: float) -> str:
    h = int(hours)
    m = int(round((hours - h) * 60))
    return f"{h:02}:{m:02}"