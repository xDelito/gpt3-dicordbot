import discord
import openai

openai.api_key = "ur api key"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("-"):
        await handle_image_generation(message)
        return

    if message.content.startswith("+"):
        await handle_completion(message)
        return

async def handle_image_generation(message):
    # Extraer la prompt del mensaje
    prompt = " ".join(message.content.split()[1:])

    # Generar imagen
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256",
    )

    # Obtener la URL de la imagen generada
    image_url = response["data"][0]["url"]

    # Enviar la imagen al canal
    await message.channel.send(image_url)

async def handle_completion(message):
    # Extraer la prompt del mensaje
    prompt = " ".join(message.content.split()[1:])

    # Generar completación
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # Enviar completación al canal
    await message.channel.send(response["choices"][0]["text"])

client.run("ur discord token bot")
