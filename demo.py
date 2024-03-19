from cache import *


def generate_demo():
    print("Values have been stored in the cache, but never accessed:")
    cache = ThisIsCache(2)
    cache.put(1)
    cache.put(2)
    print(cache.cache[1])
    print(cache.cache[2])
    print("\nValues have been accessed and have recorded as such:")
    cache.get(1)
    cache.get(2)
    print(cache.cache[1])
    print(cache.cache[2])
    print(
        "\nCache item (3) added; Cache item (1) has been removed as it was the last recently accessed:"
    )
    cache.put(3)
    print(cache.cache[2])
    print(cache.cache[3])
    print(
        "\nCache currently contains "
        + str(len(cache.cache))
        + " items even though 3 total have been put into it."
    )


if __name__ == "__main__":
    generate_demo()
