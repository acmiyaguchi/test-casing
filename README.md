# Testing `com.google.common.base.CaseFormat` vs `heck`

This repository contains camelCased names from mozilla-pipeline-schemas that
have been detected by diffing the resulting schemas, as described in [this
PR](https://github.com/mozilla/jsonschema-transpiler/pull/79#issuecomment-509839572).

First run the scala code and dump the results to a file.

```bash
cat cases.txt | sbt run | grep -v "\[" > guava.txt
```

Run the rust code and dump the results to a file.

```bash
cat cases.txt | cargo run --quiet > heck.txt
```

Then diff the two files to see the difference in behavior.

```bash
diff -y guava.txt heck.txt | grep "|"
```

Run the following script for a markdown formatted output:

```bash
python3 format.py case.txt guava.txt heck.txt
```

| original | java | rust |
|---|---|---|
| BuildID | build_i_d | build_id |
| D2DEnabled | d2_d_enabled | d2d_enabled |
| GPUActive | g_p_u_active | gpu_active |
| ProductID | product_i_d | product_id |
| RAM | r_a_m | ram |
| activeGMPlugins | active_g_m_plugins | active_gm_plugins |
| changesetID | changeset_i_d | changeset_id |
| closedTS | closed_t_s | closed_ts |
| debugID | debug_i_d | debug_id |
| deviceID | device_i_d | device_id |
| engagedTS | engaged_t_s | engaged_ts |
| expiredTS | expired_t_s | expired_ts |
| l2cacheKB | l2cache_k_b | l2cache_kb |
| l3cacheKB | l3cache_k_b | l3cache_kb |
| learnMoreTS | learn_more_t_s | learn_more_ts |
| loadDurationMS | load_duration_m_s | load_duration_ms |
| memoryMB | memory_m_b | memory_mb |
| offeredTS | offered_t_s | offered_ts |
| processUptimeMS | process_uptime_m_s | process_uptime_ms |
| submissionURL | submission_u_r_l | submission_url |
| subsysID | subsys_i_d | subsys_id |
| threadID | thread_i_d | thread_id |
| totalPagesAM | total_pages_a_m | total_pages_am |
| vendorID | vendor_i_d | vendor_id |
| virtualMaxMB | virtual_max_m_b | virtual_max_mb |
| votedTS | voted_t_s | voted_ts |
| windowClosedTS | window_closed_t_s | window_closed_ts |
| windowsUBR | windows_u_b_r | windows_ubr |
| xulLoadDurationMS | xul_load_duration_m_s | xul_load_duration_ms |
