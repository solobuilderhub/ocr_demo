from pyzerox import zerox
import os
from dotenv import load_dotenv
import asyncio
from pdf2image import convert_from_path
load_dotenv()

### Model Setup (Use only Vision Models) Refer: https://docs.litellm.ai/docs/providers ###

## placeholder for additional model kwargs which might be required for some models
kwargs = {}

## system prompt to use for the vision model
custom_system_prompt = """
Below is an image of a pdf of bank statement. Please make a json file containing all the details in the pdf. Do not miss any details in the pdf. For dates, maintain the format YYYY/MM/DD. In response, do not write anything else, just provide the json file.
"""
# custom_system_prompt = None  # Use None for default system prompt
# to override
# custom_system_prompt = "For the below pdf page, do something..something..." ## example

###################### Example for Azure OpenAI ######################
model = "gpt-4o-mini" ## openai model
os.environ["OPENAI_API_KEY"] = os.getenv("openai_key") ## your-api-key


# Define main async entrypoint
async def main():
    file_path = "./pdf/rohan.pdf" ## local filepath and file URL supported

    ## process only some pages or all
    select_pages = [1] ## None for all, but could be int or list(int) page numbers (1 indexed)

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