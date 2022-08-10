import asyncio
from rx_example_zoo import Animal
from rx_example_obs_output import Output

def zoo():
    elephant = Animal('Lucretia', 'trumpets')
    lion = Animal('Arnold', 'roars')
    fox = Animal('Betty', 'goes chacha-chacha-chacha')
    snake = Animal('Jake', 'hisses')

    out = Output(elephant, fox, snake, lion)

    return asyncio.gather(
        elephant.run(),
        fox.run(),
        snake.run(),
        lion.run()
    )

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(zoo())
