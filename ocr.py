from pyzerox import zerox
import os
from dotenv import load_dotenv
import asyncio
from pdf2image import convert_from_path
from prompt_file import prompt, prompt_cheque_account
load_dotenv()

### Model Setup (Use only Vision Models) Refer: https://docs.litellm.ai/docs/providers ###

## placeholder for additional model kwargs which might be required for some models
kwargs = {}

## system prompt to use for the vision model
# custom_system_prompt = """
# Convert the following PDF of an bank account statement to a json format. Do not exclude any content from the page. Provide only the JSON output.
# """
custom_system_prompt = None  # Use None for default system prompt
# to override
# custom_system_prompt = "For the below pdf page, do something..something..." ## example

###################### Example for Azure OpenAI ######################
# model = "gpt-4o-mini" ## openai model
# os.environ["OPENAI_API_KEY"] = os.getenv("openai_key") ## your-api-key

###################### Example for Anthropic ######################
model="claude-3-5-sonnet-20241022"
os.environ["ANTHROPIC_API_KEY"] = os.getenv("anthropic_api") # your-anthropic-api-key


# Define main async entrypoint
async def main():
    file_path = "./statement/rbc/rbc_cheque.pdf" ## local filepath and file URL supported

    ## process only some pages or all
    select_pages = [1,2,3,4] ## None for all, but could be int or list(int) page numbers (1 indexed)

    output_dir = "./output"  # Use a relative path to a directory within your project

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    result = await zerox(file_path=file_path, model=model, output_dir=output_dir,
                         maintain_format=True,
                        custom_system_prompt=custom_system_prompt, select_pages=select_pages, **kwargs)
    return result

# run the main function:
result = asyncio.run(main())

# print markdown result
print(result)


# """
#     Convert the following PDF page to markdown.
#     Return only the markdown with no explanation text.
#     Do not exclude any content from the page.
# """