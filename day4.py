import re
from pprint import pprint

RAW = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

fields = ['byr','iyr', 
          'eyr', 'hgt', 'hcl', 
          'ecl', 'pid']
fields.sort()

def parse_line_to_dict(line):
    """hcl:#cfa07d eyr:2025 pid:166559648
        iyr:2011 ecl:brn hgt:59in
    """
    line = line.split()
    passport = {}
    for el in line:
        key, value = el.split(':')
        passport[key] = value
    return passport

def create_passports(raw):
    lines = raw.split('\n\n')
    return [parse_line_to_dict(line) for line in lines]

def valid_passport(passport):
    return all(item in passport for item in fields)

def valid_fields(passport):
    return all([
        1920 <= int(passport.get('byr', -1)) <= 2002,
        2010 <= int(passport.get('iyr', -1)) <= 2020,
        2020 <= int(passport.get('eyr', -1)) <= 2030,
        validate_height(passport.get('hgt', '')),
        re.match(r'^#[0-9a-f]{6}$', passport.get('hcl', '')),
        passport.get('ecl') in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
        re.match(r'^[0-9]{9}$', passport.get('pid','')),
    ])

def validate_height(hgt):
    if 'cm' in hgt:
        hgt = hgt.replace('cm', '')
        try:
            return 150 <= int(hgt) <= 193
        except:
            return False
    elif 'in' in hgt:
        hgt = hgt.replace('in', '')
        try:
            return 59 <= int(hgt) <= 76
        except:
            return False

    return False

def validate1(passports):
    return sum(valid_passport(passport) for passport in passports)

def validate2(passports):
    return sum(valid_fields(passport) for passport in passports)

if __name__ == "__main__":
    with open('inputs/day4.txt') as f:
        raw = f.read()
        passports = create_passports(raw)
        pprint(validate1(passports))
        pprint(validate2(passports))

# old code - done first part like that, but decided it's bad, well
# worse than my bad code
# def parse_only_fields(raw):
#     lines = raw.split('\n\n')
#     lines = [x.split() for x in lines]
#     lines = [[y.split(':') for y in x] for x in lines] 
#     lines = [sorted([y[0] for y in x]) for x in lines]
#     return lines

# def valid_passports(passports):
#     return sum([1 if all(item in x for item in fields) else 0 for x in passports])

# with open('inputs/day4.txt') as f:
#     raw = f.read()
#     pprint(valid_passports(parse_only_fields(raw)))
