from pathlib import Path
import json, time, base64

OUT = Path("output")
OUT.mkdir(exist_ok=True)

header = (
    "#profile-title: FreeForYoung SG Ultra V2\n"
    "#announce: Singapore TOP nodes\n"
    "#subscription-auto-update-enable: 1\n"
    "#subscriptions-sort-type: ping\n"
)

(OUT/"singapore.txt").write_text(header, encoding="utf-8")
(OUT/"singapore-top10.txt").write_text(header, encoding="utf-8")
(OUT/"singapore-base64.txt").write_text(
    base64.b64encode(b"").decode()+"\n",
    encoding="utf-8"
)
(OUT/"singapore-stats.json").write_text(
    json.dumps({
        "generated": int(time.time()),
        "version": "Ultra V2"
    }, indent=2),
    encoding="utf-8"
)
