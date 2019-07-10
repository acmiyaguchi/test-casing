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

```bash
build_i_d                                                     | build_id
d2_d_enabled                                                  | d2d_enabled
g_p_u_active                                                  | gpu_active
product_i_d                                                   | product_id
r_a_m                                                         | ram
active_g_m_plugins                                            | active_gm_plugins
changeset_i_d                                                 | changeset_id
closed_t_s                                                    | closed_ts
debug_i_d                                                     | debug_id
device_i_d                                                    | device_id
engaged_t_s                                                   | engaged_ts
expired_t_s                                                   | expired_ts
l2cache_k_b                                                   | l2cache_kb
l3cache_k_b                                                   | l3cache_kb
learn_more_t_s                                                | learn_more_ts
load_duration_m_s                                             | load_duration_ms
memory_m_b                                                    | memory_mb
offered_t_s                                                   | offered_ts
process_uptime_m_s                                            | process_uptime_ms
submission_u_r_l                                              | submission_url
subsys_i_d                                                    | subsys_id
thread_i_d                                                    | thread_id
total_pages_a_m                                               | total_pages_am
vendor_i_d                                                    | vendor_id
virtual_max_m_b                                               | virtual_max_mb
voted_t_s                                                     | voted_ts
window_closed_t_s                                             | window_closed_ts
windows_u_b_r                                                 | windows_ubr
xul_load_duration_m_s                                         | xul_load_duration_ms
```
