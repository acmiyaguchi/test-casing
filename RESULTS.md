# Test Results

## Heck vs Python (regexp)

### alphanum_3

reference|control|test
-|-|-

0 mismatched out of 27

### word_4

reference|control|test
-|-|-

0 mismatched out of 256

### cases

reference|control|test
-|-|-

0 mismatched out of 232

### unit

reference|control|test
-|-|-

0 mismatched out of 22

## Heck vs Direct2Parquet

### alphanum_3

reference|control|test
-|-|-
AAa|a_aa|aaa
A7A|a7a|a7_a
7AA|7aa|7_aa
7Aa|7aa|7_aa
7A7|7a7|7_a7
77A|77a|77_a

6 mismatched out of 27

### word_4

reference|control|test
-|-|-
AAAa|aa_aa|aaaa
AAA_|aaa|aaa_
AAaA|a_aa_a|aaa_a
AAaa|a_aaa|aaaa
AAa7|a_aa7|aaa7
AAa_|a_aa|aaa_
AA7A|aa7a|aa7_a
AA7_|aa7|aa7_
AA__|aa|aa__
AaA_|aa_a|aa_a_
Aaa_|aaa|aaa_
Aa7_|aa7|aa7_
Aa__|aa|aa__
A7AA|a7aa|a7_aa
A7A7|a7a7|a7_a7
A7A_|a7a|a7_a_
A7a_|a7a|a7a_
A77A|a77a|a77_a
A77_|a77|a77_
A7__|a7|a7__
A_A_|a_a|a_a_
A_a_|a_a|a_a_
A_7A|a_7a|a_7_a
A_7_|a_7|a_7_
A__A|a_a|a__a
A__a|a_a|a__a
A__7|a_7|a__7
A___|a|a___
aAAa|a_a_aa|a_aaa
aAA_|a_aa|a_aa_
aAa_|a_aa|a_aa_
aA7A|a_a7a|a_a7_a
aA7_|a_a7|a_a7_
aA__|a_a|a_a__
aaA_|aa_a|aa_a_
aaa_|aaa|aaa_
aa7_|aa7|aa7_
aa__|aa|aa__
a7A_|a7_a|a7_a_
a7a_|a7a|a7a_
a77_|a77|a77_
a7__|a7|a7__
a_A_|a_a|a_a_
a_a_|a_a|a_a_
a_7A|a_7a|a_7_a
a_7_|a_7|a_7_
a__A|a_a|a__a
a__a|a_a|a__a
a__7|a_7|a__7
a___|a|a___
7AAA|7aaa|7_aaa
7AAa|7a_aa|7_aaa
7AA7|7aa7|7_aa7
7AA_|7aa|7_aa_
7AaA|7aa_a|7_aa_a
7Aaa|7aaa|7_aaa
7Aa7|7aa7|7_aa7
7Aa_|7aa|7_aa_
7A7A|7a7a|7_a7_a
7A7a|7a7a|7_a7a
7A77|7a77|7_a77
7A7_|7a7|7_a7_
7A_A|7a_a|7_a_a
7A_a|7a_a|7_a_a
7A_7|7a_7|7_a_7
7A__|7a|7_a__
7aA_|7a_a|7a_a_
7aa_|7aa|7aa_
7a7_|7a7|7a7_
7a__|7a|7a__
77AA|77aa|77_aa
77Aa|77aa|77_aa
77A7|77a7|77_a7
77A_|77a|77_a_
77a_|77a|77a_
777A|777a|777_a
777_|777|777_
77__|77|77__
7_A_|7_a|7_a_
7_a_|7_a|7_a_
7_7A|7_7a|7_7_a
7_7_|7_7|7_7_
7__A|7_a|7__a
7__a|7_a|7__a
7__7|7_7|7__7
7___|7|7___
_AAA|aaa|_aaa
_AAa|a_aa|_aaa
_AA7|aa7|_aa7
_AA_|aa|_aa_
_AaA|aa_a|_aa_a
_Aaa|aaa|_aaa
_Aa7|aa7|_aa7
_Aa_|aa|_aa_
_A7A|a7a|_a7_a
_A7a|a7a|_a7a
_A77|a77|_a77
_A7_|a7|_a7_
_A_A|a_a|_a_a
_A_a|a_a|_a_a
_A_7|a_7|_a_7
_A__|a|_a__
_aAA|a_aa|_a_aa
_aAa|a_aa|_a_aa
_aA7|a_a7|_a_a7
_aA_|a_a|_a_a_
_aaA|aa_a|_aa_a
_aaa|aaa|_aaa
_aa7|aa7|_aa7
_aa_|aa|_aa_
_a7A|a7_a|_a7_a
_a7a|a7a|_a7a
_a77|a77|_a77
_a7_|a7|_a7_
_a_A|a_a|_a_a
_a_a|a_a|_a_a
_a_7|a_7|_a_7
_a__|a|_a__
_7AA|7aa|_7_aa
_7Aa|7aa|_7_aa
_7A7|7a7|_7_a7
_7A_|7a|_7_a_
_7aA|7a_a|_7a_a
_7aa|7aa|_7aa
_7a7|7a7|_7a7
_7a_|7a|_7a_
_77A|77a|_77_a
_77a|77a|_77a
_777|777|_777
_77_|77|_77_
_7_A|7_a|_7_a
_7_a|7_a|_7_a
_7_7|7_7|_7_7
_7__|7|_7__
__AA|aa|__aa
__Aa|aa|__aa
__A7|a7|__a7
__A_|a|__a_
__aA|a_a|__a_a
__aa|aa|__aa
__a7|a7|__a7
__a_|a|__a_
__7A|7a|__7_a
__7a|7a|__7a
__77|77|__77
__7_|7|__7_
___A|a|___a
___a|a|___a
___7|7|___7
____||____

