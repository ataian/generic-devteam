# Socket observer proof

Use when a negative result claims that a process made no outbound connection.

- Record the backend JVM with JFR for the invocation: `jdk.SocketRead`, `jdk.SocketWrite`,
  `jdk.SocketConnect` and `jdk.ProcessStart`.
- Before trusting the negative observation, perform a synthetic loopback connect to a closed port
  and verify JFR records the refused connect. Without that canary the observer itself is unproven.
- State the observation boundary: native clients that bypass JDK checks, traffic outside the backend
  JVM and activity outside the invocation remain unobserved.
- Keep the recording, the canary event and the invocation identity with the result. A log line
  claiming "no connection" is not observer evidence.
