# Test Results

## rust vs python: alphanum_3

reference|control|test
-|-|-
a7A|a7_a|a7a

1 mismatched out of 27

## rust vs python: word_4

reference|control|test
-|-|-
Aa7A|aa7_a|aa7a
A7Aa|a7_aa|a7aa
aa7A|aa7_a|aa7a
a7AA|a7_aa|a7aa
a7Aa|a7_aa|a7aa
a7A7|a7_a7|a7a7
a7A_|a7_a|a7a
a77A|a77_a|a77a
7a7A|7a7_a|7a7a
_a7A|a7_a|a7a

10 mismatched out of 256

## rust vs python: cases

reference|control|test
-|-|-
systemGfxMonitors1ScreenWidth|system_gfx_monitors1_screen_width|system_gfx_monitors1screen_width
systemGfxMonitors1ScreenWidthZeroIndexed|system_gfx_monitors1_screen_width_zero_indexed|system_gfx_monitors1screen_width_zero_indexed

2 mismatched out of 232

## rust vs python: unit

reference|control|test
-|-|-
abc123DEF456|abc123_def456|abc123def456
abc123Def456|abc123_def456|abc123def456
abc123DEf456|abc123_d_ef456|abc123d_ef456
ABC123Def456|abc123_def456|abc123def456
ABC123dEEf456FOO|abc123d_e_ef456_foo|abc123d_e_ef456foo

5 mismatched out of 22