150 mismatched out of 256

### cases

reference|control|test
-|-|-
D2DEnabled|d2d_enabled|d2_denabled
DWriteEnabled|d_write_enabled|dwrite_enabled
GPUActive|gpu_active|gpuactive
activeGMPlugins|active_gm_plugins|active_gmplugins
speedMHz|speed_m_hz|speed_mhz

5 mismatched out of 232

### unit

reference|control|test
-|-|-
This is Human case.|this_is_human_case|this_is_human_case_
MixedUP CamelCase, with some Spaces|mixed_up_camel_case_with_some_spaces|mixed_up_camel_case__with_some_spaces
mixed_up_ snake_case with some _spaces|mixed_up_snake_case_with_some_spaces|mixed_up__snake_case_with_some__spaces
this-contains_ ALLKinds OfWord_Boundaries|this_contains_all_kinds_of_word_boundaries|this_contains__allkinds_of_word_boundaries
XMLHttpRequest|xml_http_request|xmlhttp_request
99BOTTLES|99bottles|99_bottles
abc123DEf456|abc123_d_ef456|abc123_def456
ABC123DEF456|abc123def456|abc123_def456
ABC123DEf456|abc123d_ef456|abc123_def456
ABC123dEEf456FOO|abc123d_e_ef456_foo|abc123d_eef456_foo
ABcDE|a_bc_de|abc_de

11 mismatched out of 22

## Heck vs CaseFormat

### alphanum_3

reference|control|test
-|-|-
AAA|aaa|a_a_a
AA7|aa7|a_a7
A7A|a7a|a7_a
aAA|a_aa|a_a_a
7AA|7aa|7_a_a
7Aa|7aa|7_aa
7A7|7a7|7_a7
77A|77a|77_a

8 mismatched out of 27

### word_4

