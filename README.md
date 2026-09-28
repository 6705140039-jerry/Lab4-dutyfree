### 1. Group Name - Duty Free

## 2. Who Did What

| Member | GitHub Username | File |
|---|---|---|
| Aung Myo Naing(Jerry)| 6705140039-jerry | test_deposit.py |
| So Pyay Htoo(Yummy) | 6705140034-SoPyayHtoo | test_withdraw.py |
| Zay Htet (Zett) | 6705140013-zett | test_teardown.py |
| Zarr Ni Htut(Raymand) | 6705140005-ZarrNiHtut | test_shared.py |
| Min khant Kyaw (Sonic) | squareroot99 | conftest.py |

## 3. Our Merge Conflict

### Conflict markers encountered
Git reported a content conflict in `bank.py` while pulling and rebasing `main`. The conflict markers were `<<<<<<<`, `=======`, and `>>>>>>>`.

### Final decision
We reviewed both versions of `bank.py` and combined the needed changes into one file. We then removed the conflict markers, saved the file, and continued the rebase.

### Why Git could not resolve it automatically
Both the local branch and the remote branch changed overlapping parts of `bank.py`. Git could not determine which changes to keep, so we resolved them manually.

## 4. Reflection Questions

1. **Why was your push rejected, and how did you fix it?**  
   My push was rejected because the remote repository had             commits that were missing from my local branch. I pulled the remote changes with rebase, resolved the conflict, and then pushed again.

3. **Why could Git not resolve the README conflict automatically?**  
   Both branches changed overlapping parts of the README, so Git could not determine which version to keep. I reviewed the changes and resolved the conflict manually.

4. **What is the difference between committing and pushing?**  
   Committing saves changes to the project’s history on my computer. Pushing uploads those commits to the remote repository, such as GitHub.

5. **How do fixtures reduce duplicated setup code in tests?**  
   A fixture creates reusable setup, such as a test account, that multiple tests can request. This avoids repeating the same setup code in each test.
