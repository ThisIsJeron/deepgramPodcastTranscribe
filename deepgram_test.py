from deepgram import DeepgramClient, PrerecordedOptions

# The API key we created in step 3
DEEPGRAM_API_KEY = 'acebdaa90b0ddf6750049c50b23fb030e5d90457'

# Replace with your file path
PATH_TO_FILE = 'blah.mp3'

def main():
    deepgram = DeepgramClient(DEEPGRAM_API_KEY)

    with open(PATH_TO_FILE, 'rb') as buffer_data:
        payload = { 'buffer': buffer_data }

        options = PrerecordedOptions(
            smart_format=True, model="nova-2", language="en-US"
        )

        response = deepgram.listen.prerecorded.v('1').transcribe_file(payload, options)
        print(response.to_json(indent=4))

if __name__ == '__main__':
    main()