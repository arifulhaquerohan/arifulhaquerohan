"""Render an honest, periodically refreshed time snapshot for the profile."""
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def render(now):
    start = datetime(now.year, 1, 1, tzinfo=now.tzinfo)
    end = datetime(now.year + 1, 1, 1, tzinfo=now.tzinfo)
    progress = (now - start).total_seconds() / (end - start).total_seconds()
    days_left = (end.date() - now.date()).days
    segments = ''.join(
        f'<rect x="{42 + i * 28}" y="249" width="21" height="10" rx="3" fill="{ "#50f5e9" if i < int(progress * 40) else "#213149"}"/>'
        for i in range(40)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="310" viewBox="0 0 1200 310" role="img" aria-labelledby="title desc">
<title id="title">Dhaka time snapshot and {now.year} progress</title>
<desc id="desc">Updated {now:%d %B %Y at %H:%M} in Dhaka, UTC plus six. Year {progress:.1%} complete, {days_left} calendar days until January 1. Scheduled hourly; this is not a live clock.</desc>
<rect x="1" y="1" width="1198" height="308" rx="18" fill="#090e1b" stroke="#2c3d56"/>
<g font-family="Arial, Helvetica, sans-serif">
<circle cx="48" cy="37" r="5" fill="#50f5e9"/>
<text x="64" y="42" font-size="12" letter-spacing="2" fill="#50f5e9">LOCAL TIME / DHAKA</text>
<text x="1156" y="42" text-anchor="end" font-size="12" fill="#9aabc6">BANGLADESH · UTC +06:00</text>
<path d="M42 64H1158M445 88V181M829 88V181" stroke="#27364c"/>
<text x="42" y="143" font-family="monospace" font-size="66" font-weight="700" fill="#eef5ff">{now:%H:%M}</text>
<text x="45" y="177" font-size="16" fill="#9aabc6">{now:%A · %d %B %Y}</text>
<text x="486" y="109" font-size="12" letter-spacing="2" fill="#9aabc6">YEAR IN MOTION</text>
<text x="482" y="161" font-size="46" font-weight="700" fill="#50f5e9">{progress:.1%}</text>
<text x="870" y="109" font-size="12" letter-spacing="2" fill="#9aabc6">NEXT CHAPTER IN</text>
<text x="867" y="161" font-size="46" font-weight="700" fill="#ef5bc5">{days_left}<tspan font-size="20" fill="#9aabc6"> days</tspan></text>
<text x="42" y="226" font-size="12" letter-spacing="2" fill="#c9d7ed">{now.year} / MAKE THE DAYS COUNT</text>
{segments}
<text x="42" y="289" font-size="12" fill="#9aabc6">SNAPSHOT · {now:%Y-%m-%d %H:%M} DHAKA · SCHEDULED HOURLY</text>
<text x="1156" y="289" text-anchor="end" font-size="12" fill="#9aabc6">BUILD. LEARN. ITERATE.</text>
</g></svg>'''


if __name__ == '__main__':
    target = Path(__file__).resolve().parents[1] / 'assets' / 'time-panel.svg'
    target.write_text(render(datetime.now(ZoneInfo('Asia/Dhaka'))), encoding='utf-8')
