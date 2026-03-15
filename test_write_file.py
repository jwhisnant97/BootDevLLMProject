from functions.write_file import write_file
from functions.get_file_content import get_file_content

wd = "calculator"
fp1, fp2, fp3 = "lorem.txt", "pkg/morelorem.txt", "/tmp/temp.txt"
c1, c2, c3 = "wait, this isn't lorem ipsum", "lorem ipsum dolor sit amet", "this should not be allowed"
print(f"Result from write to 'calculator/lorem.txt':")
print(write_file(wd, fp1, c1))
print(f"Content matches?: {get_file_content(wd, fp1) == c1}")

print(f"Result from write to '{wd}/{fp2}':")
print(write_file(wd, fp2, c2))
print(f"Content matches?: {get_file_content(wd, fp2) == c2}")

print(f"Result from write to '{wd}/{fp3}'")
print(write_file(wd, fp3, c3))
print(f"Content matches?: {get_file_content(wd, fp3) == c3}")