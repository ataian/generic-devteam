# Portless test containers

Use when a test suite starts containers, a database or a disposable application instance.

- Do not bind a fixed host port, container name, volume name or network name for a test run.
  Let Docker allocate the host port and read it back from `docker port` or `docker inspect`.
  Use invocation-owned names so two runs cannot contend for one resource.
- Read the suite's isolation checker before changing fixture counts, seed volume or parallel blocks.
  Its limits are part of the acceptance.
- Canary proof: before trusting a green harness, run one check that must fail without the required
  dependency, then show the real check passes. A green result without a canary cannot separate
  "nothing ran" from "nothing failed".
- Record one input hash per evidence phase. Reuse evidence only while its inputs and container
  wiring are unchanged.
- Clean up by invocation ownership and verify absence. Never use global prune, fixed-name removal
  or a purge of persistent demo state.
