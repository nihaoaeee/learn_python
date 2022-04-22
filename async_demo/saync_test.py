import asyncio


async def async_hello():
    print("hello world!")


async def print_number(num):
    print(num)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(async_hello())
    loop.run_until_complete(
        asyncio.wait([
            print_number(number) for number in range(10)
        ])
    )
    loop.close()
