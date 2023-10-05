domain_name = input()

while '.' in domain_name:
    last_dot = domain_name.rfind('.')
    print(domain_name[last_dot+1:])
    domain_name = domain_name[:last_dot]
print(domain_name)
