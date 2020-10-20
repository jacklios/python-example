import aysncio


async def main():
    print("hello")
    await aysncio.sleep(1)
    print("world")

aysncio.run(main())