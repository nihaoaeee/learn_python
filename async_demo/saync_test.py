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
    import asyncio
    import datetime

    async def display_date():
        loop = asyncio.get_running_loop()
        end_time = loop.time() + 5.0
        while True:
            print(datetime.datetime.now())
            if (loop.time() + 1.0) >= end_time:
                break
            await asyncio.sleep(1)

    asyncio.run(display_date())
