flag_register = 0b00000000000000000000000000001000
the_mask = 8

# Check the state of your bit 
if flag_register & the_mask:
    print(flag_register)
else:
    print(flag_register)

# Reset your bit
flag_register = flag_register & ~the_mask
# flag_register &= ~the_mask

print(flag_register)

# Set your bit
flag_register = flag_register | the_mask
# flag_register |= the_mask

print(flag_register)

# Negate your bit 
flag_register = flag_register ^ the_mask
# flag_register ^= the_mask

print(flag_register)
