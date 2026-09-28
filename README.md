### Group Name - Duty Free

## Who Did What

| Member | GitHub Username | File |
|---|---|---|
| Aung Myo Naing(Jerry)| 6705140039-jerry | test_deposit.py |
| So Pyay Htoo(Yummy) | 6705140034-SoPyayHtoo | test_withdraw.py |
| Zay Htet (Zett) | 6705140013-zett | test_teardown.py |
| Zarr Ni Htut(Raymand) | 6705140005-ZarrNiHtut | test_shared.py |
| Min khant Kyaw(Sonic) | squareroot99 | conftest.py |

## 3. Our Merge Conflict

### Conflict markers encountered
Git reported a content conflict in `bank.py` while pulling and rebasing `main`. The conflict markers were `<<<<<<<`, `=======`, and `>>>>>>>`.

### Final decision
We reviewed both versions of `bank.py` and combined the needed changes into one file. We then removed the conflict markers, saved the file, and continued the rebase.

### Why Git could not resolve it automatically
Both the local branch and the remote branch changed overlapping parts of `bank.py`. Git could not determine which changes to keep, so we resolved them manually.