reference|control|test
-|-|-
AAAA|aaaa|a_a_a_a
AAAa|aa_aa|a_a_aa
AAA7|aaa7|a_a_a7
AAA_|aaa|a_a_a_
AAa_|a_aa|a_aa_
AA7A|aa7a|a_a7_a
AA7a|aa7a|a_a7a
AA77|aa77|a_a77
AA7_|aa7|a_a7_
AA_A|aa_a|a_a__a
AA_a|aa_a|a_a_a
AA_7|aa_7|a_a_7
AA__|aa|a_a__
AaAA|aa_aa|aa_a_a
AaA_|aa_a|aa_a_
Aaa_|aaa|aaa_
Aa7_|aa7|aa7_
Aa_A|aa_a|aa__a
Aa__|aa|aa__
A7AA|a7aa|a7_a_a
A7A7|a7a7|a7_a7
A7A_|a7a|a7_a_
A7a_|a7a|a7a_
A77A|a77a|a77_a
A77_|a77|a77_
A7_A|a7_a|a7__a
A7__|a7|a7__
A_AA|a_aa|a__a_a
A_Aa|a_aa|a__aa
A_A7|a_a7|a__a7
A_A_|a_a|a__a_
A_a_|a_a|a_a_
A_7A|a_7a|a_7_a
A_7_|a_7|a_7_
A__A|a_a|a___a
A__a|a_a|a__a
A__7|a_7|a__7
A___|a|a___
aAAA|a_aaa|a_a_a_a
aAA7|a_aa7|a_a_a7
aAA_|a_aa|a_a_a_
aAa_|a_aa|a_aa_
aA7A|a_a7a|a_a7_a
aA7_|a_a7|a_a7_
aA_A|a_a_a|a_a__a
aA__|a_a|a_a__
aaAA|aa_aa|aa_a_a
aaA_|aa_a|aa_a_
aaa_|aaa|aaa_
aa7_|aa7|aa7_
aa_A|aa_a|aa__a
aa__|aa|aa__
a7AA|a7_aa|a7_a_a
a7A_|a7_a|a7_a_
a7a_|a7a|a7a_
a77_|a77|a77_
a7_A|a7_a|a7__a
a7__|a7|a7__
a_AA|a_aa|a__a_a
a_Aa|a_aa|a__aa
a_A7|a_a7|a__a7
a_A_|a_a|a__a_
a_a_|a_a|a_a_
a_7A|a_7a|a_7_a
a_7_|a_7|a_7_
a__A|a_a|a___a
a__a|a_a|a__a
a__7|a_7|a__7
a___|a|a___
7AAA|7aaa|7_a_a_a
7AAa|7a_aa|7_a_aa
7AA7|7aa7|7_a_a7
7AA_|7aa|7_a_a_
7AaA|7aa_a|7_aa_a
7Aaa|7aaa|7_aaa
7Aa7|7aa7|7_aa7
7Aa_|7aa|7_aa_
7A7A|7a7a|7_a7_a
7A7a|7a7a|7_a7a
7A77|7a77|7_a77
7A7_|7a7|7_a7_
7A_A|7a_a|7_a__a
7A_a|7a_a|7_a_a
7A_7|7a_7|7_a_7
7A__|7a|7_a__
7aAA|7a_aa|7a_a_a
7aA_|7a_a|7a_a_
7aa_|7aa|7aa_
7a7_|7a7|7a7_
7a_A|7a_a|7a__a
7a__|7a|7a__
77AA|77aa|77_a_a
77Aa|77aa|77_aa
77A7|77a7|77_a7
77A_|77a|77_a_
77a_|77a|77a_
777A|777a|777_a
777_|777|777_
77_A|77_a|77__a
77__|77|77__
7_AA|7_aa|7__a_a
7_Aa|7_aa|7__aa
7_A7|7_a7|7__a7
7_A_|7_a|7__a_
7_a_|7_a|7_a_
7_7A|7_7a|7_7_a
7_7_|7_7|7_7_
7__A|7_a|7___a
7__a|7_a|7__a
7__7|7_7|7__7
7___|7|7___
_AAA|aaa|__a_a_a
_AAa|a_aa|__a_aa
_AA7|aa7|__a_a7
_AA_|aa|__a_a_
_AaA|aa_a|__aa_a
_Aaa|aaa|__aaa
_Aa7|aa7|__aa7
_Aa_|aa|__aa_
_A7A|a7a|__a7_a
_A7a|a7a|__a7a
_A77|a77|__a77
_A7_|a7|__a7_
_A_A|a_a|__a__a
_A_a|a_a|__a_a
_A_7|a_7|__a_7
_A__|a|__a__
_aAA|a_aa|_a_a_a
_aAa|a_aa|_a_aa
_aA7|a_a7|_a_a7
_aA_|a_a|_a_a_
_aaA|aa_a|_aa_a
_aaa|aaa|_aaa
_aa7|aa7|_aa7
_aa_|aa|_aa_
_a7A|a7_a|_a7_a
_a7a|a7a|_a7a
_a77|a77|_a77
_a7_|a7|_a7_
_a_A|a_a|_a__a
_a_a|a_a|_a_a
_a_7|a_7|_a_7
_a__|a|_a__
_7AA|7aa|_7_a_a
_7Aa|7aa|_7_aa
_7A7|7a7|_7_a7
_7A_|7a|_7_a_
_7aA|7a_a|_7a_a
_7aa|7aa|_7aa
_7a7|7a7|_7a7
_7a_|7a|_7a_
_77A|77a|_77_a
_77a|77a|_77a
_777|777|_777
_77_|77|_77_
_7_A|7_a|_7__a
_7_a|7_a|_7_a
_7_7|7_7|_7_7
_7__|7|_7__
__AA|aa|___a_a
__Aa|aa|___aa
__A7|a7|___a7
__A_|a|___a_
__aA|a_a|__a_a
__aa|aa|__aa
__a7|a7|__a7
__a_|a|__a_
__7A|7a|__7_a
__7a|7a|__7a
__77|77|__77
__7_|7|__7_
___A|a|____a
___a|a|___a
___7|7|___7
____||____

