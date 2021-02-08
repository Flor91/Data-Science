import re  # import regex module

text = "My phone number is 415-555-4242."
print(text)

phone_regex = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
mo = phone_regex.search(text)

print("Phone: {}".format(mo.group()))

phone_groups_regex = re.compile(r"(\d)(\d\d)-(\d\d\d-\d\d\d\d)")
mog = phone_groups_regex.search(text)

print("Phone G: {}".format(mog.group()))
print("Phone G1: {}".format(mog.group(1)))
print("Phone G2: {}".format(mog.group(2)))
print("Phone G0: {}".format(mog.group(0)))
print(mog.groups())

area_code, main_number, d = mog.groups()

print("\nPipe: Matches any of either Batman or Tina Fey")
hero_regex = re.compile(r"Batman|Tina Fey")
mo1 = hero_regex.search("Batman and Tina Fey.")

print(mo1.group())

print("\nPipe inside a group: Matches either Batman, Batmobile, Batcopter")
bat_regex = re.compile(r"(Bat(man|mobile|copter))")
mob = bat_regex.search("Batmobile lost a wheel")
print(mob.group())
print(mob.group(1))
print(mob.group(2))
print(mob.groups())

print("\n?: Optional group")
bat_regex = re.compile(r"Bat(wo)?man")
mow = bat_regex.search("The Adventures of Batwoman")
print(mow.group())

print("\n*: Match zero or more times")
bat_regex = re.compile(r"Bat(wo)*man")
mo = bat_regex.search("The Adventures of Batman")
print(mo.group())
mo = bat_regex.search("The Adventures of Batwowowoman")
print(mo.group())

print("\n+: Match one or more times")
bat_regex = re.compile(r"Bat(wo)+man")
mo = bat_regex.search("The Adventures of Batwowoman")
print(mo.group())

print("\nSpecific number of repetitions with {}")
bat_regex = re.compile(r"(Ha){3,4}")
mo = bat_regex.search("HaHaHaHaHa")
print(mo.group())

print("\nNon greedy matching with with {}?")
bat_regex = re.compile(r"(Ha){3,4}?")
mo = bat_regex.search("HaHaHaHaHa")
print(mo.group())

print("\nfindall() ")
p = phone_regex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(p)

print(phone_groups_regex.findall("Cell: 415-555-9999 Work: 212-555-0000"))

begins_with_hello = re.compile(r"^Hello")
print(begins_with_hello.search("He said hello.") is None)

whole_string_is_num = re.compile(r"^\d+$")
print(whole_string_is_num.search("12 34567890") is None)

at_regex = re.compile(r".at")
print(at_regex.findall("The cat in the hat sat on the flat mat."))

name_regex = re.compile(r"First Name: (.*) Last Name: (.*)")
mo = name_regex.search("First Name: Al Last Name: Sweigart")
print(mo.groups())

no_newline_regex = re.compile(".*")
print(
    no_newline_regex.search(
        "Serve the public trust.\nProtect the innocent.\nUphold the law.").
    group())

agent_names_regex = re.compile(r"Agent (\w)\w*")
print(
    agent_names_regex.sub(
        r"\1****",
        "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.",
    ))

phone_regex = re.compile(
    r"""(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )""",
    re.VERBOSE,
)
