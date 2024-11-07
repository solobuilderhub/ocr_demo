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
custom_system_prompt = None

# to override
# custom_system_prompt = "For the below pdf page, do something..something..." ## example

###################### Example for Azure OpenAI ######################
model = os.getenv("MODEL")
os.environ["AZURE_API_KEY"] = os.getenv("AZURE_API_KEY")
os.environ["AZURE_API_BASE"] = os.getenv("AZURE_API_BASE")
os.environ["AZURE_API_VERSION"] = os.getenv("AZURE_API_VERSION")


# Define main async entrypoint
async def main():
    file_path = "./pdf/Signed A901.pdf" ## local filepath and file URL supported

    ## process only some pages or all
    select_pages = 1 ## None for all, but could be int or list(int) page numbers (1 indexed)

    output_dir = "./output"  # Use a relative path to a directory within your project

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    result = await zerox(file_path=file_path, model=model, output_dir=output_dir,
                        custom_system_prompt=custom_system_prompt, select_pages=select_pages, **kwargs)
    return result

# run the main function:
result = asyncio.run(main())

# print markdown result
print(result)