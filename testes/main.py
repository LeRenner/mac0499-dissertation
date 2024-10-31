import asyncio
import time
import aiohttp

async def request_send_message(message, chat_address):
    async with aiohttp.ClientSession() as session:
        async with session.post('localhost:5877/privEndpoint_sendMessage', json={"address": chat_address, "message": message}) as response:
            try:
                return await response.json()
            except aiohttp.ContentTypeError:
                return {"error": "Local request failed"}

async def request_call_send_message():
    message_cont = "Your message here"
    current_chat_address = "aspjdoapsjdopajsodpjaopsd.onion"

    if len(message_cont) < 1:
        return

    try:
        result = await request_send_message(message_cont, current_chat_address)

        if result.get("message") == "processing":
            result = await request_send_message(message_cont, current_chat_address)

        if not result.get("error"):
            print("Message sent successfully")
        else:
            print(f"Error: {result.get('error')}")
    except Exception as error:
        print(f"Error sending message: {error}")

async def main():
    times = []
    for _ in range(5):
        start_time = time.time()
        await request_call_send_message()
        end_time = time.time()
        times.append(end_time - start_time)

    print("Times taken for each request:", times)

if __name__ == "__main__":
    asyncio.run(main())