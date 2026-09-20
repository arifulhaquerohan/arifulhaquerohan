# Updating the profile time panel

The panel is a saved snapshot, not a live clock. Automatic workflow triggers
are paused because GitHub reported that the account is locked due to a billing
issue. The job was rejected before any script ran. A repository change cannot
remove that account lock. The existing failed run remains in Actions history.

## Refresh without GitHub Actions

Run these commands in a checkout with Python 3.9+ and timezone data installed:

```sh
python3 scripts/update_time.py
git add assets/time-panel.svg
git commit -m "Refresh Dhaka time snapshot"
git push origin main
```

## Restore automation

1. Resolve the account lock using [GitHub's billing instructions](https://docs.github.com/en/billing/how-tos/troubleshooting/locked-account).
2. Run **Refresh profile time** manually from the Actions tab and confirm it succeeds.
3. Add the following alongside `workflow_dispatch` under `on` in
   `.github/workflows/profile-time.yml`, then commit and push:

```yaml
  schedule:
    - cron: '17 * * * *'
```

The workflow pins Ubuntu 24.04 to avoid the announced `ubuntu-latest` migration.
This pin addresses the informational runner notice only, not the billing lock.
Scheduled runs and GitHub image caching may delay displayed updates.
