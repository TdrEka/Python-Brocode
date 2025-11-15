# * packs arguments into a tuple.
# ** allows you to pack multiple key-word arguments

def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Lucas", "Reig", "Weidgraaf")
print()
print(add(1, 1, 1, 1))

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street= "Carrer de sant Fermi",
              city= "Torrent",
              state= "Valencia",
              country= "Spain",
              post_code= "46900")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')} - {kwargs.get('apt')}")
    print(f"{kwargs.get('state')}")



shipping_label("Lucas", "Reig", "Weidgraaf",
               street="Carrer de sant fermi",
               apt="45b",
               state="Valencia" )



