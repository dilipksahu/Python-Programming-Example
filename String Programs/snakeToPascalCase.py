# Convert Snake case to Pascal case

# Input : left_index   - Snake case
# Output : leftIndex   - Pascal case

test_str = "convert_snake_case_to_pascal_case"

print("======== replace() + title() ==========")
new_str = test_str.replace("_"," ").title().replace(" ","")        # after space caplock applied
print("Pascal Case String: ",new_str)


print("\n========== string.capwords() ========")
import string
new_str1 = string.capwords(test_str.replace("_"," ")).replace(" ","")
print("Pascal Case String: ",new_str1)