175 mismatched out of 256

### cases

reference|control|test
-|-|-
BuildID|build_id|build_i_d
D2DEnabled|d2d_enabled|d2_d_enabled
GPUActive|gpu_active|g_p_u_active
ProductID|product_id|product_i_d
RAM|ram|r_a_m
activeGMPlugins|active_gm_plugins|active_g_m_plugins
changesetID|changeset_id|changeset_i_d
closedTS|closed_ts|closed_t_s
debugID|debug_id|debug_i_d
deviceID|device_id|device_i_d
engagedTS|engaged_ts|engaged_t_s
expiredTS|expired_ts|expired_t_s
l2cacheKB|l2cache_kb|l2cache_k_b
l3cacheKB|l3cache_kb|l3cache_k_b
learnMoreTS|learn_more_ts|learn_more_t_s
loadDurationMS|load_duration_ms|load_duration_m_s
memoryMB|memory_mb|memory_m_b
offeredTS|offered_ts|offered_t_s
processUptimeMS|process_uptime_ms|process_uptime_m_s
submissionURL|submission_url|submission_u_r_l
subsysID|subsys_id|subsys_i_d
threadID|thread_id|thread_i_d
totalPagesAM|total_pages_am|total_pages_a_m
vendorID|vendor_id|vendor_i_d
virtualMaxMB|virtual_max_mb|virtual_max_m_b
votedTS|voted_ts|voted_t_s
windowClosedTS|window_closed_ts|window_closed_t_s
windowsUBR|windows_ubr|windows_u_b_r
xulLoadDurationMS|xul_load_duration_ms|xul_load_duration_m_s

29 mismatched out of 232

### unit

reference|control|test
-|-|-
This is Human case.|this_is_human_case|this is _human case.
MixedUP CamelCase, with some Spaces|mixed_up_camel_case_with_some_spaces|mixed_u_p _camel_case, with some _spaces
mixed_up_ snake_case with some _spaces|mixed_up_snake_case_with_some_spaces|mixed_up_ snake_case with some _spaces
kebab-case|kebab_case|kebab-case
SHOUTY_SNAKE_CASE|shouty_snake_case|s_h_o_u_t_y__s_n_a_k_e__c_a_s_e
this-contains_ ALLKinds OfWord_Boundaries|this_contains_all_kinds_of_word_boundaries|this-contains_ _a_l_l_kinds _of_word__boundaries
XMLHttpRequest|xml_http_request|x_m_l_http_request
FIELD_NAME11|field_name11|f_i_e_l_d__n_a_m_e11
99BOTTLES|99bottles|99_b_o_t_t_l_e_s
abc123DEF456|abc123_def456|abc123_d_e_f456
ABC123def456|abc123def456|a_b_c123def456
ABC123DEF456|abc123def456|a_b_c123_d_e_f456
ABC123Def456|abc123_def456|a_b_c123_def456
ABC123DEf456|abc123d_ef456|a_b_c123_d_ef456
ABC123dEEf456FOO|abc123d_e_ef456_foo|a_b_c123d_e_ef456_f_o_o
abcDEF|abc_def|abc_d_e_f
ABcDE|a_bc_de|a_bc_d_e

17 mismatched out of 22
