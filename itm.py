import sys

def search(a, b, min_base = 2, max_base = 36):
    for source_base in range( min_base, max_base + 1 ):
        try:
            num_a = int( a, source_base )
        except ValueError:
            continue

        for target_base in range( min_base, max_base + 1 ):
            try:
                num_b = int( b, target_base )
            except ValueError:
                continue

            for diff_base in range( min_base, max_base + 1 ):
                diff = int_to_base( num_a - num_b, diff_base )
                # print("try:", int_to_base( num_a, source_base ), source_base, int_to_base( num_b, target_base ), target_base, diff, diff_base )

                if sequence_is_valid( diff, diff_base ):
                    print("result:", int_to_base( num_a, source_base ), source_base, int_to_base( num_b, target_base ), target_base, diff, diff_base )
    return 0

def sequence_is_valid(n, base):
    if n[ 0 ] == "-":
        n = n[ 1: ]

    sequence = int( str( n )[ 1 ], base ) - int( str( n )[ 0 ], base )
    sequence_is_validity = True

    for digits in range( 2, len( str( n ) ) ):
        if int( str( n )[ digits ], base ) - int( str( n )[ digits - 1 ], base ) != sequence:
            sequence_is_validity = False
            break

    return sequence_is_validity

def int_to_base(n, base, digits="0123456789abcdefghijklmnopqrstuvwxyz"):
    sgn = ""

    if n < 0:
        sgn = "-"
        n = -n

    return sgn + ( int_to_base( n // base, base, digits ) if n >= base else "" ) + digits[ n % base ]

if __name__ == "__main__":
    source_base = 23
    target_base = 28
    diff_base = 34

    a    = "m42a8221"
    diff =  "usqomki"
    b    = int_to_base( int( a, source_base ) - int( diff, diff_base ), target_base )

    print("task:", a, source_base, b, target_base, diff, diff_base)
    search( a, b )
    print("diff in base 12:", int_to_base( int( diff, diff_base ), 12 ) )
