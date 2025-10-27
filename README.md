# static_code_analysis
| Issue Type         | Line(s) | Description                                                  | Fix Approach                                                  |
|--------------------|---------|--------------------------------------------------------------|---------------------------------------------------------------|
| Mutable default arg | 12      | `logs=[]` shared across calls                                 | Change default to None and initialize inside function         |
| Bare except        | 19      | Bare except block suppresses all exceptions                  | Catch specific exceptions and handle/log them                 |
| Dangerous function  | 59      | Use of unsafe `eval()`                                        | Remove `eval()`, replace with safe alternatives (logging)     |
| Missing docstrings  | Multiple| Lack of module and function docstrings                        | Add descriptive docstrings to module and each function        |
| Naming conventions  | Multiple| Function names not in snake_case                              | Rename all functions following snake_case style               |
| File handling      | 26,32    | File open calls missing encoding and not using context manager | Use `with open()` and specify `encoding='utf-8'`              |
| Line length        | Multiple| Some lines exceed 79 characters                               | Break long lines suitably                                      |
| Global usage       | Various | Use of `global` keyword                                       | Refactor to pass state via parameters / classes if possible   |
| Logging style      | Various | Use of f-string formatting in logging                        | Use lazy `%s` style formatting in logging statements           |

### Reflection Questions and Answers

1. **Which issues were the easiest to fix, and which were the hardest? Why?**  
   Easiest issues were formatting and docstring additions, as they mostly required following style guides. The hardest was fixing risky functions like `eval()`, and mutable default arguments because they required redesigning parts of code to avoid side effects and security flaws.

2. **Did the static analysis tools report any false positives? If so, describe one example.**  
   Static analysis tools can report false positives especially with broad exception handling warnings where catching `Exception` is sometimes necessary. For instance, a tool might flag a broad except block even if handled carefully in context.

3. **How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.**  
   Static analysis tools should be part of CI pipelines and pre-commit hooks to catch issues early. Locally, developers should run tools in their IDE or terminal before pushing code. Proper configuration and regular review of results help balance noise and value.

4. **What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**  
   Fixes improved code clarity with consistent style and naming, enhanced security by removing unsafe patterns, and increased maintainability with proper docstrings and error handling. Code became more robust and easier to debug and extend.

