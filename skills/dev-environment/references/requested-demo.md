# Retire the previous demo

Use only as the first step after acceptance of a plan with a requested demonstration. Inspect the project’s demo state, including stopped remnants. Verified absence completes this step; an inspection failure does not.

Before removal, verify exclusive ownership of the old demo’s containers, volumes, network and private runtime directory. Retire it with project commands and verify those resources are gone. Preserve review evidence and unrelated resources. A stopped runtime is not retired.

If inspection, ownership, removal or verification fails, stop before committing the plan or writing any ticket. Tell the customer exactly what failed and resolve it with them. Do not apply and revert a planned product fix to bypass this prerequisite.
