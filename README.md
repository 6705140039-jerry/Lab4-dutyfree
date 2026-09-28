# Lab 4 — Automated Software Testing

## Group Name

**Duty Free**

## Who Did What

| Member | Student ID | File |
|---|---:|---|
| Aung Myo Naing (Jerry) | 6705140039 | test_deposit.py |
| Min Khant Kyaw (Sonic) | 6705140008 | test_withdraw.py |
| So Pyay Htoo (Yummy) | 6705140034 | conftest.py |
| Zay Htet (Zett) | 6705140013 | test_teardown.py |
| Zarr Ni Htut (Raymand) | 6705140005 | test_shared.py |

## Our Merge Conflict

During Round 3, multiple group members edited the same section of `README.md` at approximately the same time. Git could not automatically combine the changes and inserted conflict markers.

The conflict markers encountered were:

```text
<<<<<<< HEAD
| Aung Myo Naing| 6705140039-jerry| test_deposit.py |
=======
| Zarr Ni Htut | 6705140005-ZarrNiHtut| test_shared.py |
>>>>>>> commit
```

Both rows were kept in the final version because each row represented a different group member's contribution. Git could not resolve the conflict automatically because the changes were made to the same part of the same file.

After resolving the conflict, the conflict markers were removed and the README contained all five group members.

## Git Contribution Summary

Run:

```bash
git shortlog -sn
```

Paste the actual output from the final shared repository below.

```text
PASTE ACTUAL git shortlog -sn OUTPUT HERE
```

## Reflection Questions

### 1. Why was your push rejected, and how did you fix it?

The push was rejected because another group member had pushed changes to the shared repository before my push, so my local repository was not up to date. I fixed it by running `git pull` and then `git push` again.

### 2. Why could Git not resolve the README conflict automatically?

Git could not resolve the conflict because different group members changed the same part of `README.md`. Git could not determine automatically which version should be kept.

### 3. What is the difference between committing and pushing?

A commit saves a snapshot of changes in the local Git repository. A push uploads those commits to GitHub so other group members can see them.

### 4. How do fixtures reduce duplicated setup code in tests?

Fixtures provide reusable setup code for tests. They avoid repeating the same setup steps in every test.

## Final Verification

Run these commands before submission:

```bash
git pull
git shortlog -sn
git log --oneline --graph
pytest -v
pytest -v -s
```

Check that:
- All five members appear in `git shortlog -sn`.
- All tests pass.
- No merge conflict markers remain.
- The README is complete.
- The repository is public.

## GitHub Repository

Paste the actual public GitHub repository URL here:

`https://github.com/<owner>/lab04-<group-name>`
